#! /usr/bin/python
# files_manager.py - Orgnize files of the given folder.

import sys, os, shutil, pyperclip

# Files classes.
CLASSES = ('Documents', 'Compressed', 'Programs', 'Videos', 'Music','Images')
DOCUMENTS, COMPRESSED, PROGRAMS, VIDEOS, MUSIC, IMAGES =  CLASSES

# Get the folder path.
if len(sys.argv) > 1:
    folder_path = sys.argv[1]
else:
    folder_path = pyperclip.paste()
folder_path = os.path.abspath(folder_path)

# Check folder path validity.
if not os.path.exists(folder_path):
    print('Invalid folder path.')
    sys.exit(1)

# Check classes availability.
for c in CLASSES:
    class_folder = os.path.join(folder_path, c)
    if os.path.exists(class_folder):
        print(c + ' Folder found.')
    else:
        print('Making directory for %s' % c)
        os.mkdir(class_folder)

# All files list.
files = os.listdir(folder_path)

# Loop through all files and move every file according to its extension.
for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isdir(file_path):
        continue
    
    if file.endswith('.pdf') or file.endswith('.txt') or file.endswith('.odt') or file.endswith('.docx'):
        print('Moving %s to %s...' % (file, DOCUMENTS))
        shutil.move(file_path, os.path.join(folder_path, DOCUMENTS))
    elif file.endswith('.zip') or file.endswith('.rar') or file.endswith('.tar') or file.endswith('.tar.gz') or file.endswith('.tar.xz'):
        print('Moving %s to %s...' % (file, COMPRESSED))
        shutil.move(file_path, os.path.join(folder_path, COMPRESSED))
    elif file.endswith('.deb') or file.endswith('.rpm') or file.endswith('.exe') or file.endswith('.AppImage'):
        print('Moving %s to %s...' % (file, PROGRAMS))
        shutil.move(file_path, os.path.join(folder_path, PROGRAMS))
    elif file.endswith('.mp4') or file.endswith('.mkv'):
        print('Moving %s to %s...' % (file, VIDEOS))
        shutil.move(file_path, os.path.join(folder_path, VIDEOS))
    elif file.endswith('.mp3'):
        print('Moving %s to %s...' % (file, MUSIC))
        shutil.move(file_path, os.path.join(folder_path, MUSIC))
    elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.svg'):
        print('Moving %s to %s...' % (file, IMAGES))
        shutil.move(file_path, os.path.join(folder_path, IMAGES))
print('Done!')
