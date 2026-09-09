# Git Stash Demo: Emergency Context Switching

This repository serves as a hands-on demonstration of using Git to manage sudden priority shifts. It simulates a real-world scenario where a developer must pause incomplete feature work to address an urgent production bug.

## 🎯 Project Objectives

* **Safely pause work:** Learn to clear the working directory without committing half-finished code.
* **Handle hotfixes:** Switch to the `main` branch to address critical bugs in a clean environment.
* **Restore state:** Return to the feature branch and recover the exact workspace state using Git's stash stack.

## 🚀 How to Run the Simulation

1. **Setup:** Initialize the repository, make a baseline commit, and check out a new branch named `feature/user-auth`.
2. **Simulate Work:** Generate dummy code in a new file (e.g., `auth.js`) to represent your work-in-progress.
3. **The Emergency:** Use `git stash` to temporarily store your uncommitted changes and clean your working tree.
4. **The Hotfix:** Switch back to `main`, apply a dummy patch, and commit the emergency fix.
5. **The Recovery:** Switch back to `feature/user-auth` and run `git stash pop` to resume exactly where you left off.

## 📚 Key Commands Reference

| Command | Purpose |
| :--- | :--- |
| `git stash` | Saves tracked, uncommitted changes and restores a clean working directory. |
| `git stash list` | Displays all currently saved stashes. |
| `git stash pop` | Applies the most recent stash to your workspace and deletes it from the stash queue. |

> **Note:** By default, standard stashing ignores brand new files. If you have created new files that haven't been staged yet, use `git stash -u` to ensure those untracked files are saved as well.

