%global pypi_name oslo.middleware

Name:           python-oslo-middleware
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo Middleware library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
# for docs build
BuildRequires:  python-oslo-config
BuildRequires:  python-oslo-context
BuildRequires:  python-oslo-i18n

Requires:       python-babel
Requires:       python-jinja2
Requires:       python-oslo-config
Requires:       python-oslo-context
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-six
Requires:       python-stevedore
Requires:       python-webob

%description
The OpenStack Oslo Middleware library.
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

%package doc
Summary:    Documentation for the Oslo Middleware library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description doc
Documentation for the Oslo Middleware library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

#delete tests
rm -fr %{buildroot}%{python2_sitelib}/%{pypi_name}/tests/

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_middleware
%{python2_sitelib}/*.egg-info
# compatibility oslo namespace
%{python2_sitelib}/oslo
%{python2_sitelib}/*-nspkg.pth

%files doc
%license LICENSE
%doc html

%changelog
