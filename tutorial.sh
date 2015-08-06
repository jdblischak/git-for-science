# Setup
mkdir -p ../thesis
cp code/* ../thesis
cd ../thesis

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
# Change fc_cutoff in clean.py
# +fc_cutoff = 20
# -fc_cutoff = 10
nano -w clean.py
git diff
git checkout -- clean.py
git diff
git checkout 660213b clean.py
