# revision 24737
# category Package
# catalog-ctan /macros/latex/contrib/suftesi
# catalog-date 2011-11-17 00:42:26 +0100
# catalog-license lppl
# catalog-version 0.6c
Name:		texlive-suftesi
Version:	0.6c
Release:	1
Summary:	A document class for typesetting theses, books and articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/suftesi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.doc.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/suftesi/bibliografia-suftesi.bib
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Capitoli/primo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Capitoli/quarto.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Capitoli/secondo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Capitoli/terzo.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Immagini/don.png
%doc %{_texmfdistdir}/doc/latex/suftesi/example/Immagini/lamport.jpg
%doc %{_texmfdistdir}/doc/latex/suftesi/example/MaterialeInizialeFinale/Conclusione.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/MaterialeInizialeFinale/Introduzione.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/MaterialeInizialeFinale/Ringraziamenti.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/example/bibliografia.bib
%doc %{_texmfdistdir}/doc/latex/suftesi/example/logo.png
%doc %{_texmfdistdir}/doc/latex/suftesi/example/tesi.pdf
%doc %{_texmfdistdir}/doc/latex/suftesi/example/tesi.tex
%doc %{_texmfdistdir}/doc/latex/suftesi/logo.png
%doc %{_texmfdistdir}/doc/latex/suftesi/suftesi.pdf
%doc %{_texmfdistdir}/doc/latex/suftesi/suftesi.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
