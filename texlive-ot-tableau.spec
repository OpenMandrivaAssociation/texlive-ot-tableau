%global tl_name ot-tableau
%global tl_revision 67813

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Optimality Theory tableaux in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ot-tableau
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ot-tableau.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ot-tableau.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes it easy to create beautiful optimality-theoretic
tableaux. The LaTeX source is visually very similar to a formatted
tableau, which makes working with the source code painless (well, less
painful). A variety of stylistic variants are available to suit personal
taste. The package requires xstring, amssymb, bbding, suffix, colortbl,
rotating, hhline (optionally), arydshln, and tipa (optionally).

