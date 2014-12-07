# revision 29371
# category Package
# catalog-ctan /macros/latex/contrib/probsoln
# catalog-date 2012-11-17 10:29:25 +0100
# catalog-license lppl
# catalog-version 3.02
Name:		texlive-probsoln
Version:	3.02
Release:	9
Summary:	Generate problem sheets and their solution sheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/probsoln
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/probsoln.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/probsoln.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/probsoln.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is designed for lecturers who have to generate new
problem sheets for their students on a regular basis (e.g.
yearly) by randomly selecting a specified number of problems
defined in another file. The package allows you easily to
generate a new problem sheet that is different from the
previous year, thus alleviating the temptation of students to
seek out the previous year's students and checking out their
answers. The solutions to the problems can be defined along
with the problem, making it easy to generate the solution sheet
from the same source code; problems may be reused within a
document, so that solutions may appear in a different section
of the same document as the problems they cover.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/probsoln/probsoln.sty
%doc %{_texmfdistdir}/doc/latex/probsoln/CHANGES
%doc %{_texmfdistdir}/doc/latex/probsoln/INSTALL
%doc %{_texmfdistdir}/doc/latex/probsoln/README
%doc %{_texmfdistdir}/doc/latex/probsoln/probsoln-manual.css
%doc %{_texmfdistdir}/doc/latex/probsoln/probsoln-manual.html
%doc %{_texmfdistdir}/doc/latex/probsoln/probsoln-manual.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/probsoln.pdf
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample-exclude.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample.pdf
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample2.pdf
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample2.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample3.pdf
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample3.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample4.pdf
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample4.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample5.pdf
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample5.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample6.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample7.tex
%doc %{_texmfdistdir}/doc/latex/probsoln/samples/sample8.tex
#- source
%doc %{_texmfdistdir}/source/latex/probsoln/probsoln.dtx
%doc %{_texmfdistdir}/source/latex/probsoln/probsoln.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
