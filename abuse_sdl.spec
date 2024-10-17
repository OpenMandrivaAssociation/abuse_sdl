%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define	oname	abuse

Summary:	The classic Crack-Dot-Com game
Name:		%{oname}_sdl
Version:	0.9.1
Release:	1
License:	GPLv2
Group:		Games/Arcade
URL:		https://abuse.zoy.org/
Source0:	https://github.com/Xenoveritas/abuse/archive/refs/tags/v%{version}.tar.gz
Patch:		abuse-0.9.1-compile.patch
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	SDL2_mixer-devel
BuildRequires:	cmake ninja
Requires:	TiMidity++

%description
Abuse-SDL is a port of Abuse, the classic Crack-Dot-Com game, to the
SDL library. It can run at any color depth, in a window or fullscreen,
and it has stereo sound with sound panning.

%prep
%autosetup -p1 -n %{oname}-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

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
%doc AUTHORS
%{_bindir}/abuse-tool
%{_gamesbindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{oname}
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
