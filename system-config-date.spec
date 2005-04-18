Summary: A graphical interface for modifying system date and time
Name: system-config-date
Version: 1.7.17
Release: 2
URL: http://fedora.redhat.com/projects/config-tools/
License: GPL
ExclusiveOS: Linux
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Source0: %{name}-%{version}.tar.bz2
Obsoletes: timetool
Obsoletes: dateconfig
Obsoletes: timeconfig
Obsoletes: redhat-config-date
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: python
Requires: ntp
Requires: python2
Requires: usermode >= 1.36
Requires: chkconfig
Requires: rhpl
Requires: newt
Requires: htmlview
Conflicts: firstboot <= 1.3.26

%description
system-config-date is a graphical interface for changing the system date and
time, configuring the system time zone, and setting up the NTP daemon to
synchronize the time of the system with a NTP time server.

%prep
%setup -q

%build
make

%install
make INSTROOT=$RPM_BUILD_ROOT install
desktop-file-install --vendor system --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --add-category X-Red-Hat-Base                             \
  $RPM_BUILD_ROOT%{_datadir}/applications/system-config-date.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%preun
if [ -d %{_datadir}/system-config-date ] ; then
  rm -rf %{_datadir}/system-config-date/*.pyc
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%doc doc/*
/usr/bin/system-config-date
/usr/bin/system-config-time
/usr/bin/dateconfig
/usr/sbin/timeconfig
%dir /usr/share/system-config-date
/usr/share/system-config-date/*.py
/usr/share/system-config-date/*.pyc
/usr/share/system-config-date/*.glade
%dir /usr/share/system-config-date/pixmaps/
#%dir /usr/share/firstboot/
#%dir /usr/share/firstboot/modules
#/usr/share/firstboot/modules/system-config-date.py
%attr(0644,root,root) %{_mandir}/man8/system-config-date*
%attr(0644,root,root) %{_mandir}/fr/man8/system-config-date*
%attr(0644,root,root) %{_mandir}/ja/man8/system-config-date*
%attr(0644,root,root) %{_datadir}/applications/system-config-date.desktop
%attr(0644,root,root) %{_datadir}/system-config-date/pixmaps/system-config-date.png
%attr(0644,root,root) %{_datadir}/icons/hicolor/48x48/apps/system-config-date.png
%attr(0644,root,root) %{_datadir}/system-config-date/pixmaps/map480.png
%attr(0644,root,root) %config(noreplace) /etc/security/console.apps/system-config-date
%attr(0644,root,root) %config(noreplace) /etc/pam.d/system-config-date
%attr(0644,root,root) %config(noreplace) /etc/security/console.apps/system-config-time
%attr(0644,root,root) %config(noreplace) /etc/pam.d/system-config-time
%attr(0644,root,root) %config(noreplace) /etc/security/console.apps/dateconfig
%attr(0644,root,root) %config(noreplace) /etc/pam.d/dateconfig
%attr(0644,root,root) %config(noreplace) /etc/ntp/ntpservers
%attr(0644,root,root) %config(noreplace) /usr/share/system-config-date/ntp.template

%changelog
* Tue Apr 19 2005 Matthias Clasen <mclasen@redhat.com> 1.7.17-2
- Silence %%post 

* Fri Apr 15 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.17
- make more strings translatable (#154873)

* Fri Apr 01 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.16-2
- use True, False instead of gtk.TRUE, gtk.FALSE to avoid deprecation warnings
  (#153037, patch by Colin Charles)

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 1.7.15-2
- Update the GTK+ theme icon cache on (un)install

* Sat Jan 15 2005 Nils Philippsen <nphilipp@redhat.com>
- use current default ntp.conf as template (#132787, #135142)

* Mon Dec 13 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.15-1
- don't lookup names or IP addresses as this may result in hangs (#142583)

* Mon Nov 29 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.14-1
- bump version

* Fri Nov 26 2004 Nils Philippsen <nphilipp@redhat.com>
- don't use duplicate accelerators (#134172, #140241)

* Fri Nov 26 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.13-1
- enable Gujarati and Tamil translations (#140881)

* Mon Nov 22 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.12-1
- remove wrongly encoded character (#140318) and duplicate word from French
  man page

* Wed Sep 29 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.11-1
- avoid GtkDeprecationWarning on gtk.mainquit on new pygtk (#134043)

* Tue Sep 28 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.10-1
- make timezone page contents actually be shown in firstboot

* Tue Sep 28 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.9-1
- enable choosing which notebook page(s) to show (for firstboot, #133748)
- some minor firstboot API changes, conflict with firstboot <= 1.3.26
- some minor UI tweaks
- remove pool.ntp.org from list of NTP server choices as system-config-date
  doesn't handle multi-IP machines really well ATM

* Fri Sep 17 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.8-1
- use pool.ntp.org as first choice of NTP servers (#132787)

* Thu Sep 16 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.7-2
- buildrequire python

* Tue Sep 14 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.7-1
- byte-compile python files
- first shot at something like an interface for firstboot

* Mon Sep 13 2004 Nils Philippsen <nphilipp@redhat.com>
- get widget sensitivity correct on startup (#132431)

* Thu Sep 03 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.5-1
- actually display time zone map (#131641)
- put NTP stuff into own tab to better accommodate firstboot (#131314)
- add accelerators to Date & Time tab

* Fri Aug 27 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.4-1
- handle multiple servers, broadcastclient (#115148),
  local time source (#72110)

* Tue Aug 03 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.3.1-1
- fix Japanese man page (#128766)

* Wed Apr 14 2004 Brent Fox <bfox@redhat.com> 1.7.3-3
- update desktop file (bug #120709)

* Tue Apr  6 2004 Brent Fox <bfox@redhat.com> 1.7.3-2
- fix desktop file icon path (bug #120176)

* Wed Mar 24 2004 Brent Fox <bfox@redhat.com> 1.7.3-1
- just copy over file, don't remove it (bug #119076)

* Fri Mar  5 2004 Brent Fox <bfox@redhat.com> 1.7.2-1
- preserve old restrict lines (bug #72110)

* Tue Feb  3 2004 Brent Fox <bfox@redhat.com> 1.7.1-2
- correct typo in URL in specfile

* Thu Jan  8 2004 Brent Fox <bfox@redhat.com> 1.7.1-1
- apply patch from bug #109803

* Wed Nov 19 2003 Brent Fox <bfox@redhat.com> 1.6.1-1
- rebuild

* Wed Nov 12 2003 Brent Fox <bfox@redhat.com> 1.6.0-1
- rename to system-config-date
- add Obsoletes for redhat-config-date
- adapt to Python2.3

* Mon Nov  3 2003 Brent Fox <bfox@redhat.com> 1.5.27-1
- add flag to allow timezone page to come up first

* Wed Oct 29 2003 Brent Fox <bfox@redhat.com> 1.5.26-1
- add French translation for man page from Frederic.Hornain@GB.BE

* Sun Oct 26 2003 Brent Fox <bfox@redhat.com> 1.5.25-1
- fix some other timezone po file encoding problems

* Sun Oct 26 2003 Brent Fox <bfox@redhat.com> 1.5.24-1
- make sure is.po file is UTF-8 encoded.  (bug #107439) Similar to bug #107033

* Wed Oct 15 2003 Brent Fox <bfox@redhat.com> 1.5.23-1
- UTF8-ify po/timezones/de.po (bug #107033)

* Fri Sep 19 2003 Brent Fox <bfox@redhat.com> 1.5.22-2
- rebuild

* Fri Sep 19 2003 Brent Fox <bfox@redhat.com> 1.5.22-1
- call timeconfig if the GUI cannot be started (bug #104718)

* Thu Sep 11 2003 Brent Fox <bfox@redhat.com> 1.5.21-2
- bump relnum and rebuild

* Thu Sep 11 2003 Brent Fox <bfox@redhat.com> 1.5.21-1
- rebuild with fixed po file encodings (bug #104019)

* Wed Sep 10 2003 Brent Fox <bfox@redhat.com> 1.5.20-1
- add a Requires for newt (bug #104148)

* Fri Aug 29 2003 Brent Fox <bfox@redhat.com> 1.5.19-2
- bump relnum and rebuild

* Fri Aug 29 2003 Brent Fox <bfox@redhat.com> 1.5.19-1
- if timezone in /etc/sysconfig/clock is not in zone.tab, default to America/New_York (bug #101575)

* Thu Aug 14 2003 Brent Fox <bfox@redhat.com> 1.5.18-1
- tag on every build

* Wed Jun 25 2003 Brent Fox <bfox@redhat.com> 1.5.15-2
- bump version number and rebuild

* Wed Jun 25 2003 Brent Fox <bfox@redhat.com> 1.5.15-1
- don't move /usr/share/zoneinfo/UTC into /etc/localtime (#91228)

* Mon Jun 16 2003 Brent Fox <bfox@redhat.com> 1.5.14-2
- bump number and rebuild

* Mon Jun 16 2003 Brent Fox <bfox@redhat.com> 1.5.14-1
- Add a function to get timezone date page (bug #91984)

* Tue May 27 2003 Brent Fox <bfox@redhat.com> 1.5.13-1
- if /var/spool/postfix/etc/localtime exists, copy the new timezone file there (bug #88249)

* Tue May 27 2003 Brent Fox <bfox@redhat.com> 1.5.12-1
- add a header comment to ntpservers file (bug #91619)

* Tue May 27 2003 Brent Fox <bfox@redhat.com> 1.5.11-2
- bump rel num and rebuild

* Thu May 22 2003 Brent Fox <bfox@redhat.com> 1.5.11-1
- check for the existence of hwclock before running (bug #91323)

* Thu May 22 2003 Brent Fox <bfox@redhat.com> 1.5.10-1
- pull zonetab classes out into separate file to fix bug (#90185)

* Tue May 20 2003 Brent Fox <bfox@redhat.com> 1.5.9-11
- copy actual timezone into /etc/localtime instead of making a symlink (bug #91228)

* Fri May 16 2003 Brent Fox <bfox@redhat.com> 1.5.9-10
- when using UTC, make /etc/localtime point to /usr/share/zoneinfo/UTC (bug #89132)

* Fri May 16 2003 Brent Fox <bfox@redhat.com> 1.5.9-9
- Added mnemonics to widgets that didn't have them (bug #91026)
- convert some timezone po files to utf-8 (bug #88461)

* Wed Feb 26 2003 Brent Fox <bfox@redhat.com> 1.5.9-8
- add requires for ntp (bug #85229)

* Fri Feb 21 2003 Brent Fox <bfox@redhat.com> 1.5.9-7
- remove dependency for gnome-python2-canvas, pygtk and ntp (bug #84837)

* Wed Feb 12 2003 Jeremy Katz <katzj@redhat.com> 1.5.9-6
- set codeset so that textmode works (#83518)

* Tue Feb 11 2003 Brent Fox <bfox@redhat.com> 1.5.9-5
- rebuild with latest docs

* Tue Feb 11 2003 Tammy Fox <tfox@redhat.com>
- updated docs

* Tue Feb  4 2003 Brent Fox <bfox@redhat.com> 1.5.9-4
- fall back to IP if we can't resolve it back to a hostname (bug #83463)

* Mon Feb  3 2003 Brent Fox <bfox@redhat.com> 1.5.9-3
- catch bogus ntp server names and raise a dialog

* Mon Feb  3 2003 Brent Fox <bfox@redhat.com> 1.5.9-2
- don't change value of ARC accidentally (bug #82281)

* Thu Jan 30 2003 Brent Fox <bfox@redhat.com> 1.5.9-1
- bump and build

* Wed Jan 29 2003 Brent Fox <bfox@redhat.com> 1.5.8-1
- use the new Red Hat ntp servers

* Thu Jan 16 2003 Brent Fox <bfox@redhat.com> 1.5.7-6
- catch error with no NTP server

* Wed Jan 15 2003 Brent Fox <bfox@redhat.com> 1.5.7-5
- write IPs to the server line instead of domain names (bug #70557)

* Tue Jan 14 2003 Brent Fox <bfox@redhat.com> 1.5.7-4
- list only stratum 2 ntp servers (bug #81629)

* Fri Jan 10 2003 Brent Fox <bfox@redhat.com> 1.5.7-3
- better check on ntp status by looking at initscrip return code
- sent ntp initscript output to /dev/null when calling os.system()

* Thu Jan  9 2003 Brent Fox <bfox@redhat.com> 1.5.7-2
- change to condrestart

* Fri Jan  3 2003 Brent Fox <bfox@redhat.com> 1.5.7-1
- create a TUI to replace timeconfig
- obsolete timeconfig

* Thu Jan  2 2003 Brent Fox <bfox@redhat.com> 1.5.6-3
- write an ipaddress for the restrict line (bug #80593)

* Mon Dec 23 2002 Brent Fox <bfox@redhat.com> 1.5.6-2
- handle missing ntpservers file
- don't pass in parent, it breaks firstboot
- handle busted ntp initscript

* Fri Dec 13 2002 Brent Fox <bfox@redhat.com> 1.5.5-2
- Print an error message if run from the console

* Fri Nov 15 2002 Brent Fox <bfox@redhat.com> 1.5.5-1
- Handle empty server lines in /etc/ntp.conf

* Tue Nov 12 2002 Brent Fox <bfox@redhat.com> 1.5.4-2
- Rebuild with latest translations

* Wed Oct 30 2002 Brent Fox <bfox@redhat.com>
- Add a build requires for python-tools

* Fri Oct 25 2002 Brent Fox <bfox@redhat.com> 1.5.4-1
- Write out an appropriate restrict line to /etc/ntp.conf
- Fixes bug 70557

* Tue Oct 22 2002 Brent Fox <bfox@redhat.com> 1.5.3-1
- Apply patch from katzj to fix bug 76313
- Fix bug 72149 correctly this time (hopefully)

* Mon Oct 14 2002 Brent Fox <bfox@redhat.com> 1.5.2-12
- Move ntpservers file into /etc/ntp.  Fixes bug 74339

* Thu Oct 10 2002 Brent Fox <bfox@redhat.com> 1.5.2-11
- Fix bug 72149.  Always apply timezone changes
- Fix bug 73498.  Apply UTC changes properly

* Tue Sep 03 2002 Brent Fox <bfox@redhat.com> 1.5.2-10
- convert desktop file to UTF8
- pull in latest translations

* Fri Aug 30 2002 Brent Fox <bfox@redhat.com> 1.5.2-9
- run chkconfig on starting/stopping ntpd

* Thu Aug 29 2002 Brent Fox <bfox@redhat.com> 1.5.2-8
- set the flag to close parent on non-NTP setups
- create an updateSpinButton function

* Tue Aug 27 2002 Brent Fox <bfox@redhat.com> 1.5.2-7
- Retrieve the only the first NTP server if there's more than one
- Only modify the first server entry if there's more than one

* Tue Aug 27 2002 Brent Fox <bfox@redhat.com> 1.5.2-6
- Handle the case of having no server line in ntp.conf

* Mon Aug 26 2002 Brent Fox <bfox@redhat.com> 1.5.2-5
- Raise error dialogs if NTP servers can't be contacted

* Wed Aug 21 2002 Brent Fox <bfox@redhat.com> 1.5.2-4
- pull translation domains from rhpl

* Wed Aug 21 2002 Brent Fox <bfox@redhat.com> 1.5.2-3
- Fix timezone selection bug

* Mon Aug 19 2002 Brent Fox <bfox@redhat.com> 1.5.2-2
- Convert desktop file to UTF-8

* Mon Aug 19 2002 Brent Fox <bfox@redhat.com> 1.5.2-1
- Limit ping timeout to 5 seconds.  We need a better solution for this in the future

* Tue Aug 13 2002 Brent Fox <bfox@redhat.com> 1.5.1-2
- Make spin buttons keyboard sensitive.  Fixes bug 68967

* Mon Aug 12 2002 Tammy Fox <tfox@redhat.com> 1.5.1-1
- replace System with SystemSetup in desktop file categories

* Tue Aug 06 2002 Brent Fox <bfox@redhat.com> 1.5-2
- use template ntp.conf file if the original has been removed for some reason

* Mon Aug 05 2002 Brent Fox <bfox@redhat.com> 1.5-1
- Fix translations for timezone list

* Fri Aug 02 2002 Brent Fox <bfox@redhat.com> 1.4-8
- Use new pam timestamp rules

* Wed Jul 31 2002 Brent Fox <bfox@redhat.com>1.4-7
- Put an end-of-line in /etc/ntp/step-tickers

* Thu Jul 25 2002 Brent Fox <bfox@redhat.com> 1.4-6
- Default to New York if the timezone in /etc/sysconfig/clock is bogus

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 1.4-5
- Fixed console file bad link

* Tue Jul 23 2002 Tammy Fox <tfox@redhat.com> 1.4-4
- Change desktop file name (bug #69470)
- Spec file fixes

* Thu Jul 18 2002 Brent Fox <bfox@redhat.com> 1.4-3
- Update for pygtk2 API change

* Wed Jul 17 2002 Brent Fox <bfox@redhat.com> 1.4-2
- Fix padding problem

* Fri Jul 12 2002 Tammy Fox <tfox@redhat.com> 1.4-1
- Updated docs for gtk2 interface
- Add note about security level and ntpd (bug #68039)
- Move desktop file to /usr/share/applications only

* Thu Jul 11 2002 Brent Fox <bfox@redhat.com> 1.3-4
- Remove some lingering references to dateconfig
- Create symbolic link from dateconfig to redhat-config-date

* Wed Jul 10 2002 Brent Fox <bfox@redhat.com> 1.3-1
- Rename dateconfig to redhat-config-date
- Check to see if we can ping ntp server before starting ntpd

* Tue Jul 9 2002 Brent Fox <bfox@redhat.com> 1.2-1
- Pull out ntp servers into a separate file
- Write /etc/ntp/step-tickers file

* Mon Jul 1 2002 Brent Fox <bfox@redhat.com> 1.1-3
- If an NTP server is already specified, add it to the combo list

* Fri Jun 28 2002 Brent Fox <bfox@redhat.com> 1.1-2
- Changed spacing of buttons on bottom of the window

* Thu Jun 27 2002 Tammy Fox <tfox@redhat.com> 1.1-2
- Added border widths to clean up interface
- Hooked up help
- Removed Apply button

* Thu Jun 27 2002 Brent Fox <bfox@redhat.com> 1.1-1
- Updated pot file and respective po files

* Sat Jun 22 2002 Brent Fox <bfox@redhat.com> 1.0.3-1
- Fixed bug 66655
- Fixed problem with selecting the current timezone in timezone_gui

* Mon Jun 17 2002 Brent Fox <bfox@redhat.com> 1.0.2-1
- Reenable the icon

* Thu May 30 2002 Brent Fox <bfox@redhat.com> 1.0.1-5
- Fixed translation bug

* Thu May 30 2002 Brent Fox <bfox@redhat.com> 1.0.1-4
- Removed Requires for pygnome

* Mon May 20 2002 Brent Fox <bfox@redhat.com> 1.0.1-3
- Pulled in documentation bugfix for bug #65228

* Mon May 13 2002 Brent Fox <bfox@redhat.com>
- Added Swedish translations to desktop file from menthos@menthos.com

* Thu May 2 2002 Brent Fox <bfox@redhat.com> 1.0.1-2
- Update for timezone translations

* Mon Apr 15 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.1-1
- Update for translations

* Mon Feb 25 2002 Brent Fox <bfox@redhat.com>
- Bump version to 1.0 

* Tue Feb 12 2002 Brent Fox <bfox@redhat.com>
- Finished port to Python2.2/GTK2
- Handle starting ntpd more gracefully
- Made variable naming more consistent

* Tue Jan 22 2002 Brent Fox <bfox@redhat.com>
- Replaced C code for timezone map with Python from anaconda
- Remove timezonemapmodule from /usr/lib/dateconfig

* Thu Oct 18 2001 Brent Fox <bfox@redhat.com>
- Put timezonemapmodule in /usr/lib/dateconfig

* Thu Aug 30 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.4-6
- Fix some character sets for translations (#52851)
- dateconfig.png isn't a config file, mark the config files as noreplace

* Mon Aug 27 2001 Tammy Fox <tfox@redhat.com>
- Updated docs for UTC button

* Thu Aug 16 2001 Brent Fox <bfox@redhat.com>
- Fix sizing for non-US languages

* Mon Aug 6 2001 Brent Fox <bfox@redhat.com>
- added redhat-config-time and redhat-config-date scripts

* Fri Aug 3 2001 Brent Fox <bfox@redhat.com>
- created an icon 
- fixed install process to install icon and drop a file in /etc/X11/sysconfig

* Fri Aug  3 2001 Preston Brown <pbrown@redhat.com>
- set hardware clock as well.

* Fri Jul 27 2001 Yukihiro Nakai <ynakai@redhat.com>
- Add Japanese translation.

* Fri Jul 20 2001 Tammy Fox <tfox@redhat.com>
- added i18n stuff
* Wed Jul 04 2001 Karsten Hopp <karsten@redhat.de>
- fix install-path (INSTROOT)
* Tue Jun 27 2001 Tammy Fox <tfox@redhat.com>
- added help and help button
* Sun Jun 24 2001 Brent Fox <bfox@redhat.com>
- got starting and stopping of ntpd working
- enabled detection of whether ntpd is currently running 
- added msf to author list
* Thu Jun 21 2001 Brent Fox <bfox@redhat.com>
- fixed problem with system path in timezone_gui.py
* Wed Jun 13 2001 Tammy Fox <tfox@redhat.com>
- improved man page
* Tue Jun 12 2001 Tammy Fox <tfox@redhat.com>
- added console access, fixed Makefile and spec file
* Mon Jun 11 2001 Brent Fox <bfox@redhat.com>
- added ntp section and timezone section
* Sun Jan 28 2001 Brent Fox <bfox@redhat.com>
- initial coding and packaging

