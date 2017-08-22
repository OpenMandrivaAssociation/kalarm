Summary:	KDE personal alarm message, command and email scheduler
Name:		kalarm
Version:	17.08.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5AlarmCalendar)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5KdepimDBusInterfaces)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:	cmake(KF5MailTransportAkonadi)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5PimCommon)
BuildRequires:	cmake(KF5PimTextEdit)
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
%{_datadir}/kconf_update/kalarm*
%dir %{_datadir}/kalarm/
%{_datadir}/kalarm/*
%{_docdir}/*/*/kalarm
%{_iconsdir}/hicolor/*/apps/kalarm.*

%{_libdir}/libexec/kauth/kalarm_helper
%{_sysconfdir}/xdg/kalarm.categories
%{_sysconfdir}/xdg/kalarm.renamecategories
%{_kde5_xmlguidir}/kalarm/kalarmui.rc
%{_datadir}/metainfo/org.kde.kalarm.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_datadir}/dbus-1/system-services/org.kde.kalarmrtcwake.service
%{_datadir}/polkit-1/actions/org.kde.kalarmrtcwake.policy
%{_sysconfdir}/dbus-1/system.d/org.kde.kalarmrtcwake.conf

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
