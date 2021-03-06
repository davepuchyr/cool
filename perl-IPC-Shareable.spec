Name:           perl-IPC-Shareable
Version:        0.61
Release:        1%{?dist}
Summary:        Share Perl variables between processes
License:        Distributable, see COPYING
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Shareable/
Source0:        http://www.cpan.org/authors/id/M/MS/MSOUTH/IPC-Shareable-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable) >= 0.607
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
IPC::Shareable allows you to tie a variable to shared memory making it easy
to share the contents of that variable with other Perl processes. Scalars,
arrays, and hashes can be tied. The variable being tied may contain
arbitrarily complex data structures - including references to arrays,
hashes of hashes, etc.

%prep
%setup -q -n IPC-Shareable-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING CREDITS DISCLAIMER README README.md TO_DO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Apr 30 2016 dave.puchyr@avaritia.com 0.61-1
- Specfile autogenerated by cpanspec 1.78.
