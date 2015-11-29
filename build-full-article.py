#!/usr/bin/env python

# Usage:
#
# python build-full-article.py > blischak-et-al.tex

################################################################################
# Setup
################################################################################

import sys
import textwrap
import glob

def write_file(fname, blankline = 1):
    handle = open(fname, "r")
    for line in handle:
        if "Table 1" in line:
            line = line.replace("Table 1", "Table \\ref{tab:resources}")
        sys.stdout.write(line)
    handle.close()
    sys.stdout.write("\n" * blankline)


################################################################################
# Add header
################################################################################

write_file("header-local.tex")

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

write_file("introduction.tex")

################################################################################
# Version your code
################################################################################

write_file("version-your-code.tex")

################################################################################
# Table
################################################################################

table_file = open("table-1-resources.tex", "r")
# Ignore subsection macro
table_file.readline()
#
sys.stdout.write("""
\\begin{table}[!ht]
\\begin{adjustwidth}{-1.25in}{0in} % Comment out/remove adjustwidth environment if table fits in text column.
\\caption{
{\\bf Resources.}}
"""
)

for line in table_file:
    sys.stdout.write(line)

sys.stdout.write("""
\label{tab:resources}
\end{adjustwidth}
\end{table}
"""
)

sys.stdout.write("\n")

################################################################################
# Share your code
################################################################################

write_file("share-your-code.tex")

################################################################################
# Contribute to other projects
################################################################################

write_file("contribute-to-other-projects.tex")

################################################################################
# Conclusion
################################################################################

write_file("conclusion.tex")

################################################################################
# Boxes
################################################################################

for i in range(7):
    box_name = glob.glob("box-" + str(i + 1) + "-*tex")[0]
    write_file(box_name)

################################################################################
# Methods
################################################################################

write_file("methods.tex")

################################################################################
# References
################################################################################

sys.stdout.write(r"\nolinenumbers" + "\n\n")
sys.stdout.write(r"\bibliography{bibliography/converted_to_latex.bib}" + "\n\n")

################################################################################
# End document
################################################################################

sys.stdout.write(r"\end{document}" + "\n\n")
