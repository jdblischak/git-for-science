#!/usr/bin/env python

# Usage:
#
# python build-full-article.py > blischak-et-al.tex

import sys
import textwrap

################################################################################
# Add header
################################################################################

header_file = open("header-local.tex", "r")
for line in header_file:
    sys.stdout.write(line)
sys.stdout.write("\n")

################################################################################
# Begin document
################################################################################

sys.stdout.write(r"\begin{document}" + "\n" +
                 r"\vspace*{0.35in}" + "\n")

################################################################################
# Add title
################################################################################

title_file = open("title.tex", "r")
title = title_file.read().strip("\n")

sys.stdout.write(textwrap.dedent("""
\\begin{flushleft}
{\\Large
\\textbf\\newline{%s}
}
\\newline
%% Insert author names, affiliations and corresponding author email (do not include titles, positions, or degrees).
\\\\
"""%(title)
))

################################################################################
# Add authors
################################################################################

authors_file = open("authors.tex", "r")
# First skip unnecessary contents needed for Authorea build
for line in authors_file:
    if "else" in line:
        break
for line in authors_file:
    sys.stdout.write(line.lstrip(" "))
sys.stdout.write("\n")

sys.stdout.write(r"\end{flushleft}" + "\n\n")

################################################################################
# Introduction
################################################################################

sys.stdout.write(r"\linenumbers" + "\n\n")

intro_file = open("introduction.tex", "r")
for line in intro_file:
    sys.stdout.write(line)
sys.stdout.write("\n")

################################################################################
# Version your code
################################################################################

version_file = open("version-your-code.tex", "r")
for line in version_file:
    sys.stdout.write(line)
sys.stdout.write("\n")

################################################################################
# Share your code
################################################################################

share_file = open("share-your-code.tex", "r")
for line in share_file:
    sys.stdout.write(line)
sys.stdout.write("\n")

################################################################################
# Contribute to other projects
################################################################################

contribute_file = open("contribute-to-other-projects.tex", "r")
for line in contribute_file:
    sys.stdout.write(line)
sys.stdout.write("\n")

################################################################################
# Conclusion
################################################################################

conclusion_file = open("conclusion.tex", "r")
for line in conclusion_file:
    sys.stdout.write(line)
sys.stdout.write("\n")

################################################################################
# Methods
################################################################################

methods_file = open("methods.tex", "r")
for line in methods_file:
    sys.stdout.write(line)
sys.stdout.write("\n")

################################################################################
# References
################################################################################

sys.stdout.write(r"\nolinenumbers" + "\n\n")
sys.stdout.write(r"\bibliography{bibliography/converted_to_latex.bib}" + "\n\n")

################################################################################
# End document
################################################################################

sys.stdout.write(r"\end{document}" + "\n\n")
