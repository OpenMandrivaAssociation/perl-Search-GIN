%define upstream_name    Search-GIN
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Generalized Inverted Indexing for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/Search-GIN
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Search-GIN-%{upstream_version}.tar.gz

BuildRequires:	make
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
BuildRequires:	perl(namespace::autoclean)
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

