Name:       libavif
Version:    0.8.1
Release:    1
Summary:    Library for encoding and decoding .avif files
 
License:    BSD
URL:        https://github.com/AOMediaCodec/libavif
Source0:    https://github.com/AOMediaCodec/libavif/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:     https://patch-diff.githubusercontent.com/raw/AOMediaCodec/libavif/pull/270.patch
 
BuildRequires:  cmake
BuildRequires:  nasm
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(zlib)
 
%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:
 
https://aomediacodec.github.io/av1-avif/
 
%package devel
Summary:        Development files for libavif
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description devel
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
%cmake  -DAVIF_CODEC_AOM=1 \
        -DAVIF_CODEC_DAV1D=1 \
        -DAVIF_CODEC_RAV1E=1 \
        -DAVIF_BUILD_APPS=1 \
        -DAVIF_BUILD_GDK_PIXBUF=1
%make_build

%install
%make_install -C build

%files
%license LICENSE
%{_libdir}/libavif.so.6*
 
%files devel
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc
 
%files tools
%doc CHANGELOG.md README.md
%{_bindir}/avifdec
%{_bindir}/avifenc
 
%files -n avif-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-avif.so
