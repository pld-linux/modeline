Summary:	XFree86/SVGAlib/FrameBuffer mode lines generator
Summary(pl.UTF-8):	Generator trybów graficznych dla XFree86/SVGAlib/FrameBuffer
Name:		modeline
Version:	0.6.5
Release:	3
License:	GPL
Group:		Base/Utilities
Source0:	http://home.kvalito.no/~bragthor/cgi-bin/countdown.cgi?modeline/%{name}-%{version}.tar.bz2
# Source0-md5:	cc5cabf6f8143d7e5e2df1587227c678
Patch0:		%{name}-acbuild.patch
URL:		http://home.kvalito.no/~bragthor/files.shtml
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modeline is a small utility to make XFree86/SVGAlib/FrameBuffer
modelines.

%description -l pl.UTF-8
Modeline jest małym narzędziem do generowania trybów graficznych dla
XFree86, SVGAlib oraz FrameBuffera.

%prep
%setup  -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
install /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/mode.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
