#!/usr/bin/env python

"""
Identify high-quality CTCF binding sites.

1. Remove peaks with low fold change in enrichment over control.
2. Keep only those regions bound by CTCF in all three tissue types.
"""

import pybedtools
import math

data = "../data"

# For details of MACS2 output format:
# https://github.com/taoliu/MACS#output-files
epithelial = pybedtools.BedTool(data + "/epithelial/epithelial_peaks.narrowPeak")
proximal_tube = pybedtools.BedTool(data + "/proximal-tube/proximal-tube_peaks.narrowPeak")
kidney = pybedtools.BedTool(data + "/kidney/kidney_peaks.narrowPeak")

def filter_fold_change(feature, fc = 1):
    """
    Removes peaks with a fold change over the control less than fc.
    """
    if float(feature[7]) >= fc:
        return True
    else:
        return False

# Filter based on fold-change over control sample
fc_cutoff = 10
epithelial = epithelial.filter(filter_fold_change, fc = fc_cutoff).saveas()
proximal_tube = proximal_tube.filter(filter_fold_change, fc = fc_cutoff).saveas()
kidney = kidney.filter(filter_fold_change, fc = fc_cutoff).saveas()
# Identify only those sites that are peaks in all three tissue types
combined = pybedtools.BedTool().multi_intersect(
           i = [epithelial.fn, proximal_tube.fn, kidney.fn])
union = combined.filter(lambda x: int(x[3]) == 3).saveas()
union.cut(range(3)).saveas(data + "/sites-union.bed")
