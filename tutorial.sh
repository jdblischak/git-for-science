# Setup
mkdir thesis
cd thesis
touch process.sh analyze.R
echo '#!/usr/bin/env python

# Thesis project:
# Remove bad samples.
# Export clean data as a matrix.

# Usage: clean.py input [input ...] > data_clean.py

import sys
import os
' > clean.py
# Version your code
git init
git config user.name "First Last"
git config user.email "user@domain"
git status
git add process.sh
git status
git add clean.py analyze.R
git commit -m "Add initial version of thesis code."
git log
# Change description in clean.py
# +# Remove samples with more than 5% missing data.
# -# Remove bad samples.
nano clean.py
git diff
git checkout -- clean.py
git diff
git checkout 660213b clean.py
