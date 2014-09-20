%global cartridgedir %{_libexecdir}/openshift/cartridges/amq
%global frameworkdir %{_libexecdir}/openshift/cartridges/amq

Name: openshift-origin-cartridge-amq
Version: 0.1.0
Release: 1%{?dist}
Summary: Red Hat JBoss A-MQ cartridge
Group: Development/Languages
License: ASL 2.0
URL: https://www.openshift.com
Source0: %{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Red Hat JBoss A-MQ cartridge for openshift. (Cartridge Format V2)


%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
cp -r * %{buildroot}%{cartridgedir}/

%clean
rm -rf %{buildroot}


%post

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%dir %{cartridgedir}/bin
%dir %{cartridgedir}/env
%dir %{cartridgedir}/metadata
%dir %{cartridgedir}/versions
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{frameworkdir}
%{_sysconfdir}/openshift/cartridges/v2/%{name}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Thu Mar 24 2014 Hiram Chirino <hchirino@redhat.com> 0.1.0-1
- Initial implementation based on the AMQ cartridge


