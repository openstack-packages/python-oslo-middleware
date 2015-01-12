%global pypi_name oslo.middleware
%global pkg_name oslo-middleware

Name:           python-oslo-middleware
Version:        XXX
Release:        XXX{?dist}
Summary:        OpenStack oslo.middleware library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-oslo-config
Requires:       python-oslo-i18n
Requires:       python-six
Requires:       python-webob

%description
An OpenStack library for middleware.

%package doc
Summary:    Documentation for the Oslo middleware library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description doc
Documentation for the Oslo middleware library.

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
%doc README.rst LICENSE
%{python2_sitelib}/oslo
%{python2_sitelib}/oslo_middleware
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*-nspkg.pth

%files doc
%doc html LICENSE


%changelog
* Mon Oct 20 2014 Dan Prince <dprince@redhat.com> - XXX
- Initial package
