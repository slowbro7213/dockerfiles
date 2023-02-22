import os
import yaml
import json
from pathlib import Path


def get_project_root() -> Path:
    # must maintain this file path. ( project_root/src/common/fileutil.py )
    return str(Path(__file__).parent.parent.parent)


def read_file(path):

    s = ''
    with open(path, 'r') as f:
        lines = f.readlines()
        s = ' '.join(lines)
        return s


def read_yaml(path):

    with open(path, 'r') as file:
        yobj = yaml.safe_load(file)
        return yobj


def read_json(path):

    with open(path, 'r') as file:
        jobj = json.load(file)
        return jobj
    

def remove_file(path):
    
    if os.path.exists(path):
        try:
            os.remove(path)
            return True
        except Exception as e:
            raise e
    else:
        return False