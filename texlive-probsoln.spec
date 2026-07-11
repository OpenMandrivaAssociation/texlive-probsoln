%global tl_name probsoln
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.05
Release:	%{tl_revision}.1
Summary:	Generate problem sheets and their solution sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/probsoln
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/probsoln.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/probsoln.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/probsoln.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is designed for lecturers who have to generate new problem
sheets for their students on a regular basis (e.g. yearly) by randomly
selecting a specified number of problems defined in another file. The
package allows you easily to generate a new problem sheet that is
different from the previous year, thus alleviating the temptation of
students to seek out the previous year's students and checking out their
answers. The solutions to the problems can be defined along with the
problem, making it easy to generate the solution sheet from the same
source code; problems may be reused within a document, so that solutions
may appear in a different section of the same document as the problems
they cover.

