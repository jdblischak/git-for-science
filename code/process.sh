#!/bin/bash

# Download bam files and call peaks.

ENCODE=https://www.encodeproject.org/files
OUTDIR=../data
MACS2="macs2 callpeak -f BAM -g hs"

################################################################################

echo "Processing kidney epithelial cell data"
# Kidney epithelial cells
# https://www.encodeproject.org/experiments/ENCSR000DVH/
# Rep 1 - ENCFF001HQY
# Rep 2 - ENCFF001HRF
# Control - ENCFF001HRJ

# Setup
SUBDIR=$OUTDIR/epithelial
mkdir -p $SUBDIR

# Download
# $ENCODE/$SAMPLE/@@download/$SAMPLE.bam
if [[ ! -e $SUBDIR/ENCFF001HQY.bam ]]
then
  echo "Downloading data"
  for SAMPLE in ENCFF001HQY ENCFF001HRF ENCFF001HRJ
  do
    wget -O $SUBDIR/$SAMPLE.bam $ENCODE/$SAMPLE/@@download/$SAMPLE.bam
  done
fi

# Run MACS2
echo "Running MACS2"
$MACS2 -t $SUBDIR/ENCFF001HQY.bam $SUBDIR/ENCFF001HRF.bam -c $SUBDIR/ENCFF001HRJ.bam \
       -n epithelial --outdir $SUBDIR

################################################################################

echo "Processing proximal tube data"
# Epithelial cell of proximal tube
# https://www.encodeproject.org/experiments/ENCSR000DXD/
# Rep 1 - ENCFF001HWB
# Rep 2 - ENCFF001HWC
# Control - ENCFF001HWN

# Setup
SUBDIR=$OUTDIR/proximal-tube
mkdir -p $SUBDIR

# Download
# $ENCODE/$SAMPLE/@@download/$SAMPLE.bam
if [[ ! -e $SUBDIR/ENCFF001HWB.bam ]]
then
  echo "Downloading data"
  for SAMPLE in ENCFF001HWB ENCFF001HWC ENCFF001HWN
  do
    wget -O $SUBDIR/$SAMPLE.bam $ENCODE/$SAMPLE/@@download/$SAMPLE.bam
  done
fi

# Run MACS2
echo "Running MACS2"
$MACS2 -t $SUBDIR/ENCFF001HWB.bam $SUBDIR/ENCFF001HWC.bam -c $SUBDIR/ENCFF001HWN.bam \
       -n proximal-tube --outdir $SUBDIR

################################################################################

echo "Processing kidney data"
# kidney
# https://www.encodeproject.org/experiments/ENCSR000DMC/
# Rep 1 - ENCFF000RWX
# Rep 2 - ENCFF000RWW
# Rep 3 - ENCFF000RWZ
# Control - ENCFF000RXD

# Setup
SUBDIR=$OUTDIR/kidney
mkdir -p $SUBDIR

# Download
# $ENCODE/$SAMPLE/@@download/$SAMPLE.bam
if [[ ! -e $SUBDIR/ENCFF000RWX.bam ]]
then
  echo "Downloading data"
  for SAMPLE in ENCFF000RWX ENCFF000RWW ENCFF000RWZ ENCFF000RXD
  do
    wget -O $SUBDIR/$SAMPLE.bam $ENCODE/$SAMPLE/@@download/$SAMPLE.bam
  done
fi

# Run MACS2
echo "Running MACS2"
$MACS2 -t $SUBDIR/ENCFF000RWX.bam $SUBDIR/ENCFF000RWW.bam $SUBDIR/ENCFF000RWZ.bam \
       -c $SUBDIR/ENCFF000RXD.bam \
       -n kidney --outdir $SUBDIR
