#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-xlswriter
Version  : 1.3.0
Release  : 3
URL      : https://pecl.php.net/get/xlswriter-1.3.0.tgz
Source0  : https://pecl.php.net/get/xlswriter-1.3.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: php-xlswriter-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
[![Build Status](https://travis-ci.org/viest/php-ext-excel-export.svg?branch=master)](https://travis-ci.org/viest/php-ext-excel-export)
[![Build status](https://ci.appveyor.com/api/projects/status/w4cfjo9e4gsrs6rn/branch/master?svg=true)](https://ci.appveyor.com/project/viest/php-ext-excel-export/branch/master)
[![](https://img.shields.io/github/release/viest/php-ext-excel-export.svg)](https://github.com/viest/php-ext-excel-export)
[![](https://img.shields.io/badge/PHP-%3E%3D%207.0-brightgreen.svg)](https://github.com/viest/php-ext-excel-export)
[![](https://img.shields.io/github/contributors/viest/php-ext-excel-export.svg)](https://github.com/viest/php-ext-excel-export)
[![](https://img.shields.io/badge/platform-macos%20%7C%20linux%20%7C%20windows-brightgreen.svg)](https://github.com/viest/php-ext-excel-export)
[![](https://img.shields.io/badge/license-BSD-green.svg)](https://github.com/viest/php-ext-excel-export)
[![](https://img.shields.io/github/issues/viest/php-ext-excel-export.svg)](https://github.com/viest/php-ext-excel-export)

%package lib
Summary: lib components for the php-xlswriter package.
Group: Libraries

%description lib
lib components for the php-xlswriter package.


%prep
%setup -q -n xlswriter-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/xlswriter.so
