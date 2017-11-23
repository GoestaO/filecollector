import os
import shutil


def findAllFiles(directory):
    filelist = []
    files = os.listdir(directory)
    for f in files:
        file = os.path.join(directory, f)
        if os.path.isfile(file):
            filelist.append(file)
        if os.path.isdir(file):
            find_files(directory=file, filelist=filelist)
    return filelist


def find_files(directory, filelist):
    files = os.listdir(directory)
    for f in files:
        file = os.path.join(directory, f)
        if os.path.isfile(file):
            filelist.append(file)
        if os.path.isdir(file):
            find_files(directory=file, filelist=filelist)


def showFilteredFiles(src, filetype):
    all_files = findAllFiles(directory=src)
    filtered_files = filterFiles(filelist=all_files, filetype=filetype)
    return filtered_files


def filterFiles(filelist, filetype):
    return list(filter(lambda x: x.endswith(filetype), filelist))


def copyFiles(file_list=None, destination=None):
    if not os.path.exists(destination):
        os.makedirs(destination)
    for f in file_list:
        try:
            shutil.copy(f, destination)
        except shutil.SameFileError as e:
            print("{}".format(e))
            continue


def consolidate(src, filetype, dest):
    filtered_files = showFilteredFiles(src=src, filetype=filetype)
    copyFiles(filtered_files)
