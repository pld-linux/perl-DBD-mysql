%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	mysql
Summary:	DBD::mysql perl module
Summary(pl):	Modu³ perla DBD::mysql
Name:		perl-DBD-mysql
Version:	2.1017
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI >= 1.13
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL for Perl is the driver code that enables Perl to access MySQL
databases via the DBI module.

%description -l pl
Sterownik pozwalaj±cy na dostêp do baz MySQL z poziomu Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/DBD/mysql.pm
%{perl_sitearch}/Mysql
%{perl_sitearch}/Mysql.pm
%dir %{perl_sitearch}/auto/DBD/mysql
%{perl_sitearch}/auto/DBD/mysql/mysql.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/mysql/mysql.so
%{_mandir}/man3/[DM]*
