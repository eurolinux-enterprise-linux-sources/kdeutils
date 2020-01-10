
Name: kdeutils
Epoch: 6
Version: 4.10.5
Release: 3%{?dist}
Summary: KDE Utilities

Group: Applications/System
License: GPLv2
URL: http://www.kde.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires:  kde-filesystem

%if 0%{?fedora}
Requires: kfloppy >= %{version}
Requires: superkaramba >= %{version}
Requires: filelight >= 1:%{version}
Requires: kremotecontrol >= %{version}
%endif
Requires: kcharselect >= %{version}
Requires: sweeper >= %{version}
Requires: %{name}-minimal = %{epoch}:%{version}-%{release}

# when split occured (https://bugzilla.redhat.com/810650)
Obsoletes: kdeutils-libs < 6:4.6.95-10

%description
Kdeutils metapackage, to ease migration to split applications

%package common 
Summary: Common files for %{name} 
%description common
%{summary}.

%package minimal
Summary: Minimal set of KDE Utilities
# when split occured
Obsoletes: kdeutils-minimal-libs < 6:4.6.95-10
Requires: ark >= %{version}
Requires: kcalc >= %{version}
Requires: kdf >= %{version}
Requires: kgpg >= %{version}
Requires: ktimer >= %{version}
Requires: kwallet >= %{version}
%description minimal
Minimal set of utilites for KDE 4.
Includes:
  * ark: tar/gzip archive manager
  * kcalc: scientific calculator
  * kdf: view disk usage
  * kgpg: gpg gui
  * ktimer: task scheduler
  * kwallet: kde wallet management tool


%prep

%build

%install


%files
# empty

%files common
# empty

%files minimal
# empty



%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 6:4.10.5-3
- Mass rebuild 2013-12-27

* Mon Jul 22 2013 Than Ngo <than@redhat.com> - 6:4.10.5-2
- add fedora/rhel condition

* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 6:4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 6:4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 6:4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 6:4.10.0-1
- 4.10.0

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.90-1
- 4.9.90

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.3-1
- 4.9.3

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.2-1
- 4.9.2

* Wed Sep 05 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.1-1
- 4.9.1

* Fri Jul 27 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.8.97-1
- 4.8.97

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.8.95-1
- 4.8.95

* Sun Jun 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.8.90-1
- 4.8.90

* Mon May 21 2012 Than Ngo <than@redhat.com> - 6:4.8.3-2
- rhel/fedora condition

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 6:4.8.3-1
- 4.8.3

