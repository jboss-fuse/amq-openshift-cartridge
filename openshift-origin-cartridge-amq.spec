%global cartridgedir %{_libexecdir}/openshift/cartridges/amq
%global frameworkdir %{_libexecdir}/openshift/cartridges/amq

%global product_build_number 389

Name: openshift-origin-cartridge-amq
Version: 6.1.0.redhat.%{product_build_number}
Release: 1%{?dist}
Summary: A-MQ cartridge
Group: Development/Languages
License: ASL 2.0
URL: https://www.openshift.com
Source0: https://github.com/jboss-fuse/amq-openshift-cartridge/archive/openshift-enterprise-rpm-6.1.zip
Source1: http://repository.jboss.org/nexus/content/groups/ea/org/jboss/amq/jboss-a-mq/6.1.0.redhat-%{product_build_number}/jboss-a-mq-6.1.0.redhat-%{product_build_number}.zip
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
A-MQ cartridge for openshift.


%prep
%setup -q -n amq-openshift-cartridge-openshift-enterprise-rpm-6.1

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
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Wed Jul 09 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.385-2
- RPM version of the AMQ cart

* Thu Mar 24 2014 Hiram Chirino <hchirino@redhat.com> 0.1.0
- Initial implementation based on the AMQ cartridge

