
Name:           securefs
Version:        0.8.2
Release:        1%{?dist}
Summary:        securefs is an encrypted filesystem in userspace (FUSE)
License:        MIT
URL:            https://github.com/netheril96/securefs
Source0:        https://github.com/netheril96/securefs/archive/0.8.2.tar.gz

          

%description
securefs is a filesystem in userspace (FUSE) with transparent encryption (when writing) and decryption (when reading).

%prep
%setup -c %{name}-%{version}

%install
install -D -m 0755 ./securefs %{buildroot}%{_bindir}/securefs
install -D -m 0644 ./securefs.1 %{buildroot}%{_mandir}/man1/securefs.1

%files
%{_bindir}/securefs
%{_mandir}/man1/*
