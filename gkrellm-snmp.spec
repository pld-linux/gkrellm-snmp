Summary:	SNMP monitor plugin for gkrellm
Summary(pl.UTF-8):	Plugin gkrellm z monitorem SNMP
Summary(pt_BR.UTF-8):	Plugin gkrellm para monitoração SNMP
Name:		gkrellm-snmp
Version:	0.21
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://triq.net/gkrellm/gkrellm_snmp-%{version}.tar.gz
# Source0-md5:	f90d86413fb8f25c4f31a5ed9dc21b98
Patch0:		%{name}-makefile.patch
URL:		http://triq.net/gkrellm.html
BuildRequires:	gkrellm-devel
BuildRequires:	imlib-devel
BuildRequires:	net-snmp-compat-libs
BuildRequires:	net-snmp-devel
Requires:	gkrellm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GKrellM plugin which lets you monitor SNMP variables.

%description -l pl.UTF-8
Plugin GKrellM pozwalający monitorować zmienne SNMP.

%description -l pt_BR.UTF-8
Um plugin GKrellM para monitoração de variáveis SNMP.

%prep
%setup -q -n gkrellm_snmp-%{version}
%patch0 -p1

%build
%{__make} netsnmp \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

install gkrellm_snmp.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog FAQ TODO
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellm_snmp.so
