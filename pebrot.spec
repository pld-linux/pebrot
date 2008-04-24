Summary:	MSN messenger text mode client
Name:		pebrot
Version:	0.8.8
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pebrot/%{name}-%{version}.tar.bz2
# Source0-md5:	aa07bcb3cb7556bdd20a42b48ac45643
URL:		http://pebrot.sourceforge.net/
BuildRequires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pebrot is a text MSN messenger client implemented with Python. It has
also a pretty and colorful Curses-based interface.

%prep
%setup -q
mv i18n/pt{_PT,}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%find_lang %{name}

rm -rf $RPM_BUILD_ROOT%{_docdir}/pebrot

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%doc pebrotrc logos utils
%attr(755,root,root) %{_bindir}/pebrot
%dir %{py_sitescriptdir}/pypebrot
%{py_sitescriptdir}/pypebrot/*.py[co]