* Thu Apr 12 2012 Rex Dieter <rdieter@fedoraproject.org> 6:4.8.2-2
- Obsoletes: kdeutils-libs (#810650)

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 6:4.8.1-1
- 4.8.1

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 6:4.7.97-1
- 4.7.97

* Tue Dec 27 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.95-2
- filelight epoch 1

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 6:4.7.95-1
- 4.7.95

* Mon Dec 19 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.90-2
- drop filelight epoch

* Thu Dec 08 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.90-1
- 4.7.90
- metapackage for spilt kdeutils modules
- (main) Requires: +filelight +kremotecontrol

* Fri Dec 02 2011 Than Ngo <than@redhat.com> - 4.7.3-3
- fix rhel condition

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.3-2
- rebuild (libarchive)

* Mon Oct 31 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.3-1
- 4.7.3
- pkgconfig-style deps

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6:4.7.2-2.1
- rebuild with new gmp without compat lib

* Tue Oct 18 2011 Than Ngo <than@redhat.com> 6:4.7.2-2
- Resolves: bz#744215, CVE-2011-2725 KDE Utilities Ark path traversal

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 6:4.7.2-1.1
- rebuild with new gmp

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.2-1
- 4.7.2

* Wed Sep 28 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.1-4
- better/upstreamable kgpg/gpg2 patch

* Tue Sep 27 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.1-3
- respin job-originating-user-name.patch to catch old AttributeError too

* Tue Sep 27 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.7.1-2
- monitor.py:441:get_notifications:KeyError: 'job-originating-user-name' (#739642)
- s/hal-cups-utils/system-config-printer-udev/

* Tue Sep 06 2011 Than Ngo <than@redhat.com> - 6:4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 6:4.7.0-1
- 4.7.0

* Fri Jul 22 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.6.95-10
- split packaging (#725020)

* Mon Jul 11 2011 Jaroslav Reznik <jreznik@redhat.com> - 6:4.6.95-1
- 4.6.95 (rc2)

* Mon Jun 27 2011 Than Ngo <than@redhat.com> - 6:4.6.90-1
- 4.6.90 (rc1)

* Tue Jun 14 2011 Jaroslav Reznik <jreznik@redhat.com> - 6:4.6.80-1
- 4.6.80 (beta1)

* Fri Apr 29 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.6.3-1
- 4.6.3

* Wed Apr 06 2011 Than Ngo <than@redhat.com> - 6:4.6.2-1
- 4.6.2

* Thu Mar 24 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.6.1-2
- ark uses 7z, not 7za (#607126)
- Wrong default configuration of Gnupg in Kgpg (#647876)

* Mon Feb 28 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.6.1-1
- 4.6.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Rex Dieter <rdieter@fedoraproject.org> 6:4.6.0-2
- move Obsoletes: kdeutils-devel elsewhere (kdesdk-devel)

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 6:4.6.0-1
- 4.6.0

* Thu Jan 06 2011 Jaroslav Reznik <jreznik@redhat.com> 6:4.5.95-1
- 4.5.95 (4.6rc2)

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 6:4.5.90-1
- 4.5.90 (4.6rc1)

* Sat Dec 04 2010 Thomas Janssen <thomasj@fedoraproject.org> 6:4.5.85-1
- 4.5.85 (4.6beta2)

* Sun Nov 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.5.80-1
- 4.5.80 (4.6beta1)
- Obsoletes/Provides: filelight
- Obsoletes: kdeutils-devel

* Sun Oct 31 2010 Than Ngo <than@redhat.com> - 6:4.5.3-1
- 4.5.3

* Sat Oct 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.5.2-1
- 4.5.2

* Tue Sep 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.5.1-2
- -minimal: Conflicts: kdeutils < 6:4.5.0-2

* Sat Aug 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.5.1-1
- 4.5.1

* Mon Aug 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.5.0-2
- -minimal subpkg (#624138)

* Thu Aug 05 2010 Than Ngo <than@redhat.com> - 6:4.5.0-1
- 4.5.0

* Sat Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.4.92-1
- 4.5 RC2 (4.4.92)

* Fri Jun 25 2010 Jaroslav Reznik <jreznik@redhat.com> - 6:4.4.90-1
- 4.5 RC1 (4.4.90)

* Mon Jun 07 2010 Jaroslav Reznik <jreznik@redhat.com> - 6:4.4.85-1
- 4.5 Beta 2 (4.4.85)

* Tue May 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.4.80-2
- drop oldish Obsoletes 
- cleanup %%description , probably could use more love

* Fri May 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 6:4.4.80-1
- 4.5 Beta 1 (4.4.80)
- -devel subpkg

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 6:4.4.3-1
- 4.4.3

* Sat Apr 03 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:4.4.2-1.1
- use the xz and lzma formats only if compiled in libarchive (upstream patch)
- fix build with old libarchive w/o archive_write_set_*_lzma (upstream patch)

* Mon Mar 29 2010 Lukas Tinkl <ltinkl@redhat.com> - 6:4.4.2-1
- 4.4.2

* Thu Mar 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.4.1-3
- BR: kdebase-devel
- drop old pykde4 patch

* Wed Mar 24 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:4.4.1-2
- -printer-applet: add support for automatic printer driver installation
                   (Tim Waugh, #576660, F13+)
- -printer-applet: add missing Requires: dbus-python
- remove obsolete F10- upgrade path Requires for -printer-applet

* Sat Feb 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:4.4.1-1
- 4.4.1

* Fri Feb 05 2010 Than Ngo <than@redhat.com> - 6:4.4.0-1
- 4.4.0

* Sun Jan 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.98-1
- KDE 4.3.98 (4.4rc3)

* Thu Jan 21 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.95-1
- KDE 4.3.95 (4.4rc2)

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- kde-4.3.90 (4.4rc1)

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-1
- kde-4.3.85 (4.4beta2)

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.3.80-3
- Repositioning the KDE Brand (#547361)

* Fri Dec 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.80-2
- BR: xz-devel

* Tue Dec  1 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.80-1
- KDE 4.4 beta1 (4.3.80)

* Tue Nov 24 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.2.svn1048496
- Add BR on kdebase-workspace for irkick

* Sun Nov 22 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.1.svn1048496
- Update to 4.3.75 snapshot

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-2
- rhel cleanup, Fix conditional for RHEL

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Sun Aug 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 6:4.3.0-3
- include epoch's in -libs-related Requires

* Sat Aug 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 6:4.3.0-2
- -libs subpkg reborn: Multilib conflicts for index.cache.bz2 (#515087)
- %%check: desktop-file-validate

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 6:4.3.0-1
- 4.3.0

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Mon Jul 13 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)
- Add support for PackageKit service packs (#504136)

* Wed May 20 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.85-3
- remove F9 kjots hack

* Wed May 20 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.85-2
- reenable printer-applet

* Thu May 14 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.85-1
- KDE 4.3 beta 1

* Thu Apr 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-4
- revert -printer-applet dep changes (and drop for f11+)

* Wed Apr 15 2009 Than Ngo <than@redhat.com> - 4.2.2-3
- drop the BR on PyKDE4, system-config-printer-libs
  it's just needed for runtime
- fix kdeutils-printer-applet dependency
- apply upstream patch to fix several issues in ark

* Wed Apr 01 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.2-2
- optimize scriptlets

* Tue Mar 31 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Sat Mar 14 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.1-3.2
- also drag in the printer-applet on F9

* Sat Mar 14 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.1-3.1
- also build printer-applet on F9, but don't drag it in by default

* Fri Mar 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-3
- *really* make a -printer-applet subpkg

* Fri Mar 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-2
- -printer-applet subpkg
- cleanup unused -libs/-devel crud

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Wed Jan 14 2009 Rex Dieter <rdieter@fedoraproject.org> 4.1.96-2
- (Build)Req: system-config-printer-libs

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Fri Dec 12 2008 Than Ngo <than@redhat.com> 4.1.85-1
- 4.2beta2

* Mon Dec 08 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.80-5
- BR: PyKDE4-devel >= %%version (vs previously unversioned BR)

* Mon Dec 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-4
- rebuild for Python 2.6

* Mon Dec 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-3
- BR plasma-devel instead of kdebase-workspace-devel

* Thu Nov 20 2008 Than Ngo <than@redhat.com> 4.1.80-2
- merged

* Thu Nov 20 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 6:4.1.80-1
- 4.1.80
- BR cmake >= 2.6.2
- make install/fast

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Mon Sep 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-3
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Sun Sep 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- (re)add unpackaged HTML/en/kcontrol/ files

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Tue Jul 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-1.1
- omit printer_applet from F-9 build

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Mon Jul 21 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-1.1
- reinclude kjots on F9 (moved to kdepim in 4.1, we don't ship kdepim 4 in F9)

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Fri Jul 11 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98

* Thu Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Thu Jul 03 2008 Rex Dieter <rdieter@fedorproject.org> 4.0.84-2.1
- disable printer applet (for now, to avoid kdebindings/PyKDE4 deps madness)

* Thu Jul 03 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-2
- %%description: -kedit, -kjots, +kwalletmanager, +superkaramba, +sweeper

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Sat Jun 21 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.83-2
- add explicit dep on rhpl to work around missing dep in
  system-config-printer (#452575)

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Sun Jun 15 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-1
- 4.0.82

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Wed May 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.72-1
- update to 4.0.72
- Obsoletes/Provides: okteta, update file list and description for okteta
- remove .so symlinks which should not be in a non-devel package

* Fri Apr 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-4
- add BR libarchive-devel

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- rebuild for NDEBUG and _kde4_libexecdir

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Tue Feb 05 2008 Than Ngo <than@redhat.com> 4.0.1-2
- backport to fix the wrong signal name of a KSelectAction

* Thu Jan 31 2008 Rex Dieter <rdieter@fedoraproject.org> 6:4.0.1-1
- kde-4.0.1

* Wed Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 6:4.0.0-2
- drop Requires: %%name-libs (doesn't exist anymore)

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 6:4.0.0-1
- kde-4.0.0

* Fri Dec 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.97.0-3
- libs subpkg
- Obsoletes: -extras
- omit parallel-install symlink hack

* Wed Dec 12 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 6:3.97.0-2
- rebuild for changed _kde4_includedir

* Wed Dec 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.97.0-1
- kde-3.97.0

* Sat Dec 01 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.96.2-2
- kcalc_32bit patch

* Sat Dec 01 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.96.2-1
- kde-3.96.2

* Sat Nov 24 2007 Sebastian Vahl <fedora@deadbabylon.de> 6:3.96.1-1
- kde-3.96.1
- added epoch in changelog (also backwards)

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 6:3.96.0-6
- BR: kde-filesystem >= 4

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 6:3.96.0-5
- BR: libXcomposite-devel
- BR: libXdamage-devel
- BR: libxkbfile-devel
- BR: libXv-devel
- BR: libXxf86misc-devel
- BR: libXScrnSaver-devel

* Fri Nov 16 2007 Sebastian Vahl <fedora@deadbabylon.de> 6:3.96.0-4
- require /sbin/ldconfig xdg-utils on %%post and %%postun
- some small spec cleanups
- +BR: kde-filesystem
- +BR: kde4-macros(api)

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 6:3.96.0-3
- BR: libzip-devel
- added %%defattr to package devel

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 6:3.96.0-2
- re-added missing epoch (from kdeutils3)

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 6:3.96.0-1
- Initial version for Fedora
