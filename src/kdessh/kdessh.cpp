/* vi: ts=8 sts=4 sw=4
 *
 * $Id: kdessh.cpp 986418 2009-06-24 16:22:23Z kossebau $
 *
 * This file is part of the KDE project, module kdesu.
 * Copyright (C) 2000 Geert Jansen <jansen@kde.org>
 */

 /*
 
  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

 */

#include <unistd.h>
#include <string.h>
#include <pwd.h>
#include <stdlib.h>
#include <errno.h>

#include <sys/time.h>
#include <sys/resource.h>


#include <KDebug>
#include <KApplication>
#include <KStandardDirs>
#include <KConfig>
#include <KLocale>
#include <KAboutData>
#include <KCmdLineArgs>
#include <KMessageBox>

#include <kdesu/ssh.h>
#include <kdesu/client.h>
#include <kdesu/defaults.h>

#include <kdeutils-version.h>

#include "sshdlg.h"

#include <QByteArray>

using namespace KDESu;

int main(int argc, char *argv[])
{
    KAboutData aboutData("kdessh", 0, ki18n("KDE ssh"),
	    KDEUTILS_VERSION_STRING, ki18n("Runs a program on a remote host"),
	    KAboutData::License_Artistic,
	    ki18n("Copyright (c) 2000 Geert Jansen"), KLocalizedString(),
	    "http://utils.kde.org/projects/kdessh");
    aboutData.addAuthor(ki18n("Geert Jansen"), ki18n("Maintainer"),
	    "jansen@kde.org", "http://www.stack.nl/~geertj/");

    KCmdLineArgs::init(argc, argv, &aboutData);

    KCmdLineOptions options;
    options.add("+host", ki18n("Specifies the remote host"));
    options.add("+command", ki18n("The command to run"));
    options.add("u <user>", ki18n("Specifies the target uid"));
    options.add("s <path>", ki18n("Specify remote stub location"), "kdesu_stub");
    options.add("n", ki18n("Do not keep password"));
    options.add("q", ki18n("Stop the daemon (forgets all passwords)"));
    options.add("t", ki18n("Enable terminal output (no password keeping)"));
    KCmdLineArgs::addCmdLineOptions(options);

    KApplication app;
    // Check if ssh is available
    if (KStandardDirs::findExe(QString::fromLatin1("ssh")).isEmpty())
    {
        kError(1511) << "ssh not found\n";
        exit(1);
    }

    KCmdLineArgs *args = KCmdLineArgs::parsedArgs();

    // Stop daemon and exit?
    if (args->isSet("q"))
    {
	KDEsuClient client;
	if (client.ping() == -1)
	{
	    kError(1511) << "Daemon not running -- nothing to stop\n";
	    exit(1);
	}
	if (client.stopServer() != -1)
	{
	    kDebug(1511) << "Daemon stopped\n";
	    exit(0);
	}
	kError(1511) << "Could not stop daemon\n";
	exit(1);
    }

    if (args->count() < 2)
	KCmdLineArgs::usageError(i18n("No command or host specified."));

    // Get remote userid
    QByteArray user = args->getOption("u").toLocal8Bit();
    if (user.isNull())
    {
	struct passwd *pw = getpwuid(getuid());
	if (pw == 0L)
	{
	    kError(1511) << "You don't exist!\n";
	    exit(1);
	}
	user = pw->pw_name;
    }

    // Remote stub location
    QByteArray stub = args->getOption("s").toLocal8Bit();

    // Get remote host, command
    QByteArray host = args->arg(0).toLocal8Bit();
    QByteArray command = args->arg(1).toLocal8Bit();
    for (int i=2; i<args->count(); i++)
    {
	command += ' ';
	command += args->arg(i).toLocal8Bit();
    }

    // Check for daemon and start if necessary
    bool have_daemon = true;
    KDEsuClient client;
    if (!client.isServerSGID())
    {
	kWarning(1511) << "Daemon not safe (not sgid), not using it.\n";
	have_daemon = false;
    }
    else if ((client.ping() == -1) && (client.startServer() == -1))
    {
	kWarning(1511) << "Could not start daemon, reduced functionality.\n";
	have_daemon = false;
    }

    // Try to exec the command with kdesud?
    bool keep = !args->isSet("n") && have_daemon;
    bool terminal = args->isSet("t");
    if (keep && !terminal)
    {
	client.setHost(host);
	if (client.exec(command, user) != -1)
	    return 0;
    }

    // Set core dump size to 0 because we will have
    // root's password in memory.
    struct rlimit rlim;
    rlim.rlim_cur = rlim.rlim_max = 0;
    if (setrlimit(RLIMIT_CORE, &rlim))
    {
	kError(1511) << "rlimit(): " << perror << "\n";
	exit(1);
    }


    // Read configuration
    KConfigGroup config = KGlobal::config()->group("Passwords");
    const int timeout = config.readEntry(QString::fromLatin1("Timeout"), defTimeout);

    SshProcess proc(host, user);
    proc.setStub(stub);
    const int needpw = proc.checkNeedPassword();
    if (needpw < 0)
    {
	const QString msg = i18n("Ssh returned with an error.\n"
		"The error message is:\n\n") + proc.error();
	KMessageBox::error(0L, msg);
	exit(1);
    }

    QByteArray password;
    if (needpw != 0)
    {
	KDEsshDialog *dlg = new KDEsshDialog(host, user, stub,
		proc.prompt(), keep && !terminal);
	dlg->addLine(i18n("Command"), command);
	const int res = dlg->exec();
	if (res == KDEsshDialog::Rejected)
	    exit(0);
	keep = dlg->keep();
	password = dlg->password();
	delete dlg;
    } else
	keep = 0;

    // Make the dialog go away.
    app.processEvents();

    // Run command
    if (keep && have_daemon)
    {
	client.setHost(host);
	client.setPass(password, timeout);
	return client.exec(command, user);
    } else
    {
	proc.setCommand(command);
	proc.setTerminal(terminal);
	proc.setErase(true);
	return proc.exec(password);
    }
}

