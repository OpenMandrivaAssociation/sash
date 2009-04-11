Summary:	A statically linked shell, including some built-in basic commands
Name:		sash
Version:	3.7
Release:	%mkrel 8
License:	GPL
Group:		Shells
Url:		http://www.canb.auug.org.au/~dbell/
Source0:	http://www.canb.auug.org.au/~dbell/programs/%{name}-%{version}.tar.bz2
Patch0:		sash-3.7-optflags.patch
Patch2: 	sash-3.4-losetup.patch
Patch3: 	sash-3.4-fix-loop__remove_it_when_kernel_headers_are_fixed.patch
Patch4:		sash-3.7-linux2.6-buildfix.patch
Patch5:		sash-3.6-scriptarg.patch
Patch6:		sash-pwdfunc.patch
Patch7:		sash-3.7-segfault.patch
Patch8:		sash-3.7-special-script-call-esp-for-glibc-post.patch
Conflicts:      glibc < 6:2.3.3-2mdk
BuildRequires:	zlib-devel glibc-static-devel e2fsprogs-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Sash is a simple, standalone, statically linked shell which includes
simplified versions of built-in commands like ls, dd and gzip.  Sash
is statically linked so that it can work without shared libraries, so
it is particularly useful for recovering from certain types of system
failures.  Sash can also be used to safely upgrade to new versions of
shared libraries.

%prep
%setup -q
%patch0 -p1 -b ".misc"
%patch2 -p1 -b ".losetup"
%patch3 -p1
%patch4 -p1 -b .peroyvind
%patch5 -p1 -b .scriptarg
%patch6 -p1 -b ".pwd"
%patch7 -p1 -b ".segf"
%patch8 -p1 -b ".scriptarg" -z .pix

%build
make RPM_OPT_FLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -s -D sash %{buildroot}/sbin/sash
install -D sash.1 %{buildroot}%{_mandir}/man8/sash.8

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/sash
%_mandir/*/*


