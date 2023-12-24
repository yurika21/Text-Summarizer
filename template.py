import os
from pathlib import Path
import logging

# for debugging and finding warnign messages ig?
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer" 

list_of_files = [
    ".github/workflows/.gitkeep", #git keep is a hidden file, will be deleted later
    f"src/{project_name}/__init__.py", #init is a constructor file that makes this as a local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    # / \ is different in linux and windows so this file Path helps give me the path one by one based on OS
    filepath = Path(filepath)
    # os. is a module and allows the code to be portable (bcz of different /\)
    filedir, filename = os.path.split(filepath)

    # if filedir not empty then
    if filedir != '':
        # create the directory/folder
        os.makedirs(filedir, exist_ok=True) #exist_ok -> if the directory already exists, it will not be created again
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # create the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if doesnt exist or file size 0 (replace only if exists but empty to not lose code)
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
