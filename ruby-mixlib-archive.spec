#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	mixlib-archive
Summary:	A simple interface to various archive formats
Name:		ruby-%{pkgname}
Version:	0.4.8
Release:	1
License:	APACHE-2.0
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	fd5990c8bb77045692dc40d03e417b09
URL:		https://github.com/chef/mixlib-archive
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rake < 13
BuildRequires:	ruby-rake >= 12
BuildRequires:	ruby-rspec < 4
BuildRequires:	ruby-rspec >= 3.0
%endif
Requires:	ruby-mixlib-log
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple interface to various archive formats.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/mixlib/archive.rb
%{ruby_vendorlibdir}/mixlib/archive
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
