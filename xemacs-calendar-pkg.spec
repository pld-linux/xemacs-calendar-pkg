Summary:	Calendar and diary support
Summary(pl):	Kalendarz i dziennik dla XEmacsa
Name:		xemacs-calendar-pkg
%define 	srcname	calendar
Version:	1.23
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	de5fd826168913232c48aa88ec0f1d5c
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs calendar and diary modes Read about Calendar in XEmacs info
manual. To let XEmacs automatically remid you about uopcoming events,
add this to you ~/.emacs:
(require 'appt)
(display-time)
(appt-initialize)
(diary)

%description -l pl
Kalendarz i dziennik dla XEmacsa. Opis znale¼æ mo¿na w podrêczniku
XEmacsa (szukaj Calendar). Aby XEmacs sam przypomina³ o nadchodz±cych
wydarzeniach, warto dopisaæ do ~/.emacs:
(require 'appt)
(display-time)
(appt-initialize)
(setq european-calendar-style t)
(diary)

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/calendar/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
