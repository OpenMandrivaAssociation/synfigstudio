%define major		0
%define libname		%mklibname synfigapp %{major}
%define develname	%mklibname synfigapp -d

Name:		synfigstudio
Summary:	Vector-based 2D animation GUI
Version:	0.64.3
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		http://www.synfig.org
Source0:	http://sourceforge.net/projects/synfig/files/releases/0.64.3/source/%{name}-%{version}.tar.gz
Patch0:		synfigstudio-0.64.3-cflags.patch
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ETL) >= 0.04.17
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(synfig) >= 0.64.3
BuildRequires:	synfig  >= 0.64.3
BuildRequires:  autoconf
BuildRequires:  intltool
BuildRequires:	fontconfig
BuildRequires:  desktop-file-utils
Requires:	synfig >= 0.64.3

%description
synfig is a vector based 2D animation renderer. It is designed to be
capable of producing feature-film quality animation.

This package contains the graphical user interface for synfig.

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

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure --disable-update-mimedb
%make

%install
%makeinstall_std

desktop-file-install \
        --delete-original                                       \
        --dir=%{buildroot}%{_datadir}/applications           \
        %{buildroot}%{_datadir}/applications/synfigstudio.desktop
        
%find_lang %{name}        

%files -f %{name}.lang
%doc AUTHORS README NEWS TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/%{name}

%files -n %{libname}
%{_libdir}/libsynfigapp.so.%{major}*

%files -n %{develname}
%{_libdir}/libsynfigapp.so
%{_includedir}/synfigapp-0.0

