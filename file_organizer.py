import os
import shutil
def fileOrganizer(path):
    list_of_files = os.listdir(path)
    for file in list_of_files:
        fileName, ext = os.path.splitext(file)
        ext = ext[1:]
        if ext == '':
            continue

        if os.path.exists(path + '/' + ext):
            shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
        else:
            os.makedirs(path + '/' + ext)
            shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
            print(f"Moved {file} successfully to {path + '/' + ext + '/' + file}")
while True:
    print('This is a file organizer to sort your messed up files. | File Organizer 1.0 by Alvi')
    path = input('Enter Your Messed Up path/directory:\n')
    fileOrganizer(path)
    print('Take a look at your organized files now. \n')