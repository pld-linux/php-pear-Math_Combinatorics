%define		_class		Math
%define		_subclass	Combinatorics
%define		_status		stable
%define		_pearname	Math_Combinatorics
Summary:	%{_pearname} - A package that produces combinations and permutations
Summary(pl.UTF-8):	%{_pearname} - pakiet do generowania kombinacji oraz permutacji
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5b8faac5e40d0bcf74e09b046d4733dc
URL:		http://pear.php.net/package/Math_Combinatorics/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Math_Combinatorics-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package that returns all the combinations and permutations, without
repetition, of a given set and subset size. Associative arrays are
preserved.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten zwraca wszystkie kombinacje oraz permutacje bez powtórzeń z
zadanego zbioru oraz rozmiaru podzbioru. Tablice asocjacyjne są
zachowywane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Math_Combinatorics/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/Combinatorics.php
