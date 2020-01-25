#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Unicode
%define		pnam	MapUTF8
Summary:	Unicode::MapUTF8 - conversions to and from arbitrary character sets and UTF8
Summary(pl.UTF-8):	Unicode::MapUTF8 - konwersje między dowolnym zestawem znaków a UTF8
Name:		perl-Unicode-MapUTF8
Version:	1.11
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16e66ee0bdc0e6cc9c36e29212d8ffdc
URL:		http://search.cpan.org/dist/Unicode-MapUTF8/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Jcode
BuildRequires:	perl-Unicode-Map
BuildRequires:	perl-Unicode-Map8
BuildRequires:	perl-Unicode-String
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::MapUTF8 provides an adapter layer between core routines for
converting to and from UTF8 and other encodings. In essence, a way to
give multiple existing Unicode modules a single common interface so
you don't have to know the underlaying implementations to do simple
UTF8 to-from other character set encoding conversions. As such, it
wraps the Unicode::String, Unicode::Map8, Unicode::Map and Jcode
modules in a standardized and simple API.

%description -l pl.UTF-8
Unicode::MapUTF8 udostępnia warstwę pośrednią pomiędzy wewnętrznymi
funkcjami do konwersji pomiędzy UTF8 a innymi kodowaniami. W
szczególności jest sposobem na udostępnienie wielu istniejącym modułom
Unicode wspólnego interfejsu, dzięki czemu nie trzeba znać
implementacji każdego modułu do zastosowania prostej konwersji z/do
UTF8. Unicode::MapUTF8 opakowuje moduły Unicode::String,
Unicode::Map8, Unicode::Map i Jcode w ustandaryzowane i proste API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Unicode/MapUTF8.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
