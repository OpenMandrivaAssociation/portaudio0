%define _provides_exceptions devel(libportaudio

%define	major 0
%define libname %mklibname portaudio %{major}
%define conflict1 %mklibname portaudio 2

Summary:	PortAudio is a free, cross platform, open-source, audio I/O library
Name:		portaudio0
Version:	18.1
Release:	%mkrel 7
URL:		http://www.portaudio.com/
Group:		System/Libraries
License:	BSD
Source0:	portaudio_v18_1.tar.bz2
Patch0:		portaudio_v18_1-libtool.diff
Patch1:		portaudio_v18_1-unix_oss.diff
Patch2:		portaudio_v18_1-oss_in_only.diff
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
Summary:	PortAudio is a free, cross platform, open-source, audio I/O library
Group:          System/Libraries

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

%package -n	%{libname}-devel
Summary:	Static library and header files for the PortAudio library
Group:		Development/C
Conflicts:	%{conflict1}-devel
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
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

This package contains the static PortAudio library and its header
files.

%prep

%setup -q -n portaudio_v18_1

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644

# strip away annoying ^M
find . -type f | xargs perl -p -i -e 's/\r//'

%patch0 -p1 -b .libtool
%patch1 -p0 -b .unix_oss
%patch2 -p0 -b .oss_in_only

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal-1.7; autoconf

%configure2_5x

%make

#CC="gcc" \
#    CFLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -D_GNU_SOURCE -Ipa_common -Ipablio"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE.txt README.txt
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc docs/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a


