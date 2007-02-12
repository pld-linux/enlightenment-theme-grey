%define	_theme	grey
Summary:	A dark, light on resources, modified default E17 theme using grey-ish colors
Summary(pl.UTF-8):   Ciemny, ale z jasnymi zasobami, zmodyfikowany domyślny motyw E17 z szarawymi kolorami
Name:		enlightenment-theme-%{_theme}
Version:	2006.07.19	
Release:	1
License:	BSD
Group:		Themes
Source0:	http://www.get-e.org/Themes/E17/_files/%{_theme}.edj
# Source0-md5:	7a17042695d598eacdc2c4caeb1746cc
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenment >= 0.16.999
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A dark, light on resources, modified default E17 theme using grey-ish
colors.

%description -l pl.UTF-8
Ciemny, ale z jasnymi zasobami, zmodyfikowany domyślny motyw E17 z
szarawymi kolorami.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/data/themes/%{_theme}.edj
