%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	mysql
Summary:	DBD::mysql perl module
Summary(pl):	ModuЁ perla DBD::mysql
Summary(ru):	Perl-интерфейс к Mysql
Summary(uk):	Perl-╕нтерфейс до Mysql
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
M(y)sql.pm and DBD::mSQL(mysql) implement two different approaches to
communicate with an mSQL or mysql server. DBD::mSQL(mysql) is built
upon the DBI, the generic Perl Database Interface. It brings you an
identical interface to a broad variety of databases and is in this
regard comparable to ODBC. The advantage of the DBI approach is
portability and interoperability. M(y)sql.pm are the elder species.
They were written before DBI was available but inspired by an early
draft of the DBI specification. As they have been circulating longer
they are more mature and pretty stable. They're also more complete
than DBD::mSQL and DBD::mysql.

As of Msql-Mysql-modules 1.1815, we consider DBD::mSQL and DBD::mysql
superior over MsqlPerl and MysqlPerl: They are sufficiently stable
(there's only one known problem in DBI itself and it's announced to be
fixed in DBI 0.92) and definitely faster. Anyways, you have to decide
on your own about the trade-offs.

%description -l pl
Sterownik pozwalaj╠cy na dostЙp do baz MySQL z poziomu Perla.

%description -l ru
M(y)sql.pm и DBD::mSQL(mysql) реализуют два разных подхода к общению с
сервером mSQL или mysql. DBD::mSQL(mysql) построен на базе DBI,
стандартного Perl-интерфейса к базам данных. Он предоставляет
единообразный интерфейс к самым разнообразным базам данных и сравним в
этом отношении с ODBC. Преимуществами подхода DBI является легкая
портируемость и взаимодйествие. M(y)sql.pm - это более старые особи.
Они были написаны до того, как стал доступным DBI, но основываются на
ранних черновиках спецификации DBI. Так как они используются дольше,
они более отлажены и стабильны. Также они более завершенные, чем
DBD::mSQL и DBD::mysql.

На момент версии модулей Msql/Mysql 1.1815 мы считаем DBD::mSQL и
DBD::mysql лучшим выбором, чем MsqlPerl и MysqlPerl. Они достаточно
стабильны (известна только одна проблема в собственно DBI и объявлено
что она будет исправлена в DBI 0.92) и быстрее, чем их Perl'овские
собратья. Тем не менее, выбор за вами.

%description -l uk
M(y)sql.pm та DBD::mSQL(mysql) реал╕зують два р╕зних п╕дходи до
сп╕лкування з сервером mSQL або mysql. DBD::mSQL(mysql) побудовано на
баз╕ DBI, стандартного ╕нтерфейсу Perl до баз даних. В╕н нада╓
╕дентичний ╕нтерфейс до самих р╕зноман╕тних баз даних ╕ може бути
пор╕вняний в цьому в╕дношенн╕ з ODBC. Перевагами п╕дходу DBI ╓ легка
переносим╕сть та вза╓мод╕я. M(y)sql.pm - це б╕льш стар╕ програми. Вони
були написан╕ до того, як з'явився DBI, але базуються на ранн╕х
проектах спецификац╕╖ DBI. Виходячи з того, що вони використовуються
довше, вони б╕льш в╕длагоджен╕ та стаб╕льн╕. Також вони б╕льш
завершен╕, н╕ж DBD::mSQL та DBD::mysql.

На момент верс╕╖ модул╕в Msql/Mysql 1.1815 ми вважа╓мо DBD::mSQL та
DBD::mysql кращими за MsqlPerl та MysqlPerl. Вони достатньо стаб╕льн╕
(в╕дома т╕льки одна проблема у власне DBI ╕ заявлено, що вона буде
виправлена в DBI 0.92) ╕ швидше за ╖х Perl'╕вських брат╕в. Проте,
виб╕р за вами.

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
