Summary:	A statically linked shell, including some built-in basic commands
Name:		sash
Version:	3.8
Release:	3
License:	GPL
Group:		Shells
Url:		http://www.canb.auug.org.au/~dbell/
Source0:	http://www.canb.auug.org.au/~dbell/programs/%{name}-%{version}.tar.gz
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
