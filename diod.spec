Name:
Version:
Release:

Summary:  I/O forwarding server for 9P.
License: GPL
Group: Applications/System
# URL: http://sourceforge.net/projects/npfs
Source0: %{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# tcp_wrappers-devel on rhel6
BuildRequires: tcp_wrappers
BuildRequires: zlib-devel
BuildRequires: lua

%description
diod is a 9P2000.h server used in combination with the kernel v9fs file
system for I/O forwarding on Linux clusters.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf ${RPM_BUILD_ROOT}

# %post
# if [ -x /sbin/chkconfig ]; then /sbin/chkconfig --add diod; fi

# %preun
# if [ "$1" = 0 ]; then
#   %{_sysconfdir}/init.d/diod stop >/dev/null 2>&1 || :
#   if [ -x /sbin/chkconfig ]; then /sbin/chkconfig --del diod; fi
# fi

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README INSTALL ChangeLog
%{_sbindir}/*
%{_mandir}/man8/*
%attr(0755,root,root) %{_sysconfdir}/init.d/diod