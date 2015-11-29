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
    """Write contents of file to standard out.

    Args:
        fname - the filename (str)
        blankline - the number of blank lines to add after the text (int)
    """
    handle = open(fname, "r")
    for line in handle:
        if "Table 1" in line:
            line = line.replace("Table 1", "Table \\ref{tab:resources}")
        sys.stdout.write(line)
    handle.close()
    sys.stdout.write("\n" * blankline)

def write_figure(caption, label):
    """Write labeled figure with the provided caption.

    Args:
        caption - a list of strings
        label - a string to be used with \label
    """
    sys.stdout.write("\\begin{figure}[h]\n")
    # Remove \ref macro from figure caption
    caption[0] = caption[0].split("}.")[1]
    # Bold face the caption title
    caption[0] = "\\bf" + caption[0]

    sys.stdout.write("\\cprotect\\caption{{" + caption[0] + "\n")
    for line in caption[1:]:
        sys.stdout.write(line)

    # End caption
    sys.stdout.write("}\n")
    # Add label
    sys.stdout.write("\\label{%s}\n"%(label))
    # End figure
    sys.stdout.write("\\end{figure}\n\n")

################################################################################
# Extract figure legends
################################################################################

d_figs = {}
for i in range(4):
    d_figs[i + 1] = []

legend_file = open("figures/figure-legends.tex", "r")
# Skip subsection macro and blank line
legend_file.readline()
legend_file.readline()

i = 1
for line in legend_file:
    if line != "\n":
        d_figs[i] = d_figs[i] + [line]
    else:
        i = i + 1

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
# Figure 1 and 2
################################################################################

write_figure(d_figs[1], label = "fig:Fig1")
write_figure(d_figs[2], label = "fig:Fig2")

################################################################################
# Share your code
################################################################################

write_file("share-your-code.tex")

################################################################################
# Figure 3
################################################################################

write_figure(d_figs[3], label = "fig:Fig3")

################################################################################
# Contribute to other projects
################################################################################

write_file("contribute-to-other-projects.tex")

################################################################################
# Figure 4
################################################################################

write_figure(d_figs[4], label = "fig:Fig4")

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
write_file("blischak-et-al.bbl")

################################################################################
# Supporting Information Legends
################################################################################

write_file("supporting-information-legends.tex")

################################################################################
# End document
################################################################################

sys.stdout.write(r"\end{document}" + "\n\n")
