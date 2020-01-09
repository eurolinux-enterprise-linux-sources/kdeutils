/* vi: ts=8 sts=4 sw=4
 *
 * $Id: sshdlg.h 699126 2007-08-12 02:56:26Z henrique $
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

#ifndef SSHDLG_H
#define SSHDLG_H

#include <k3passworddialog.h>


class KDEsshDialog
    : public K3PasswordDialog
{
    Q_OBJECT

public:
    KDEsshDialog(const QString &host, const QString &user, const QString &stub,
                 const QString &prompt, bool enableKeep);
    ~KDEsshDialog();

protected:
    bool checkPassword(const char *password);
    
private:
    QByteArray m_User, m_Host, m_Stub;
};
    

#endif // SSHDLG_H
