%define release 1
%define prefix /usr
%define name madedit
%define version 0.3.4.1


Summary: madedit : GTK+ based text/hex editor
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Vendor: Alston Chen
URL: http://madedit.sourceforge.net/
Group: Applications/Editors
Source0: %{name}-%{version}.tar.gz
Packager: Minggang Li <minggang.li@gmail.com>
BuildRoot: %{_builddir}/%{name}-%{version}-root

BuildRequires: gtk2-devel >= 2.4.0
Requires: gtk2 >= 2.4.0

Docdir: %{prefix}/share/doc

%description
MadEdit is a cross-platform Text/Hex Editor.
MadEdit supports many useful functions, e.g. SyntaxHighlightings,
WordWrap, Encodings, Column/Hex Modes.

%prep
%setup

%build

%configure --with-wx-config=${HOME}/wxWidgets/RELEASE/wx-config LIBS="${HOME}/wxWidgets/RELEASE/lib/libwx_gtk2u_core-2.8.a ${HOME}/wxWidgets/RELEASE/lib/libwx_baseu-2.8.a -lgtk-x11-2.0 -lgthread-2.0 /usr/X11R6/lib/libXinerama.a /usr/X11R6/lib/libXxf86vm.a /usr/X11R6/lib/libSM.a /usr/X11R6/lib/libICE.a" glib_gtk2_LIBS="-lm" WX_LIBS="-lm"
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,0755)
%doc README.txt
%{_bindir}/*
%{_datadir}/madedit/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/locale/zh_TW/LC_MESSAGES/madedit.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/madedit.mo
%{_datadir}/locale/it_IT/LC_MESSAGES/madedit.mo
%{_datadir}/locale/ja_JP/LC_MESSAGES/madedit.mo
%{_datadir}/locale/ru_RU/LC_MESSAGES/madedit-mod.mo
%{_datadir}/locale/es/LC_MESSAGES/madedit-mod.mo
%{_datadir}/locale/el/LC_MESSAGES/madedit-mod.mo
%{_datadir}/locale/de_DE/LC_MESSAGES/madedit-mod.mo
%{_datadir}/locale/pl_PL/LC_MESSAGES/madedit-mod.mo

%changelog
