#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gcr
Version  : 3.20.0
Release  : 3
URL      : https://download.gnome.org/sources/gcr/3.20/gcr-3.20.0.tar.xz
Source0  : https://download.gnome.org/sources/gcr/3.20/gcr-3.20.0.tar.xz
Summary  : GObject and GUI library for high level crypto parsing and display
Group    : Development/Tools
License  : LGPL-2.0
Requires: gcr-bin
Requires: gcr-data
Requires: gcr-lib
Requires: gcr-doc
Requires: gcr-locales
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : dbus-extras
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(p11-kit-1)

%description
GCR is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides the viewer for crypto files on the GNOME
desktop.

%package bin
Summary: bin components for the gcr package.
Group: Binaries
Requires: gcr-data

%description bin
bin components for the gcr package.


%package data
Summary: data components for the gcr package.
Group: Data

%description data
data components for the gcr package.


%package dev
Summary: dev components for the gcr package.
Group: Development
Requires: gcr-lib
Requires: gcr-bin
Requires: gcr-data
Provides: gcr-devel

%description dev
dev components for the gcr package.


%package doc
Summary: doc components for the gcr package.
Group: Documentation

%description doc
doc components for the gcr package.


%package lib
Summary: lib components for the gcr package.
Group: Libraries
Requires: gcr-data

%description lib
lib components for the gcr package.


%package locales
Summary: locales components for the gcr package.
Group: Default

%description locales
locales components for the gcr package.


