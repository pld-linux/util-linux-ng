# TODO:
# - if it obsoletes setarch, compat symlinks and P/O list should be merged
#
# Conditional build:
%bcond_with	uClibc	# don't build few utilities
%bcond_without	selinux # build without SELinux support
#
%define	snap	rc2
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
Version:	2.13
Release:	1.%{snap}.1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v%{version}/%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	284e98596a9b2be663d82dc6c7dab309
# Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Source1:	util-linux-non-english-man-pages.tar.bz2
# Source1-md5:	81bbcc9a820512ecde87a8f31de0b745
Source2:	login.pamd
Source3:	util-linux-blockdev.init
Source4:	util-linux-blockdev.sysconfig
URL:		http://userweb.kernel.org/~kzak/util-linux-ng/
BuildRequires:	audit-libs-devel >= 1.0.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cryptsetup-luks-devel
BuildRequires:	e2fsprogs-devel >= 1.36
BuildRequires:	gettext-devel
BuildRequires:	intltool
%{?with_selinux:BuildRequires:	libselinux-devel}
%{!?with_uClibc:BuildRequires:	ncurses-devel >= 5.0}
%{!?with_uClibc:BuildRequires:	pam-devel >= 0.99.7.1}
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
%{!?with_uClibc:BuildRequires:	zlib-devel}
%{!?with_uClibc:Requires:	pam >= 0.99.7.1}
Provides:	fdisk
Provides:	util-linux = %{version}-%{release}
Obsoletes:	cramfs
Obsoletes:	rawdevices
Obsoletes:	schedutils
Obsoletes:	setarch
Obsoletes:	util-linux
Obsoletes:	util-linux-suids
Conflicts:	shadow-extras < 1:4.0.3-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debugcflags	-O1 -g

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
programas de sistema como login.

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
programas de sistema como login.

%description -l ru.UTF-8
Этот пакет содержит большой набор системных утилит низкого уровня,
которые необходимы для функционирования системы Linux. Он включает, в
числе прочих, инструменты конфигурации, такие как fdisk, и системные
программы, такие как login.

%description -l tr.UTF-8
şlevsel durumdaki bir Linux sistemi için gerekli birçok alt düzey
sistem araçlarını içerir. Bunlar arasında fdisk gibi yapılandırma
uygulamaları ve logger gibi sistem programları sayılabilir.

%description -l uk.UTF-8
Цей пакет містить великий набір системних утиліт низького рівня, які
необхідні для функціонування системи Linux. Він містить, окрім інших,
конфігураційні інструменти (такі як fdisk) та системні програми (такі
як login).

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
Requires:	cryptsetup-luks >= 1.0.4
Requires:	libgcrypt >= 1.2.0-6
Requires:	libgpg-error >= 1.0-4

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
Requires:	pam >= 0.99.7.1
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

%prep
%setup -q -a1 -n %{name}-%{version}-%{snap}

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--with%{?with_uClibc:out}-pam \
	--with%{!?with_selinux:out}-selinux \
	--disable-use-tty-group \
	--disable-wall \
	--enable-kill \
	--enable-login-chown-vcs \
	--enable-login-utils \
	--enable-partx \
	--enable-rdev \
	--enable-write \
	--with-audit \
	--with-fsprobe=blkid

%{__make}

%ifarch ppc
%{__cc} %{rpmcflags} %{rpmldflags} clock-ppc.c -o clock-ppc
%endif

cd sys-utils
makeinfo ipc.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,sysconfig,security} \
	$RPM_BUILD_ROOT/var/lock

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install misc-utils/scriptreplay.1 $RPM_BUILD_ROOT%{_mandir}/man1/

sed -i -e 's,/usr/spool/mail,/var/mail,g' $RPM_BUILD_ROOT%{_mandir}/man1/login.1

mv $RPM_BUILD_ROOT%{_sbindir}/{addpart,delpart,partx} $RPM_BUILD_ROOT/sbin

install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/login
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/blockdev
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/blockdev

:> $RPM_BUILD_ROOT/etc/security/blacklist.login
:> $RPM_BUILD_ROOT/var/lock/wtmpxlock

