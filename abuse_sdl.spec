%define	oname	abuse
%define	Summary	The classic Crack-Dot-Com game

Summary:	%{Summary}
Name:		%{oname}_sdl
Version:	0.8
Release:	%mkrel 69.1
License:	GPLv2
Group:		Games/Arcade
URL:		http://abuse.zoy.org/
Source0:	http://www.labyrinth.net.au/~trandor/files/%{oname}-%{version}.tar.gz
BuildRequires:	alsa-lib-devel
BuildRequires:	imagemagick
BuildRequires:	MesaGLU-devel
BuildRequires:	SDL-devel
Requires: TiMidity++
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot

%description
Abuse-SDL is a port of Abuse, the classic Crack-Dot-Com game, to the
SDL library. It can run at any color depth, in a window or fullscreen,
and it has stereo sound with sound panning.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Abuse
Comment=%{Summary}
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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS README TODO
%{_bindir}/abuse-tool
%{_gamesbindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{oname}
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_mandir}/man6/*
