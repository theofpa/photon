Summary:        Google's data interchange format - C implementation
Name:           protobuf-c
Version:        1.2.1
Release:        1%{?dist}
License:        BSD-3-Clause
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://github.com/google/protobuf-c/
Source0:        %{name}-%{version}.tar.gz
%define         sha1 protobuf-c=3ecd015299d5a8ab8304bf5eeea2fd0f75c1f6bb
BuildRequires:  protobuf >= 2.6.0
BuildRequires:  protobuf-devel >= 2.6.0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libstdc++
BuildRequires:  curl
BuildRequires:  make
BuildRequires:  unzip
Requires:       protobuf

%description
Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data. You can find protobuf's documentation on the Google Developers site. This is the C implementation.

%package        devel
Summary:        Development files for protobuf
Group:          Development/Libraries
Requires:       protobuf-c = %{version}-%{release}

%description    devel
The protobuf-c-devel package contains libraries and header files for
developing applications that use protobuf-c.

%package        static
Summary:        protobuf-c static lib
Group:          Development/Libraries
Requires:       protobuf = %{version}-%{release}

%description    static
The protobuf-c-static package contains static protobuf-c libraries.

%prep
%setup
autoreconf -iv

%build
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/protoc-c
%{_libdir}/libprotobuf-c.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libprotobuf-c.la
%{_libdir}/libprotobuf-c.so

%files static
%defattr(-,root,root)
%{_libdir}/libprotobuf-c.a

%changelog
*   Sat Mar 18 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.2.1-1
-   Initial packaging for Photon
