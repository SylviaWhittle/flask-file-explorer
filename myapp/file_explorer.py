import os
from flask import Blueprint, render_template, url_for, request
from pathlib import Path

bp = Blueprint('file_explorer', __name__)

# @bp.route('/')
# def index():
#     # get file structure

#     directories = ['Documents', 'Images', 'Videos', 'Desktop']

#     files = ['file1.txt', 'file2.txt', 'image1.png']

#     return render_template('main-page/index.html', info='info!', files = files, directories = directories)

@bp.route('/', methods=['POST', 'GET'])
def explore():
    requested_dir = request.args.get('path')
    current_path = request.args.get('current_path')

    print('EXPLORE TRIGGERED')
    print(f'requested_dir={requested_dir}')
    print(f'current_path={current_path}')

    if requested_dir is None and current_path is None:
        current_path = Path('./')
    elif requested_dir == '..':
        print(f' back: current path: {current_path} | current path parent: {Path(current_path).parent}')
        current_path = Path(current_path).parent
    else:
        current_path = Path(current_path) / requested_dir

    print(f"current_path: {current_path}")


    directories = []
    files = []

    for entry in current_path.glob('./*'):
        if entry.is_dir():
            print(f'is directory: {str(entry)}')
            directories.append(str(entry.relative_to(current_path)))
        else:
            print(f'is file: {str(entry)}')
            files.append(str(entry.relative_to(current_path)))

    return render_template('main-page/index.html', current_path=current_path.resolve(), files=files, directories=directories)