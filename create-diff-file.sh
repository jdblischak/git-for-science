#!/bin/bash

# A file with changes highlighted is required for resubmission.

# Usage:
#
# bash create-diff-file.sh TAG IN_NAME OUT_NAME
#
# TAG: The name of the tag of the previous version (must be on GitHub)
# IN_NAME: The name of the tex file to compare
# OUT_NAME: The name of the tex file with changes highlighted
#
# Examples:
#
# # For the first revision:
# bash create-diff-file.sh 2015-05-08 blischak-et-al-2015.tex diff.tex
#
# # For the second revision:
# bash create-diff-file.sh 2015-08-27-revision blischak-et-al-2015.tex diff2.tex

TAG=$1
IN_NAME=$2
OUT_NAME=$3

# Download version of repo from TAG
if [[ -f $TAG.zip ]]
then
  echo "$TAG was already downloaded"
else
  wget https://github.com/jdblischak/git-for-science/archive/$TAG.zip
  unzip $TAG.zip
fi

# The following only needs to be applied to the original sumbission.
# Change the lstlisting sections to verbatim.
# Otherwise the file output by latexdiff cannot be compiled.
if [[ $TAG == 2015-05-08 ]]
then
  sed -i s/lstlisting/verbatim/g git-for-science-$TAG/$IN_NAME
fi

# Create tex file with differences highlighted
latexdiff git-for-science-$TAG/$IN_NAME $IN_NAME > $OUT_NAME

# Compile diff.tex
bash compile-to-pdf.sh $OUT_NAME
