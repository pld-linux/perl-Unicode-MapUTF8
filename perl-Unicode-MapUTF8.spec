#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	MapUTF8
Summary:	Unicode::MapUTF8 - Conversions to and from arbitrary character sets and UTF8
Summary(pl):	Unicode::MapUTF8 - konwersje miêdzy dowolnym zestawem znaków a UTF8
Name:		perl-Unicode-MapUTF8
Version:	1.09
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Jcode
BuildRequires:	perl-Unicode-Map
BuildRequires:	perl-Unicode-Map8
BuildRequires:	perl-Unicode-String
%endif
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::MapUTF8 provides an adapter layer between core routines for
converting to and from UTF8 and other encodings.  In essence, a way to
give multiple existing Unicode modules a single common interface so
you don't have to know the underlaying implementations to do simple
UTF8 to-from other character set encoding conversions.  As such, it
wraps the Unicode::String, Unicode::Map8, Unicode::Map and Jcode
modules in a standardized and simple API.

%description -l pl
Unicode::MapUTF8 udostêpnia warstwê po¶redni± pomiêdzy wewnêtrznymi
funkcjami do konwersji pomiêdzy UTF8 a innymi kodowaniami. W
szczególno¶ci jest sposobem na udostêpnienie wielu istniej±cym modu³om
Unicode wspólnego interfejsu, dziêki czemu nie trzeba znaæ
implementacji ka¿dego modu³u do zastosowania prostej konwersji z/do
UTF8. Unicode::MapUTF8 opakowuje modu³y Unicode::String,
Unicode::Map8, Unicode::Map i Jcode w ustandaryzowane i proste API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
