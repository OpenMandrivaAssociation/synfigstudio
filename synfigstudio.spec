%define major		0
%define libname		%mklibname synfigapp %{major}
%define develname	%mklibname synfigapp -d

Name:		synfigstudio
Summary:	Vector-based 2D animation GUI
Version:	0.61.09
Release:	%mkrel 5
Source0:	http://downloads.sourceforge.net/synfig/%{name}-%{version}.tar.gz
URL:		http://www.synfig.org
License:	GPLv2+
Group:		Graphics
BuildRequires:	etl
BuildRequires:	synfig-devel
BuildRequires:	synfig
BuildRequires:	gtkmm2.4-devel
BuildRequires:	sigc++2.0-devel
BuildRequires:	libltdl-devel
BuildRequires:	gettext
BuildRequires:	cvs
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
synfig is a vector based 2D animation renderer. It is designed to be
capable of producing feature-film quality animation.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
synfig is a vector based 2D animation renderer. It is designed to be
capable of producing feature-film quality animation.

This package contains the shared library provided by synfigstudio.

%package -n %{develname}
Summary:	Development headers and libraries for %{name}
Group:		Development/C++
Provides:	synfigapp-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
synfig is a vector based 2D animation renderer. It is designed to be
capable of producing feature-film quality animation.

This package contains the development files for the shared library
provided by synfigstudio.

This package contains the graphical user interface for synfig.

%prep
%setup -q

%build
%configure2_5x
%make
								
%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

sed -i -e 's,synfig_icon.png,synfig_icon,g' %{buildroot}%{_datadir}/applications/*

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README NEWS TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/synfig_icon.*
%{_datadir}/mime-info/%{name}.*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsynfigapp.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libsynfigapp.so
%{_libdir}/*.*a
%{_includedir}/synfigapp-0.0

