%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE personal alarm message, command and email scheduler
Name:		kalarm
Version:	23.08.5
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(KPim5IMAP)
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5AkonadiContact)
BuildRequires:	cmake(KPim5AkonadiMime)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KPim5CalendarUtils)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KPim5IdentityManagement)
BuildRequires:	cmake(KPim5Libkdepim)
BuildRequires:	cmake(KPim5MailCommon)
BuildRequires:	cmake(KPim5MailTransport)
BuildRequires:	cmake(KPim5Mime)
BuildRequires:	cmake(KPim5PimCommon)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	xsltproc
BuildRequires:	sasl-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(x11)
Conflicts:	kmail < 3:17.04.0
Conflicts:	kalarm < 3:17.04.0
Obsoletes:	kalarmcal < %{EVRD}
Obsoletes:	%{_lib}KF5AlarmCal5 < %{EVRD}

%description
KAlarm is a personal alarm message, command and email scheduler. It lets you
set up personal alarm messages which pop up on the screen at the chosen time,
or you can schedule commands to be executed or emails to be sent.

%files -f %{name}.lang
%{_kde5_applicationsdir}/org.kde.kalarm.desktop
%{_kde5_autostart}/kalarm.autostart.desktop
%{_bindir}/kalarm
%{_bindir}/kalarmautostart
%{_datadir}/config.kcfg/kalarmconfig.kcfg
%dir %{_datadir}/kalarm/
%{_datadir}/kalarm/*
%{_docdir}/*/*/kalarm
%{_iconsdir}/hicolor/*/apps/kalarm.*
%{_libdir}/libexec/kauth/kalarm_helper
%{_datadir}/qlogging-categories5/kalarm.categories
%{_datadir}/qlogging-categories5/kalarm.renamecategories
%{_kde5_xmlguidir}/kalarm/kalarmui.rc
%{_datadir}/metainfo/org.kde.kalarm.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_datadir}/dbus-1/system-services/org.kde.kalarm.rtcwake.service
%{_datadir}/dbus-1/system.d/org.kde.kalarm.rtcwake.conf
%{_datadir}/knotifications5/kalarm.notifyrc
%{_datadir}/polkit-1/actions/org.kde.kalarm.rtcwake.policy
%{_libdir}/libkalarmcalendar.so.5*
%{_libdir}/libkalarmplugin.so.5*
%{_libdir}/qt5/plugins/pim5/kalarm/akonadiplugin.so
%{_datadir}/icons/*/*/*/show-today.*

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
