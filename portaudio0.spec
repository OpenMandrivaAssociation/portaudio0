%define _provides_exceptions devel(libportaudio

%define	major 0
%define libname %mklibname portaudio %{major}

Summary:	Cross platform audio I/O library
Name:		portaudio0
Version:	18.1
Release:	%mkrel 14
URL:		http://www.portaudio.com/
Group:		System/Libraries
License:	BSD
Source0:	portaudio_v18_1.tar.bz2
Patch0:		portaudio_v18_1-libtool.diff
Patch1:		portaudio_v18_1-unix_oss.diff
Patch2:		portaudio_v18_1-oss_in_only.diff
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
Summary:	Cross platform audio I/O library
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
Conflicts:	portaudio-devel
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
autoreconf -fi
chmod a+x ./configure
%configure2_5x
%make

#CC="gcc" \
#    CFLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -D_GNU_SOURCE -Ipa_common -Ipablio"

%install
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE.txt README.txt
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc docs/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 18.1-14mdv2011.0
+ Revision: 667806
- mass rebuild

* Tue Dec 21 2010 Funda Wang <fwang@mandriva.org> 18.1-13mdv2011.0
+ Revision: 623669
- update libtool patch
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 18.1-12mdv2010.1
+ Revision: 521158
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 18.1-11mdv2010.0
+ Revision: 426748
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 18.1-10mdv2009.0
+ Revision: 225022
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Mar 06 2008 Anssi Hannula <anssi@mandriva.org> 18.1-9mdv2008.1
+ Revision: 180948
- simplify conflicts

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 18.1-8mdv2008.1
+ Revision: 171048
- rebuild
- summary is not licence tag
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Nov 14 2006 Anssi Hannula <anssi@mandriva.org> 18.1-7mdv2007.0
+ Revision: 83964
- provide portaudio0-devel

* Mon Nov 13 2006 Oden Eriksson <oeriksson@mandriva.com> 18.1-6mdv2007.0
+ Revision: 83786
- fix correct conflict

* Mon Nov 13 2006 Oden Eriksson <oeriksson@mandriva.com> 18.1-5mdv2007.1
+ Revision: 83712
- rebuild
- Import portaudio0

* Mon Nov 13 2006 Oden Eriksson <oeriksson@mandriva.com> 18.1-1mdv2007.1
- renamed to portaudio0
- nuke provides

* Fri Sep 16 2005 Oden Eriksson <oeriksson@mandriva.com> 18.1-4mdk
- use libtool to make the shared lib (P0, debian)
- added two oss patches (P1, P2, debian)

* Fri Sep 16 2005 Oden Eriksson <oeriksson@mandriva.com> 18.1-3mdk
- link it against -lpthread (gb)

* Fri May 06 2005 Oden Eriksson <oeriksson@mandriva.com> 18.1-2mdk
- fix requires-on-release

* Mon Sep 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 18.1-1mdk
- initial mandrake package
- build it different and add pablio to it (P0)

