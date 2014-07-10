%global cartridgedir %{_libexecdir}/openshift/cartridges/amq
%global frameworkdir %{_libexecdir}/openshift/cartridges/amq

Name: amq-openshift-cartridge-openshift-enterprise-rpm
Version: 6.1.0.redhat.385
Release: 2%{?dist}
Summary: A-MQ cartridge
Group: Development/Languages
License: ASL 2.0
URL: https://www.openshift.com
Source0: https://github.com/jboss-fuse/amq-openshift-cartridge/archive/openshift-enterprise-rpm-6.1-6.1.0.redhat.385-2.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
A-MQ cartridge for openshift.


%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
mkdir -p %{buildroot}/%{_sysconfdir}/openshift/cartridges
cp -r * %{buildroot}%{cartridgedir}/
ln -s %{cartridgedir}/conf/ %{buildroot}/%{_sysconfdir}/openshift/cartridges/%{name}


%clean
rm -rf %{buildroot}


%post
%{_sbindir}/oo-admin-cartridge --action install --offline --source /usr/libexec/openshift/cartridges/amq

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%dir %{cartridgedir}/bin
%dir %{cartridgedir}/env
%dir %{cartridgedir}/metadata
%dir %{cartridgedir}/versions
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{frameworkdir}
%{_sysconfdir}/openshift/cartridges/%{name}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Wed Jul 09 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.385-2
- RPM version of the AMQ cart

* Thu Mar 24 2014 Hiram Chirino <hchirino@redhat.com> 0.1.0
- Initial implementation based on the AMQ cartridge

