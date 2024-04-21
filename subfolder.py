import os

root_dir = '/path/to/your/folder'

for root, dirs, files in os.walk(root_dir):
    # Modify dirs in-place to skip unwanted directories
    dirs[:] = [d for d in dirs if 'temp' not in d]

    print(f"Currently in directory: {root}")
    for dir in dirs:
        print(f"Subfolder: {dir}")
    for file in files:
        print(f"File: {file}")
