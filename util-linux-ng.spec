#
# Conditional build:
%bcond_with		uClibc		# link initrd version with static glibc instead of uClibc
%bcond_without	dietlibc	# link initrd version with dietlibc instead of uClibc
%bcond_without	selinux 	# SELinux support
%if "%{pld_release}" == "ac"
%bcond_with		initrd		# don't build initrd version
%bcond_with		fallocate	# fallocate utility (needs glibc 2.11 to compile)
%else
%bcond_without	initrd		# don't build initrd version
%bcond_without	fallocate	# fallocate utility (needs glibc 2.11 to compile)
%endif

%if "%{pld_release}" == "ac"
%define		pam_ver 0.79.0
%else
%define		pam_ver 0.99.7.1
%endif

Summary:	Collection of basic system utilities for Linux
Summary(de.UTF-8):	Sammlung von grundlegenden Systemdienstprogrammen für Linux
Summary(es.UTF-8):	Colectánea de utilitarios básicos de sistema para Linux
Summary(fr.UTF-8):	Ensemble d'utilitaires système de base pour Linux
Summary(pl.UTF-8):	Zbiór podstawowych narzędzi systemowych dla Linuksa
Summary(pt_BR.UTF-8):	Coletânea de utilitários básicos de sistema para Linux
Summary(ru.UTF-8):	Набор базовых системных утилит для Linux
Summary(tr.UTF-8):	Temel sistem araçları
Summary(uk.UTF-8):	Набір базових системних утиліт для Linux
Name:		util-linux-ng
Version:	2.19
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.kernel.org/pub/linux/utils/util-linux/v2.19/util-linux-%{version}.tar.bz2
# Source0-md5:	590ca71aad0b254e2631d84401f28255
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/util-linux-non-english-man-pages.tar.bz2
# Source1-md5:	3c940c7e7fe699eaa2ddb1bffb3de2fe
Source2:	login.pamd
Source3:	util-linux-blockdev.init
Source4:	util-linux-blockdev.sysconfig
Patch0:		%{name}-ppc.patch
Patch1:		%{name}-union-mount.patch
Patch2:		util-linux-ctrlaltdel-man.patch
Patch3:		util-linux-fdformat-ide.patch
Patch4:		util-linux-fhs.patch
Patch5:		util-linux-hotkeys.patch
Patch7:		util-linux-login-lastlog.patch
Patch8:		util-linux-procpartitions.patch
Patch9:		util-linux-swaponsymlink.patch
Patch10:	util-linux-diet.patch
URL:		http://userweb.kernel.org/~kzak/util-linux/
BuildRequires:	audit-libs-devel >= 1.0.6
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel
%{?with_fallocate:BuildRequires:	glibc-devel >= 6:2.11}
BuildRequires:	gtk-doc-automake
%{?with_selinux:BuildRequires:	libselinux-devel}
%{?with_selinux:BuildRequires:	libsepol-devel}
BuildRequires:	libtool
BuildRequires:	linux-libc-headers >= 7:2.6.27
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pam-devel >= %{pam_ver}
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.470
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
%if %{with initrd}
	%if %{with uClibc}
BuildRequires:	uClibc-static >= 2:0.9.29
	%else
		%if %{with dietlibc}
BuildRequires:	dietlibc-static >= 2:0.32-7
		%else
BuildRequires:	glibc-static
		%endif
	%endif
%endif
Requires:	pam >= %{pam_ver}
Provides:	fdisk
Provides:	linux32
Provides:	sparc32
Provides:	util-linux = %{version}-%{release}
Obsoletes:	cramfs
Obsoletes:	ionice
Obsoletes:	linux32
Obsoletes:	rawdevices
Obsoletes:	schedutils
Obsoletes:	setarch
Obsoletes:	sparc32
Obsoletes:	util-linux
Obsoletes:	util-linux-suids
Conflicts:	e2fsprogs < 1.41.8-5
Conflicts:	shadow-extras < 1:4.0.3-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debugcflags	-O1 -g

# for some reason known only to rpm there must be "\\|" not "\|" here
%define		dietarch	%(echo %{_target_cpu} | sed -e 's/i.86\\|pentium.\\|athlon/i386/;s/amd64/x86_64/;s/armv.*/arm/')
%define		dietlibdir	%{_prefix}/lib/dietlibc/lib-%{dietarch}

%ifarch ppc ppc64
# for dietlibc
%define		filterout_ld	-Wl,-z,relro
%endif

%description
util-linux contains a large variety of low-level system utilities
necessary for a functional Linux system. This includes, among other
things, configuration tools such as fdisk and system programs such as
logger.

%description -l de.UTF-8
util-linux enthält eine große Anzahl an
low-level-Systemdienstprogrammen, die für ein funktionierendes
Linux-System erforderlich sind. Dazu gehören Konfigurationstools wie
'fdisk' und Systemprogramme wie 'logger'.

%description -l es.UTF-8
util-linux contiene una gran variedad de utilitarios de sistema de
bajo nivel necesarios a un sistema Linux funcional. Esto incluye,
entre otras cosas, herramientas de configuración como fdisk y
programas de sistema como logger.

%description -l fr.UTF-8
util-linux contient une grande variété d'utilitaire système bas niveau
nécessaires au fonctionnement d'un système Linux. Cela comprend, entre
autres, les outils de configuration comme fdisk et des programmes
systèmes comme logger.

%description -l pl.UTF-8
util-linux zawiera wiele różnych, niskopoziomowych narzędzi
systemowych niezbędnych do prawidłowego działania Linuksa. W pakiecie
znajdują się między innymi narzędzia konfiguracyjne, takie jak fdisk i
programy systemowe, takie jak logger.

%description -l pt_BR.UTF-8
util-linux contém uma grande variedade de utilitários de sistema de
baixo-nível necessários para um sistema Linux funcional. Isso inclui,
entre outras coisas, ferramentas de configuração como fdisk e
programas de sistema como logger.

%description -l ru.UTF-8
Этот пакет содержит большой набор системных утилит низкого уровня,
которые необходимы для функционирования системы Linux. Он включает, в
числе прочих, инструменты конфигурации, такие как fdisk, и системные
программы, такие как logger.

%description -l tr.UTF-8
şlevsel durumdaki bir Linux sistemi için gerekli birçok alt düzey
sistem araçlarını içerir. Bunlar arasında fdisk gibi yapılandırma
uygulamaları ve logger gibi sistem programları sayılabilir.

%description -l uk.UTF-8
Цей пакет містить великий набір системних утиліт низького рівня, які
необхідні для функціонування системи Linux. Він містить, окрім інших,
конфігураційні інструменти (такі як fdisk) та системні програми (такі
як logger).

%package -n blockdev
Summary:	Support for blockdev
Summary(pl.UTF-8):	Obsługa blockdev
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	coreutils
Requires:	rc-scripts

%description -n blockdev
The utility blockdev allows one to call block device ioctls from the
command line. This package also includes initscript to set blockdev
parameters at system startup.

%description -n blockdev -l pl.UTF-8
Narzędzie blockdev pozwala na wywołania ioctl dla urządzeń blokowych z
linii poleceń. Ten pakiet zawiera także skrypt inicjalizacyjny do
ustawiania parametrów blockdev przy starcie systemu.

