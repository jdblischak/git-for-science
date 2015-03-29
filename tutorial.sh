# Setup
mkdir thesis
cd thesis
touch process.sh clean.py analyze.R
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
echo "# Removes samples with more than 5% missing data" > clean.py
git diff
git checkout -- clean.py
git diff
git checkout 660213b91af167d992885e45ab19f585f02d4661 clean.py
