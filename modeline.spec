Summary:	XFree86/SVGAlib/FrameBuffer mode lines generator
Summary(pl):	Generator trybów graficznych dla XFree86/SVGAlib/FrameBuffer
Name:		modeline
Version:	0.6.5
Release:	2
License:	GPL
Group:		Base/Utilities
Source0:	http://home.kvalito.no/~bragthor/cgi-bin/countdown.cgi?modeline/%{name}-%{version}.tar.bz2
# Source0-md5:	cc5cabf6f8143d7e5e2df1587227c678
URL:		http://home.kvalito.no/~bragthor/files.shtml
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modeline is a small utility to make XFree86/SVGAlib/FrameBuffer
modelines.

%description -l pl
Modeline jest ma³ym narzêdziem do generowania trybów graficznych dla
XFree86, SVGAlib oraz FrameBuffera.

%prep
%setup  -q

%build
%{__aclocal}
%{__autoconf}
install %{_datadir}/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/mode.conf $RPM_BUILD_ROOT/%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%config %{_sysconfdir}/*
