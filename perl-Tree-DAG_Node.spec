Name:           perl-Tree-DAG_Node
Version:        1.12
Release:        1%{?dist}
Summary:        Class for representing nodes in a tree
Group:          Development/Libraries
License:        Artistic 2.0
URL:            http://search.cpan.org/dist/Tree-DAG_Node/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RS/RSAVAGE/Tree-DAG_Node-%{version}.tgz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Pod) >= 1.45
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This class encapsulates/makes/manipulates objects that represent nodes in a
tree structure. The tree structure is not an object itself, but is emergent
from the linkages you create between nodes. This class provides the methods
for making linkages that can be used to build up a tree, while preventing you
from ever making any kinds of linkages that are not allowed in a tree (such as
having a node be its own mother or ancestor, or having a node have two
mothers).

%prep
%setup -q -n Tree-DAG_Node-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Tree/
%{_mandir}/man3/Tree::DAG_Node.3pm*

%changelog
* Wed Jul  3 2013 Paul Howarth <paul@city-fan.org> - 1.12-1
- Update to 1.12
  - Change text in README referring to licence to match text in body of source,
    since it was in conflict with the Artistic Licence V 2.0
  - Rename CHANGES to Changes as per CPAN::Changes::SPEC
  - Various spelling fixes in the docs

* Mon Feb  4 2013 Paul Howarth <paul@city-fan.org> - 1.11-1
- Update to 1.11
  - License clarified as Artistic 2.0 (CPAN RT#83088)

* Fri Feb  1 2013 Paul Howarth <paul@city-fan.org> - 1.10-1
- Update to 1.10
  - Look for but don't require Test::Pod ≥ 1.45 (CPAN RT#83077)

* Fri Nov 23 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-2
- Update dependencies
- Remove BuildRoot cleaning

* Fri Nov  9 2012 Paul Howarth <paul@city-fan.org> - 1.09-1
- Update to 1.09
  - No code changes
  - For pre-reqs such as strict, warnings, etc., which ship with Perl, set the
    version requirement to 0 (CPAN RT#80663)

* Fri Nov  2 2012 Paul Howarth <paul@city-fan.org> - 1.07-1
- Update to 1.07
  - New maintainer: Ron Savage
  - Pre-emptive apologies for any changes which are not back-compatible; no
    such problems are expected, but the introduction of new methods may
    disconcert some viewers
  - Fix CPAN RT#78858 and audit code for similar problems
  - Fix CPAN RT#79506
  - Rename ChangeLog to CHANGES, and add Changelog.ini
  - Replace all uses of cyclicity_fault() and Carp::croak with die
  - Remove unused methods: decommission_root(), cyclicity_allowed(),
    cyclicity_fault(), inaugurate_root(), no_cyclicity() and _update_links();
    OK - cyclicity_fault() was called once - it just died
  - Add methods: format_node(), hashref2string(), is_root(), node2string(),
    tree2string()
  - Reformat the POD big-time
  - Add Build.PL
  - Re-write Makefile.PL
  - Remove use vars(@ISA $Debug $VERSION), and replace latter 2 with 'our ...'
  - Rename t/00_about_verbose.t to t/about.perl.t
  - Add scripts/cut.and.paste.subtrees.pl (Warning: Some trees get into an
    infinite loop)
  - Add t/cut.and.paste.subtrees.t (Warning: Some trees get into an infinite
    loop)
  - Document the options (discouraged by Sean) supported in the call to
    new($hashref)
- This release by RSAVAGE -> update source URL
- BR: perl(Test::More) and perl(Test::Pod) ≥ 1.00
- Modernize spec file:
  - Drop %%clean section
  - Drop buildroot definition and cleaning
  - Don't use macros for commands
  - Don't need to remove empty directories from the buildroot
  - Use %%{_fixperms} macro rather than our own chmod incantation
  - Drop %%defattr, redundant since rpm 4.4

* Mon Oct 29 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-15
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.06-13
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.06-11
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.06-9
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.06-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.06-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-4
- fix source url

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-3
- Rebuild for perl 5.10 (again)

* Thu Jan 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-1
- 1.06

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-4
- Rebuild for FC6.

* Wed Feb 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-3
- Rebuild for FC5 (perl 5.8.8).

* Fri Jul  1 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-2
- Dist tag.

* Thu Dec 30 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.05-0.fdr.1
- Update to 1.05.

* Sun Jul 04 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.04-0.fdr.1
- First build.
