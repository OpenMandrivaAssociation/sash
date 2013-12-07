Summary:	A statically linked shell, including some built-in basic commands
Name:		sash
Version:	3.7
Release:	20
License:	GPL
Group:		Shells
Url:		http://www.canb.auug.org.au/~dbell/
Source0:	http://www.canb.auug.org.au/~dbell/programs/%{name}-%{version}.tar.bz2
Patch0:		sash-3.7-optflags.patch
Patch2:		sash-3.7-losetup.patch
Patch3:		sash-3.7-fix-loop__remove_it_when_kernel_headers_are_fixed.patch
Patch4:		sash-3.7-linux2.6-buildfix.patch
Patch5:		sash-3.6-scriptarg.patch
Patch6:		sash-pwdfunc.patch
Patch7:		sash-3.7-segfault.patch
Patch8:		sash-3.7-special-script-call-esp-for-glibc-post.patch
Conflicts:	glibc < 6:2.3.3-2mdk
BuildRequires:	pkgconfig(zlib)
BuildRequires:	glibc-static-devel
BuildRequires:	pkgconfig(ext2fs)

%description
Sash is a simple, standalone, statically linked shell which includes
simplified versions of built-in commands like ls, dd and gzip.  Sash
is statically linked so that it can work without shared libraries, so
it is particularly useful for recovering from certain types of system
failures.  Sash can also be used to safely upgrade to new versions of
shared libraries.

%prep
%setup -q
%patch0 -p1 -b .misc~
%patch2 -p1 -b .losetup~
%patch3 -p1 -b .loop~
%patch4 -p1 -b .peroyvind~
%patch5 -p1 -b .scriptarg~
%patch6 -p1 -b .pwd~
%patch7 -p1 -b .segf~
%patch8 -p1 -b .scriptarg~

%build
%make RPM_OPT_FLAGS="%{optflags}" LDFLAGS="-static %{ldflags}"

%install
install -m755 sash -D %{buildroot}/sbin/sash
install -m644 sash.1 -D %{buildroot}%{_mandir}/man8/sash.8

%files
/sbin/sash
%{_mandir}/man8/sash.8*

%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.7-12mdv2011.0
+ Revision: 669958
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.7-11mdv2011.0
+ Revision: 607510
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3.7-10mdv2010.1
+ Revision: 520214
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.7-9mdv2010.0
+ Revision: 427011
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 3.7-8mdv2009.1
+ Revision: 366282
- rediff loop patch
- rediff losetup patch
- rediff optflags patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.7-7mdv2009.0
+ Revision: 225365
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.7-6mdv2008.1
+ Revision: 126961
- kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.7-6mdv2007.0
+ Revision: 119970
- Import sash

* Tue Apr 25 2006 Pixel <pixel@mandriva.com> 3.7-5mdk
- rebuild (ie ensure we are statically linked with a recent zlib, cf #21942)

* Fri Oct 14 2005 Pixel <pixel@mandriva.com> 3.7-4mdk
- rebuild

* Thu Jun 03 2004 Pixel <pixel@mandrakesoft.com> 3.7-3mdk
- fedora patch sash-3.6-scriptarg broke --ignore-remaining-args special option

* Sun Apr 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.7-2mdk
- fix buildrequires

* Sun Apr 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.7-1mdk
- 3.7
- fix build with 2.6 kernel headers
- sync with fedora (P5, P6 & P7)
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install

