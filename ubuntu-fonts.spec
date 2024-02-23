Name: ubuntu-fonts
Version: 0.83
Release: 1%{?dist}
Summary: The Ubuntu Font Family

License: LicenseRef-Ubuntu-Font-Licence-Version-1.0
URL: https://font.ubuntu.com/
Source: https://assets.ubuntu.com/v1/0cef8205-ubuntu-font-family-0.83.zip

BuildArch: noarch

%description
The Ubuntu Font Family are a set of matching new libre/open fonts in
development during 2010--2011.
And with further expansion work and bug fixing during 2015.
The development is being funded by Canonical Ltd on behalf the wider
Free Software community and the Ubuntu project.
The technical font design work and implementation is being undertaken
by Dalton Maag.

%prep
%setup -qn ubuntu-font-family-0.83

%build

%install
mkdir -p -- %{buildroot}/%{_datadir}/fonts/%{name}
install -m 644 Ubuntu-Th.ttf \
               Ubuntu-L.ttf \
               Ubuntu-R.ttf \
               Ubuntu-M.ttf \
               Ubuntu-B.ttf \
               Ubuntu-LI.ttf \
               Ubuntu-RI.ttf \
               Ubuntu-MI.ttf \
               Ubuntu-BI.ttf \
               UbuntuMono-R.ttf \
               UbuntuMono-B.ttf \
               UbuntuMono-RI.ttf \
               UbuntuMono-BI.ttf \
               Ubuntu-C.ttf \
               %{buildroot}/%{_datadir}/fonts/%{name}

%files
%{_datadir}/fonts/%{name}/Ubuntu-Th.ttf
%{_datadir}/fonts/%{name}/Ubuntu-L.ttf
%{_datadir}/fonts/%{name}/Ubuntu-R.ttf
%{_datadir}/fonts/%{name}/Ubuntu-M.ttf
%{_datadir}/fonts/%{name}/Ubuntu-B.ttf
%{_datadir}/fonts/%{name}/Ubuntu-LI.ttf
%{_datadir}/fonts/%{name}/Ubuntu-RI.ttf
%{_datadir}/fonts/%{name}/Ubuntu-MI.ttf
%{_datadir}/fonts/%{name}/Ubuntu-BI.ttf
%{_datadir}/fonts/%{name}/UbuntuMono-R.ttf
%{_datadir}/fonts/%{name}/UbuntuMono-B.ttf
%{_datadir}/fonts/%{name}/UbuntuMono-RI.ttf
%{_datadir}/fonts/%{name}/UbuntuMono-BI.ttf
%{_datadir}/fonts/%{name}/Ubuntu-C.ttf
%license LICENCE.txt LICENCE-FAQ.txt copyright.txt TRADEMARKS.txt
%doc README.txt CONTRIBUTING.txt FONTLOG.txt

%post
fc-cache -f %{_datadir}/fonts/%{name}/ || true

%postun
fc-cache -f %{_datadir}/fonts/ || true

%changelog
* Fri Feb 23 2024 Michael Federczuk <federczuk.michael@protonmail.com> - 0.83-1
- Initial packaging
