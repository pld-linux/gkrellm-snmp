Summary:	SNMP monitor plugin for gkrellm
Summary(pl):	Plugin gkrellm z monitorem SNMP
Summary(pt_BR):	Plugin gkrellm para monitoração SNMP
Name:		gkrellm-snmp
Version:	0.18
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://triq.net/gkrellm/gkrellm_snmp-%{version}.tar.gz
URL:		http://triq.net/gkrellm.html
BuildRequires:	gkrellm-devel
BuildRequires:	ucd-snmp-devel >= 4.2.6
BuildRequires:	imlib-devel
Requires:	gkrellm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
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

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README ChangeLog FAQ TODO
%attr(755,root,root) %{_libdir}/gkrellm/gkrellm_snmp.so
