#
# Conditional build:
%bcond_without	introspection	# disable introspection
#
Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	2.0.4
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	413be319ba171feed9348d1bede6b0a7
Patch0:		%{name}-sync-builtins.patch
Patch1:		%{name}-pl.po.patch
URL:		http://webkitgtk.org/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	at-spi2-core-devel >= 2.6.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bison >= 1.875
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	enchant-devel >= 0.22
BuildRequires:	flex >= 2.5.33
BuildRequires:	fontconfig-devel >= 2.5.0
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	gcc-c++ >= 6:4.7
BuildRequires:	geoclue-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 1.0.3
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.3
BuildRequires:	gtk+2-devel >= 2:2.24.10
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	harfbuzz-devel >= 0.9.7
BuildRequires:	harfbuzz-icu-devel >= 0.9.7
BuildRequires:	libicu-devel >= 4.2.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libstdc++-devel
# libtool with -fuse-ld= gcc option support
BuildRequires:	libtool >= 2:2.4.2-13
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	pango-devel >= 1:1.32.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	ruby
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/ld.gold
Requires:	cairo >= 1.10
Requires:	enchant >= 0.22
Requires:	fontconfig-libs >= 2.5.0
Requires:	freetype >= 1:2.1.8
Requires:	glib2 >= 1:2.36.0
Requires:	gstreamer >= 1.0.3
Requires:	gstreamer-plugins-base >= 1.0.3
Requires:	gtk+2 >= 2:2.24.10
Requires:	harfbuzz >= 0.9.7
Requires:	libsoup >= 2.42.0
Requires:	libxml2 >= 1:2.6.30
Requires:	libxslt >= 1.1.7
Requires:	pango >= 1:1.32.0
%{?with_introspection:Conflicts:	gir-repository < 0.6.5-7}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
webkit is a port of the WebKit embeddable web component to GTK+.

%description -l pl.UTF-8
webkit to port osadzalnego komponentu WWW WebKit do GTK+.

%package devel
Summary:	Development files for WebKit for GTK+ 2
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.36.0
Requires:	gtk+2-devel >= 2:2.24.10
Requires:	libsoup-devel >= 2.42.0
Requires:	libstdc++-devel

%description devel
Development files for WebKit for GTK+ 2.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK+ 2.

%prep
%setup -q -n webkitgtk-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I Source/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LDFLAGS="%{rpmldflags} -fuse-ld=gold" \
	--disable-gtk-doc \
	--disable-silent-rules \
	--disable-webkit2 \
	--enable-geolocation \
	--enable-glx \
	%{__enable_disable introspection} \
	--enable-webgl \
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

%find_lang WebKitGTK-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f WebKitGTK-2.0.lang
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