%package -n losetup
Summary:	Programs for setting up and configuring loopback devices
Summary(de.UTF-8):	Programme zum Einrichten und Konfigurieren von Loopback-Geräten
Summary(fr.UTF-8):	Programmes pour mettre en place et configurer les loopback
Summary(pl.UTF-8):	Program do konfiguracji urządzenia blokowego loopback
Summary(ru.UTF-8):	Программы для настройки loopback-устройств
Summary(tr.UTF-8):	Yerel-çevrim aygıtlarının kurulması ve ayarlanması için programlar
Summary(uk.UTF-8):	Програми для конфігурації loopback-пристроїв
Group:		Applications/System

%description -n losetup
Linux supports a special block device called the loopback device,
which maps a normal file onto a virtual block device. This package
contains programs for setting up and removing the mapping between
files and loopback devices.

Block loopback devices should not be confused with the networking
loopback device, which is configured with the normal ifconfig command.

%description -n losetup -l de.UTF-8
Linux unterstützt ein spezielles Blockgerät, das sogenannte Loopback,
das eine normale Datei auf ein virtuelles Blockgerät abbildet. Das
Paket enthält Programme zum Einrichten und Entfernen der Zuordnung
zwischen Dateien und Loopback-Geräten.

%description -n losetup -l fr.UTF-8
Linux gère un périphérique bloc spécial appelé « loopback », qui
correspond à un fichier normal sur un périphérique bloc virtuel. Ce
paquetage contient les programmes pour configurer et supprimer la
correspondance entre les fichiers et les périphériques loopback.

Les périphériques bloc loopback ne doivent pas être confondus avec le
périphérique loopback du réseau, configuré avec la commande ifconfig
normale.

%description -n losetup -l pl.UTF-8
Linux wspiera specjalne urządzenie blokowe loopback, które mapuje
normalny plik w wirtualne urządzenie blokowe. Pakiet ten zawiera
program, przy pomocy którego będziesz mógł je skonfigurować.

Urządzenie blokowe loopback nie powinno być mylone z sieciowym
interfejsem loopback, który jest konfigurowany przy pomocy polecenia
ifconfig.

%description -n losetup -l ru.UTF-8
Linux поддерживает специальное блочное устройство, называемое
loopback, которое отображает обычный файл в виртуальное блочное
устройство. Это позволяет использовать файл как виртуальную файловую
систему. Losetup используется для связи loopback-устройств с обычными
файлами или блочными устройствами, для отсоединения loopback-устройств
и запросов их статуса.

%description -n losetup -l tr.UTF-8
Linux özel bir blok aygıt olan yerel-çevrim aygıtını (loopback device)
destekler. Bu aygıt normal bir dosyanın sanal bir blok aygıtı üzerine
haritasını çıkarır. Bu paket, dosyalar ve yerel-çevrim aygıtları
arasındaki haritalama işleminin kurulması ve kaldırılması için
programlar içerir. Blok yerel-çevrim aygıtı ifconfig komutu ile
yapılandırılan ağ yerel-çevrim aygıtı ile karıştırılmamalıdır.

%description -n losetup -l uk.UTF-8
Linux підтримує спеціальний блочний пристрій, loopback, який
відображує звичайний файл у віртуальний блочний пристрій. Це дозволяє
використовувати файл як віртуальну файлову систему. Losetup
використовують для зв'язку loopback-пристроїв зі звичайними файлами
або блочними пристроями, для від'єднання loopback-пристроїв та
запросів їх стану.

%package -n mount
Summary:	Programs for mounting and unmounting filesystems
Summary(de.UTF-8):	Programme zum montieren und abmontieren von Dateisystemen
Summary(fr.UTF-8):	Programme pour monter et démonter des systèmes de fichiers
Summary(pl.UTF-8):	Programy do montowania i odmontowywania systemów plików
Summary(ru.UTF-8):	Программы для монтирования и размонтирования файловых систем
Summary(tr.UTF-8):	Dosya sistemlerini bağlamak ve çözmek için programlar
Summary(uk.UTF-8):	Програми для монтування та розмонтування файлових систем
Group:		Applications/System
Conflicts:	nfs-utils-common < 1.1.3-3

%description -n mount
mount is used for adding new filesystems, both local and networked, to
your current directory structure. The filesystems must already exist
for this to work. It can also be used to change the access types the
kernel uses for already-mounted filesystems.

This package is critical for the functionality of your system.

%description -n mount -l de.UTF-8
mount wird zum Hinzufügen neuer Dateisysteme (lokal und im Netzwerk)
zu Ihrer aktuellen Verzeichnisstruktur verwendet. Die Dateisysteme
müssen bereits existieren. Außerdem können die Zugriffstypen geändert
werden, die der Kernel für bereits montierte Dateisysteme verwendet.

Dieses Paket ist für Ihr System unbedingt erforderlich.

%description -n mount -l fr.UTF-8
mount sert à ajouter de nouveaux systèmes de fichiers, locaux ou
réseaux, à votre structure de répertoire. Les systèmes de fichiers
doivent déjà exister pour que cela fonctionne. Il peut aussi servir à
changer les types d'accès pour les systèmes de fichiers déjà montés.

Ce paquetage est critique pour le fonctionnement de votre système.

%description -n mount -l pl.UTF-8
Program mount jest używany przez system do montowania systemów plików,
zarówno lokalnych jak i sieciowych (np. NFS).

Pakiet ten jest niezbędny do prawidłowej pracy twojego Linuksa.

%description -n mount -l ru.UTF-8
Пакет mount содержит программы mount, umount, swapon и swapoff. Файлы
в вашей системе организованы в виде одного большого дерева или
иерархии. Эти файлы могут быть размещены на разных устройствах.
Команда mount присоединяет файловую систему на некотором устройстве к
дереву файлов вашей системы. Команда umount отсоединяет файловую
систему от дерева. Swapon и swapoff, соответственно, разрешает и
запрещает своппинг в определенные файлы и устройства.

%description -n mount -l tr.UTF-8
mount, hem yerel hem de ağ dosya sistemlerinin dizin yapısına
eklenmesi için kullanılır. Bunun için bağlanacak dosya sisteminin
önceden hazırlanmış olması gerekir. Aynı zamanda çekirdeğin bağlanmış
dosya sistemlerine erişimini değiştirmek için de kullanılır. Bu paket
sisteminizin işlevselliği açısından kritiktir.

%description -n mount -l uk.UTF-8
Пакет mount містить програми mount, umount, swapon та swapoff. Файли у
вашій системі організовані у вигляді одного великого дерева або
ієрархії. Ці файли можуть бути розташовані на різних пристроях.
Команда mount під'єднує файлову систему на деякому пристрої до дерева
файлів вашої системи. Команда umount від'єднує файлову систему від
дерева. Swapon та swapoff, відповідно, дозволяє та заборонює свопінг у
визначені файли або пристрої.

%package chkdupexe
Summary:	chkdupexe - find duplicate executables
Summary(pl.UTF-8):	chkdupexe odszukuje powtarzające się pliki uruchamialne
Group:		Applications/System
Provides:	util-linux-chkdupexe = %{version}-%{release}
Obsoletes:	util-linux-chkdupexe

%description chkdupexe
chkdupexe will scan the union of $PATH and a hardcoded list of common
locations for binaries. It will report dangling symlinks and
duplicately-named binaries.

%description chkdupexe -l pl.UTF-8
chkdupexe przeszukuje katalogi z $PATH oraz inne powszechnie znane
katalogi z plikami uruchamialnymi i informuje o powtarzających się
plikach w różnych katalogach.

