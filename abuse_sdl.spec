%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define	oname	abuse

Summary:	The classic Crack-Dot-Com game
Name:		%{oname}_sdl
Version:	0.8
Release:	3
License:	GPLv2
Group:		Games/Arcade
URL:		http://abuse.zoy.org/
Source0:	http://www.labyrinth.net.au/~trandor/files/%{oname}-%{version}.tar.bz2
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	SDL_mixer-devel
Requires:	TiMidity++

%description
Abuse-SDL is a port of Abuse, the classic Crack-Dot-Com game, to the
SDL library. It can run at any color depth, in a window or fullscreen,
and it has stereo sound with sound panning.

%prep
%setup -q -n %{oname}-%{version}

%build
export CC=gcc
export CXX=g++
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Abuse
Comment=The classic Crack-Dot-Com game
Exec=%{_gamesbindir}/%{oname}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert doc/%{oname}.png %{buildroot}%{_iconsdir}/%{name}.png
convert -size 48x48 doc/%{oname}.png %{buildroot}%{_liconsdir}/%{name}.png
convert -size 16x16 doc/%{oname}.png %{buildroot}%{_miconsdir}/%{name}.png

install -d %{buildroot}{%{_gamesdatadir}/%{oname},%{_gamesbindir}}
mv %{buildroot}%{_bindir}/%{oname} %{buildroot}%{_gamesbindir}/%{oname}

%files
%doc AUTHORS README TODO
%{_bindir}/abuse-tool
%{_gamesbindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{oname}
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_mandir}/man6/*


%changelog
* Mon May 16 2011 Zombie Ryushu <ryushu@mandriva.org> 0.8-1mdv2011.0
+ Revision: 675074
- Fix build requires for mixer
- Fix build requires for mixer
- Fix build requires for mixer
- Fix 0.8
- Fix 0.8
- update to 0.8

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-3mdv2011.0
+ Revision: 609905
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2010.1
+ Revision: 508018
- use configure2_5x

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Dec 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdv2009.1
+ Revision: 311990
- nuke upstream implemented patches
- sync patches with fedora (P0,P1)

  + Zombie Ryushu <ryushu@mandriva.org>
    - Preliminary 0.7.1 Version
    - Preliminary 0.7.1 Version

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.7.0-12mdv2009.0
+ Revision: 218432
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.7.0-12mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix broken menu item (tried executing non-existant binary)


* Sun Jan 21 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7.0-11mdv2007.0
+ Revision: 111431
- sync with debian patches (should now work on x86_64, ppc & sparc too)
- Import abuse_sdl

* Fri Aug 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7.0-10mdv2007.0
- add xdg menu

* Tue Jun 27 2006 Lenny Cartier <lenny@mandriva.com> 0.7.0-9mdv2007.0
- rebuild

* Tue Mar 21 2006 Lenny Cartier <lenny@mandriva.com> 0.7.0-8mdk
- rebuild

* Wed Dec 15 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.7.0-7mdk
- add debian patches (P1)
- drop workaround patch (P0) as debian patch seems to really fix the problem (finally:)

* Wed Jun 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.7.0-6mdk
- rebuild
- change summary macro to avoid conflicts if we were to build debug package
- fix buildrequires for lib64

