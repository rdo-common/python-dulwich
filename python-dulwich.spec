%global srcname dulwich

%filter_provides_in %{python_sitearch}
%filter_setup

Name:           python-%{srcname}
Version:        0.9.5
Release:        1%{?dist}
Summary:        A python implementation of the Git file formats and protocols

License:        GPLv2+ or ASL 2.0
URL:            http://samba.org/~jelmer/dulwich/
Source0:        https://pypi.python.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose

%if 0%{?rhel} < 7 || 0%{?fedora} < 14
BuildRequires:  python-unittest2
%endif

%description
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
CFLAGS="%{optflags}" %{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

#%check
#cd dulwich/tests
#nosetests test*.py

%files
%doc COPYING NEWS README docs/
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%{python2_sitearch}/%{srcname}*
%exclude %{python2_sitearch}/%{srcname}/tests*

%changelog
* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Tests are currently not working
- Update to new upstream version 0.9.5

* Mon Oct 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to new upstream version 0.9.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to new upstream version 0.9.0
- Now dual-licensed GPLv2+ or ASL 2.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.7-1
- Update to new upstream version 0.8.7

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.6-1
- Update to new upstream version 0.8.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Matěj Cepl <mcepl@redhat.com> - 0.8.5-2
- We don’t need python-unittest2 anymore.

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.5-1
- Update to new upstream version 0.8.5

* Fri Apr 06 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.4-1
- Update to new upstream version 0.8.4

* Fri Feb 24 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.3-1
- Update to new upstream version 0.8.3

* Sat Jan 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-2
- Add missing BR

* Fri Jan 27 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-1
- Update to new upstream version 0.8.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update to new upstream version 0.8.0

* Sun Apr 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Update to new upstream version 0.7.1

* Fri Mar 11 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-3
- Test section reworked

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Update to new upstream version 0.7.0

* Mon Nov 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Filtering added
- Update to new upstream version 0.6.2

* Wed Sep 01 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Fix grep parameter
- Run all test now
- Update to new upstream version 0.6.1

* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-3
- Remove exec permission from test.py
- Add python-nose

* Fri Jun 25 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-2
- Change summary
- Change to srcname
- Fix rpmlint issue
- Add check section and exclude the tests directory

* Thu Jun 17 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Fix some rpmlint issues
- Add docs directory
- Update to new upstream version 0.6.0

* Wed Apr 28 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Add Doc
- Add BR setuptools

* Fri Apr 16 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> 0.5.0-1
- Initial package