%package -n tunelp
Summary:	Configures kernel parallel port driver
Summary(de.UTF-8):	Konfiguriert den Kerneltreiber für den parallelen Port
Summary(fr.UTF-8):	Configure le pilote du port parallèle dans le noyau
Summary(pl.UTF-8):	Program do konfigurowania sterownika portu równoległego
Summary(tr.UTF-8):	Çekirdeğin paralel bağlantı noktası sürücüsünü ayarlar
License:	GPL v2+
Group:		Applications/System

%description -n tunelp
tunelp aids in configuring the kernel parallel port driver.

%description -n tunelp -l de.UTF-8
tunelp hilft bei der Konfiguration des Kernel-Parallelport-Treibers.

%description -n tunelp -l fr.UTF-8
« tunelp » aide à configurer le pilote du noyau pour le port
parallèle.

%description -n tunelp -l pl.UTF-8
Program do konfigurowania sterownika portu równoległego.

%description -n tunelp -l tr.UTF-8
Paralel bağlantı noktası sürücüsünü ayarlar.

%package -n login
Summary:	login is used when signing onto a system
Summary(pl.UTF-8):	login jest używany do rozpoczęcia pracy w systemie
Group:		Applications/System
Requires:	pam >= %{pam_ver}
Obsoletes:	heimdal-login

%description -n login
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however).

%description -n login -l pl.UTF-8
login jest używany do rozpoczęcia pracy w systemie. Może być używany
do przełączania z jednego użytkownika na innego w każdym momencie
(jednak większość nowoczesnych powłok ma takie funkcje wbudowane).

%package -n agetty
Summary:	Alternative Linux getty
Summary(pl.UTF-8):	Alternatywny getty
Group:		Applications/System
Requires:	login

%description -n agetty
agetty is simple Linux getty with serial support.

%description -n agetty -l pl.UTF-8
agetty jest prostym linuksowym getty z obsługą portu szeregowego.

%package -n libblkid
Summary:	Library to handle device identification and token extraction
Summary(pl.UTF-8):	Biblioteka do obsługi identyfikacji urządzeń
License:	LGPL v2.1+
Group:		Libraries
Requires:	libuuid = %{version}-%{release}
Obsoletes:	util-linux-ng-libs

%description -n libblkid
Library to handle device identification and token extraction.

%description -n libblkid -l pl.UTF-8
Biblioteka do obsługi identyfikacji urządzeń i wydobywania tokenów.

%package -n libblkid-devel
Summary:	Header files for blkid library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki blkid
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libblkid = %{version}-%{release}
Requires:	libuuid-devel = %{version}-%{release}
Obsoletes:	util-linux-ng-devel

%description -n libblkid-devel
Header files for blkid library.

%description -n libblkid-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki blkid.

%package -n libblkid-static
Summary:	Static library to handle device identification and token extraction
Summary(pl.UTF-8):	Statyczna biblioteka do obsługi identyfikacji urządzeń
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libblkid-devel = %{version}-%{release}
Requires:	libuuid-static = %{version}-%{release}
Obsoletes:	util-linux-ng-static

%description -n libblkid-static
Static library to handle device identification and token extraction.

%description -n libblkid-static -l pl.UTF-8
Statyczna biblioteka do obsługi identyfikacji urządzeń i wydobywania
tokenów.

%package -n libblkid-dietlibc
Summary:	Static dietlibc library to handle device identification and token extraction
Summary(pl.UTF-8):	Statyczna biblioteka dietlibc do obsługi identyfikacji urządzeń
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libblkid-devel = %{version}-%{release}
Requires:	libuuid-dietlibc = %{version}-%{release}

%description -n libblkid-dietlibc
Library to handle device identification and token extraction - static
dietlibc version.

%description -n libblkid-dietlibc -l pl.UTF-8
Biblioteka do obsługi identyfikacji urządzeń i wydobywania tokenów -
wersja statyczna dla dietlibc.

%package -n libuuid
Summary:	Library for accessing and manipulating UUID
Summary(pl.UTF-8):	Biblioteka umożliwiająca dostęp i zmiany UUID
License:	BSD
Group:		Libraries
Conflicts:	e2fsprogs < 1.34-3

%description -n libuuid
Library for accessing and manipulating UUID.

%description -n libuuid -l pl.UTF-8
Biblioteka umożliwiająca dostęp i zmiany UUID.

%package -n libuuid-devel
Summary:	Header files for library for accessing and manipulating UUID
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki umożliwiającej dostęp i zmiany UUID
License:	BSD
Group:		Development/Libraries
Requires:	libuuid = %{version}-%{release}
Conflicts:	e2fsprogs-devel < 1.34-3

%description -n libuuid-devel
Library for accessing and manipulating UUID - development files.

%description -n libuuid-devel -l pl.UTF-8
Biblioteka umożliwiająca dostęp i zmiany UUID - pliki dla
programistów.

%package -n libuuid-static
Summary:	Static library for accessing and manipulating UUID
Summary(pl.UTF-8):	Statyczna biblioteka umożliwiająca dostęp i zmiany UUID
License:	BSD
Group:		Development/Libraries
Requires:	libuuid-devel = %{version}-%{release}
Conflicts:	e2fsprogs-static < 1.34-3

%description -n libuuid-static
Library for accessing and manipulating UUID - static version.

%description -n libuuid-static -l pl.UTF-8
Biblioteka umożliwiająca dostęp i zmiany UUID - wersja statyczna.

%package -n libuuid-dietlibc
Summary:	Static dietlibc library for accessing and manipulating UUID
Summary(pl.UTF-8):	Statyczna biblioteka dietlibc umożliwiająca dostęp i zmiany UUID
License:	BSD
Group:		Development/Libraries
Requires:	libuuid-devel = %{version}-%{release}
Conflicts:	e2fsprogs-static < 1.34-3

%description -n libuuid-dietlibc
Library for accessing and manipulating UUID - static dietlibc version.

%description -n libuuid-dietlibc -l pl.UTF-8
Biblioteka umożliwiająca dostęp i zmiany UUID - wersja statyczna dla
dietlibc.

%package -n uuidd
Summary:	Helper daemon to guarantee uniqueness of time-based UUIDs
Summary(pl.UTF-8):	Pomocniczy demon gwarantujący unikalność UUID-ów opartych na czasie
License:	GPL v2
Group:		Daemons
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/groupmod
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/usermod
Requires:	libuuid = %{version}-%{release}
Provides:	group(uuidd)
Provides:	user(uuidd)
Conflicts:	libuuid < 1.40.5-0.1

%description -n uuidd
The uuidd package contains a userspace daemon (uuidd) which guarantees
uniqueness of time-based UUID generation even at very high rates on
SMP systems.

%description -n uuidd -l pl.UTF-8
Ten pakiet zawiera działającego w przestrzeni użytkownika demona
(uuidd) gwarantującego unikalność generowania UUID-ów opartych na
czasie nawet przy bardzo dużej częstotliwości na systemach SMP.

%package -n libmount
Summary:	Library to handle mounting-related tasks
Summary(pl.UTF-8):	Biblioteka obsługująca zadania związane z montowaniem
License:	LGPL
Group:		Libraries
Requires:	libblkid = %{version}-%{release}

%description -n libmount
Library to handle mounting-related tasks.

