import sys
import os
from rich import print
from rich.theme import Theme
from rich.console import Console

# Name of the new project
PROJECT = sys.argv[1]
# The directory for the projects
PATH = f"/home/nick/Projects/{PROJECT}"
# Avaliable languages
LANG_OPTIONS = ["Python"]

print_theme = Theme({"exists": "green", "creating": "dark_orange3"})
console = Console(theme=print_theme)


def main():
    lang = select_lang(LANG_OPTIONS)
    # Create the new project folder
    create_dir()
    # Check or Download files
    check_file(file="flake.nix", lang=lang, download=True)
    check_file(file=".envrc")
    # Ask to create git repo
    while True:
        ans = input("Do you want to create a github repo? (Y | N) --> ").lower()
        if ans == "y":
            check_file(file=".gitignore", lang=lang, download=True)
            create_repo()
            break
        elif ans == "n":
            break


# Selecting a language
def select_lang(lang_options) -> str:
    lang = ""
    while lang not in lang_options:
        for i in range(len(lang_options)):
            print(f"{i + 1}. {lang_options[i]}\n")
        try:
            lang = lang_options[int(input("Select a number. --> ")) - 1]
        except (ValueError, IndexError):
            print("Enter a correct number\n")
    return lang


# Create and check for project directory and files
def create_dir():
    try:
        os.mkdir(PATH)
        print(f"\nI created the folder {PROJECT}")
    except FileExistsError:
        print(f"\nThe folder {PROJECT} already exists...")

    os.chdir(PATH)


def check_file(file, lang=None, download=False):
    full_path = os.path.join(PATH, file)
    if os.path.isfile(full_path):
        console.print(f"{file} exists", style="exists")
        return
    else:
        # Download from the Templates repo
        if download:
            console.print(f"Downloading {file}", style="creating")
            os.system(
                f"wget https://raw.githubusercontent.com/spector700/Templates/main/{lang}/{file}"
            )
        # Create the .envrc
        else:
            console.print("Creating .envrc...", style="creating")
            with open(".envrc", "w") as direnv:
                direnv.write("use flake")


# Creates the repo and the github remote repo
def create_repo():
    os.system("git init -b main")
    os.system(f"gh repo create {PROJECT} --add-readme --public --source=.")
    os.system("git add . && git commit -m 'initial commit'")
    os.system("git push --set-upstream origin main")


if __name__ == "__main__":
    main()
