%define debug_package %{nil}

Summary:	A statically linked shell, including some built-in basic commands
Name:		sash
Version:	3.8
Release:	8
License:	GPL
Group:		Shells
Url:		http://www.canb.auug.org.au/~dbell/
Source0:	http://www.canb.auug.org.au/~dbell/programs/%{name}-%{version}.tar.gz
Patch5:		sash-3.6-scriptarg.patch
Patch6:		sash-pwdfunc.patch
Patch7:		sash-3.7-segfault.patch
Patch8:		sash-3.8-special-script-call-esp-for-glibc-post.patch
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
%apply_patches

%build

%make OPT="%{optflags}" LDFLAGS="-static %{ldflags}" CC=gcc

%install
install -m755 sash -D %{buildroot}/sbin/sash
install -m644 sash.1 -D %{buildroot}%{_mandir}/man8/sash.8

%files
/sbin/sash
%{_mandir}/man8/sash.8*
