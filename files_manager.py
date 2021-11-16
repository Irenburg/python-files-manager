#! /usr/bin/python
# files_manager.py - Orgnize files of the given folder.

import sys, os, shutil, pyperclip

# Files classes.
CLASSES = ('Documents', 'Compressed', 'Programs', 'Videos', 'Music','Images')
DOCUMENTS, COMPRESSED, PROGRAMS, VIDEOS, MUSIC, IMAGES =  CLASSES

class FileTypes:
    """ Add more types here """
    DOCUMENTS = ('.pdf', '.txt', '.odt', '.docx')
    COMPRESSED = ('.zip', '.rar', '.tar', '.7z', '.tar.gz', '.tar.xz')
    PROGRAMS = ('.deb', '.rpm', '.exe', '.AppImage')
    VIDEOS = ('.mp4', '.mkv')
    MUSIC = ('.mp3',)
    IMAGES = ('.png', '.jpg', '.jpeg', '.svg')


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
    
    if file.endswith(FileTypes.DOCUMENTS):
        print('Moving %s to %s...' % (file, DOCUMENTS))
        shutil.move(file_path, os.path.join(folder_path, DOCUMENTS))
    if file.endswith(FileTypes.COMPRESSED):
        print('Moving %s to %s...' % (file, COMPRESSED))
        shutil.move(file_path, os.path.join(folder_path, COMPRESSED))
    if file.endswith(FileTypes.PROGRAMS):
        print('Moving %s to %s...' % (file, PROGRAMS))
        shutil.move(file_path, os.path.join(folder_path, PROGRAMS))
    if file.endswith(FileTypes.VIDEOS):
        print('Moving %s to %s...' % (file, VIDEOS))
        shutil.move(file_path, os.path.join(folder_path, VIDEOS))
    if file.endswith(FileTypes.MUSIC):
        print('Moving %s to %s...' % (file, MUSIC))
        shutil.move(file_path, os.path.join(folder_path, MUSIC))
    if file.endswith(FileTypes.IMAGES):
        print('Moving %s to %s...' % (file, IMAGES))
        shutil.move(file_path, os.path.join(folder_path, IMAGES))


print('Done!')
