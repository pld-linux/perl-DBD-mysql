#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests require access to a working MySQL
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	mysql
Summary:	A MySQL interface for Perl
Summary(cs):	MySQL rozhranМ pro Perl
Summary(da):	En MySQL-grФnseflade for Perl
Summary(de):	Ein MySQL Interface fЭr Perl
Summary(es):	Interfaz MySQL para Perl
Summary(fr):	Interface MySQL pour Perl
Summary(it):	Interfaccia MySQL per Perl
Summary(ja):	Perl ╓н MySQL ╔╓╔С╔©║╪╔у╔╖╔╓╔╧
Summary(ko):	фчю╩ ю╖гя MySQL юнемфДюл╫╨
Summary(nb):	Et MySQL-grensesnitt for Perl
Summary(pl):	DBD::mysql - perlowy interfejs do MySQL-a
Summary(pt):	Uma interface de Perl para o MySQL
Summary(pt_BR):	Uma interface de Perl para o MySQL
Summary(ru):	Интерфейс MySQL для Perl
Summary(sv):	Ett grДnssnitt till MySQL fЖr Perl
Summary(uk):	Perl-╕нтерфейс до MySQL
Summary(zh_CN):	Perl ╣д MySQL ╫ГцФ║ё
Name:		perl-DBD-mysql
Version:	3.0004
Release:	3
# NOTE: libmysqlclient infects everything that links against it with GPL
License:	GPL (perl code also Artistic)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d328b9fdaf899eba6d72258242ad0a0
URL:		http://search.cpan.org/dist/DBD-mysql/
BuildRequires:	mysql-devel
BuildRequires:	perl-DBI >= 1.13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-DBD-Mysql
Obsoletes:	perl-DBD-MySQL
Obsoletes:	perl-Msql-Mysql-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M(y)sql.pm and DBD::mSQL(mysql) implement two different approaches to
communicate with an mSQL or MySQL server. DBD::mSQL(mysql) is built
upon the DBI, the generic Perl Database Interface. It brings you an
identical interface to a broad variety of databases and is in this
regard comparable to ODBC. The advantage of the DBI approach is
portability and interoperability. M(y)sql.pm are the elder species.
They were written before DBI was available but inspired by an early
draft of the DBI specification. As they have been circulating longer
they are more mature and pretty stable. They're also more complete
than DBD::mSQL and DBD::mysql.

%description -l cs
Implementace DBI pro MySQL do Perlu.

%description -l da
En implementation af DBI for MySQL.

%description -l de
Eine Implementierung von DBI fЭr MySQL.

%description -l es
ImplementaciСn del DBI para MySQL.

%description -l fr
Mise en oeuvre de DBI pour MySQL.

%description -l it
Implementazione di DBI per MySQL.

%description -l ja
MySQL мя DBI ╪баУ

%description -l ko
MySQLю╩ ю╖гя DBIюг ╫ггЖ.

%description -l nb
En implementasjon av DBI for MySQL.

%description -l pl
Sterownik pozwalaj╠cy na dostЙp do baz MySQL z poziomu Perla.

%description -l pt
Uma implementaГЦo de DBI para o MySQL.

%description -l pt_BR
Uma implementaГЦo de DBI para o MySQL.

%description -l ru
M(y)sql.pm и DBD::mSQL(mysql) реализуют два разных подхода к общению с
сервером mSQL или MySQL. DBD::mSQL(mysql) построен на базе DBI,
стандартного Perl-интерфейса к базам данных. Он предоставляет
единообразный интерфейс к самым разнообразным базам данных и сравним в
этом отношении с ODBC. Преимуществами подхода DBI является легкая
портируемость и взаимодйествие. M(y)sql.pm - это более старые особи.
Они были написаны до того, как стал доступным DBI, но основываются на
ранних черновиках спецификации DBI. Так как они используются дольше,
они более отлажены и стабильны. Также они более завершенные, чем
DBD::mSQL и DBD::mysql.

%description -l sv
En implementation av DBI fЖr MySQL.

%description -l uk
M(y)sql.pm та DBD::mSQL(mysql) реал╕зують два р╕зних п╕дходи до
сп╕лкування з сервером mSQL або MySQL. DBD::mSQL(mysql) побудовано на
баз╕ DBI, стандартного ╕нтерфейсу Perl до баз даних. В╕н нада╓
╕дентичний ╕нтерфейс до самих р╕зноман╕тних баз даних ╕ може бути
пор╕вняний в цьому в╕дношенн╕ з ODBC. Перевагами п╕дходу DBI ╓ легка
переносим╕сть та вза╓мод╕я. M(y)sql.pm - це б╕льш стар╕ програми. Вони
були написан╕ до того, як з'явився DBI, але базуються на ранн╕х
проектах спецификац╕╖ DBI. Виходячи з того, що вони використовуються
довше, вони б╕льш в╕длагоджен╕ та стаб╕льн╕. Також вони б╕льш
завершен╕, н╕ж DBD::mSQL та DBD::mysql.

%description -l zh_CN
р╩жж MySQL ╣д DBI й╣й╘╢Кй╘║ё

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# we don't need no bundles
rm -rf lib/Bundle

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{?perl_install_postclean}
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pdir}/%{pnam}/INSTALL.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorarch}/DBD/mysql.pm
%dir %{perl_vendorarch}/DBD/mysql
%{perl_vendorarch}/DBD/mysql/GetInfo.pm
%{perl_vendorarch}/Mysql
%{perl_vendorarch}/Mysql.pm
%dir %{perl_vendorarch}/auto/DBD/mysql
%{perl_vendorarch}/auto/DBD/mysql/mysql.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/mysql/mysql.so
%{_mandir}/man3/[DM]*
