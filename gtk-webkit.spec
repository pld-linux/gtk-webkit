# TODO: optflags
%define snap	r28383
Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	1.0.0
Release:	0.%{snap}.1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://nightly.webkit.org/files/trunk/src/WebKit-%{snap}.tar.bz2
# Source0-md5:	84feb25058000b15be34e09db7679b7a
URL:		http://www.webkit.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel >= 7.11.0
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.0
BuildRequires:	gperf
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.0.0
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
Requires:	librsvg-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	xorg-lib-libXft-devel >= 2.0.0

%description devel
Development files for webkit.

%description devel -l pl.UTF-8
Pliki programistyczne webkit.

%prep
%setup -q -n WebKit-%{snap}

%build
WebKitTools/Scripts/build-webkit --gtk \
	--qmakearg=WEBKIT_INC_DIR=%{_includedir}/WebKit \
	--qmakearg=WEBKIT_LIB_DIR=%{_libdir} \
	--qmake=qt4-qmake

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C WebKitBuild/Release install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWebKitGtk.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWebKitGtk.so
%{_libdir}/libWebKitGtk.prl
%{_includedir}/WebKit
%{_pkgconfigdir}/WebKitGtk.pc
