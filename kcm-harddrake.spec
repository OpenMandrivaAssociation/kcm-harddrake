Name:           kcm-harddrake
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching harddrake
Version:        1.0
Release:        6
BuildArch:      noarch
Source0:        kcm_harddrake.desktop

%description
Harddrake launcher for KDE Control Center

%prep

%build

%install
mkdir -p %{buildroot}%{_kde_services}
cp -f %{SOURCE0} %{buildroot}%{_kde_services}/

%files
%defattr(-,root,root)
%doc
%{_kde_services}/kcm_harddrake.desktop

