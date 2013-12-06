# revision 31713
# category Package
# catalog-ctan /macros/latex/contrib/suftesi
# catalog-date 2013-09-21 14:06:34 +0200
# catalog-license lppl
# catalog-version 1.9
Name:		texlive-suftesi
Version:	1.9
Release:	5
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
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/collection/collection-art1.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/collection/collection.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/Capitoli/primo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/Capitoli/secondo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/Capitoli/terzo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/MaterialeInizialeFinale/Introduzione.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/MaterialeInizialeFinale/Ringraziamenti.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/cognome-tesi.bib
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/cognome-tesi.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/immagini/don.png
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/immagini/lamport.jpg
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-magistrale/immagini/logo.png
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-triennale/cognome-tesi.bib
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-triennale/cognome-tesi.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-triennale/immagini/don.png
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-triennale/immagini/lamport.jpg
%doc %{_texmfdistdir}/doc/latex/suftesi/templates/tesi-triennale/immagini/logo.png
#- source
%doc %{_texmfdistdir}/source/latex/suftesi/suftesi.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
