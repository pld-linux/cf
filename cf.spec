Summary:	Console Fucker - attaching to Linux console remotely
Summary(pl.UTF-8):	Console Fucker - zdalne podłączanie się do konsoli linuksowej
Name:		cf
Version:	0.7.4
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://glen.alkohol.ee/cf/%{name}-%{version}.tar.bz2
# Source0-md5:	33ca5671128a6dd0c5af0e8c14f67c89
URL:		http://glen.alkohol.ee/cf/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Console Fucker program allows you 'attach' Linux console remotely.

%description -l pl.UTF-8
Program Console Fucker pozwala na zdalne podłączanie się do konsoli
linuksowej.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}

install cf $RPM_BUILD_ROOT%{_sbindir}
ln -s ../sbin/cf $RPM_BUILD_ROOT%{_bindir}/cdump

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/cf
%attr(755,root,root) %{_bindir}/cdump
