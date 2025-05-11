%define major 16

%define veryoldlibname	%mklibname avif 15
%define oldlibname	%mklibname avif %{major}
%define libname		%mklibname avif
%define develname	%mklibname avif -d

Name:       libavif
Version:    1.3.0
Release:    1
Summary:    Library for encoding and decoding .avif files
 
License:    BSD
URL:        https://github.com/AOMediaCodec/libavif
Source0:    https://github.com/AOMediaCodec/libavif/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libavif-no-avifgainmaputil.patch
 
BuildRequires:  cmake
BuildRequires:  nasm
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libyuv)
BuildRequires:  pkgconfig(libsharpyuv)
BuildRequires:  pkgconfig(SvtAv1Enc)

 
%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:
 
https://aomediacodec.github.io/av1-avif/

%package -n %{libname}
Summary:        Libavif is shared library from libavif
Group:          System/Libraries
%rename %{oldlibname}
Obsoletes:	%{veryoldlibname} < %{EVRD}

%description -n %{libname}
Libavif is shared library from libavif
 
%package -n %{develname}
Summary:        Development files for libavif
Requires:       %{libname} = %{version}
Requires:	pkgconfig(libyuv)
# Renamed 2025/02/11 before 6.0
%if "%{develname}" != "%{name}-devel"
%rename %{name}-devel
%endif
 
%description -n %{develname}
This package holds the development files for libavif.
 
%package tools
Summary:        Tools to encode and decode AVIF files
 
%description tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:
 
https://aomediacodec.github.io/av1-avif/
 
This package holds the commandline tools to encode and decode AVIF files.
 
%package     -n avif-pixbuf-loader
Summary:        AVIF image loader for GTK+ applications
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
Requires:       gdk-pixbuf2.0
 
%description -n avif-pixbuf-loader
Avif-pixbuf-loader contains a plugin to load AVIF images in GTK+ applications.
 
%prep
%autosetup -p1
 
%build
%cmake  -DAVIF_CODEC_AOM=SYSTEM \
        -DAVIF_CODEC_DAV1D=SYSTEM \
        -DAVIF_CODEC_RAV1E=SYSTEM \
        -DAVIF_CODEC_SVT=SYSTEM \
	-DAVIF_JPEG=SYSTEM \
	-DAVIF_LIBSHARPYUV=SYSTEM \
	-DAVIF_LIBYUV=SYSTEM \
	-DAVIF_ZLIBPNG=SYSTEM \
        -DAVIF_BUILD_APPS=ON \
        -DAVIF_BUILD_GDK_PIXBUF=ON \
	-G Ninja
%ninja_build

%install
%ninja_install -C build


%files -n %{libname}
%{_libdir}/libavif.so.%{major}*

%files -n %{develname}
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc
 
%files tools
%doc CHANGELOG.md README.md
%{_bindir}/avifdec
%{_bindir}/avifenc
%{_bindir}/avifgainmaputil
 
%files -n avif-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-avif.so
%{_datadir}/thumbnailers/avif.thumbnailer
