Name: gkrellm-snmp
Version: 0.10pre
Release: 1cl
Summary: SNMP monitor plugin for gkrellm
Summary(pt_BR): Plugin gkrellm para monitoração SNMP
Summary(es): SNMP monitor plugin for gkrellm
License: GPL
Group: X11
Group(pt_BR): X11
Group(es): X11
Source: http://triq.net/gkrellm/gkrellm_snmp-0.10-pre.tar.gz
Requires: gkrellm >= 1.0.2, ucd-snmp
BuildRequires: gkrellm-devel, gtk+-devel, imlib-devel, ucd-snmp-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
A GKrellM plugin which lets you monitor SNMP variables.

%description -l pt_BR
Um plugin GKrellM para monitoração de variáveis SNMP.

%description -l es
A GKrellM plugin which lets you monitor SNMP variables.

%prep
%setup -q -n gkrellm_snmp-0.10

%build
CFLAGS="%{optflags}" make

%install
rm -rf %{buildroot}
install -D -m644 gkrellm_snmp.so %{buildroot}%{_libdir}/gkrellm/plugins/gkrellm_snmp.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog FAQ TODO
%{_libdir}/gkrellm/plugins/gkrellm_snmp.so

%changelog
* Thu Nov 30 2000 Claudio Matsuoka <claudio@conectiva.com>
- package created
