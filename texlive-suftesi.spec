%global tl_name suftesi
%global tl_revision 73055

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2.6
Release:	%{tl_revision}.1
Summary:	A document class for typesetting theses, books and articles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/suftesi
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/suftesi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class can be used to typeset any kind of book (originally designed
for use in the humanities).

