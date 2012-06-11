# revision 26217
# category Package
# catalog-ctan /macros/latex/contrib/suftesi
# catalog-date 2012-04-23 11:23:52 +0200
# catalog-license lppl
# catalog-version 0.9
Name:		texlive-suftesi
Version:	0.9
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
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Capitoli/primo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Capitoli/secondo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Capitoli/terzo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Immagini/don.png
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Immagini/lamport.jpg
%doc %{_texmfdistdir}/doc/latex/suftesi/example/MaterialeInizialeFinale/Introduzione.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/MaterialeInizialeFinale/Ringraziamenti.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/bibliografia.bib
%doc %{_texmfdistdir}/doc/latex/suftesi/example/logo.png
%doc %{_texmfdistdir}/doc/latex/suftesi/example/tesi.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/suftesi.pdf
#- source
%doc %{_texmfdistdir}/source/latex/suftesi/suftesi.dtx
%doc %{_texmfdistdir}/source/latex/suftesi/suftesi.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
