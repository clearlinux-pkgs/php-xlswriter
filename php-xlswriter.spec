#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-xlswriter
Version  : 1.5.2
Release  : 44
URL      : https://pecl.php.net/get/xlswriter-1.5.2.tgz
Source0  : https://pecl.php.net/get/xlswriter-1.5.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause MIT MPL-2.0
Requires: php-xlswriter-lib = %{version}-%{release}
Requires: php-xlswriter-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pkgconfig(zlib)

%description
<div align=center>
<img height="214" src="resource/logo_now.png"/>
</div>
<div align=center>
<a href="https://github.com/viest/php-ext-xlswriter/releases"><img src="https://img.shields.io/github/release/viest/php-ext-excel-export.svg"/></a>
</div>

%package lib
Summary: lib components for the php-xlswriter package.
Group: Libraries
Requires: php-xlswriter-license = %{version}-%{release}

%description lib
lib components for the php-xlswriter package.


%package license
Summary: license components for the php-xlswriter package.
Group: Default

%description license
license components for the php-xlswriter package.


%prep
%setup -q -n xlswriter-1.5.2
cd %{_builddir}/xlswriter-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-xlswriter
cp %{_builddir}/xlswriter-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-xlswriter/72d13362dec407c193d41ea7c26fd7b89d9f3451
cp %{_builddir}/xlswriter-%{version}/library/libexpat/expat/COPYING %{buildroot}/usr/share/package-licenses/php-xlswriter/1830cf88edd943aadba8ca7504d45113ca3431a2
cp %{_builddir}/xlswriter-%{version}/library/libxlsxio/LICENSE.txt %{buildroot}/usr/share/package-licenses/php-xlswriter/a42a589f60ae3155c09811bb4ed5f96dc16a5391
cp %{_builddir}/xlswriter-%{version}/library/libxlsxwriter/License.txt %{buildroot}/usr/share/package-licenses/php-xlswriter/e101f13f75dd50ddea7a13e13571ca7436e8b9e0
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/xlswriter.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-xlswriter/1830cf88edd943aadba8ca7504d45113ca3431a2
/usr/share/package-licenses/php-xlswriter/72d13362dec407c193d41ea7c26fd7b89d9f3451
/usr/share/package-licenses/php-xlswriter/a42a589f60ae3155c09811bb4ed5f96dc16a5391
/usr/share/package-licenses/php-xlswriter/e101f13f75dd50ddea7a13e13571ca7436e8b9e0
