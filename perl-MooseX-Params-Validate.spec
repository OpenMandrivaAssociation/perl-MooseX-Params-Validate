%define upstream_name    MooseX-Params-Validate
%define upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	An extension of Params::Validate for using Moose's types
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-Params-Validate-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Devel::Caller)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
BuildArch:	noarch

%description
This module fills a gap in Moose by adding method parameter validation to
Moose. This is just one of many developing options, it should not be
considered the "official" one by any means though.

You might also want to explore 'MooseX::Method::Signatures' and
'MooseX::Declare'

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc  README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 657798
- rebuild for updated spec-helper

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1
+ Revision: 635190
- update to new version 0.16

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 612305
- update to new version 0.15

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 526449
- update to 0.14

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 472242
- update to 0.13

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 393831
- adding missing buildrequires:
- using %%perl_convert_version
- fixed license field

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.12

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2010.0
+ Revision: 391187
- update to new version 0.10

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.09-2mdv2010.0
+ Revision: 375939
- rebuild

* Mon Apr 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 366767
- import perl-MooseX-Params-Validate


* Mon Apr 13 2009 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist


