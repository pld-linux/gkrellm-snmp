Summary:	SNMP monitor plugin for gkrellm
Summary(es):	SNMP monitor plugin for gkrellm
Summary(pl):	Plugin gkrellm z monitorem SNMP
Summary(pt_BR):	Plugin gkrellm para monitoração SNMP
Name:		gkrellm-snmp
Version:	0.17
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://triq.net/gkrellm/gkrellm_snmp-%{version}.tar.gz
BuildRequires:	gkrellm-devel
BuildRequires:	ucd-snmp-devel >= 4.2.1
BuildRequires:	imlib-devel
Requires:	gkrellm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A GKrellM plugin which lets you monitor SNMP variables.

%description -l es
A GKrellM plugin which lets you monitor SNMP variables.

%description -l pl
Plugin GKrellM pozwalaj±cy monitorowaæ zmienne SNMP.

%description -l pt_BR
Um plugin GKrellM para monitoração de variáveis SNMP.

%prep
%setup -q -n gkrellm_snmp-%{version}

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm

install gkrellm_snmp.so $RPM_BUILD_ROOT%{_libdir}/gkrellm

gzip -9nf README ChangeLog FAQ TODO

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gkrellm/gkrellm_snmp.so
