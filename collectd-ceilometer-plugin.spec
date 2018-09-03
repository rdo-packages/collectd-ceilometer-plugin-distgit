%global pypi_name collectd-ceilometer-plugin
%if 0%{?fedora} > 12
%global with_python3 1
%else
%global with_python3 0
%endif

Name:           %{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        OpenStack Ceilometer plugin for collectd

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-hacking
BuildRequires:  python-coverage
BuildRequires:  python-flake8
BuildRequires:  python-mock
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslotest
BuildRequires:  python-os-testr
BuildRequires:  python-testrepository
BuildRequires:  pylint
BuildRequires:  python-subunit
BuildRequires:  python-sphinx
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx


%description
OpenStack Ceilometer plugin for collectd. This plugin
for collectd publishes telemetry data gathered by collectd to Ceilometer. This
enables a more comprehensive telemetry set to be made available to Ceilometer
which will enable smarter scheduling and environmental service assurance.

%package -n     python2-%{pypi_name}
Summary:        OpenStack Ceilometer plugin for collectd
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python-requests
Requires:       libvirt-python
Requires:       python-pbr
Requires:       python-babel
%description -n python2-%{pypi_name}
OpenStack Ceilometer plugin for collectd. This plugin
for collectd publishes telemetry data gathered by collectd to Ceilometer. This
enables a more comprehensive telemetry set to be made available to Ceilometer
which will enable smarter scheduling and environmental service assurance.

%if 0%{?with_python3} > 0
%package -n     python3-%{pypi_name}
Summary:        OpenStack Ceilometer plugin for collectd
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-requests
Requires:       libvirt-python3
Requires:       python3-pbr
Requires:       python3-babel

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-hacking
BuildRequires:  python3-coverage
BuildRequires:  python3-flake8
BuildRequires:  python3-mock
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-os-testr
BuildRequires:  python3-testrepository
BuildRequires:  python3-pylint
BuildRequires:  python3-subunit
BuildRequires:  python3-sphinx
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-setuptools
%description -n python3-%{pypi_name}
OpenStack Ceilometer plugin for collectd. This plugin
for collectd publishes telemetry data gathered by collectd to Ceilometer. This
enables a more comprehensive telemetry set to be made available to Ceilometer
which will enable smarter scheduling and environmental service assurance.
%endif

%package -n python-%{pypi_name}-doc
Summary:        collectd-ceilometer-plugin documentation
%description -n python-%{pypi_name}-doc
Documentation for collectd-ceilometer-plugin

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%if 0%{?with_python3} > 0
%py3_build
%endif
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3} > 0
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
%endif

%py2_install


%check
%{__python2} setup.py testr --slowest

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python2_sitelib}/collectd_ceilometer
%{python2_sitelib}/collectd_ceilometer_plugin-%{version}-py?.?.egg-info

%if 0%{?with_python3} > 0
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/collectd_ceilometer
%{python3_sitelib}/collectd_ceilometer_plugin-%{version}-py?.?.egg-info
%endif

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html

%changelog
* Wed Feb 22 2017 Matthias Runge <mrunge@redhat.com> - 1.0.1-2
- libvirt-python3 instead of python3-libvirt-python

* Wed Dec 07 2016 Matthias Runge <mrunge@redhat.com> - 1.0.1-1
- Initial package.
