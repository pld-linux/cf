# TODO: optlags
Summary:	Console Fucker - attaching to Linux console remotely
Summary(pl):	Console Fucker - zdalne pod³±czanie siê do konsoli linuksowej
Name:		cf
Version:	0.7.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://glen.alkohol.ee/cf/%{name}-%{version}.tar.bz2
# Source0-md5:	503093d7c2b31c8b70aede7bdf1e8afd
URL:		http://glen.alkohol.ee/cf/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Console Fucker program allows you 'attach' Linux console remotely.

%description -l pl
Program Console Fucker pozwala na zdalne pod³±czanie siê do konsoli
linuksowej.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}

install cf $RPM_BUILD_ROOT%{_sbindir}
ln -s ../sbin/cf $RPM_BUILD_ROOT%{_bindir}/cdump

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/cf
%attr(755,root,root) %{_bindir}/cdump
