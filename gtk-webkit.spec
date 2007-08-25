%define snap	20070810
Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webkit
Version:	0.0
Release:	0.%{snap}.1
License:	BSD-like
Group:		X11/Libraries
Source0:	webkit-svn.tar.bz2
# Source0-md5:	f021365830e08bf10b3edb7d5a15bf3c
Patch0:		%{name}-qmake.patch
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
%setup -q -n webkit
%patch0 -p1

%build
WebKitTools/Scripts/build-webkit --gdk

%install
rm -rf $RPM_BUILD_ROOT
cd WebKitBuild/Release
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWebKitGdk.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWebKitGdk.so
%{_libdir}/libWebKitGdk.prl
%{_includedir}/qt4/WebKitGtk
%{_pkgconfigdir}/WebKitGdk.pc
