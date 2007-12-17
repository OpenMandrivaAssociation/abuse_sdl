%define	oname	abuse
%define	name	%{oname}_sdl
%define	version	0.7.0
%define	release	%mkrel 12
%define	Summary	The classic Crack-Dot-Com game
%define	frabsv	210

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.labyrinth.net.au/~trandor/files/%{name}-%{version}.tar.bz2
Source1:	http://www.cs.uidaho.edu/~cass0664/fRaBs/frabs%{frabsv}_unix.src.tar.bz2
#Patch0:	%{name}-nocrash-hack.patch.bz2
#Patch1: 	abuse_sdl-0.7.0-debian-fixes.patch.bz2
Patch2:		abuse_sdl-0.7.0-c++-compliance.patch
Patch3:		abuse_sdl-0.7.0-disable-lisp-cache.patch
Patch4:		abuse_sdl-0.7.0-datatypes.patch
Patch5:		abuse_sdl-0.7.0-header-order.patch
Patch6:		abuse_sdl-0.7.0-spelling.patch
Patch7:		abuse_sdl-0.7.0-stack-malloc-sizeof.patch
Patch8:		abuse_sdl-0.7.0-tint-fileptr.patch
Patch9:		abuse_sdl-0.7.0-unused-vars.patch
License:	GPL
Group:		Games/Arcade
URL:		http://www.labyrinth.net.au/~trandor/abuse/
BuildRequires:	ImageMagick SDL-devel alsa-lib-devel MesaGLU-devel

%description
Abuse-SDL is a port of Abuse, the classic Crack-Dot-Com game, to the
SDL library. It can run at any color depth, in a window or fullscreen,
and it has stereo sound with sound panning.

%prep
%setup -q -a1
#%patch0 -p0
#%patch1 -p1
%patch2 -p1 -b .c++_compliance
%patch3 -p1 -b .disable_lisp_cache
%patch4 -p1 -b .datatypes
%patch5 -p1 -b .header_order
%patch6 -p1 -b .spelling
%patch7 -p1 -b .stack_malloc_sizeof
%patch8 -p1 -b .tint_fileptr
%patch9 -p1 -b .unused_vars

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

mkdir -p %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{oname}" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="Abuse"\
		longtitle="%{Summary}" \
		xdg="true"
EOF

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
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert %{oname}.png %{buildroot}%{_iconsdir}/%{name}.png
convert -size 48x48 %{oname}.png %{buildroot}%{_liconsdir}/%{name}.png
convert -size 16x16 %{oname}.png %{buildroot}%{_miconsdir}/%{name}.png

install -d %{buildroot}{%{_gamesdatadir}/%{oname},%{_gamesbindir}}
mv %{buildroot}%{_bindir}/%{oname}.sdl %{buildroot}%{_gamesbindir}
cat > %{buildroot}%{_gamesbindir}/%{oname} << EOF
#!/bin/sh
cd %{_gamesdatadir}/%{oname}/frabs%{frabsv}_unix.src
exec %{_gamesbindir}/%{oname}.sdl -datadir %{_gamesdatadir}/%{oname}/frabs%{frabsv}_unix.src "\$@"
EOF
chmod +x $RPM_BUILD_ROOT%{_gamesbindir}/%{oname}
cp -a frabs%{frabsv}_unix.src %{buildroot}%{_gamesdatadir}/%{oname}/

%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc AUTHORS README TODO
%{_gamesbindir}/*
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{oname}
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_mandir}/man6/*