%ifarch ppc
mv -f $RPM_BUILD_ROOT/sbin/hwclock $RPM_BUILD_ROOT/sbin/hwclock.rtc
install clock-ppc $RPM_BUILD_ROOT/sbin/hwclock.adb
#yneed fix:
# hwclock.adb is for PowerMac (default)
# hwclock.rtc is for RS/6000 (PreP,CHRP)
ln -sf hwclock.adb $RPM_BUILD_ROOT/sbin/hwclock
%endif

ln -sf hwclock $RPM_BUILD_ROOT/sbin/clock
echo '.so hwclock.8' > $RPM_BUILD_ROOT%{_mandir}/man8/clock.8

for d in cs de es fi fr hu id it ja ko nl pl ; do
	for m in man1 man5 man8 ; do
		if [ -d man/$d/$m ]; then
			install -d $RPM_BUILD_ROOT%{_mandir}/$d/$m
			install man/$d/$m/* $RPM_BUILD_ROOT%{_mandir}/$d/$m
		fi
	done
done

# cleanup, remove files not included in package
rm $RPM_BUILD_ROOT%{_bindir}/{chfn,chsh,newgrp} \
	$RPM_BUILD_ROOT%{_sbindir}/{vigr,vipw} \
	$RPM_BUILD_ROOT%{_mandir}/man1/{chfn,chsh,newgrp}.1 \
	$RPM_BUILD_ROOT%{_mandir}/man8/{vigr,vipw}.8 \
	$RPM_BUILD_ROOT%{_mandir}/*/man1/{arch,chfn,chsh,clear,last,mesg,newgrp,od,passwd,reset,sg,wall}.1 \
	$RPM_BUILD_ROOT%{_mandir}/*/man5/nfs.5 \
	$RPM_BUILD_ROOT%{_mandir}/*/man8/{display-services,elvtune,fast*,halt,initctl,need,provide,reboot,setfdprm,shutdown,simpleinit,sln,vigr,vipw}.8

%ifnarch %{ix86}
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man8/{ramsize,rdev,rootflags,vidmode}.8
%endif
%ifarch sparc sparc64
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man8/{cfdisk,sfdisk}.8
%endif

%{!?with_uClibc:%find_lang %{name}}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n blockdev
/sbin/chkconfig --add blockdev
%service blockdev restart

%preun -n blockdev
if [ "$1" = "0" ]; then
	%service blockdev stop
	/sbin/chkconfig --del blockdev
fi

%files %{!?with_uClibc:-f %{name}.lang}
%defattr(644,root,root,755)
%doc */README.* text-utils/LICENSE.pg NEWS

%attr(755,root,root) /sbin/clock
%ifarch ppc
%attr(755,root,root) %config(noreplace) %verify(not link) /sbin/hwclock
%attr(755,root,root) /sbin/hwclock.adb
%attr(755,root,root) /sbin/hwclock.rtc
%else
%attr(755,root,root) /sbin/hwclock*
%endif

%{_mandir}/man8/clock.8*
%{_mandir}/man8/hwclock.8*
%lang(es) %{_mandir}/es/man8/clock.8*
%lang(es) %{_mandir}/es/man8/hwclock.8*
%lang(ja) %{_mandir}/ja/man8/clock.8*
%lang(ja) %{_mandir}/ja/man8/hwclock.8*

