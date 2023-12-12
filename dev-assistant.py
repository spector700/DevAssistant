import sys
import os
from rich import print
from rich.theme import Theme
from rich.console import Console

# Name of the new project
project = sys.argv[1]
# The directory for the projects
path = f"/home/nick/Projects/{project}"
# Avaliable languages
lang_options = ["Python"]

print_theme = Theme({"exists": "green", "creating": "dark_orange3"})
console = Console(theme=print_theme)


def main():
    lang = select_lang(lang_options)
    # Create the new project folder
    create_dir(lang)
    # Ask to create git repo
    while True:
        ans = input("Do you want to create a github repo? (y | n)\n").lower()
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
            print(f"{i + 1}. {lang_options[i]}\n")
        try:
            lang = lang_options[int(input("Select a number. \n")) - 1]
        except (ValueError, IndexError):
            print("Enter a correct number\n")
    return lang


# Create and check for project directory and files
def create_dir(lang: str):
    try:
        os.mkdir(path)
        print(f"\nI created the folder {project}")
    except FileExistsError:
        print(f"\nThe folder {project} already exists...")

    os.chdir(path)

    # Check for flake
    full_path = os.path.join(path, "flake.nix")
    if os.path.isfile(full_path):
        console.print("\nflake.nix exists", style="exists")
    else:
        console.print("Downloading flake.nix", style="creating")
        os.system(
            f"wget https://raw.githubusercontent.com/spector700/Templates/main/{lang}/flake.nix"
        )

    # Check for .envrc
    full_path = os.path.join(path, ".envrc")
    if os.path.isfile(full_path):
        console.print(".envrc exists", style="exists")
    else:
        console.print("Creating .envrc...", style="creating")
        with open(".envrc", "w") as direnv:
            direnv.write("use flake")

    # Check for .gitignore
    full_path = os.path.join(path, ".gitignore")
    if os.path.isfile(full_path):
        console.print(".gitignore exists\n", style="exists")
    else:
        console.print("Downloading .gitignore", style="creating")
        os.system(
            f"wget https://raw.githubusercontent.com/spector700/Templates/main/{lang}/.gitignore"
        )


# Creates the repo and the github remote repo
def create_repo():
    os.system("git init -b main")
    os.system(f"gh repo create {project} --add-readme --public --source=.")
    os.system("git add . && git commit -m 'initial commit'")
    os.system("git push --set-upstream origin main")


if __name__ == "__main__":
    main()
