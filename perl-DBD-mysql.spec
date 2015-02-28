#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests require access to a working MySQL

%define		pdir	DBD
%define		pnam	mysql
%include	/usr/lib/rpm/macros.perl
Summary:	A MySQL interface for Perl
Summary(cs.UTF-8):	MySQL rozhraní pro Perl
Summary(da.UTF-8):	En MySQL-grænseflade for Perl
Summary(de.UTF-8):	Ein MySQL Interface für Perl
Summary(es.UTF-8):	Interfaz MySQL para Perl
Summary(fr.UTF-8):	Interface MySQL pour Perl
Summary(it.UTF-8):	Interfaccia MySQL per Perl
Summary(ja.UTF-8):	Perl の MySQL インターフェイス
Summary(ko.UTF-8):	펄을 위한 MySQL 인터페이스
Summary(nb.UTF-8):	Et MySQL-grensesnitt for Perl
Summary(pl.UTF-8):	DBD::mysql - perlowy interfejs do MySQL-a
Summary(pt.UTF-8):	Uma interface de Perl para o MySQL
Summary(pt_BR.UTF-8):	Uma interface de Perl para o MySQL
Summary(ru.UTF-8):	Интерфейс MySQL для Perl
Summary(sv.UTF-8):	Ett gränssnitt till MySQL för Perl
Summary(uk.UTF-8):	Perl-інтерфейс до MySQL
Summary(zh_CN.UTF-8):	Perl 的 MySQL 界面。
Name:		perl-DBD-mysql
Version:	4.029
Release:	1
# NOTE: libmysqlclient infects everything that links against it with GPL
License:	GPL (Perl code also Artistic)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcb8b105f771c04a8ebf3523eb073db7
Patch0:		headers.patch
URL:		http://search.cpan.org/dist/DBD-mysql/
BuildRequires:	mysql-devel >= 5.0.27
BuildRequires:	perl-DBI >= 1.13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-DBD-MySQL
Obsoletes:	perl-DBD-Mysql
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

%description -l cs.UTF-8
Implementace DBI pro MySQL do Perlu.

%description -l da.UTF-8
En implementation af DBI for MySQL.

%description -l de.UTF-8
Eine Implementierung von DBI für MySQL.

%description -l es.UTF-8
Implementación del DBI para MySQL.

%description -l fr.UTF-8
Mise en oeuvre de DBI pour MySQL.

%description -l it.UTF-8
Implementazione di DBI per MySQL.

%description -l ja.UTF-8
MySQL 用 DBI 実装

%description -l ko.UTF-8
MySQL을 위한 DBI의 실현.

%description -l nb.UTF-8
En implementasjon av DBI for MySQL.

%description -l pl.UTF-8
Sterownik pozwalający na dostęp do baz MySQL z poziomu Perla.

%description -l pt.UTF-8
Uma implementação de DBI para o MySQL.

%description -l pt_BR.UTF-8
Uma implementação de DBI para o MySQL.

%description -l ru.UTF-8
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

%description -l sv.UTF-8
En implementation av DBI för MySQL.

%description -l uk.UTF-8
M(y)sql.pm та DBD::mSQL(mysql) реалізують два різних підходи до
спілкування з сервером mSQL або MySQL. DBD::mSQL(mysql) побудовано на
базі DBI, стандартного інтерфейсу Perl до баз даних. Він надає
ідентичний інтерфейс до самих різноманітних баз даних і може бути
порівняний в цьому відношенні з ODBC. Перевагами підходу DBI є легка
переносимість та взаємодія. M(y)sql.pm - це більш старі програми. Вони
були написані до того, як з'явився DBI, але базуються на ранніх
проектах спецификації DBI. Виходячи з того, що вони використовуються
довше, вони більш відлагоджені та стабільні. Також вони більш
завершені, ніж DBD::mSQL та DBD::mysql.

%description -l zh_CN.UTF-8
一种 MySQL 的 DBI 实施措施。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
# we don't need no bundles
%{__rm} -r lib/Bundle

%build
%{__perl} Makefile.PL \
	--cflags="$(mysql_config --cflags) %{rpmcflags} -Werror=implicit-function-declaration" \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{?perl_install_postclean}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/DBD/mysql/INSTALL.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.pod TODO
%{perl_vendorarch}/DBD/mysql.pm
%dir %{perl_vendorarch}/DBD/mysql
%{perl_vendorarch}/DBD/mysql/GetInfo.pm
%dir %{perl_vendorarch}/auto/DBD/mysql
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/mysql/mysql.so
%{_mandir}/man3/DBD::mysql*.3pm*
