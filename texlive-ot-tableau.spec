Name:		texlive-ot-tableau
Version:	67813
Release:	1
Summary:	Optimality Theory tableaux in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ot-tableau
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ot-tableau.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ot-tableau.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes it easy to create beautiful optimality-
theoretic tableaux. The LaTeX source is visually very similar
to a formatted tableau, which makes working with the source
code painless (well, less painful). A variety of stylistic
variants are available to suit personal taste.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ot-tableau/ot-tableau.sty
%doc %{_texmfdistdir}/doc/latex/ot-tableau/README
%doc %{_texmfdistdir}/doc/latex/ot-tableau/ot-tableau.pdf
%doc %{_texmfdistdir}/doc/latex/ot-tableau/ot-tableau.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
