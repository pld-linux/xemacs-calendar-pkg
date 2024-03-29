Summary:	Calendar and diary support
Summary(pl.UTF-8):	Kalendarz i dziennik dla XEmacsa
Name:		xemacs-calendar-pkg
%define 	srcname	calendar
Version:	1.38
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	58bb8539f0983d1824ecacd402326301
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

%description -l pl.UTF-8
Kalendarz i dziennik dla XEmacsa. Opis znaleźć można w podręczniku
XEmacsa (szukaj Calendar). Aby XEmacs sam przypominał o nadchodzących
wydarzeniach, warto dopisać do ~/.emacs:
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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/calendar/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
