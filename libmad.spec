Summary:	MPEG audio decoder library
Summary(pl):	Biblioteka dekodera strumieni audio MPEG
Name:		libmad
Version:	0.15.0b
Release:	1.1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	2e4487cdf922a6da2546bad74f643205
URL:		http://www.underbit.com/products/mad/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Provides:	mad-libs
Obsoletes:	mad-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II
and Layer III a.k.a. MP3) are fully implemented.

%description -l pl
MAD jest wysokiej jako¶ci dekoderem audio MPEG. Obecnie wspiera MPEG-1
oraz MPEG-2, jak równie¿ tzw. MPEG 2.5. Wszystkie trzy warstwy audio
(Layer I, Layer II oraz Layer III znany równie¿ jako MP3) s± w pe³ni
zaimplementowane.

%package devel
Summary:	Header files for libmad
Summary(pl):	Pliki nag³ówkowe do libmad
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	mad-devel

%description devel
Header files for libmad.

%description devel -l pl
Pliki nag³ówkowe biblioteki libmad.

%package static
Summary:	Static mad libraries
Summary(pl):	Biblioteki statyczne do mad
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static mad libraries.

%description static -l pl
Biblioteki statyczne do mad.

%prep
%setup -q
#%patch -p1

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES CREDITS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
