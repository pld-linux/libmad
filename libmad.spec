Summary:	MPEG audio decoder library
Summary(pl):	Biblioteka dekodera strumieni audio MPEG
Name:		libmad
Version:	0.15.1b
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	1be543bc30c56fb6bea1d7bf6a64e66c
URL:		http://www.underbit.com/products/mad/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
Provides:	mad-libs = %{version}
Obsoletes:	mad-libs < 0.15.0b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II
and Layer III a.k.a. MP3) are fully implemented.

%description -l pl
MAD jest wysokiej jako�ci dekoderem audio MPEG. Obecnie obs�uguje
MPEG-1 oraz rozszerzenie MPEG-2 dla ni�szych cz�stotliwo�ci
pr�bkowania, jak r�wnie� tzw. MPEG 2.5. Wszystkie trzy warstwy audio
(Layer I, Layer II oraz Layer III znany r�wnie� jako MP3) s� w pe�ni
zaimplementowane.

%package devel
Summary:	Header files for libmad library
Summary(pl):	Pliki nag��wkowe biblioteki libmad
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	mad-devel = %{version}
Obsoletes:	mad-devel < 0.15.0b

%description devel
Header files for libmad library.

%description devel -l pl
Pliki nag��wkowe biblioteki libmad.

%package static
Summary:	Static mad library
Summary(pl):	Biblioteka statyczna mad
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	mad-static = %{version}
Obsoletes:	mad-static < 0.15.0b

%description static
Static mad library.

%description static -l pl
Biblioteka statyczna mad.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{!?debug:dis}%{?debug:en}able-debugging \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT CREDITS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
