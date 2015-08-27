#!/bin/bash

# A file with changes highlighted is required for resubmission.

# Download original submission
wget https://github.com/jdblischak/git-for-science/archive/2015-05-08.zip
unzip 2015-05-08.zip

# Change the lstlisting sections to verbatim.
# Otherwise the file output by latexdiff cannot be compiled.
sed -i s/lstlisting/verbatim/g git-for-science-2015-05-08/blischak-et-al-2015.tex

# Create tex file with differences highlighted
latexdiff git-for-science-2015-05-08/blischak-et-al-2015.tex blischak-et-al-2015.tex > diff.tex

# Compile diff.tex
latex diff
bibtex diff
latex diff
pdflatex diff
