%define		oname	7kaa

Name:		%{oname}-music
Version:	2.13
Release:	4
Summary:	Game music files for Seven Kingdoms: Ancient Adversaries
Group:		Games/Strategy
License:	Freeware
URL:		http://7kfans.com/
Source0:	http://www.7kfans.com/downloads/%{name}.tar.bz2
Suggests:	%{oname} >= %{version}
BuildArch:	noarch

%description
Game music files used by Seven Kingdoms: Ancient Adversaries game.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{oname}/music
cp -r music/* %{buildroot}%{_datadir}/%{oname}/music/

%files
%doc COPYING-Music.txt README-Music.txt
%{_datadir}/%{oname}/music



%changelog
* Fri Mar 23 2012 Andrey Bondrov <abondrov@mandriva.org> 2.13-2
+ Revision: 786272
- imported package 7kaa-music

