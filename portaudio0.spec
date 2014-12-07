# (tpg) is this still needed ?
#define _provides_exceptions devel(libportaudio

%define major 0
%define libname %mklibname portaudio %{major}
%define devname %mklibname portaudio0 -d

Summary:	Cross platform audio I/O library
Name:		portaudio0
Version:	18.1
Release:	22
Group:		System/Libraries
License:	BSD
Url:		http://www.portaudio.com/
Source0:	portaudio_v18_1.tar.bz2
Patch0:		portaudio_v18_1-libtool.diff
Patch1:		portaudio_v18_1-unix_oss.diff
Patch2:		portaudio_v18_1-oss_in_only.diff

%description
PortAudio is a free, cross platform, open-source, audio I/O 
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh 
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support. 

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are 
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc. 

%package -n	%{libname}
Summary:	Cross platform audio I/O library
Group:		System/Libraries

%description -n	%{libname}
PortAudio is a free, cross platform, open-source, audio I/O 
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh 
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support. 

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are 
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc. 

%package -n	%{devname}
Summary:	Development library and header files for the PortAudio library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	portaudio-devel

%description -n	%{devname}
This package contains the development PortAudio library and its header
files.

%prep
%setup -qn portaudio_v18_1

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644

# strip away annoying ^M
find . -type f | xargs perl -p -i -e 's/\r//'

%patch0 -p1 -b .libtool
%patch1 -p0 -b .unix_oss
%patch2 -p0 -b .oss_in_only
autoreconf -fi
chmod a+x ./configure

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libportaudio.so.%{major}*

%files -n %{devname}
%doc docs/*
%doc LICENSE.txt README.txt
%{_includedir}/*
%{_libdir}/*.so

