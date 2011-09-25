%define         _state          stable
%define         orgname         smokeqt
%define         qtver           4.7.4

Summary:	smokeqt - A SMOKE library
Summary(pl.UTF-8):	smokeqt - Biblioteka SMOKE
Name:		smokeqt
Version:	4.7.1
Release:	4
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	147d73b6f05105ebacd4d8c2f316254c
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	phonon-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	qscintilla2-devel
BuildRequires:	qscintilla2-devel
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtDeclarative-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtHelp-devel >= %{qtver}
BuildRequires:	QtMultimedia-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	QtXmlPatterns-devel  >= %{qtver}
BuildRequires:	qwt-devel
BuildRequires:	smokegen-devel >= %{version}
Obsoletes:	kde4-kdebindings-smoke-qt < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMOKE library (Scripting Meta Object Kompiler Engine).

%description -l pl.UTF-8
Biblioteka SMOKE (Scripting Meta Object Kompiler Engine - silnik
kompilatora metaobiektów skryptowych).

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	smokegen-devel >= %{version}
Obsoletes:	kde4-kdebindings-smoke-devel < 4.6.99

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libsmoke*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmoke*.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/smoke
%{_datadir}/smokegen/qt-config.xml
%{_datadir}/smokegen/qtdefines
%attr(755,root,root) %{_libdir}/libsmoke*.so
