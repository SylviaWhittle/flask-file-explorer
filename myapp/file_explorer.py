import os
from flask import Blueprint, render_template, url_for, request, jsonify
from pathlib import Path
from pprint import pprint
import json
import time

bp = Blueprint('file_explorer', __name__)

# @bp.route('/')
# def index():
#     # get file structure

#     directories = ['Documents', 'Images', 'Videos', 'Desktop']

#     files = ['file1.txt', 'file2.txt', 'image1.png']

#     return render_template('main-page/index.html', info='info!', files = files, directories = directories)


def list_directory(requested_dir: str, current_path: str):

    print('---- processing directory ----')
    print(f'requested_dir {requested_dir}')
    print(f'current_path: {current_path}')

    if requested_dir == 'None' or requested_dir == 'undefined':
        requested_dir = None
    if current_path == 'None' or current_path == 'undefined':
        current_path = None

    if requested_dir is None and current_path is None:
        print('requested_dir and current_path both None')
        current_path = Path('./')
    elif current_path is None:
        print('current_path is None')
        raise ValueError('current_path can not be None if requested_dir is not None')
    elif requested_dir == '..':
        print(f' back: current path: {current_path} | current path parent: {Path(current_path).parent}')
        current_path = Path(current_path).parent
    else:
        print('entering sub-directory')
        current_path = Path(current_path) / requested_dir
        print(f'sub directory: {current_path}')
    
    # find files and directories in current path
    directories = []
    files = []

    for entry in current_path.glob('./*'):
        if entry.is_dir():
            print(f'is directory: {str(entry)}')
            directories.append(str(entry.relative_to(current_path)))
        else:
            print(f'is file: {str(entry)}')
            files.append(str(entry.relative_to(current_path)))

    print('----                 ----')

    return str(current_path.resolve()), files, directories



@bp.route('/', methods=['POST', 'GET'])
def explore():
    requested_dir = request.args.get('path')
    current_path = request.args.get('current_path')

    print('EXPLORE TRIGGERED')
    print(f'requested_dir={requested_dir}')
    print(f'current_path={current_path}')

    current_path, files, directories = list_directory(requested_dir=requested_dir, current_path=current_path)

    return render_template('main-page/index.html', current_path=current_path, files=files, directories=directories)


@bp.route('/get-data', methods=['POST', 'GET'])
def get_data():
    print('GET-DATA TRIGGERED')
    request_json = request.get_json()
    print(f'request json: {request_json}')

    requested_dir = str(request_json['requested_dir'])
    print(f'input requested dir: {requested_dir}')
    current_path = str(request_json['current_path'])
    print(f'input current_path: {current_path}')
    
    current_path, files, directories = list_directory(requested_dir=requested_dir, current_path=current_path)

    data = {
        "current_path": current_path,
        "files": files,
        "directories": directories
    }

    print('sending data:')
    print(data)

    return jsonify(data)

@bp.route('/load-config', methods=['POST', 'GET'])
def load_config():

    # get path to config

    # verify config path

    # generate config (if needed)

    # open config file

    # return config file contents

    pass

@bp.route('/update-config', methods=['POST'])
def update_config():

    # get updated config
    config = request.form['config']
    print(f'received config: {config}')

    # open config file

    # clear config file

    # add updated config

    # save config file

    return f'received config: {config}'

@bp.route('/run', methods=['POST', 'GET'])
def run():

    # check input directory

    # check 

    pass