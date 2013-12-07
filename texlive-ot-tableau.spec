# revision 17829
# category Package
# catalog-ctan /macros/latex/contrib/ot-tableau
# catalog-date 2010-04-14 18:13:33 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-ot-tableau
Version:	20100414
Release:	4
Summary:	Optimality Theory tableaux in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ot-tableau
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ot-tableau.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ot-tableau.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100414-2
+ Revision: 754559
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100414-1
+ Revision: 719172
- texlive-ot-tableau
- texlive-ot-tableau
- texlive-ot-tableau
- texlive-ot-tableau

