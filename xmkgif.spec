Name: xmkgif
Version: 0.1	
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
%autosetup -n xrectangle-%{version}


%build
make %{?_smp_mflags}


%install
%make_install
install -m 755 -d %{buildroot}/%{_sbindir}
ln -s ../bin/%{name} %{buildroot}/%{_sbindir}

%files
%doc



%changelog
* Wed Apr 13 2016 Veaceslav Mindru <vmindru@redhat.com> - 0.1
  - Add gui dialogues 
