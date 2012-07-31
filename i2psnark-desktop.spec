Name:		i2psnark-desktop
Version:	0.2
Release:	1%{?dist}
Summary:	Desktop files for i2psnark

Group:		Applications/Internet
# License for this desktop package
License:	GPL
URL:		http://www.i2p2.de
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	desktop-file-utils
Requires:	i2p zenity
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

BuildArch: 	noarch

%description
Desktop files for the I2P BitTorrent client i2psnark.


%prep
%setup -q


%build


%install
make install PREFIX=%{buildroot}


%post
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%doc
%{_datadir}/applications/i2psnark.desktop
%{_bindir}/i2psnark-add

%changelog

