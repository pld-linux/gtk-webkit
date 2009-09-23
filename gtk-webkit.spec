# TODO: optflags
Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	1.1.14
Release:	2
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/webkit-%{version}.tar.gz
# Source0-md5:	bff87d1ddc562223cb99201950d7e138
URL:		http://webkitgtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel >= 7.11.0
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.21.3
BuildRequires:	fontconfig-devel >= 1.0.0
BuildRequires:	gnome-keyring-devel >= 2.26.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.2.0
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxslt-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.0.0
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
webkit is a port of the WebKit embeddable web component to GTK+.

%description -l pl.UTF-8
webkit to port osadzalnego komponentu WWW WebKit do GTK+.

%package devel
Summary:	Development files for webkit
Summary(pl.UTF-8):	Pliki programistyczne webkit
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel >= 7.11.0
Requires:	fontconfig-devel >= 1.0.0
Requires:	libicu-devel
Requires:	librsvg-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	xorg-lib-libXft-devel >= 2.0.0

%description devel
Development files for webkit.

%description devel -l pl.UTF-8
Pliki programistyczne webkit.

%prep
%setup -q -n webkit-%{version}

%build
%{__gtkdocize}
%{__aclocal} -I autotools
%{__libtoolize}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-dom-storage \
	--enable-gnomekeyring \
	--enable-icon-database \
	--enable-svg-experimental \
	--enable-svg-filters \
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
%dir %{_datadir}/webkit-1.0
%{_datadir}/webkit-1.0/images
%{_datadir}/webkit-1.0/resources
%{_datadir}/webkit-1.0/webinspector

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkit-1.0.so
%{_libdir}/libwebkit-1.0.la
%{_includedir}/webkit-1.0
%{_pkgconfigdir}/webkit-1.0.pc
