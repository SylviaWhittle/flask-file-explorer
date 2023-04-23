from pathlib import Path

for entry in Path('./').glob('./*'):
    if entry.is_dir():
        print(f'dir: {entry}')
    else:
        print(f'file: {entry}')
