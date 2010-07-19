# TODO: optflags
#
# Conditional build:
%bcond_without	introspection	# disable introspection

Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	1.3.3
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/webkit-%{version}.tar.gz
# Source0-md5:	22af6591b124610a8df55c7a87989349
URL:		http://webkitgtk.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	enchant-devel >= 0.22
BuildRequires:	flex >= 2.5.33
BuildRequires:	fontconfig-devel >= 2.4.0
BuildRequires:	geoclue-devel
BuildRequires:	gettext-devel
%{?with_introspection:BuildRequires:	gir-repository-devel}
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 0.6.2}
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.25
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libicu-devel >= 4.2.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-devel >= 2.30.0
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
Requires:	fontconfig-devel >= 1.0.0
Requires:	glib2-devel >= 1:2.22.0
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	libicu-devel
Requires:	libsoup-devel >= 2.30.0
Requires:	libstdc++-devel
Requires:	xorg-lib-libXft-devel >= 2.0.0

%description devel
Development files for WebKit.

%description devel -l pl.UTF-8
Pliki programistyczne WebKit.

%prep
%setup -q -n webkit-%{version}

# http://trac.webkit.org/browser/trunk/WebKit/gtk/JSCore.gir.in
%{__sed} -i -e 's,repository version="1.0",repository version="1.1",' WebKit/gtk/JSCore-1.0.gir

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

%find_lang webkit-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f webkit-2.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsc-1
%attr(755,root,root) %{_libdir}/libwebkitgtk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkitgtk-1.0.so.0
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
%attr(755,root,root) %{_libdir}/libwebkitgtk-1.0.so
%{_libdir}/libwebkitgtk-1.0.la
%if %{with introspection}
%{_datadir}/gir-1.0/JSCore-1.0.gir
%{_datadir}/gir-1.0/WebKit-1.0.gir
%endif
%{_includedir}/webkit-1.0
%{_pkgconfigdir}/webkit-1.0.pc