%description -n libmount -l pl.UTF-8
Biblioteka obsługująca zadania związane z montowaniem.

%package -n libmount-devel
Summary:	Header files for mount library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mount
License:	LGPL
Group:		Development/Libraries
Requires:	libblkid-devel = %{version}-%{release}
Requires:	libmount = %{version}-%{release}

%description -n libmount-devel
Header files for mount library.

%description -n libmount-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki mount.

%package -n libmount-static
Summary:	Static version of mount library
Summary(pl.UTF-8):	Statyczna wersja biblioteki mount
License:	LGPL
Group:		Development/Libraries
Requires:	libmount-devel = %{version}-%{release}

%description -n libmount-static
Static version of mount library.

%description -n libmount-static -l pl.UTF-8
Statyczna wersja biblioteki mount.

%package -n libmount-dietlibc
Summary:	Static dietlibc mount library
Summary(pl.UTF-8):	Statyczna biblioteka mount dla dietlibc
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libblkid-devel = %{version}-%{release}
Requires:	libblkid-dietlibc = %{version}-%{release}
Requires:	libuuid-devel = %{version}-%{release}
Requires:	libuuid-dietlibc = %{version}-%{release}

%description -n libmount-dietlibc
Static dietlibc version of mount library.

%description -n libmount-dietlibc -l pl.UTF-8
Statyczna wersja biblioteki mount dla dietlibc.

%package -n fsck
Summary:	Check and repair a Linux file system
Summary(pl.UTF-8):	Sprawdzanie i naprawa linuksowego systemu plików
Group:		Applications/System

%description -n fsck
Check and repair a Linux file system.

%description -n fsck -l pl.UTF-8
Sprawdzanie i naprawa linuksowego systemu plików.

%package initrd
Summary:	blkid - initrd version
Summary(pl.UTF-8):	blkid - wersja dla initrd
Group:		Base
Conflicts:	geninitrd < 10000.10

%description initrd
This package includes a blkid utility to recognize partitions by label
or UUID - staticaly linked for initrd.

%description initrd -l pl.UTF-8
Pakiet ten zawiera narzędzie blkid do rozpoznawania partycji przez
etykietę lub UUID - statycznie skonsolidowane na potrzeby initrd.

%prep
%setup -q -a1 -n util-linux-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

sed -i -e 's/-lncursesw/-lncursesw -ltinfow/' configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

export CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses -DHAVE_LSEEK64_PROTOTYPE -DHAVE_LLSEEK_PROTOTYPE"
%if %{with initrd}
%{?with_uClibc:xCC="%{_target_cpu}-uclibc-gcc"}
%{?with_dietlibc:xCC="diet %{__cc}"; xCC=${xCC#*ccache }}
%configure \
%if %{with dietlibc}
	ac_cv_header_crypt_h="no" \
%endif
	CC="$xCC" \
	--disable-shared \
	--enable-static \
	--disable-fsck \
	--disable-login-utils \
	--disable-schedutils \
	--disable-silent-rules \
	--disable-use-tty-group \
	--disable-wall \
	--without-audit \
	--without-ncurses \
	--without-pam \
	--without-selinux

# configure gets it unconditionally wrong
sed -i -e 's/#define HAVE_WIDECHAR 1//' config.h

sed -i -e 's/ cal\$(EXEEXT) / /; s/ lsblk\$(EXEEXT)//' misc-utils/Makefile

for dir in shlibs/* disk-utils misc-utils fsck fdisk schedutils hwclock; do
	%{__make} -C $dir \
	%if %{with uClibc}
		LDFLAGS="-Wl,-static"
	%endif
	%if %{with dietlibc}
		CPPFLAGS="$CPPFLAGS -D_BSD_SOURCE" \
		LDFLAGS="-lcompat"
	%endif
	# empty line required because there is a backslash up there
	%{__make} -C $dir install DESTDIR=`pwd`/initrd
done

%{__make} clean
%endif

%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	%{!?with_fallocate:--disable-fallocate} \
	--disable-silent-rules \
	--disable-use-tty-group \
	--disable-wall \
	--enable-kill \
	--enable-login-chown-vcs \
	--enable-login-utils \
	--enable-partx \
	--enable-write \
	--with-audit \
	--with-pam \
	--with%{!?with_selinux:out}-selinux

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,sysconfig,security} \
	$RPM_BUILD_ROOT{/%{_lib},/var/{lock,lib/libuuid}}
%{?with_dietlibc:install -d $RPM_BUILD_ROOT%{dietlibdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -i -e 's,/usr/spool/mail,/var/mail,g' $RPM_BUILD_ROOT%{_mandir}/man1/login.1

mv $RPM_BUILD_ROOT%{_sbindir}/{addpart,delpart,partx} $RPM_BUILD_ROOT/sbin

cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/login
install -p %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/blockdev
cp -a %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/blockdev

:> $RPM_BUILD_ROOT/etc/security/blacklist.login
:> $RPM_BUILD_ROOT/var/lock/wtmpxlock
:> $RPM_BUILD_ROOT%{_sysconfdir}/blkid.tab

for lib in blkid uuid mount; do
	mv $RPM_BUILD_ROOT%{_libdir}/lib${lib}.so.* $RPM_BUILD_ROOT/%{_lib}
	ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/lib${lib}.so.*.*.*) \
		 $RPM_BUILD_ROOT%{_libdir}/lib${lib}.so
done

ln -sf hwclock $RPM_BUILD_ROOT/sbin/clock
echo '.so hwclock.8' > $RPM_BUILD_ROOT%{_mandir}/man8/clock.8

for d in cs de es fi fr hu id it ja ko nl pl ; do
	for m in man1 man5 man8 ; do
		if [ -d man/$d/$m ]; then
			install -d $RPM_BUILD_ROOT%{_mandir}/$d/$m
			cp -a man/$d/$m/* $RPM_BUILD_ROOT%{_mandir}/$d/$m
		fi
	done
done

# cleanup, remove files not included in package
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{chfn,chsh,newgrp} \
	$RPM_BUILD_ROOT%{_sbindir}/{vigr,vipw} \
	$RPM_BUILD_ROOT%{_mandir}/man1/{chfn,chsh,newgrp}.1 \
	$RPM_BUILD_ROOT%{_mandir}/man8/{vigr,vipw}.8 \
	$RPM_BUILD_ROOT%{_mandir}/*/man1/{arch,reset}.1 \
	$RPM_BUILD_ROOT%{_mandir}/*/man5/nfs.5 \
	$RPM_BUILD_ROOT%{_mandir}/*/man8/{elvtune,setfdprm,sln,ramsize,raw,rdev,rootflags,vidmode}.8

%ifarch sparc sparc64
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man8/{cfdisk,sfdisk}.8
%endif

%if %{with initrd}
install -d $RPM_BUILD_ROOT%{_libdir}/initrd
install -p initrd%{_bindir}/* $RPM_BUILD_ROOT%{_libdir}/initrd/
install -p initrd%{_sbindir}/* $RPM_BUILD_ROOT%{_libdir}/initrd/
ln -s fsck $RPM_BUILD_ROOT%{_libdir}/initrd/e2fsck

# We don't need those
%{__rm} $RPM_BUILD_ROOT%{_libdir}/initrd/{chkdupexe,ddate,uuidd,mcookie,whereis,mkfs*,fsck.minix,isosize,logger}

%if %{with dietlibc}
cp -a initrd%{_libdir}/lib*.a $RPM_BUILD_ROOT%{dietlibdir}
%endif
%endif

%find_lang util-linux

%clean
rm -rf $RPM_BUILD_ROOT

%post -n blockdev
/sbin/chkconfig --add blockdev
%service blockdev restart

%preun -n blockdev
if [ "$1" = "0" ]; then
	%service blockdev stop
	/sbin/chkconfig --del blockdev
fi

%post	-n libblkid -p /sbin/ldconfig
%postun -n libblkid -p /sbin/ldconfig

%post   -n libuuid -p /sbin/ldconfig
%postun -n libuuid -p /sbin/ldconfig

%pre    -n uuidd
if [ "$(getgid libuuid 2>/dev/null)" = "222" ]; then
        /usr/sbin/groupmod -n uuidd libuuid
fi
%groupadd -g 222 uuidd
if [ "$(id -u libuuid 2>/dev/null)" = "222" ]; then
        /usr/sbin/usermod -l uuidd libuuid
fi
%useradd -u 222 -r -d /var/lib/libuuid -s /bin/false -c "UUID generator helper daemon" -g uuidd uuidd

%postun -n uuidd
if [ "$1" = "0" ]; then
        %userremove uuidd
        %groupremove uuidd
fi

%post	-n libmount -p /sbin/ldconfig
%postun -n libmount -p /sbin/ldconfig

%files -f util-linux.lang
%defattr(644,root,root,755)
%doc */README.* text-utils/LICENSE.pg NEWS

%attr(755,root,root) /sbin/clock
%attr(755,root,root) /sbin/hwclock*
%{_mandir}/man8/clock.8*
%{_mandir}/man8/hwclock.8*
%lang(es) %{_mandir}/es/man8/clock.8*
%lang(es) %{_mandir}/es/man8/hwclock.8*
%lang(ja) %{_mandir}/ja/man8/clock.8*
%lang(ja) %{_mandir}/ja/man8/hwclock.8*

%ghost %{_sysconfdir}/blkid.tab
%attr(755,root,root) /sbin/blkid
%attr(755,root,root) /sbin/findfs
%{_mandir}/man8/blkid.8*
%{_mandir}/man8/findfs.8*

%attr(755,root,root) %{_bindir}/linux*
%attr(755,root,root) %{_bindir}/setarch
%{_mandir}/man8/linux*
%{_mandir}/man8/setarch.8*
%ifarch s390 s390x
%attr(755,root,root) %{_bindir}/s390*
%{_mandir}/man8/s390*
%endif
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_bindir}/i386
%{_mandir}/man8/i386*
%ifarch %{x8664}
%attr(755,root,root) %{_bindir}/x86_64
%{_mandir}/man8/x86_64*
%endif
%endif
%ifarch ppc ppc64
%attr(755,root,root) %{_bindir}/ppc*
%{_mandir}/man8/ppc*
%endif
%ifarch sparc sparc64
%attr(755,root,root) %{_bindir}/sparc*
%{_mandir}/man8/sparc*
%endif
%ifarch ia64
%attr(755,root,root) %{_bindir}/i386
%attr(755,root,root) %{_bindir}/ia64
%{_mandir}/man8/i386*
%{_mandir}/man8/ia64*
%endif

%attr(755,root,root) /bin/dmesg
%attr(755,root,root) /bin/kill
%attr(755,root,root) /bin/lsblk
%attr(755,root,root) /bin/more
%attr(755,root,root) /sbin/addpart
%attr(755,root,root) /sbin/ctrlaltdel
%attr(755,root,root) /sbin/delpart
%attr(755,root,root) /sbin/fsfreeze
%attr(755,root,root) /sbin/fstrim
%attr(755,root,root) /sbin/mkfs
%attr(755,root,root) /sbin/mkswap
%attr(755,root,root) /sbin/partx
%attr(755,root,root) /sbin/swaplabel
%if "%{pld_release}" != "ac"
%attr(755,root,root) /sbin/switch_root
%endif
%attr(755,root,root) /sbin/wipefs
%attr(755,root,root) %{_bindir}/cal
%attr(755,root,root) %{_bindir}/chrt
%attr(755,root,root) %{_bindir}/col
%attr(755,root,root) %{_bindir}/colcrt
%attr(755,root,root) %{_bindir}/colrm
%attr(755,root,root) %{_bindir}/column
%attr(755,root,root) %{_bindir}/cytune
%attr(755,root,root) %{_bindir}/ddate
%attr(755,root,root) %{_bindir}/flock
%{?with_fallocate:%attr(755,root,root) %{_bindir}/fallocate}
%attr(755,root,root) %{_bindir}/getopt
%attr(755,root,root) %{_bindir}/hexdump
%attr(755,root,root) %{_bindir}/ionice
%attr(755,root,root) %{_bindir}/ipcmk
%attr(755,root,root) %{_bindir}/ipcrm
%attr(755,root,root) %{_bindir}/ipcs
%attr(755,root,root) %{_bindir}/isosize
%attr(755,root,root) %{_bindir}/line
%attr(755,root,root) %{_bindir}/logger
%attr(755,root,root) %{_bindir}/look
%attr(755,root,root) %{_bindir}/lscpu
%attr(755,root,root) %{_bindir}/mcookie
%attr(755,root,root) %{_bindir}/namei
%attr(755,root,root) %{_bindir}/pg
%attr(755,root,root) %{_bindir}/rename
%attr(755,root,root) %{_bindir}/renice
%attr(755,root,root) %{_bindir}/rev
%attr(755,root,root) %{_bindir}/script
%attr(755,root,root) %{_bindir}/scriptreplay
%attr(755,root,root) %{_bindir}/setsid
%attr(755,root,root) %{_bindir}/setterm
%attr(755,root,root) %{_bindir}/tailf
%attr(755,root,root) %{_bindir}/taskset
%attr(755,root,root) %{_bindir}/ul
%attr(755,root,root) %{_bindir}/unshare
%attr(755,root,root) %{_bindir}/whereis
%attr(2755,root,tty) %{_bindir}/write
%attr(755,root,root) %{_sbindir}/fdformat
%attr(755,root,root) %{_sbindir}/ldattach
%attr(755,root,root) %{_sbindir}/readprofile
%attr(755,root,root) %{_sbindir}/rtcwake

%{_mandir}/man1/cal.1*
%{_mandir}/man1/chrt.1*
%{_mandir}/man1/col.1*
%{_mandir}/man1/colcrt.1*
%{_mandir}/man1/colrm.1*
%{_mandir}/man1/column.1*
%{_mandir}/man1/ddate.1*
%{_mandir}/man1/dmesg.1*
%{?with_fallocate:%{_mandir}/man1/fallocate.1*}
%{_mandir}/man1/flock.1*
%{_mandir}/man1/getopt.1*
%{_mandir}/man1/hexdump.1*
%{_mandir}/man1/ionice.1*
%{_mandir}/man1/ipcrm.1*
%{_mandir}/man1/ipcmk.1*
%{_mandir}/man1/ipcs.1*
%{_mandir}/man1/kill.1*
%{_mandir}/man1/line.1*
%{_mandir}/man1/logger.1*
%{_mandir}/man1/look.1*
%{_mandir}/man1/lscpu.1*
%{_mandir}/man1/mcookie.1*
%{_mandir}/man1/more.1*
%{_mandir}/man1/namei.1*
%{_mandir}/man1/pg.1*
%{_mandir}/man1/readprofile.1*
%{_mandir}/man1/renice.1*
%{_mandir}/man1/rev.1*
%{_mandir}/man1/rename.1*
%{_mandir}/man1/setsid.1*
%{_mandir}/man1/script.1*
%{_mandir}/man1/scriptreplay.1*
%{_mandir}/man1/setterm.1*
%{_mandir}/man1/tailf.1*
%{_mandir}/man1/taskset.1*
%{_mandir}/man1/ul.1*
%{_mandir}/man1/unshare.1*
%{_mandir}/man1/whereis.1*
%{_mandir}/man1/write.1*
%{_mandir}/man8/addpart.8*
%{_mandir}/man8/ctrlaltdel.8*
%{_mandir}/man8/cytune.8*
%{_mandir}/man8/delpart.8*
%{_mandir}/man8/fdformat.8*
%{_mandir}/man8/fsfreeze.8*
%{_mandir}/man8/fstrim.8*
%{_mandir}/man8/isosize.8*
%{_mandir}/man8/ldattach.8*
%{_mandir}/man8/lsblk.8*
%{_mandir}/man8/mkswap.8*
%{_mandir}/man8/partx.8*
%{_mandir}/man8/rtcwake.8*
%{_mandir}/man8/swaplabel.8*
%if "%{pld_release}" != "ac"
%{_mandir}/man8/switch_root.8*
%endif
%{_mandir}/man8/wipefs.8*

%lang(de) %{_mandir}/de/man1/kill.1*
%lang(de) %{_mandir}/de/man1/more.1*
%lang(de) %{_mandir}/de/man1/write.1*
%lang(de) %{_mandir}/de/man8/fdformat.8*

%lang(es) %{_mandir}/es/man1/colrm.1*
%lang(es) %{_mandir}/es/man1/column.1*
%lang(es) %{_mandir}/es/man1/ddate.1*
%lang(es) %{_mandir}/es/man1/getopt.1*
%lang(es) %{_mandir}/es/man1/look.1*
%lang(es) %{_mandir}/es/man1/more.1*
%lang(es) %{_mandir}/es/man1/namei.1*
%lang(es) %{_mandir}/es/man1/readprofile.1*
%lang(es) %{_mandir}/es/man1/rev.1*
%lang(es) %{_mandir}/es/man1/script.1*
%lang(es) %{_mandir}/es/man1/setterm.1*
%lang(es) %{_mandir}/es/man1/ul.1*
%lang(es) %{_mandir}/es/man1/whereis.1*
%lang(es) %{_mandir}/es/man1/write.1*
%lang(es) %{_mandir}/es/man8/cytune.8*
%lang(es) %{_mandir}/es/man8/ctrlaltdel.8*
%lang(es) %{_mandir}/es/man8/ipcrm.8*
%lang(es) %{_mandir}/es/man8/ipcs.8*
%lang(es) %{_mandir}/es/man8/mkswap.8*
%lang(es) %{_mandir}/es/man8/renice.8*
%lang(es) %{_mandir}/es/man8/setsid.8*

%lang(fi) %{_mandir}/fi/man1/cal.1*
%lang(fi) %{_mandir}/fi/man1/column.1*
%lang(fi) %{_mandir}/fi/man1/kill.1*
%lang(fi) %{_mandir}/fi/man1/more.1*
%lang(fi) %{_mandir}/fi/man1/whereis.1*
%lang(fi) %{_mandir}/fi/man1/write.1*

%lang(fr) %{_mandir}/fr/man1/cal.1*
%lang(fr) %{_mandir}/fr/man1/col.1*
%lang(fr) %{_mandir}/fr/man1/kill.1*
%lang(fr) %{_mandir}/fr/man1/more.1*
%lang(fr) %{_mandir}/fr/man1/whereis.1*
%lang(fr) %{_mandir}/fr/man1/write.1*
%lang(fr) %{_mandir}/fr/man8/ctrlaltdel.8*
%lang(fr) %{_mandir}/fr/man8/dmesg.8*
%lang(fr) %{_mandir}/fr/man8/fdformat.8*
%lang(fr) %{_mandir}/fr/man8/ipcrm.8*
%lang(fr) %{_mandir}/fr/man8/ipcs.8*
%lang(fr) %{_mandir}/fr/man8/setsid.8*

%lang(hu) %{_mandir}/hu/man1/cal.1*
%lang(hu) %{_mandir}/hu/man1/colrm.1*
%lang(hu) %{_mandir}/hu/man1/hexdump.1*
%lang(hu) %{_mandir}/hu/man1/kill.1*
%lang(hu) %{_mandir}/hu/man1/logger.1*
%lang(hu) %{_mandir}/hu/man1/more.1*
%lang(hu) %{_mandir}/hu/man1/setterm.1*
%lang(hu) %{_mandir}/hu/man1/whereis.1*
%lang(hu) %{_mandir}/hu/man1/write.1*
%lang(hu) %{_mandir}/hu/man8/ctrlaltdel.8*
%lang(hu) %{_mandir}/hu/man8/fdformat.8*
%lang(hu) %{_mandir}/hu/man8/mkswap.8*

%lang(id) %{_mandir}/id/man1/cal.1*
%lang(id) %{_mandir}/id/man1/kill.1*
%lang(id) %{_mandir}/id/man1/logger.1*
%lang(id) %{_mandir}/id/man1/more.1*
%lang(id) %{_mandir}/id/man1/script.1*
%lang(id) %{_mandir}/id/man1/write.1*
%lang(id) %{_mandir}/id/man8/fdformat.8*

%lang(it) %{_mandir}/it/man1/kill.1*
%lang(it) %{_mandir}/it/man8/mkswap.8*
%lang(it) %{_mandir}/it/man8/setsid.8*

%lang(ja) %{_mandir}/ja/man1/cal.1*
%lang(ja) %{_mandir}/ja/man1/col.1*
%lang(ja) %{_mandir}/ja/man1/colcrt.1*
%lang(ja) %{_mandir}/ja/man1/colrm.1*
%lang(ja) %{_mandir}/ja/man1/column.1*
%lang(ja) %{_mandir}/ja/man1/ddate.1*
%lang(ja) %{_mandir}/ja/man1/getopt.1*
%lang(ja) %{_mandir}/ja/man1/hexdump.1*
%lang(ja) %{_mandir}/ja/man1/kill.1*
%lang(ja) %{_mandir}/ja/man1/line.1*
%lang(ja) %{_mandir}/ja/man1/logger.1*
%lang(ja) %{_mandir}/ja/man1/login.1*
%lang(ja) %{_mandir}/ja/man1/look.1*
%lang(ja) %{_mandir}/ja/man1/mcookie.1*
%lang(ja) %{_mandir}/ja/man1/more.1*
%lang(ja) %{_mandir}/ja/man1/namei.1*
%lang(ja) %{_mandir}/ja/man1/readprofile.1*
%lang(ja) %{_mandir}/ja/man1/rename.1*
%lang(ja) %{_mandir}/ja/man1/rev.1*
%lang(ja) %{_mandir}/ja/man1/script.1*
%lang(ja) %{_mandir}/ja/man1/setterm.1*
%lang(ja) %{_mandir}/ja/man1/ul.1*
%lang(ja) %{_mandir}/ja/man1/whereis.1*
%lang(ja) %{_mandir}/ja/man1/write.1*
%lang(ja) %{_mandir}/ja/man8/ctrlaltdel.8*
%lang(ja) %{_mandir}/ja/man8/cytune.8*
%lang(ja) %{_mandir}/ja/man8/dmesg.8*
%lang(ja) %{_mandir}/ja/man8/fdformat.8*
%lang(ja) %{_mandir}/ja/man8/ipcrm.8*
%lang(ja) %{_mandir}/ja/man8/ipcs.8*
%lang(ja) %{_mandir}/ja/man8/isosize.8*
%lang(ja) %{_mandir}/ja/man8/mkswap.8*
%lang(ja) %{_mandir}/ja/man8/renice.8*
%lang(ja) %{_mandir}/ja/man8/setsid.8*

%lang(ko) %{_mandir}/ko/man1/cal.1*
%lang(ko) %{_mandir}/ko/man1/col.1*
%lang(ko) %{_mandir}/ko/man1/colcrt.1*
%lang(ko) %{_mandir}/ko/man1/colrm.1*
%lang(ko) %{_mandir}/ko/man1/column.1*
%lang(ko) %{_mandir}/ko/man1/ddate.1*
%lang(ko) %{_mandir}/ko/man1/getopt.1*
%lang(ko) %{_mandir}/ko/man1/hexdump.1*
%lang(ko) %{_mandir}/ko/man1/kill.1*
%lang(ko) %{_mandir}/ko/man1/logger.1*
%lang(ko) %{_mandir}/ko/man1/look.1*
%lang(ko) %{_mandir}/ko/man1/mcookie.1*
%lang(ko) %{_mandir}/ko/man1/more.1*
%lang(ko) %{_mandir}/ko/man1/namei.1*
%lang(ko) %{_mandir}/ko/man1/readprofile.1*
%lang(ko) %{_mandir}/ko/man1/rev.1*
%lang(ko) %{_mandir}/ko/man1/script.1*
%lang(ko) %{_mandir}/ko/man1/setterm.1*
%lang(ko) %{_mandir}/ko/man1/ul.1*
%lang(ko) %{_mandir}/ko/man1/whereis.1*
%lang(ko) %{_mandir}/ko/man1/write.1*
%lang(ko) %{_mandir}/ko/man8/ctrlaltdel.8*
%lang(ko) %{_mandir}/ko/man8/dmesg.8*
%lang(ko) %{_mandir}/ko/man8/fdformat.8*
%lang(ko) %{_mandir}/ko/man8/ipcrm.8*
%lang(ko) %{_mandir}/ko/man8/ipcs.8*
%lang(ko) %{_mandir}/ko/man8/mkswap.8*
%lang(ko) %{_mandir}/ko/man8/renice.8*
%lang(ko) %{_mandir}/ko/man8/setsid.8*

%lang(nl) %{_mandir}/nl/man1/kill.1*

%lang(pl) %{_mandir}/pl/man1/cal.1*
%lang(pl) %{_mandir}/pl/man1/col.1*
%lang(pl) %{_mandir}/pl/man1/colcrt.1*
%lang(pl) %{_mandir}/pl/man1/colrm.1*
%lang(pl) %{_mandir}/pl/man1/getopt.1*
%lang(pl) %{_mandir}/pl/man1/hexdump.1*
%lang(pl) %{_mandir}/pl/man1/kill.1*
%lang(pl) %{_mandir}/pl/man1/look.1*
%lang(pl) %{_mandir}/pl/man1/logger.1*
%lang(pl) %{_mandir}/pl/man1/more.1*
%lang(pl) %{_mandir}/pl/man1/rev.1*
%lang(pl) %{_mandir}/pl/man1/script.1*
%lang(pl) %{_mandir}/pl/man1/setterm.1*
%lang(pl) %{_mandir}/pl/man1/ul.1*
%lang(pl) %{_mandir}/pl/man1/whereis.1*
%lang(pl) %{_mandir}/pl/man1/write.1*
%lang(pl) %{_mandir}/pl/man8/ctrlaltdel.8*
%lang(pl) %{_mandir}/pl/man8/dmesg.8*
%lang(pl) %{_mandir}/pl/man8/fdformat.8*
%lang(pl) %{_mandir}/pl/man8/ipcrm.8*
%lang(pl) %{_mandir}/pl/man8/ipcs.8*
%lang(pl) %{_mandir}/pl/man8/mkswap.8*
%lang(pl) %{_mandir}/pl/man8/renice.8*

%lang(ru) %{_mandir}/ru/man1/ddate.1*

%attr(755,root,root) /sbin/fdisk
%attr(755,root,root) /sbin/fsck.minix
%attr(755,root,root) /sbin/mkfs.minix
%ifnarch sparc sparc64
%attr(755,root,root) /sbin/cfdisk
%attr(755,root,root) /sbin/sfdisk
%endif

%{_mandir}/man8/fdisk.8*
%ifnarch sparc sparc64
%{_mandir}/man8/cfdisk.8*
%{_mandir}/man8/sfdisk.8*
%endif
%{_mandir}/man8/fsck.minix.8*
%{_mandir}/man8/mkfs.bfs.8*
%{_mandir}/man8/mkfs.minix.8*
%{_mandir}/man8/mkfs.8*

%lang(es) %{_mandir}/es/man8/fdisk.8*
%lang(es) %{_mandir}/es/man8/fsck.minix.8*
%lang(es) %{_mandir}/es/man8/mkfs.minix.8*
%lang(es) %{_mandir}/es/man8/mkfs.8*

%lang(fr) %{_mandir}/fr/man8/fdisk.8*
%ifnarch sparc sparc64
%lang(fr) %{_mandir}/fr/man8/cfdisk.8*
%lang(fr) %{_mandir}/fr/man8/sfdisk.8*
%endif
%lang(fr) %{_mandir}/fr/man8/mkfs.minix.8*
%lang(fr) %{_mandir}/fr/man8/mkfs.8*

%lang(hu) %{_mandir}/hu/man8/mkfs.8*

%lang(it) %{_mandir}/it/man8/fdisk.8*
%ifnarch sparc sparc64
%lang(it) %{_mandir}/it/man8/cfdisk.8*
%endif

%lang(ja) %{_mandir}/ja/man8/fdisk.8*
%ifnarch sparc sparc64
%lang(ja) %{_mandir}/ja/man8/cfdisk.8*
%lang(ja) %{_mandir}/ja/man8/sfdisk.8*
%endif
%lang(ja) %{_mandir}/ja/man8/fsck.minix.8*
%lang(ja) %{_mandir}/ja/man8/mkfs.bfs.8*
%lang(ja) %{_mandir}/ja/man8/mkfs.minix.8*
%lang(ja) %{_mandir}/ja/man8/mkfs.8*

%lang(ko) %{_mandir}/ko/man8/fdisk.8*
%lang(ko) %{_mandir}/ko/man8/fsck.minix.8*
%lang(ko) %{_mandir}/ko/man8/mkfs.minix.8*
%lang(ko) %{_mandir}/ko/man8/mkfs.8*

%lang(pl) %{_mandir}/pl/man8/fdisk.8*
%lang(pl) %{_mandir}/pl/man8/fsck.minix.8*
%lang(pl) %{_mandir}/pl/man8/mkfs.minix.8*
%lang(pl) %{_mandir}/pl/man8/mkfs.8*

%attr(755,root,root) /sbin/fsck.cramfs
%attr(755,root,root) /sbin/mkfs.cramfs
%attr(755,root,root) /sbin/mkfs.bfs

%ghost /var/lock/wtmpxlock

%files -n blockdev
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/blockdev
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/blockdev
%attr(755,root,root) /sbin/blockdev
%{_mandir}/man8/blockdev.8*
%lang(ja) %{_mandir}/ja/man8/blockdev.8*

%files -n mount
%defattr(644,root,root,755)
%attr(4755,root,root) /bin/mount
%attr(4755,root,root) /bin/umount
%attr(755,root,root) /sbin/pivot_root
%attr(755,root,root) /sbin/swapon
%attr(755,root,root) /sbin/swapoff

%{_mandir}/man5/fstab.5*

%{_mandir}/man8/mount.8*
%{_mandir}/man8/umount.8*
%{_mandir}/man8/pivot_root.8*
%{_mandir}/man8/swapon.8*
%{_mandir}/man8/swapoff.8*

%lang(cs) %{_mandir}/cs/man5/fstab.5*

%lang(de) %{_mandir}/de/man5/fstab.5*

%lang(es) %{_mandir}/es/man5/fstab.5*
%lang(es) %{_mandir}/es/man8/mount.8*
%lang(es) %{_mandir}/es/man8/umount.8*
%lang(es) %{_mandir}/es/man8/swapon.8*
%lang(es) %{_mandir}/es/man8/swapoff.8*

%lang(fr) %{_mandir}/fr/man5/fstab.5*
%lang(fr) %{_mandir}/fr/man8/mount.8*
%lang(fr) %{_mandir}/fr/man8/umount.8*

%lang(hu) %{_mandir}/hu/man5/fstab.5*
%lang(hu) %{_mandir}/hu/man8/mount.8*
%lang(hu) %{_mandir}/hu/man8/umount.8*

%lang(it) %{_mandir}/it/man5/fstab.5*
%lang(it) %{_mandir}/it/man8/mount.8*
%lang(it) %{_mandir}/it/man8/umount.8*
%lang(it) %{_mandir}/it/man8/swapon.8*
%lang(it) %{_mandir}/it/man8/swapoff.8*

%lang(ja) %{_mandir}/ja/man5/fstab.5*
%lang(ja) %{_mandir}/ja/man8/mount.8*
%lang(ja) %{_mandir}/ja/man8/umount.8*
%lang(ja) %{_mandir}/ja/man8/pivot_root.8*
%lang(ja) %{_mandir}/ja/man8/swapon.8*
%lang(ja) %{_mandir}/ja/man8/swapoff.8*

%lang(ko) %{_mandir}/ko/man5/fstab.5*
%lang(ko) %{_mandir}/ko/man8/mount.8*
%lang(ko) %{_mandir}/ko/man8/umount.8*
%lang(ko) %{_mandir}/ko/man8/swapon.8*
%lang(ko) %{_mandir}/ko/man8/swapoff.8*

%lang(pl) %{_mandir}/pl/man5/fstab.5*
%lang(pl) %{_mandir}/pl/man8/mount.8*
%lang(pl) %{_mandir}/pl/man8/umount.8*
%lang(pl) %{_mandir}/pl/man8/swapon.8*
%lang(pl) %{_mandir}/pl/man8/swapoff.8*

%files -n losetup
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/losetup
%{_mandir}/man8/losetup.8*
%lang(fr) %{_mandir}/fr/man8/losetup.8*
%lang(it) %{_mandir}/it/man8/losetup.8*
%lang(ja) %{_mandir}/ja/man8/losetup.8*
%lang(ko) %{_mandir}/ko/man8/losetup.8*
%lang(pl) %{_mandir}/pl/man8/losetup.8*

%files chkdupexe
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chkdupexe
%{_mandir}/man1/chkdupexe.1*
%lang(ja) %{_mandir}/ja/man1/chkdupexe.1*
%lang(ko) %{_mandir}/ko/man1/chkdupexe.1*
%lang(pl) %{_mandir}/pl/man1/chkdupexe.1*

%files -n tunelp
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tunelp
%{_mandir}/man8/tunelp.8*
%lang(es) %{_mandir}/es/man8/tunelp.8*
%lang(ja) %{_mandir}/ja/man8/tunelp.8*
%lang(pl) %{_mandir}/pl/man8/tunelp.8*

%files -n login
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/login
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.login
%attr(755,root,root) /bin/login
%{_mandir}/man1/login.1*
%lang(de) %{_mandir}/de/man1/login.1*
%lang(es) %{_mandir}/es/man1/login.1*
%lang(hu) %{_mandir}/hu/man1/login.1*
%lang(id) %{_mandir}/id/man1/login.1*
%lang(ja) %{_mandir}/ja/man1/login.1*
%lang(ko) %{_mandir}/ko/man1/login.1*
%lang(pl) %{_mandir}/pl/man1/login.1*

%files -n agetty
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/agetty
%{_mandir}/man8/agetty.8*
%lang(es) %{_mandir}/es/man8/agetty.8*
%lang(ja) %{_mandir}/ja/man8/agetty.8*

%files -n libblkid
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libblkid.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libblkid.so.1

%files -n libblkid-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblkid.so
%{_libdir}/libblkid.la
%{_includedir}/blkid
%{_pkgconfigdir}/blkid.pc
%{_mandir}/man3/libblkid.3*

%files -n libblkid-static
%defattr(644,root,root,755)
%{_libdir}/libblkid.a

%if %{with initrd} && %{with dietlibc}
%files -n libblkid-dietlibc
%defattr(644,root,root,755)
%{dietlibdir}/libblkid.a
%endif

%files -n libuuid
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uuidgen
%attr(755,root,root) /%{_lib}/libuuid.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libuuid.so.1
%{_mandir}/man1/uuidgen.1*

%files -n libuuid-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuuid.so
%{_libdir}/libuuid.la
%{_includedir}/uuid
%{_pkgconfigdir}/uuid.pc
%{_mandir}/man3/uuid*.3*

%files -n libuuid-static
%defattr(644,root,root,755)
%{_libdir}/libuuid.a

%if %{with initrd} && %{with dietlibc}
%files -n libuuid-dietlibc
%defattr(644,root,root,755)
%{dietlibdir}/libuuid.a
%endif

%files -n uuidd
%defattr(644,root,root,755)
%attr(6755,uuidd,uuidd) %{_sbindir}/uuidd
%attr(2775,uuidd,uuidd) /var/lib/libuuid
%{_mandir}/man8/uuidd.8*

%files -n libmount
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libmount.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libmount.so.1
# move to -n mount when mount starts to use libmount
%attr(755,root,root) /bin/findmnt
%{_mandir}/man8/findmnt.8*

%files -n libmount-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmount.so
%{_libdir}/libmount.la
%{_includedir}/libmount
%{_pkgconfigdir}/mount.pc

%files -n libmount-static
%defattr(644,root,root,755)
%{_libdir}/libmount.a

%if %{with initrd} && %{with dietlibc}
%files -n libmount-dietlibc
%defattr(644,root,root,755)
%{dietlibdir}/libmount.a
%endif

%files -n fsck
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/fsck
%{_mandir}/man8/fsck.8*

%if %{with initrd}
%files initrd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/initrd/*
%endif
