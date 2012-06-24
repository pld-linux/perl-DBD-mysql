#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests require access to a working MySQL
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	mysql
Summary:	A MySQL interface for Perl
Summary(cs):	MySQL rozhran� pro Perl
Summary(da):	En MySQL-gr�nseflade for Perl
Summary(de):	Ein MySQL Interface f�r Perl
Summary(es):	Interfaz MySQL para Perl
Summary(fr):	Interface MySQL pour Perl
Summary(it):	Interfaccia MySQL per Perl
Summary(ja):	Perl �� MySQL ���󥿡��ե�����
Summary(ko):	���� ���� MySQL �������̽�
Summary(nb):	Et MySQL-grensesnitt for Perl
Summary(pl):	DBD::mysql - perlowy interfejs do MySQL-a
Summary(pt):	Uma interface de Perl para o MySQL
Summary(pt_BR):	Uma interface de Perl para o MySQL
Summary(ru):	��������� MySQL ��� Perl
Summary(sv):	Ett gr�nssnitt till MySQL f�r Perl
Summary(uk):	Perl-��������� �� MySQL
Summary(zh_CN):	Perl �� MySQL ���档
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
Eine Implementierung von DBI f�r MySQL.

%description -l es
Implementaci�n del DBI para MySQL.

%description -l fr
Mise en oeuvre de DBI pour MySQL.

%description -l it
Implementazione di DBI per MySQL.

%description -l ja
MySQL �� DBI ����

%description -l ko
MySQL�� ���� DBI�� ����.

%description -l nb
En implementasjon av DBI for MySQL.

%description -l pl
Sterownik pozwalaj�cy na dost�p do baz MySQL z poziomu Perla.

%description -l pt
Uma implementa��o de DBI para o MySQL.

%description -l pt_BR
Uma implementa��o de DBI para o MySQL.

%description -l ru
M(y)sql.pm � DBD::mSQL(mysql) ��������� ��� ������ ������� � ������� �
�������� mSQL ��� MySQL. DBD::mSQL(mysql) �������� �� ���� DBI,
������������ Perl-���������� � ����� ������. �� �������������
������������� ��������� � ����� ������������� ����� ������ � ������� �
���� ��������� � ODBC. �������������� ������� DBI �������� ������
������������� � ��������������. M(y)sql.pm - ��� ����� ������ �����.
��� ���� �������� �� ����, ��� ���� ��������� DBI, �� ������������ ��
������ ���������� ������������ DBI. ��� ��� ��� ������������ ������,
��� ����� �������� � ���������. ����� ��� ����� �����������, ���
DBD::mSQL � DBD::mysql.

%description -l sv
En implementation av DBI f�r MySQL.

%description -l uk
M(y)sql.pm �� DBD::mSQL(mysql) ���̦����� ��� Ҧ���� Ц����� ��
�Ц�������� � �������� mSQL ��� MySQL. DBD::mSQL(mysql) ���������� ��
��ڦ DBI, ������������ ���������� Perl �� ��� �����. ��� �����
���������� ��������� �� ����� Ҧ�����Φ���� ��� ����� � ���� ����
��Ҧ������ � ����� צ������Φ � ODBC. ���������� Ц����� DBI � �����
��������ͦ��� �� ������Ħ�. M(y)sql.pm - �� ¦��� ���Ҧ ��������. ����
���� ������Φ �� ����, �� �'������ DBI, ��� ��������� �� ���Φ�
�������� ���������æ� DBI. �������� � ����, �� ���� ����������������
�����, ���� ¦��� צ��������Φ �� ���¦��Φ. ����� ���� ¦���
�������Φ, Φ� DBD::mSQL �� DBD::mysql.

%description -l zh_CN
һ�� MySQL �� DBI ʵʩ��ʩ��

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