%prep
%setup -q -n gcr-3.20.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492699466
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1492699466
rm -rf %{buildroot}
%make_install
%find_lang gcr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gcr-viewer
/usr/libexec/gcr-prompter

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gck-1.typelib
/usr/lib64/girepository-1.0/Gcr-3.typelib
/usr/lib64/girepository-1.0/GcrUi-3.typelib
/usr/share/GConf/gsettings/org.gnome.crypto.pgp.convert
/usr/share/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
/usr/share/applications/gcr-prompter.desktop
/usr/share/applications/gcr-viewer.desktop
/usr/share/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
/usr/share/dbus-1/services/org.gnome.keyring.SystemPrompter.service
/usr/share/gcr-3/ui/gcr-pkcs11-import-dialog.ui
/usr/share/gcr-3/ui/gcr-unlock-options-widget.ui
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml
/usr/share/icons/hicolor/16x16/apps/gcr-gnupg.png
/usr/share/icons/hicolor/16x16/apps/gcr-key-pair.png
/usr/share/icons/hicolor/16x16/apps/gcr-key.png
/usr/share/icons/hicolor/16x16/apps/gcr-password.png
/usr/share/icons/hicolor/16x16/apps/gcr-smart-card.png
/usr/share/icons/hicolor/22x22/apps/gcr-gnupg.png
/usr/share/icons/hicolor/22x22/apps/gcr-key-pair.png
/usr/share/icons/hicolor/22x22/apps/gcr-key.png
/usr/share/icons/hicolor/22x22/apps/gcr-password.png
/usr/share/icons/hicolor/22x22/apps/gcr-smart-card.png
/usr/share/icons/hicolor/24x24/apps/gcr-gnupg.png
/usr/share/icons/hicolor/24x24/apps/gcr-key-pair.png
/usr/share/icons/hicolor/24x24/apps/gcr-key.png
/usr/share/icons/hicolor/24x24/apps/gcr-password.png
/usr/share/icons/hicolor/24x24/apps/gcr-smart-card.png
/usr/share/icons/hicolor/256x256/apps/gcr-gnupg.png
/usr/share/icons/hicolor/256x256/apps/gcr-password.png
/usr/share/icons/hicolor/256x256/apps/gcr-smart-card.png
/usr/share/icons/hicolor/32x32/apps/gcr-gnupg.png
/usr/share/icons/hicolor/32x32/apps/gcr-key-pair.png
/usr/share/icons/hicolor/32x32/apps/gcr-key.png
/usr/share/icons/hicolor/32x32/apps/gcr-password.png
/usr/share/icons/hicolor/32x32/apps/gcr-smart-card.png
/usr/share/icons/hicolor/48x48/apps/gcr-gnupg.png
/usr/share/icons/hicolor/48x48/apps/gcr-key-pair.png
/usr/share/icons/hicolor/48x48/apps/gcr-key.png
/usr/share/icons/hicolor/48x48/apps/gcr-password.png
/usr/share/icons/hicolor/48x48/apps/gcr-smart-card.png
/usr/share/mime/packages/gcr-crypto-types.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gck-1/gck/gck-deprecated.h
/usr/include/gck-1/gck/gck-enum-types.h
/usr/include/gck-1/gck/gck-version.h
/usr/include/gck-1/gck/gck.h
/usr/include/gck-1/gck/pkcs11.h
/usr/include/gck-1/gck/pkcs11n.h
/usr/include/gck-1/gck/pkcs11x.h
/usr/include/gcr-3/gcr/gcr-base.h
/usr/include/gcr-3/gcr/gcr-certificate-chain.h
/usr/include/gcr-3/gcr/gcr-certificate-request.h
/usr/include/gcr-3/gcr/gcr-certificate.h
/usr/include/gcr-3/gcr/gcr-collection.h
/usr/include/gcr-3/gcr/gcr-column.h
/usr/include/gcr-3/gcr/gcr-comparable.h
/usr/include/gcr-3/gcr/gcr-deprecated-base.h
/usr/include/gcr-3/gcr/gcr-enum-types-base.h
/usr/include/gcr-3/gcr/gcr-filter-collection.h
/usr/include/gcr-3/gcr/gcr-fingerprint.h
/usr/include/gcr-3/gcr/gcr-icons.h
/usr/include/gcr-3/gcr/gcr-import-interaction.h
/usr/include/gcr-3/gcr/gcr-importer.h
/usr/include/gcr-3/gcr/gcr-library.h
/usr/include/gcr-3/gcr/gcr-mock-prompter.h
/usr/include/gcr-3/gcr/gcr-parser.h
/usr/include/gcr-3/gcr/gcr-pkcs11-certificate.h
/usr/include/gcr-3/gcr/gcr-prompt.h
/usr/include/gcr-3/gcr/gcr-secret-exchange.h
/usr/include/gcr-3/gcr/gcr-secure-memory.h
/usr/include/gcr-3/gcr/gcr-simple-certificate.h
/usr/include/gcr-3/gcr/gcr-simple-collection.h
/usr/include/gcr-3/gcr/gcr-system-prompt.h
/usr/include/gcr-3/gcr/gcr-system-prompter.h
/usr/include/gcr-3/gcr/gcr-trust.h
/usr/include/gcr-3/gcr/gcr-types.h
/usr/include/gcr-3/gcr/gcr-union-collection.h
/usr/include/gcr-3/gcr/gcr-unlock-options.h
/usr/include/gcr-3/gcr/gcr-version.h
/usr/include/gcr-3/gcr/gcr.h
/usr/include/gcr-3/ui/gcr-certificate-basics-widget.h
/usr/include/gcr-3/ui/gcr-certificate-details-widget.h
/usr/include/gcr-3/ui/gcr-certificate-renderer.h
/usr/include/gcr-3/ui/gcr-certificate-widget.h
/usr/include/gcr-3/ui/gcr-collection-model.h
/usr/include/gcr-3/ui/gcr-combo-selector.h
/usr/include/gcr-3/ui/gcr-deprecated.h
/usr/include/gcr-3/ui/gcr-enum-types.h
/usr/include/gcr-3/ui/gcr-failure-renderer.h
/usr/include/gcr-3/ui/gcr-import-button.h
/usr/include/gcr-3/ui/gcr-key-renderer.h
/usr/include/gcr-3/ui/gcr-key-widget.h
/usr/include/gcr-3/ui/gcr-list-selector.h
/usr/include/gcr-3/ui/gcr-prompt-dialog.h
/usr/include/gcr-3/ui/gcr-renderer.h
/usr/include/gcr-3/ui/gcr-secure-entry-buffer.h
/usr/include/gcr-3/ui/gcr-tree-selector.h
/usr/include/gcr-3/ui/gcr-ui.h
/usr/include/gcr-3/ui/gcr-unlock-options-widget.h
/usr/include/gcr-3/ui/gcr-viewer-widget.h
/usr/include/gcr-3/ui/gcr-viewer.h
/usr/lib64/libgck-1.so
/usr/lib64/libgcr-3.so
/usr/lib64/libgcr-base-3.so
/usr/lib64/libgcr-ui-3.so
/usr/lib64/pkgconfig/gck-1.pc
/usr/lib64/pkgconfig/gcr-3.pc
/usr/lib64/pkgconfig/gcr-base-3.pc
/usr/lib64/pkgconfig/gcr-ui-3.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/gck/GckAttributes.html
/usr/share/gtk-doc/html/gck/GckEnumerator.html
/usr/share/gtk-doc/html/gck/GckModule.html
/usr/share/gtk-doc/html/gck/GckObject.html
/usr/share/gtk-doc/html/gck/GckObjectCache.html
/usr/share/gtk-doc/html/gck/GckSession.html
/usr/share/gtk-doc/html/gck/GckSlot.html
/usr/share/gtk-doc/html/gck/annotation-glossary.html
/usr/share/gtk-doc/html/gck/gck-Errors.html
/usr/share/gtk-doc/html/gck/gck-GckAttribute.html
/usr/share/gtk-doc/html/gck/gck-GckModule-lists.html
/usr/share/gtk-doc/html/gck/gck-Library-Utilities.html
/usr/share/gtk-doc/html/gck/gck-Miscellaneous-Functions.html
/usr/share/gtk-doc/html/gck/gck-PKCS11-URIs.html
/usr/share/gtk-doc/html/gck/gck.devhelp2
/usr/share/gtk-doc/html/gck/home.png
/usr/share/gtk-doc/html/gck/index.html
/usr/share/gtk-doc/html/gck/index.sgml
/usr/share/gtk-doc/html/gck/left-insensitive.png
/usr/share/gtk-doc/html/gck/left.png
/usr/share/gtk-doc/html/gck/pkcs11-links.html
/usr/share/gtk-doc/html/gck/reference.html
/usr/share/gtk-doc/html/gck/right-insensitive.png
/usr/share/gtk-doc/html/gck/right.png
/usr/share/gtk-doc/html/gck/style.css
/usr/share/gtk-doc/html/gck/up-insensitive.png
/usr/share/gtk-doc/html/gck/up.png
/usr/share/gtk-doc/html/gcr-3/GcrCertificate.html
/usr/share/gtk-doc/html/gcr-3/GcrCertificateChain.html
/usr/share/gtk-doc/html/gcr-3/GcrCertificateWidget.html
/usr/share/gtk-doc/html/gcr-3/GcrCollection.html
/usr/share/gtk-doc/html/gcr-3/GcrCollectionModel.html
/usr/share/gtk-doc/html/gcr-3/GcrComboSelector.html
/usr/share/gtk-doc/html/gcr-3/GcrComparable.html
/usr/share/gtk-doc/html/gcr-3/GcrImportButton.html
/usr/share/gtk-doc/html/gcr-3/GcrImporter.html
/usr/share/gtk-doc/html/gcr-3/GcrKeyWidget.html
/usr/share/gtk-doc/html/gcr-3/GcrListSelector.html
/usr/share/gtk-doc/html/gcr-3/GcrParser.html
/usr/share/gtk-doc/html/gcr-3/GcrPkcs11Certificate.html
/usr/share/gtk-doc/html/gcr-3/GcrPrompt.html
/usr/share/gtk-doc/html/gcr-3/GcrPromptDialog.html
/usr/share/gtk-doc/html/gcr-3/GcrRenderer.html
/usr/share/gtk-doc/html/gcr-3/GcrSecretExchange.html
/usr/share/gtk-doc/html/gcr-3/GcrSecureEntryBuffer.html
/usr/share/gtk-doc/html/gcr-3/GcrSimpleCertificate.html
/usr/share/gtk-doc/html/gcr-3/GcrSimpleCollection.html
/usr/share/gtk-doc/html/gcr-3/GcrSystemPrompt.html
/usr/share/gtk-doc/html/gcr-3/GcrSystemPrompter.html
/usr/share/gtk-doc/html/gcr-3/GcrTreeSelector.html
/usr/share/gtk-doc/html/gcr-3/GcrViewer.html
/usr/share/gtk-doc/html/gcr-3/GcrViewerWidget.html
/usr/share/gtk-doc/html/gcr-3/annotation-glossary.html
/usr/share/gtk-doc/html/gcr-3/certificate-widget.png
/usr/share/gtk-doc/html/gcr-3/certificates.html
/usr/share/gtk-doc/html/gcr-3/ch01.html
/usr/share/gtk-doc/html/gcr-3/collections.html
/usr/share/gtk-doc/html/gcr-3/combo-selector.png
/usr/share/gtk-doc/html/gcr-3/gcr-3.devhelp2
/usr/share/gtk-doc/html/gcr-3/gcr-GcrCertificateRequest.html
/usr/share/gtk-doc/html/gcr-3/gcr-GcrColumn.html
/usr/share/gtk-doc/html/gcr-3/gcr-GcrImportInteraction.html
/usr/share/gtk-doc/html/gcr-3/gcr-Key-Fingerprints.html
/usr/share/gtk-doc/html/gcr-3/gcr-Library-PKCS#11.html
/usr/share/gtk-doc/html/gcr-3/gcr-Library-Utilities.html
/usr/share/gtk-doc/html/gcr-3/gcr-Non-pageable-Memory.html
/usr/share/gtk-doc/html/gcr-3/gcr-Trust-Storage-and-Lookups.html
/usr/share/gtk-doc/html/gcr-3/home.png
/usr/share/gtk-doc/html/gcr-3/import-button.png
/usr/share/gtk-doc/html/gcr-3/index.html
/usr/share/gtk-doc/html/gcr-3/index.sgml
/usr/share/gtk-doc/html/gcr-3/key-widget.png
/usr/share/gtk-doc/html/gcr-3/left-insensitive.png
/usr/share/gtk-doc/html/gcr-3/left.png
/usr/share/gtk-doc/html/gcr-3/list-selector.png
/usr/share/gtk-doc/html/gcr-3/misc.html
/usr/share/gtk-doc/html/gcr-3/prompts.html
/usr/share/gtk-doc/html/gcr-3/right-insensitive.png
/usr/share/gtk-doc/html/gcr-3/right.png
/usr/share/gtk-doc/html/gcr-3/storage.html
/usr/share/gtk-doc/html/gcr-3/style.css
/usr/share/gtk-doc/html/gcr-3/tree-selector.png
/usr/share/gtk-doc/html/gcr-3/up-insensitive.png
/usr/share/gtk-doc/html/gcr-3/up.png
/usr/share/gtk-doc/html/gcr-3/viewer-widget.png
/usr/share/gtk-doc/html/gcr-3/widgets.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgck-1.so.0
/usr/lib64/libgck-1.so.0.0.0
/usr/lib64/libgcr-3.so.1
/usr/lib64/libgcr-3.so.1.0.0
/usr/lib64/libgcr-base-3.so.1
/usr/lib64/libgcr-base-3.so.1.0.0
/usr/lib64/libgcr-ui-3.so.1
/usr/lib64/libgcr-ui-3.so.1.0.0

%files locales -f gcr.lang
%defattr(-,root,root,-)

