%global srcname dulwich
%global sum A python implementation of the Git file formats and protocols

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$
%else
%bcond_without python2
%bcond_with    python3
%global __provides_exclude_from ^(%{python2_sitearch}/.*\\.so)$
%endif

Name:           python-%{srcname}
Version:        0.19.11
Release:        1%{?dist}
Summary:        %{sum}

License:        GPLv2+ or ASL 2.0
URL:            https://www.dulwich.io/
Source0:        %pypi_source dulwich

BuildRequires:  gcc

%if (0%{?rhel} && 0%{?rhel} < 7) || (0%{?fedora} && 0%{?fedora} < 14)
BuildRequires:  python-unittest2
%endif

%description
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n %{srcname}-core
Summary:        Shared files for Dulwich

%description -n %{srcname}-core
Files to ensure functionality for both python2 and python3 packages of Dulwich.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
Requires:       %{srcname}-core%{?_isa} = %{version}-%{release}
BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  python2-sphinx
BuildRequires:  python-docutils

%description -n python2-%{srcname}
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.
%endif

%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       %{srcname}-core%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-docutils

%description -n python3-%{srcname}
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.
%endif

%prep
%autosetup -n %{srcname}-%{version}

# Package provideing sphinx ext: sphinx_epytext not available
sed -i '/sphinx_epytext/d' docs/conf.py

%build
%if %{with python2}
%py2_build
sphinx-build -b html docs docs/build/html
rm -rf build/html/{.buildinfo,doctrees}
%endif
%if %{with python3}
%py3_build
pushd docs
# Not using {smp_flags} as sphinx fails with it from time to time
sphinx-build-3 -b html -d py3/doctrees . py3/html
rm -rf py3/html/.buildinfo
popd
%endif

%install
%if %{with python2}
%py2_install
# Remove extra copy of text docs
rm -rf %{buildroot}%{python2_sitearch}/docs/tutorial/
%endif
%if %{with python3}
%py3_install
# Remove extra copy of text docs
rm -rf %{buildroot}%{python3_sitearch}/docs/tutorial/
%endif

#%check
# FIXME test_non_ascii fails cause of unicode issue
#nosetests -e non_ascii -w dulwich/tests -v

%files -n %{srcname}-core
%doc AUTHORS README.rst
%license COPYING
%{_bindir}/dul-*
%{_bindir}/%{srcname}

%if %{with python2}
%files -n python2-%{srcname}
%doc docs/build/html/
%{python2_sitearch}/%{srcname}*
%exclude %{python2_sitearch}/%{srcname}/tests*
%endif

%if %{with python3}
%files -n python3-%{srcname}
%doc docs/py3/html/
%{python3_sitearch}/%{srcname}*
%exclude %{python3_sitearch}/%{srcname}/tests*
%endif

%changelog
* Fri Mar 1 2019 Yatin Karel <ykarel@redhat.com> - 0.19.11-1
- Update to new upstream version 0.19.11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.19.9-1
- Update to new upstream version 0.19.9

* Mon Aug 27 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.19.6-1
- Update to new upstream version 0.19.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.19.2-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.19.2-1
- Update to new upstream version 0.19.2

* Fri Mar 23 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.19.0-1
- Update to new upstream version 0.19.0

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.18.6-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Alan Pevec <alan.pevec@redhat.com> 0.18.6-1
- Update to 0.18.6
- Fixes CVE-2017-16228

* Fri Oct 13 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.18.4-1
- Update to new upstream version 0.16.0 (rhbz#*1405983)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to new upstream version 0.16.0

* Sat Jan 21 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.0-1
- Update to new upstream version 0.15.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 02 2016 Raphael Groner <projects.rg@smart.ms> - 0.12.0-2
- Generate documentation for python3
- Split binaries in subpackage to avoid duplication
- Execute tests
- Fix rhbz#1304050

* Tue Feb 02 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to new upstream version 0.12.0

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.2-3
- Cleanup and py3

* Tue Oct 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.2-2
- Update docs
- Update to new upstream version 0.11.2

* Tue Oct 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.1-1
- Update to new upstream version 0.11.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.0-1
- Fix for CVE-2014-9706 (rhbz#1204889, rhbz#1204890, and rhbz#1204891)
- Update to new upstream version 0.10.0

* Mon Mar 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.9-1
- Update to new upstream version 0.9.9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.7-1
- Update to new upstream version 0.9.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.6-1
- Update to new upstream version 0.9.6

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