%attr(755,root,root) /bin/dmesg
%attr(755,root,root) /bin/kill
%{!?with_uClibc:%attr(755,root,root) /bin/more}
%attr(755,root,root) /sbin/mkfs
%attr(755,root,root) /sbin/mkswap
%attr(755,root,root) /sbin/ctrlaltdel
%attr(755,root,root) /sbin/addpart
%attr(755,root,root) /sbin/delpart
%attr(755,root,root) /sbin/partx
%attr(755,root,root) %{_bindir}/cal
%attr(755,root,root) %{_bindir}/chrt
%attr(755,root,root) %{_bindir}/col
%attr(755,root,root) %{_bindir}/colcrt
%attr(755,root,root) %{_bindir}/colrm
%attr(755,root,root) %{_bindir}/column
%attr(755,root,root) %{_bindir}/ddate
%attr(755,root,root) %{_bindir}/fdformat
%attr(755,root,root) %{_bindir}/flock
%attr(755,root,root) %{_bindir}/getopt
%attr(755,root,root) %{_bindir}/hexdump
%attr(755,root,root) %{_bindir}/ionice
%attr(755,root,root) %{_bindir}/ipcrm
%attr(755,root,root) %{_bindir}/ipcs
%attr(755,root,root) %{_bindir}/isosize
%attr(755,root,root) %{_bindir}/line
%attr(755,root,root) %{_bindir}/logger
%attr(755,root,root) %{_bindir}/look
%attr(755,root,root) %{_bindir}/mcookie
%attr(755,root,root) %{_bindir}/namei
%{!?with_uClibc:%attr(755,root,root) %{_bindir}/pg}
%attr(755,root,root) %{_bindir}/rename
%attr(755,root,root) %{_bindir}/renice
%attr(755,root,root) %{_bindir}/rev
%attr(755,root,root) %{_bindir}/script
%attr(755,root,root) %{_bindir}/scriptreplay
%attr(755,root,root) %{_bindir}/setarch
%attr(755,root,root) %{_bindir}/setsid
%{!?with_uClibc:%attr(755,root,root) %{_bindir}/setterm}
%attr(755,root,root) %{_bindir}/tailf
%attr(755,root,root) %{_bindir}/taskset
%{!?with_uClibc:%attr(755,root,root) %{_bindir}/ul}
%attr(755,root,root) %{_bindir}/whereis
%attr(2755,root,tty) %{_bindir}/write
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
%{_mandir}/man1/flock.1*
%{_mandir}/man1/getopt.1*
%{_mandir}/man1/hexdump.1*
%{_mandir}/man1/ionice.1*
%{_mandir}/man1/ipcrm.1*
%{_mandir}/man1/ipcs.1*
%{_mandir}/man1/kill.1*
%{_mandir}/man1/line.1*
%{_mandir}/man1/logger.1*
%{_mandir}/man1/look.1*
%{_mandir}/man1/mcookie.1*
%{!?with_uClibc:%{_mandir}/man1/more.1*}
%{_mandir}/man1/namei.1*
%{!?with_uClibc:%{_mandir}/man1/pg.1*}
%{_mandir}/man1/readprofile.1*
%{_mandir}/man1/renice.1*
%{_mandir}/man1/rev.1*
%{_mandir}/man1/rename.1*
%{_mandir}/man1/setsid.1*
%{_mandir}/man1/script.1*
%{_mandir}/man1/scriptreplay.1*
%{!?with_uClibc:%{_mandir}/man1/setterm.1*}
%{_mandir}/man1/tailf.1*
%{_mandir}/man1/taskset.1*
%{!?with_uClibc:%{_mandir}/man1/ul.1*}
%{_mandir}/man1/whereis.1*
%{_mandir}/man1/write.1*

%{_mandir}/man8/addpart.8*
%{_mandir}/man8/ctrlaltdel.8*
%{_mandir}/man8/cytune.8*
%{_mandir}/man8/delpart.8*
%{_mandir}/man8/fdformat.8*
%{_mandir}/man8/isosize.8*
%{_mandir}/man8/mkswap.8*
%{_mandir}/man8/partx.8*
%{_mandir}/man8/rtcwake.8*
%{_mandir}/man8/setarch.8*

%lang(cs) %{_mandir}/cs/man1/write.1*

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
%lang(fr) %{_mandir}/fr/man1/rev.1*
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

%lang(it) %{_mandir}/it/man1/cal.1*
%lang(it) %{_mandir}/it/man1/kill.1*
%lang(it) %{_mandir}/it/man1/rename.1*
%lang(it) %{_mandir}/it/man1/rev.1*

%lang(it) %{_mandir}/it/man8/ctrlaltdel.8*
%lang(it) %{_mandir}/it/man8/dmesg.8*
%lang(it) %{_mandir}/it/man8/fdformat.8*
%lang(it) %{_mandir}/it/man8/ipcrm.8*
%lang(it) %{_mandir}/it/man8/ipcs.8*
%lang(it) %{_mandir}/it/man8/mkfs.8*
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
%lang(ja) %{_mandir}/ja/man1/look.1*
%lang(ja) %{_mandir}/ja/man1/mcookie.1*
%lang(ja) %{_mandir}/ja/man1/more.1*
%lang(ja) %{_mandir}/ja/man1/namei.1*
%lang(ja) %{_mandir}/ja/man1/readprofile.1*
%lang(ja) %{_mandir}/ja/man1/rename.1*
%lang(ja) %{_mandir}/ja/man1/replay.1*
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

