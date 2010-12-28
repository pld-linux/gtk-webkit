# TODO: optflags
#
# Conditional build:
%bcond_without	introspection	# disable introspection

Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	1.2.4
Release:	3
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/webkit-%{version}.tar.gz
# Source0-md5:	dc3a92dd0e8c2e70263fbfdf809b51a5
Patch0:		gobject-introspection.patch
URL:		http://webkitgtk.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	enchant-devel >= 0.22
BuildRequires:	flex >= 2.5.33
BuildRequires:	fontconfig-devel >= 2.4.0
BuildRequires:	geoclue-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 0.9.5}
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.25
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libicu-devel >= 4.2.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-devel >= 2.30.2-4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.0.0
BuildRequires:	xorg-lib-libXt-devel
Requires:	gtk+2 >= 2:2.20.0
Requires:	libsoup >= 2.30.0
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
Requires:	atk-devel
Requires:	cairo-devel
Requires:	dbus-devel
Requires:	dbus-glib-devel
Requires:	enchant-devel
Requires:	expat-devel
Requires:	fontconfig-devel >= 1.0.0
Requires:	freetype-devel
Requires:	gdk-pixbuf2-devel
Requires:	geoclue-devel
Requires:	glib2-devel >= 1:2.22.0
Requires:	gnutls-devel
Requires:	gstreamer-devel
Requires:	gstreamer-plugins-base-devel
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	libgcrypt-devel
Requires:	libgpg-error-devel
Requires:	libicu-devel
Requires:	libjpeg-devel-8b
Requires:	libpng-devel
Requires:	libsoup-devel >= 2.30.0
Requires:	libstdc++-devel
Requires:	libtasn1-devel
Requires:	libuuid-devel
Requires:	libxcb-devel
Requires:	libxml2-devel
Requires:	libxslt-devel
Requires:	pango-devel
Requires:	pcre-devel
Requires:	pixman-devel
Requires:	sqlite3-devel
Requires:	xcb-util-devel
Requires:	xorg-lib-libICE-devel
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXdmcp-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXft-devel >= 2.0.0
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-lib-libXt-devel

%description devel
Development files for WebKit.

%description devel -l pl.UTF-8
Pliki programistyczne WebKit.

%prep
%setup -q -n webkit-%{version}
%patch0 -p1

%build
%{__gtkdocize}
%{__aclocal} -I autotools
%{__libtoolize}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--enable-3D-transforms \
	--enable-dom-storage \
	--enable-geolocation \
	--enable-icon-database \
	--%{!?with_introspection:dis}%{?with_introspection:en}able-introspection \
	--enable-video

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang webkit

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f webkit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsc
%attr(755,root,root) %{_libdir}/libwebkit-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkit-1.0.so.2
%if %{with introspection}
%{_libdir}/girepository-1.0/JSCore-1.0.typelib
%{_libdir}/girepository-1.0/WebKit-1.0.typelib
%endif
%dir %{_datadir}/webkit-1.0
%{_datadir}/webkit-1.0/images
%{_datadir}/webkit-1.0/resources
%{_datadir}/webkit-1.0/webinspector

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkit-1.0.so
%{_libdir}/libwebkit-1.0.la
%if %{with introspection}
%{_datadir}/gir-1.0/JSCore-1.0.gir
%{_datadir}/gir-1.0/WebKit-1.0.gir
%endif
%{_includedir}/webkit-1.0
%{_pkgconfigdir}/webkit-1.0.pc
