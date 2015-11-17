# README

This subdirectory contains the example scripts to accompany the manuscript.
Read the section [Version your code][version] for the full explanation.

[version]: https://www.authorea.com/users/5990/articles/17489/_show_article#article-paragraph-version__minus__your__minus__code__dot__tex-landing-welcome

## process.sh

`process.sh` downloads the ENCODE CTCF ChIP-seq data from multiple types of kidney samples and calls peaks.
Run it as follows:

```bash
bash process.sh
```

## clean.py

`clean.py` filters peaks with a fold change cutoff and merges peaks from the different kidney samples.
Run it as follows:

```bash
python clean.py
```

## analyze.R

`analyze.R` creates diagnostic plots on the length of the peaks and their distribution across the genome.
Run it as follows:

```bash
Rscript analyze.R
```
