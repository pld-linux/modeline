Summary:	XFree86/SVGAlib/FrameBuffer mode lines generator
Summary(pl):	Generator trybów graficznych dla XFree86/SVGAlib/FrameBuffer
Name:		modeline
Version:	0.6.5
Release:	1
License:	GPL
Group:		Base/Utilities
Group(de):	Gründsätzlich/Werkzeuge
Group(pl):	Podstawowe/Narzêdzia
Source0:	http://home.kvalito.no/~bragthor/cgi-bin/countdown.cgi?modeline/%{name}-%{version}.tar.gz
URL:		http://home.kvalito.no/~bragthor/files/files.shtml
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
aclocal
autoconf
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/mode.conf $RPM_BUILD_ROOT/%{_sysconfdir}

gzip -9nf README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%config %{_sysconfdir}/*
