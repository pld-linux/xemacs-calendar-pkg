Summary:	Calendar and diary support
Summary(pl):	Kalendarz i dziennik dle XEmacsa
Name:		xemacs-calendar-pkg
%define 	srcname	calendar
Version:	1.18
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	1fbd29614f2b1b29494dc2ea3241c16a
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
Kalendarz i dziennik dla XEmacsa. Opis znale�� mo�na w podr�czniku
XEmacsa (szukaj Calendar). Aby XEmacs sam przypomina� o nadchodz�cych
wydarzeniach, warto dopisa� do ~/.emacs:
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

gzip -9nf lisp/calendar/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/calendar/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
