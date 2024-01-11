%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE personal alarm message, command and email scheduler
Name:		plasma6-kalarm
Version:	24.01.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kalarm-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6MailCommon)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6PimCommon)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	xsltproc
BuildRequires:	sasl-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(x11)
Conflicts:	kmail < 3:17.04.0
Conflicts:	kalarm < 3:17.04.0
Obsoletes:	kalarmcal < %{EVRD}
Obsoletes:	%{_lib}KF6AlarmCal6 < %{EVRD}

%description
KAlarm is a personal alarm message, command and email scheduler. It lets you
set up personal alarm messages which pop up on the screen at the chosen time,
or you can schedule commands to be executed or emails to be sent.

%files -f kalarm.lang
%{_datadir}/applications/org.kde.kalarm.desktop
%{_sysconfdir}/xdg/autostart/kalarm.autostart.desktop
%{_bindir}/kalarm
%{_bindir}/kalarmautostart
%{_datadir}/config.kcfg/kalarmconfig.kcfg
%dir %{_datadir}/kalarm/
%{_datadir}/kalarm/*
%{_docdir}/*/*/kalarm
%{_iconsdir}/hicolor/*/apps/kalarm.*
%{_datadir}/qlogging-categories6/kalarm.categories
%{_datadir}/qlogging-categories6/kalarm.renamecategories
%{_datadir}/metainfo/org.kde.kalarm.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_datadir}/dbus-1/system-services/org.kde.kalarm.rtcwake.service
%{_datadir}/dbus-1/system.d/org.kde.kalarm.rtcwake.conf
%{_datadir}/knotifications6/kalarm.notifyrc
%{_datadir}/polkit-1/actions/org.kde.kalarm.rtcwake.policy
%{_libdir}/qt6/plugins/pim6/kalarm/akonadiplugin.so
%{_libdir}/libexec/kf6/kauth/kalarm_helper
%{_libdir}/libkalarmcalendar.so*
%{_libdir}/libkalarmplugin.so*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kalarm-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kalarm
