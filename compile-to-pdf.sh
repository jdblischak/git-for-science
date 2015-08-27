#!/bin/bash

# Compile tex to pdf

TEX=$1

BASE=${TEX%.tex}

# Number the figures
latex $BASE
# Add the bibliography
bibtex $BASE
# Number the in-text citations
latex $BASE
# Convert to pdf
pdflatex $BASE
