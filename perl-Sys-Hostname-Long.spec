#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sys-Hostname-Long
Version  : 1.5
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/S/SC/SCOTT/Sys-Hostname-Long-1.5.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SC/SCOTT/Sys-Hostname-Long-1.5.tar.gz
Summary  : 'Try every conceivable way to get full hostname'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
Sys::Hostname::Long
===================
INSTALLATION
To install this module type the following:

%package dev
Summary: dev components for the perl-Sys-Hostname-Long package.
Group: Development
Provides: perl-Sys-Hostname-Long-devel = %{version}-%{release}

%description dev
dev components for the perl-Sys-Hostname-Long package.


%prep
%setup -q -n Sys-Hostname-Long-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Sys/Hostname/Long.pm
/usr/lib/perl5/vendor_perl/5.28.0/Sys/Hostname/testall.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sys::Hostname::Long.3
