/* vi: ts=8 sts=4 sw=4
 *
 * $Id: sshdlg.cpp 984649 2009-06-21 10:29:31Z mlaurent $
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
 
#include "sshdlg.h"

#include <KLocale>
#include <KMessageBox>

#include <kdesu/ssh.h>

#include <QByteArray>

using namespace KDESu;

KDEsshDialog::KDEsshDialog(const QString &host, const QString &user, const QString &stub,
                           const QString& _prompt, bool enableKeep)
    : K3PasswordDialog(Password, enableKeep, 0)
{
    QString prompt( _prompt );
    m_Host = host.toLatin1();
    m_User = user.toLatin1();
    m_Stub = stub.toLatin1();

    setCaption(QString::fromLatin1("%1@%2").arg(user).arg(host));

    // Make the prompt a little more polite :-)
    if (prompt.toLower().left(6) == QString::fromLatin1("enter "))
        prompt.remove(0, 6);
    const int pos = prompt.indexOf(':');
    if (pos != -1)
        prompt.remove(pos, 10);
    prompt += '.';
    prompt.prepend(i18n("The action you requested needs authentication. "
                        "Please enter "));
    setPrompt(prompt);
}


KDEsshDialog::~KDEsshDialog()
{
}


bool KDEsshDialog::checkPassword(const char *password)
{
    SshProcess proc(m_Host, m_User);
    proc.setStub(m_Stub);

    const int ret = proc.checkInstall(password);
    switch (ret)
    {
    case -1:
	KMessageBox::error(this, i18n("Conversation with ssh failed.\n"));
	done(Rejected);
	return false;

    case 0:
	return true;

    case SshProcess::SshNotFound:
	KMessageBox::sorry(this,
		i18n("The programs 'ssh' or 'kdesu_stub' cannot be found.\n"
		"Make sure your PATH is set correctly."));
	done(Rejected);
	return false;

    case SshProcess::SshIncorrectPassword:
	KMessageBox::sorry(this, i18n("Incorrect password. Please try again."));
	return false;

    default:
        KMessageBox::error(this, i18n("Internal error: Illegal return from "
                "SshProcess::checkInstall()"));
        done(Rejected);
    }
    return true;
}


#include "sshdlg.moc"
