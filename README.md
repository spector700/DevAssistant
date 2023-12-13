# DevAssistant

Automation tool to create a nix flake dev environment with flake.nix and direnv. Also create a github repo if desired.


## Lanuages
These are the current lanuages that have a flake [template](https://github.com/spector700/Templates).

- Python
- Rust
- NodeJS

## Installation

### Dependencies
- python
- wget
- gh

Clone the Repository:
```bash
git clone https://github.com/spector700/DevAssistant.git
cd DevAssistant
```

## Usage

1. Run the sh file with the project name.
To use it anywhere you can alias the dev-assistant.sh in your shell config

```bash
sh dev-assistant.sh goofy
# Then follow the prompts

1. Python
2. Rust
3. NodeJS
Select a number. --> 
```
2. It will download the flake.nix for the language you chose and create a .envrc

```bash
Downloading flake.nix
--2023-12-12 20:46:29--  https://raw.githubusercontent.com/spector700/Templates/main/Python/flake.nix
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8000::154, 2606:50c0:8001::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1297 (1.3K) [text/plain]
Saving to: ‘flake.nix’

flake.nix                             100%[========================================================================>]   1.27K  --.-KB/s    in 0s      

2023-12-12 20:46:29 (159 MB/s) - ‘flake.nix’ saved [1297/1297]

Creating .envrc...
Do you want to create a github repo? (Y | N) -->
```



3. If you want to create a github repo, it will guide you with gh (github cli) to create an access token.
Then you will be able to create the repo.
```bash
Do you want to create a github repo? (Y | N) --> y
Downloading .gitignore
--2023-12-12 20:49:03--  https://raw.githubusercontent.com/spector700/Templates/main/Python/.gitignore
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8002::154, 2606:50c0:8003::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8 [text/plain]
Saving to: ‘.gitignore’

.gitignore                            100%[========================================================================>]       8  --.-KB/s    in 0s      

2023-12-12 20:49:04 (1.04 MB/s) - ‘.gitignore’ saved [8/8]

Initialized empty Git repository in /home/nick/Projects/goofy/.git/
✓ Created repository spector700/goofy on GitHub
✓ Added remote git@github.com:spector700/goofy.git
[main (root-commit) f8bc136] initial commit
 3 files changed, 49 insertions(+)
 create mode 100644 .envrc
 create mode 100644 .gitignore
 create mode 100644 flake.nix
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 908 bytes | 908.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:spector700/goofy.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

