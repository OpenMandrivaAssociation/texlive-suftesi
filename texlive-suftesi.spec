# revision 24413
# category Package
# catalog-ctan /macros/latex/contrib/suftesi
# catalog-date 2011-10-25 23:33:31 +0200
# catalog-license lppl
# catalog-version 0.6a
Name:		texlive-suftesi
Version:	0.6a
Release:	1
Summary:	A document class for typesetting theses, books and articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/suftesi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class is specifically designed for use with theses in the
humanities.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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