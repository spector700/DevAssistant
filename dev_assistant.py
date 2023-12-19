#!/usr/bin/env python

import os
import sys

from rich import print

if len(sys.argv) == 1:
    sys.exit("Usage: DevAssistant <project name>")

# Name of the new project
PROJECT = sys.argv[1]
# The directory for the projects
PATH = os.path.join(os.path.expanduser("~"), "Projects", PROJECT)
# Avaliable languages
LANG_OPTIONS = ["Python", "Rust", "NodeJS"]


def main():
    lang = select_lang(LANG_OPTIONS)
    # Create the new project folder
    create_dir(lang)
    # Ask to create git repo
    while True:
        ans = input("\nDo you want to create a github repo? (y | n) --> ").lower()
        if ans == "y":
            create_repo()
            break
        elif ans == "n":
            break


# Selecting a language
def select_lang(lang_options) -> str:
    lang = ""
    while lang not in lang_options:
        for i in range(len(lang_options)):
            print(f"{i + 1}. {lang_options[i]}")
        try:
            lang = lang_options[int(input("Select a number. --> ")) - 1]
        except (ValueError, IndexError):
            print("Enter a correct number\n")
    return lang


# Create and check for project directory and files
def create_dir(lang):
    try:
        os.mkdir(PATH)
        print(f"\nI created the folder {PROJECT}\n")
    except FileExistsError:
        print(f"\nThe folder {PROJECT} already exists...\n")

    os.chdir(PATH)
    os.system(f"nix flake init --refresh -t github:spector700/Templates/#{lang}")


# Creates the repo and the github remote repo
def create_repo():
    os.system("git init -b main")
    os.system("git add . && git commit -m 'initial commit'")
    os.system(f"gh repo create {PROJECT} --public --source=. --push")


if __name__ == "__main__":
    main()
