%define debug_package %{nil}
Name:       wlandrv-plugin-tizen-ap6335
Summary:    Firmware & tools for ap6335
Version: 1.0.0
Release:    0
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz

%description
firmware & tools for ap6335

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/lib/firmware
mkdir -p %{buildroot}/usr/bin

cp -af wlandrv-plugin-ap6335/* %{buildroot}/

find wlandrv-plugin-ap6335/lib/firmware/brcm/*  -exec basename {} \; | sed 's/^/\/lib\/firmware\/brcm\//g' >bcm.files
find wlandrv-plugin-ap6335/usr/bin/*  -exec basename {} \; | sed 's/^/\/usr\/bin\//g' >>bcm.files

%files -f bcm.files
%defattr(-, root, root, -)
