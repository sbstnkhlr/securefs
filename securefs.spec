
Name:           securefs
Version:        0.8.2
Release:        1%{?dist}
Summary:        securefs is an encrypted filesystem in userspace (FUSE)
License:        MIT
URL:            https://github.com/netheril96/securefs
Source0:        https://github.com/netheril96/securefs/releases/download/v%{version}/securefs_v%{version}_linux-static_amd64.tar.gz

                

%description
securefs is a filesystem in userspace (FUSE) with transparent encryption (when writing) and decryption (when reading).

%prep
%setup -c %{name}-%{version}

%install
install -D -m 0755 ./gocryptfs %{buildroot}%{_bindir}/securefs
install -D -m 0644 ./gocryptfs.1 %{buildroot}%{_mandir}/man1/securefs.1

%files
%{_bindir}/securefs
%{_mandir}/man1/*
