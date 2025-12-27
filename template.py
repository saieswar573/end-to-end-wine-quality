import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "mlProject"

list_of_files = [
    f"src/{project_name}/_init_.py",
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/_init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init_.py",
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constants/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    # CREATE DIRECTORY
    filedir = filepath.parent
    if not filedir.exists():
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory : {filedir}")

    # CREATE FILE
    if not filepath.exists():
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file : {filepath}")