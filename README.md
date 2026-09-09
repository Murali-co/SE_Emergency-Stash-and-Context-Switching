SE\_Emergency-Stash-and-Context-Switching

# SE\_Emergency-Stash-and-Context-Switching



\## Objective

Handle a sudden priority shift without losing uncommitted progress, using git stash.



\## Scenario

A developer is mid-way through building a new feature. The code is incomplete and not ready to commit. Suddenly, an urgent production bug comes in and must be fixed immediately, without losing the unfinished feature work.



\## Workflow



\### 1. Start the feature

Created a new branch off main:

git checkout -b feature-branch



Wrote incomplete code in feature.py (not committed, deliberately unfinished).



\### 2. Emergency interrupts, stash the work

git stash push -u -m "WIP: feature in progress"



The -u flag includes untracked files, since feature.py was never staged.

Result: working directory is clean, unfinished work is safely stored.



\### 3. Switch to main and apply the hotfix

git checkout main

git add hotfix.py

git commit -m "hotfix: fix urgent production bug"

git push origin main



The fix is committed and pushed to main, completely separate from the feature branch.



\### 4. Return to the feature branch and restore work

git checkout feature-branch

git stash pop



The exact unfinished code from Step 1 is restored.

git stash list is now empty, the stash was consumed.



\### 5. Finish and push the feature work

git add feature.py

git commit -m "wip: continue new feature after hotfix interruption"

git push origin feature-branch



\## Branch Summary

main branch: initial commit then hotfix commit

feature-branch: initial commit then feature.py commit



The two branches never merged. Main shipped the emergency fix independently, and feature-branch resumed exactly where the developer left off, with zero work lost.



\## Key Concept

git stash acts as a temporary drawer for uncommitted changes. It allows a developer to clear the working directory without committing broken or incomplete code, switch branches freely to handle urgent tasks, and restore the exact previous state afterward with git stash pop. This makes it possible to context switch under pressure without risking lost work or polluting commit history with unfinished code.

