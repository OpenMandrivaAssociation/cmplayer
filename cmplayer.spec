######################################################
# SpecFile: cmplayer.spec
# Generato: http://www.mandrivausers.ro/
# MRB: Falticska Florin
# this spec file assume the source license
######################################################

Summary:	A multimedia player
Name: 		cmplayer
Version:	0.5.4
Release:	5
Group:		Video
License:	GPLv2
URL:		https://code.google.com/p/cmplayer
Source0:	http://cmplayer.googlecode.com/files/%{name}-%{version}-src.tar.gz
Patch0:		cmplayer-0.5.4-ru.patch

BuildRequires:	qt4-devel >= 4.6
BuildRequires:	vlc-devel >= 1.1
Requires:	vlc >= 1.1
Suggests:	task-vlc >= 1.1

%description
CMPlayer is a media player.
Features:
-can play files and DVD
-generates playlist automatically
-supports DVD menu
-can change playback speed
-supports A-B repeat
-remembers play history
-can replay from stopped point
-and many, many more

%prep
%setup -q
%patch0 -p1 -b .ru
rm -rf arch
rm -rf debian
rm -rf rpm

%build
%make QMAKE=qmake \
	PREFIX=%{_prefix} \
	CMPLAYER_ACTION_PATH=%{_datadir}/kde4/apps/solid/actions \
	CMPLAYER_VLC_PLUGINS_PATH=%{_libdir}/%{name}/vlc-plugins

%install
make QMAKE=qmake \
	PREFIX=%{_prefix} \
	DEST_DIR=%{buildroot} \
	CMPLAYER_ACTION_PATH=%{_datadir}/kde4/apps/solid/actions \
	CMPLAYER_VLC_PLUGINS_PATH=%{_libdir}/%{name}/vlc-plugins \
	install

%files
%doc copyright.txt gpl.txt icon-authors.txt icon-copying.txt install.txt changes.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/vlc-plugins/libcmplayer-afilter_plugin.so
%{_libdir}/%{name}/vlc-plugins/libcmplayer-vfilter_plugin.so
%{_libdir}/%{name}/vlc-plugins/libcmplayer-vout_plugin.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/solid/actions/%{name}-opendvd.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

