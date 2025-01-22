%undefine _debugsource_packages

Name:		traefik-certs-dumper
Version:	2.9.3
Release:	1
Source0:	https://github.com/ldez/traefik-certs-dumper/archive/refs/tags/v%{version}.tar.gz
Source1:	vendor.tar.xz
Summary:	Tool to dump ACME data from Traefik to certificates
URL:		https://github.com/ldez/traefik-certs-dumper
License:	Apache-2.0
Group:		Servers

%description
Tool to dump ACME data from Traefik to certificates

%prep
%autosetup -p1 -a1

%conf

%build
go build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 traefik-certs-dumper %{buildroot}%{_bindir}/

%files
%{_bindir}/traefik-certs-dumper
