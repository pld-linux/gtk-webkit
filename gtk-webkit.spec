#
# Conditional build:
%bcond_without	introspection	# disable introspection
#
Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	1.10.1
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	28c930cda012391453c476cdacfaca65
URL:		http://webkitgtk.org/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bison >= 1.875
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	cairo-gobject-devel >= 1.10
BuildRequires:	enchant-devel >= 0.22
BuildRequires:	flex >= 2.5.33
BuildRequires:	fontconfig-devel >= 2.4.0
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	geoclue-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 0.9.5}
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libicu-devel >= 4.2.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-devel >= 2.40.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	pango-devel >= 1:1.21
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	cairo >= 1.10
Requires:	enchant >= 0.22
Requires:	glib2 >= 1:2.32.0
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
Requires:	gtk+2 >= 2:2.20.0
Requires:	libsoup >= 2.40.0
Requires:	libxml2 >= 1:2.6.30
Requires:	libxslt >= 1.1.7
Requires:	pango >= 1:1.21
%{?with_introspection:Conflicts:	gir-repository < 0.6.5-7}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
webkit is a port of the WebKit embeddable web component to GTK+.

%description -l pl.UTF-8
webkit to port osadzalnego komponentu WWW WebKit do GTK+.

%package devel
Summary:	Development files for WebKit
Summary(pl.UTF-8):	Pliki programistyczne WebKit
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10
Requires:	enchant-devel >= 0.22
Requires:	fontconfig-devel >= 2.4.0
Requires:	freetype-devel >= 1:2.1.8
Requires:	geoclue-devel
Requires:	glib2-devel >= 1:2.32.0
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-base-devel >= 1.0.0
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	libicu-devel >= 4.2.1
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libsoup-devel >= 2.38
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 1:2.6.30
Requires:	libxslt-devel >= 1.1.7
Requires:	pango-devel >= 1:1.21
Requires:	sqlite3-devel >= 3
Requires:	xorg-lib-libXt-devel

%description devel
Development files for WebKit.

%description devel -l pl.UTF-8
Pliki programistyczne WebKit.

%prep
%setup -q -n webkitgtk-%{version}
#patch0 -p1
#patch1 -p2

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I Source/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
# replace -g2 with -g1 to not run into 4 GB ar format limit
# https://bugs.webkit.org/show_bug.cgi?id=91154
# http://sourceware.org/bugzilla/show_bug.cgi?id=14625
export CFLAGS="%(echo %{rpmcflags} | sed 's/ -g2/ -g1/g')"
export CXXFLAGS="%(echo %{rpmcxxflags} | sed 's/ -g2/ -g1/g')"
%configure \
	--disable-silent-rules \
	--disable-webkit2 \
	--enable-geolocation \
	--enable-gtk-doc \
	--enable-icon-database \
	--enable-introspection%{!?with_introspection:=no} \
	--enable-video \
	--with-font-backend=freetype \
	--with-gstreamer=1.0 \
	--with-gtk=2.0 \
	--with-html-dir=%{_gtkdocdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*-1.0.la
# packaged in gtk-webkit3
%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}/webkitgtk

%find_lang webkitgtk-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f webkitgtk-2.0.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS 
%attr(755,root,root) %{_bindir}/jsc-1
%attr(755,root,root) %{_libdir}/libwebkitgtk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkitgtk-1.0.so.0
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-1.0.so.0
%if %{with introspection}
%{_libdir}/girepository-1.0/JSCore-1.0.typelib
%{_libdir}/girepository-1.0/WebKit-1.0.typelib
%endif
%dir %{_datadir}/webkitgtk-1.0
%{_datadir}/webkitgtk-1.0/images
%{_datadir}/webkitgtk-1.0/resources
%{_datadir}/webkitgtk-1.0/webinspector

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-1.0.so
%attr(755,root,root) %{_libdir}/libwebkitgtk-1.0.so
%if %{with introspection}
%{_datadir}/gir-1.0/JSCore-1.0.gir
%{_datadir}/gir-1.0/WebKit-1.0.gir
%endif
%{_includedir}/webkitgtk-1.0
%{_pkgconfigdir}/javascriptcoregtk-1.0.pc
%{_pkgconfigdir}/webkit-1.0.pc
