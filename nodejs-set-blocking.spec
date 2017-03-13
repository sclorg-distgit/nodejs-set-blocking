%{?scl:%scl_package nodejs-set-blocking}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name set-blocking

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    2.0.0
Release:    2%{?dist}
Summary:    Set blocking stdio and stderr ensuring that terminal output does not truncate
License:    ISC
URL:        https://github.com/yargs/set-blocking#readme
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Set blocking stdio and stderr ensuring that terminal output does not truncate

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE.txt
%doc README.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-2
- Initial build

