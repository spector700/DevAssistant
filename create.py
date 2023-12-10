import sys
import os

lang = ""
# Name of the new project
project = sys.argv[1]
# The directory for the projects
path = f"/home/nick/Projects/{project}"

# Selecting a language
while lang != "python":
    lang = input("What language: ")

def create():
    try:
        os.mkdir(path)
        print(f"I created the folder {project}")
    except FileExistsError:
        print(f"The folder {project} already exists...")
        
if __name__ == "__main__":
    create()