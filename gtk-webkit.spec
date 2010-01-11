# TODO: optflags
Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	1.1.18
Release:	0.1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/webkit-%{version}.tar.gz
# Source0-md5:	10e52c30837fe0e2ac663fcb4290e1d3
URL:		http://webkitgtk.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	enchant-devel >= 0.22
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.0
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-devel >= 2.28.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-devel
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
Requires:	fontconfig-devel >= 1.0.0
Requires:	glib2-devel >= 1:2.22.0
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libicu-devel
Requires:	libsoup-devel >= 2.28.0
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
	--enable-icon-database \
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
