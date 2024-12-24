# USTH ICT 2024 Advanced Programming with Python COURSE
Students are expected to:
* Fork this repository to your github account
* Push your commits regularly, with **proper** commit messages


# Student Info
* Student Name: Pham The Minh 
* Student ID: 23BI14279

# how to use Git:

## Setup Git
To configure Git for the first time:
```bash
git config --global user.name "USERNAME"
git config --global user.email "EMAIL"
```
To clone a repository:
```bash
git clone <repository-link>
```

---

## Basic Git Commands

### Adding and Committing Changes
1. Add files to the staging area:
   ```bash
   git add <file>
   ```
   To add all files:
   ```bash
   git add *
   ```
2. Commit the changes with a message:
   ```bash
   git commit -m "Commit message"
   ```
3. Push changes to the main branch:
   ```bash
   git push origin main
   ```

### Deleting Files
1. Delete the file:
   ```bash
   del <file>
   ```
2. Stage the deletion:
   ```bash
   git add -u
   ```
3. Commit and push the changes.

### Renaming Files
Rename a file and stage the change in one step:
```bash
git mv <oldfile> <newfile>
```

### Pulling Updates
To fetch and merge the latest changes from the remote repository, run:
```bash
git pull
```
It’s recommended to pull updates when starting your work session in VS Code.

---

## Installing Git on Linux
1. Install Git:
   ```bash
   sudo apt update && sudo apt install git
   ```
2. Install the Git Credential Manager:
   [Git Credential Manager Releases](https://github.com/git-ecosystem/git-credential-manager/releases)
3. Configure the credential manager:
   ```bash
   git config --global credential.helper manager
   ```

### Troubleshooting Credential Manager Issues 
If you encounter the error:
```
fatal: No credential store has been selected.
```
Follow these steps:
1. Set the `GCM_CREDENTIAL_STORE` environment variable or configure the credential store:
   ```bash
   git config --global credential.credentialStore <option>
   ```
   Replace `<option>` with one of the following:
   - `secretservice`: Freedesktop.org Secret Service (requires GUI).
   - `gpg`: GNU `pass` compatible credential storage (requires GPG and `pass`).
   - `cache`: Git's in-memory credential cache.
   - `plaintext`: Store credentials in plain-text files (**insecure**).

For more details, refer to the [Git Credential Manager Documentation](https://aka.ms/gcm/credstores).

### Alternative Approach
* can run Git commands directly in VS Code’s terminal without installing the Git Credential Manager. 
* IT t will have a window to login from browser, but if run in Terminal still need to go with credential manager

---

This guide provides a structured overview for setting up and using Git effectively. For further details, consult the official [Git documentation](https://git-scm.com/doc).