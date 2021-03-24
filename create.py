import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
token = os.getenv("TOKEN")
g = Github(token)

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = g.get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))
    commands = [f'cd {path} + {str(folderName)}',
        f'echo "# {repo.name}" >> README.md',
        'git init',
        f'git remote add origin https://github.com/{username}/{folderName}.git',
        'git add .',
        'git commit -m "Initial commit"',
        'git push -u origin master',
        'cp /Users/ato/scripts/website_code/andyto.uk/push .']
    for c in commands:
        os.system(c)
    print(f"Succesfully pushed {folderName} to GitHub")

if __name__ == "__main__":
    create()
