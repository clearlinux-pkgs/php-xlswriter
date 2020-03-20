#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-xlswriter
Version  : 1.3.4
Release  : 11
URL      : https://pecl.php.net/get/xlswriter-1.3.4.tgz
Source0  : https://pecl.php.net/get/xlswriter-1.3.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: php-xlswriter-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : zlib-dev

%description
<div align=center>
<img height="214" src="resource/logo_now.png"/>
</div>
<div align=center>
<a href="https://travis-ci.org/viest/php-ext-xlswriter"><img src="https://travis-ci.org/viest/php-ext-xlswriter.svg?branch=master"/></a>
<a href="https://ci.appveyor.com/project/viest/php-ext-excel-export/branch/master"><img src="https://ci.appveyor.com/api/projects/status/w4cfjo9e4gsrs6rn/branch/master?svg=true"/></a>
<a href="https://github.com/viest/php-ext-xlswriter/releases"><img src="https://img.shields.io/github/release/viest/php-ext-excel-export.svg"/></a>
</div>

%package lib
Summary: lib components for the php-xlswriter package.
Group: Libraries

%description lib
lib components for the php-xlswriter package.


%prep
%setup -q -n xlswriter-1.3.4
cd %{_builddir}/xlswriter-1.3.4

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
/usr/lib64/extensions/no-debug-non-zts-20190902/xlswriter.so
