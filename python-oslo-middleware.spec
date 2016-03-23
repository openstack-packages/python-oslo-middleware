%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global pypi_name oslo.middleware
%global pkg_name oslo-middleware

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-oslo-middleware
Version:        3.7.0
Release:        1%{?dist}
Summary:        OpenStack Oslo Middleware library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python2-%{pkg_name}
Summary:        OpenStack Oslo Middleware library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
# for docs build
BuildRequires:  python-oslo-config
BuildRequires:  python-oslo-context
BuildRequires:  python-oslo-i18n
BuildRequires:  python-oslo-utils
# Required for testing
BuildRequires:  python-fixtures
BuildRequires:  python-hacking
BuildRequires:  python-mock
BuildRequires:  python-oslotest
BuildRequires:  python-testtools
BuildRequires:  python-webob

Requires:       python-babel
Requires:       python-jinja2
Requires:       python-oslo-config
Requires:       python-oslo-context
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-six
Requires:       python-stevedore
Requires:       python-webob

%description -n python2-%{pkg_name}
The OpenStack Oslo Middleware library.
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Middleware library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# for docs build
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-context
BuildRequires:  python3-oslo-i18n
# Required for testing
BuildRequires:  python3-fixtures
BuildRequires:  python3-hacking
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-testtools
BuildRequires:  python3-webob

Requires:       python3-babel
Requires:       python3-jinja2
Requires:       python3-oslo-config
Requires:       python3-oslo-context
Requires:       python3-oslo-i18n
Requires:       python3-oslo-utils
Requires:       python3-six
Requires:       python3-stevedore
Requires:       python3-webob

%description -n python3-%{pkg_name}
The OpenStack Oslo Middleware library.
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Middleware library

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-fixtures
Requires:  python3-hacking
Requires:  python3-mock
Requires:  python3-oslotest
Requires:  python3-testtools

%description -n python3-%{pkg_name}-tests
Tests for the Oslo Middleware library.

%endif

%package doc
Summary:    Documentation for the Oslo Middleware library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description doc
Documentation for the Oslo Middleware library.

%package -n python2-%{pkg_name}-tests
Summary:    Tests for the Oslo Middleware library

Requires:  python-%{pkg_name} = %{version}-%{release}
Requires:  python-fixtures
Requires:  python-hacking
Requires:  python-mock
Requires:  python-oslotest
Requires:  python-testtools

%description -n python2-%{pkg_name}-tests
Tests for the Oslo Middleware library.

%description
The OpenStack Oslo Middleware library.
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -rf {test-,}requirements.txt

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif

%files -n python2-%{pkg_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_middleware
%{python2_sitelib}/*.egg-info
%exclude %{python2_sitelib}/oslo_middleware/tests/

%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_middleware
%{python3_sitelib}/*.egg-info

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_middleware/tests/
%endif

%files doc
%license LICENSE
%doc html

%files -n python2-%{pkg_name}-tests
%{python2_sitelib}/oslo_middleware/tests/

%changelog
* Wed Mar 23 2016 Haikel Guemar <hguemar@fedoraproject.org> 3.7.0-
- Update to 3.7.0