%attr(755,root,root) /sbin/fdisk
%attr(755,root,root) /sbin/fsck.minix
%attr(755,root,root) /sbin/mkfs.minix
%ifnarch sparc sparc64
%{!?with_uClibc:%attr(755,root,root) /sbin/cfdisk}
%attr(755,root,root) /sbin/sfdisk
%endif

%{_mandir}/man8/fdisk.8*
%ifnarch sparc sparc64
%{!?with_uClibc:%{_mandir}/man8/cfdisk.8*}
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
%{!?with_uClibc:%lang(fr) %{_mandir}/fr/man8/cfdisk.8*}
%lang(fr) %{_mandir}/fr/man8/sfdisk.8*
%endif
%lang(fr) %{_mandir}/fr/man8/mkfs.minix.8*
%lang(fr) %{_mandir}/fr/man8/mkfs.8*

%lang(hu) %{_mandir}/hu/man8/mkfs.8*

%lang(it) %{_mandir}/it/man8/fdisk.8*
%ifnarch sparc sparc64
%{!?with_uClibc:%lang(it) %{_mandir}/it/man8/cfdisk.8*}
%endif

%lang(ja) %{_mandir}/ja/man8/fdisk.8*
%ifnarch sparc sparc64
%{!?with_uClibc:%lang(ja) %{_mandir}/ja/man8/cfdisk.8*}
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

%{!?with_uClibc:%attr(755,root,root) /sbin/fsck.cramfs}
%{!?with_uClibc:%attr(755,root,root) /sbin/mkfs.cramfs}
%attr(755,root,root) /sbin/mkfs.bfs

%attr(755,root,root) %{_bindir}/cytune

%ifarch %{ix86}
%attr(755,root,root) %{_sbindir}/ramsize
%attr(755,root,root) %{_sbindir}/rdev
%attr(755,root,root) %{_sbindir}/rootflags
%attr(755,root,root) %{_sbindir}/vidmode

%{_mandir}/man8/ramsize.8*
%{_mandir}/man8/rdev.8*
%{_mandir}/man8/rootflags.8*
%{_mandir}/man8/vidmode.8*

%lang(de) %{_mandir}/de/man8/ramsize.8*
%lang(de) %{_mandir}/de/man8/rdev.8*
%lang(de) %{_mandir}/de/man8/rootflags.8*
%lang(de) %{_mandir}/de/man8/vidmode.8*

%lang(es) %{_mandir}/es/man8/ramsize.8*
%lang(es) %{_mandir}/es/man8/rdev.8*
%lang(es) %{_mandir}/es/man8/rootflags.8*
%lang(es) %{_mandir}/es/man8/vidmode.8*

%lang(ja) %{_mandir}/ja/man8/ramsize.8*
%lang(ja) %{_mandir}/ja/man8/rdev.8*
%lang(ja) %{_mandir}/ja/man8/rootflags.8*
%lang(ja) %{_mandir}/ja/man8/vidmode.8*

%lang(ko) %{_mandir}/ko/man8/ramsize.8*
%lang(ko) %{_mandir}/ko/man8/rdev.8*
%lang(ko) %{_mandir}/ko/man8/rootflags.8*
%lang(ko) %{_mandir}/ko/man8/vidmode.8*

%lang(pl) %{_mandir}/pl/man8/ramsize.8*
%lang(pl) %{_mandir}/pl/man8/rdev.8*
%lang(pl) %{_mandir}/pl/man8/rootflags.8*
%lang(pl) %{_mandir}/pl/man8/vidmode.8*
%endif

%{_infodir}/ipc*

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

%if !%{with uClibc}
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
%lang(it) %{_mandir}/it/man1/login.1*
%lang(ja) %{_mandir}/ja/man1/login.1*
%lang(ko) %{_mandir}/ko/man1/login.1*
%lang(pl) %{_mandir}/pl/man1/login.1*
%endif

%files -n agetty
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/agetty

%{_mandir}/man8/agetty.8*
%lang(es) %{_mandir}/es/man8/agetty.8*
%lang(ja) %{_mandir}/ja/man8/agetty.8*
