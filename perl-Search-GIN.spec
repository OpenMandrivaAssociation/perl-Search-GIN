%define upstream_name    Search-GIN
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generalized Inverted Indexing for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Search/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Stream::Bulk)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl(MooseX::Types::Set::Object)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Set::Object)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::TempDir)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(File::NFSLock)
BuildArch:	noarch

%description
This is used by the KiokuDB manpage for custom indexing.

More documentation will be released shortly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 658163
- add r
- rebuild for updated spec-helper

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1
+ Revision: 635242
- update to new version 0.08

* Thu Jan 06 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 629072
- new upstream tarball, with same version number (sic)

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 596644
- update to 0.07

* Fri Jul 30 2010 Shlomi Fish <shlomif@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 563367
- import perl-Search-GIN


* Fri Jul 30 2010 Shlomi Fish <shlomif@iglu.org.il> 0.04-1mdv
- Updated to the new version.

* Fri Feb 05 2010 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
