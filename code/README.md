# README

This subdirectory contains the example scripts to accompany the manuscript.
Read the section [Version your code][version] for the full explanation.
The commands described below should be executed from within the subdirectory `code`.

[version]: https://www.authorea.com/users/5990/articles/17489/_show_article#article-paragraph-version__minus__your__minus__code__dot__tex-landing-welcome

## process.sh

`process.sh` downloads the ENCODE CTCF ChIP-seq data from multiple types of kidney samples and calls peaks.
The downloaded BAM files and [MACS2][] output are saved in tissue-specific subdirectories in `../data/`.
Run it as follows:

```bash
bash process.sh
```

You will need to have Python 2.7 installed because it is a [prerequisite][] for the peak caller [MACS2][].
To install MACS2, run:

```bash
pip install macs2
```

[prerequisite]: https://github.com/taoliu/MACS/blob/master/INSTALL.rst#prerequisites
[MACS2]: https://github.com/taoliu/MACS

## clean.py

`clean.py` filters peaks with a fold change cutoff and merges peaks from the different kidney samples.
It creates the file `../data/sites-union.bed`.
Run it as follows:

```bash
python clean.py
```

It can be run with either Python2 or Python3.
You will first need to install [bedtools][] and [pybedtools][].
See their documentation for instructions, but as an example, this can be accomplished on Ubuntu with the following:

```bash
apt-get install bedtools
pip install pybedtools
```

[bedtools]: http://bedtools.readthedocs.org/en/latest/content/installation.html
[pybedtools]: http://pythonhosted.org/pybedtools/main.html

## analyze.R

`analyze.R` creates diagnostic plots on the length of the peaks and their distribution across the genome.
It creates the file `../data/sites-union.pdf`.
Run it as follows:

```bash
Rscript analyze.R
```
