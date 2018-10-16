#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kross
Version  : 5.51.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.51/portingAids/kross-5.51.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.51/portingAids/kross-5.51.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.51/portingAids/kross-5.51.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kross-bin = %{version}-%{release}
Requires: kross-lib = %{version}-%{release}
Requires: kross-license = %{version}-%{release}
Requires: kross-locales = %{version}-%{release}
Requires: kross-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

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
Requires: kross-man = %{version}-%{release}

%description bin
bin components for the kross package.


%package dev
Summary: dev components for the kross package.
Group: Development
Requires: kross-lib = %{version}-%{release}
Requires: kross-bin = %{version}-%{release}
Provides: kross-devel = %{version}-%{release}

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
%setup -q -n kross-5.51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539701774
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539701774
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kross
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kross/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kross5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/lib64/libKF5KrossCore.so.5
/usr/lib64/libKF5KrossCore.so.5.51.0
/usr/lib64/libKF5KrossUi.so.5
/usr/lib64/libKF5KrossUi.so.5.51.0
/usr/lib64/qt5/plugins/krossmoduleforms.so
/usr/lib64/qt5/plugins/krossmodulekdetranslation.so
/usr/lib64/qt5/plugins/krossqts.so
/usr/lib64/qt5/plugins/script/krossqtsplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kross/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kf5kross.1
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

