Name: xmkgif
Version: 0.2.1
Release: 1%{?dist}
Summary: screen capture tool

License: MIT
URL: https://github.com/vmindru/xrectangle
Source0: https://github.com/vmindru/xrectangle/archive/%{version}.tar.gz

BuildRequires: libX11-devel
Requires: zenity,byzanz

%description
Wrapper for byzanz, allowes to capture full screen or screen area.
When executed within a X session user is presented simple GUI dialogue.


%prep
%autosetup -n xmkgif-%{version}


%build
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
cp -a xmkgif %{buildroot}%{_bindir}
cp -a xmkgif-stop %{buildroot}%{_bindir}
cp -a xrectangle %{buildroot}%{_bindir}


%files
%{_bindir}/*
%doc


%changelog
* Sun Mar 3 2019 Veaceslav Mindru <mindruv@gmail.com> - 0.2.1
  - add xmkgif-stop
* Wed Apr 13 2016 Veaceslav Mindru <vmindru@redhat.com> - 0.1
  - Add gui dialogues
