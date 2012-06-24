%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	mysql
Summary:	DBD::mysql perl module
Summary(pl):	Modu� perla DBD::mysql
Summary(ru):	Perl-��������� � Mysql
Summary(uk):	Perl-��������� �� Mysql
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
Sterownik pozwalaj�cy na dost�p do baz MySQL z poziomu Perla.

%description -l ru
M(y)sql.pm � DBD::mSQL(mysql) ��������� ��� ������ ������� � ������� �
�������� mSQL ��� mysql. DBD::mSQL(mysql) �������� �� ���� DBI,
������������ Perl-���������� � ����� ������. �� �������������
������������� ��������� � ����� ������������� ����� ������ � ������� �
���� ��������� � ODBC. �������������� ������� DBI �������� ������
������������� � ��������������. M(y)sql.pm - ��� ����� ������ �����.
��� ���� �������� �� ����, ��� ���� ��������� DBI, �� ������������ ��
������ ���������� ������������ DBI. ��� ��� ��� ������������ ������,
��� ����� �������� � ���������. ����� ��� ����� �����������, ���
DBD::mSQL � DBD::mysql.

�� ������ ������ ������� Msql/Mysql 1.1815 �� ������� DBD::mSQL �
DBD::mysql ������ �������, ��� MsqlPerl � MysqlPerl. ��� ����������
��������� (�������� ������ ���� �������� � ���������� DBI � ���������
��� ��� ����� ���������� � DBI 0.92) � �������, ��� �� Perl'������
��������. ��� �� �����, ����� �� ����.

%description -l uk
M(y)sql.pm �� DBD::mSQL(mysql) ���̦����� ��� Ҧ���� Ц����� ��
�Ц�������� � �������� mSQL ��� mysql. DBD::mSQL(mysql) ���������� ��
��ڦ DBI, ������������ ���������� Perl �� ��� �����. ��� �����
���������� ��������� �� ����� Ҧ�����Φ���� ��� ����� � ���� ����
��Ҧ������ � ����� צ������Φ � ODBC. ���������� Ц����� DBI � �����
��������ͦ��� �� ������Ħ�. M(y)sql.pm - �� ¦��� ���Ҧ ��������. ����
���� ������Φ �� ����, �� �'������ DBI, ��� ��������� �� ���Φ�
�������� ���������æ� DBI. �������� � ����, �� ���� ����������������
�����, ���� ¦��� צ��������Φ �� ���¦��Φ. ����� ���� ¦���
�������Φ, Φ� DBD::mSQL �� DBD::mysql.

�� ������ ���Ӧ� ����̦� Msql/Mysql 1.1815 �� �������� DBD::mSQL ��
DBD::mysql ������� �� MsqlPerl �� MysqlPerl. ���� ��������� ���¦��Φ
(צ���� Ԧ���� ���� �������� � ������ DBI � ��������, �� ���� ����
���������� � DBI 0.92) � ������ �� �� Perl'������� ���Ԧ�. �����,
��¦� �� ����.

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
