# Generated by rust2rpm 12
%bcond_without check
%global __cargo_skip_build 0

%global crate cargo-c

Name:           cargo-c
Version:        0.5.1
Release:        1
Summary:        Helper program to build and install c-like libraries

License:        MIT
URL:            https://crates.io/crates/cargo-c
Source:         https://github.com/lu-zero/cargo-c/archive/v0.5.1/%{crate}-%{version}.tar.gz
# Initial patched metadata
# * Update cbindgen to 0.12, https://github.com/lu-zero/cargo-c/pull/47
#Patch0:         cargo-c-fix-metadata.diff

BuildRequires:  rust-packaging

%global _description %{expand:
Helper program to build and install c-like libraries.}

%description %{_description}

%files    
%license LICENSE
%doc README.md
%{_bindir}/cargo-cbuild
%{_bindir}/cargo-cinstall

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

#generate_buildrequires
#cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
