# revision 33382
# category Package
# catalog-ctan /macros/latex/contrib/suftesi
# catalog-date 2014-04-05 12:34:01 +0200
# catalog-license lppl
# catalog-version 1.9c
Name:		texlive-suftesi
Version:	1.9c
Release:	1
Summary:	A document class for typesetting theses, books and articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/suftesi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is specifically designed for use with theses in the
humanities.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/suftesi/suftesi.cls
%doc %{_texmfdistdir}/doc/latex/suftesi/README
%doc %{_texmfdistdir}/doc/latex/suftesi/suftesi.pdf
%doc %{_texmfdistdir}/doc/latex/suftesi/templates.zip
#- source
%doc %{_texmfdistdir}/source/latex/suftesi/suftesi.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
