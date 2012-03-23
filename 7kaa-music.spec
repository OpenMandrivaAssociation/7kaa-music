%define		oname	7kaa

Name:		%{oname}-music
Version:	2.13
Release:	%mkrel 1
Summary:	Game music files for Seven Kingdoms: Ancient Adversaries
Group:		Games/Strategy
License:	Freeware
URL:		http://7kfans.com/
Source0:	http://www.7kfans.com/downloads/%{name}.tar.bz2
Suggests:	%{name} >= %{version}
BuildArch:	noarch

%description
Game music files used by Seven Kingdoms: Ancient Adversaries game.

%prep
%setup -q -n %{name}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/%{oname}/music
%__cp -r music/* %{buildroot}%{_datadir}/%{oname}/music/

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING-Music.txt README-Music.txt
%{_datadir}/%{oname}/music

