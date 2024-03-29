#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kross
Version  : 5.115.0
Release  : 64
URL      : https://download.kde.org/stable/frameworks/5.115/portingAids/kross-5.115.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.115/portingAids/kross-5.115.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.115/portingAids/kross-5.115.0.tar.xz.sig
Summary  : Multi-language application scripting
Group    : Development/Tools
License  : LGPL-2.1
Requires: kross-bin = %{version}-%{release}
Requires: kross-lib = %{version}-%{release}
Requires: kross-license = %{version}-%{release}
Requires: kross-locales = %{version}-%{release}
Requires: kross-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcompletion-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kparts-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Kross
Embedding of scripting into applications
## Introduction
Kross is a scripting bridge to embed scripting functionality
into an application. It supports QtScript as a scripting interpreter backend.

%package bin
Summary: bin components for the kross package.
Group: Binaries
Requires: kross-license = %{version}-%{release}

%description bin
bin components for the kross package.


%package dev
Summary: dev components for the kross package.
Group: Development
Requires: kross-lib = %{version}-%{release}
Requires: kross-bin = %{version}-%{release}
Provides: kross-devel = %{version}-%{release}
Requires: kross = %{version}-%{release}

%description dev
dev components for the kross package.


%package lib
Summary: lib components for the kross package.
Group: Libraries
Requires: kross-license = %{version}-%{release}

%description lib
lib components for the kross package.


%package license
Summary: license components for the kross package.
Group: Default

%description license
license components for the kross package.


%package locales
Summary: locales components for the kross package.
Group: Default

%description locales
locales components for the kross package.


%package man
Summary: man components for the kross package.
Group: Default

%description man
man components for the kross package.


%prep
%setup -q -n kross-5.115.0
cd %{_builddir}/kross-5.115.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707766227
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707766227
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kross
cp %{_builddir}/kross-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kross/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kross5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kf5kross
/usr/bin/kf5kross

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KrossCore/Kross/Core/Action
/usr/include/KF5/KrossCore/Kross/Core/ActionCollection
/usr/include/KF5/KrossCore/Kross/Core/ChildrenInterface
/usr/include/KF5/KrossCore/Kross/Core/ErrorInterface
/usr/include/KF5/KrossCore/Kross/Core/Interpreter
/usr/include/KF5/KrossCore/Kross/Core/KrossConfig
/usr/include/KF5/KrossCore/Kross/Core/Manager
/usr/include/KF5/KrossCore/Kross/Core/MetaFunction
/usr/include/KF5/KrossCore/Kross/Core/MetaType
/usr/include/KF5/KrossCore/Kross/Core/Object
/usr/include/KF5/KrossCore/Kross/Core/Script
/usr/include/KF5/KrossCore/Kross/Core/WrapperInterface
/usr/include/KF5/KrossCore/kross/core/action.h
/usr/include/KF5/KrossCore/kross/core/actioncollection.h
/usr/include/KF5/KrossCore/kross/core/childreninterface.h
/usr/include/KF5/KrossCore/kross/core/errorinterface.h
/usr/include/KF5/KrossCore/kross/core/interpreter.h
/usr/include/KF5/KrossCore/kross/core/krossconfig.h
/usr/include/KF5/KrossCore/kross/core/krosscore_export.h
/usr/include/KF5/KrossCore/kross/core/manager.h
/usr/include/KF5/KrossCore/kross/core/metafunction.h
/usr/include/KF5/KrossCore/kross/core/metatype.h
/usr/include/KF5/KrossCore/kross/core/object.h
/usr/include/KF5/KrossCore/kross/core/script.h
/usr/include/KF5/KrossCore/kross/core/wrapperinterface.h
/usr/include/KF5/KrossUi/Kross/Ui/ActionCollectionModel
/usr/include/KF5/KrossUi/Kross/Ui/ActionCollectionView
/usr/include/KF5/KrossUi/Kross/Ui/ScriptingPlugin
/usr/include/KF5/KrossUi/kross/ui/actioncollectionmodel.h
/usr/include/KF5/KrossUi/kross/ui/actioncollectionview.h
/usr/include/KF5/KrossUi/kross/ui/krossui_export.h
/usr/include/KF5/KrossUi/kross/ui/model.h
/usr/include/KF5/KrossUi/kross/ui/plugin.h
/usr/include/KF5/KrossUi/kross/ui/scriptingplugin.h
/usr/include/KF5/KrossUi/kross/ui/view.h
/usr/include/KF5/kross_version.h
/usr/lib64/cmake/KF5Kross/KF5KrossConfig.cmake
/usr/lib64/cmake/KF5Kross/KF5KrossConfigVersion.cmake
/usr/lib64/cmake/KF5Kross/KF5KrossTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Kross/KF5KrossTargets.cmake
/usr/lib64/libKF5KrossCore.so
/usr/lib64/libKF5KrossUi.so
/usr/lib64/qt5/mkspecs/modules/qt_KrossCore.pri
/usr/lib64/qt5/mkspecs/modules/qt_KrossUi.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5KrossCore.so.5.115.0
/V3/usr/lib64/libKF5KrossUi.so.5.115.0
/V3/usr/lib64/qt5/plugins/krossmoduleforms.so
/V3/usr/lib64/qt5/plugins/krossmodulekdetranslation.so
/V3/usr/lib64/qt5/plugins/krossqts.so
/V3/usr/lib64/qt5/plugins/script/krossqtsplugin.so
/usr/lib64/libKF5KrossCore.so.5
/usr/lib64/libKF5KrossCore.so.5.115.0
/usr/lib64/libKF5KrossUi.so.5
/usr/lib64/libKF5KrossUi.so.5.115.0
/usr/lib64/qt5/plugins/krossmoduleforms.so
/usr/lib64/qt5/plugins/krossmodulekdetranslation.so
/usr/lib64/qt5/plugins/krossqts.so
/usr/lib64/qt5/plugins/script/krossqtsplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kross/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kf5kross.1
/usr/share/man/ca@valencia/man1/kf5kross.1
/usr/share/man/de/man1/kf5kross.1
/usr/share/man/es/man1/kf5kross.1
/usr/share/man/it/man1/kf5kross.1
/usr/share/man/man1/kf5kross.1
/usr/share/man/nl/man1/kf5kross.1
/usr/share/man/pt/man1/kf5kross.1
/usr/share/man/pt_BR/man1/kf5kross.1
/usr/share/man/sv/man1/kf5kross.1
/usr/share/man/uk/man1/kf5kross.1

%files locales -f kross5.lang
%defattr(-,root,root,-)

