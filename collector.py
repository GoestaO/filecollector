import os
import shutil
from pprint import pprint

class Filecollector:
    def __init__(self, src, dest, filter):
        self.src = src
        self.dest = dest
        self.filter = filter
        self.filelist = []


    '''Recursive search for files'''
    def findAllFiles(self, directory=None):
        if directory == None:
            directory = self.src
        files = os.listdir(directory)
        for f in files:
            file = os.path.join(directory, f)
            if os.path.isfile(file):
            #if os.path.isfile(file) and f.endswith(self.filter):
                self.filelist.append(file)
            if os.path.isdir(file):
                self.findAllFiles(directory=file)

    def filterFiles(self, filelist, filetype):
        return filter(lambda x: x.endswith(filetype), filelist)


    def copyFiles(self, listoffiles=None, destination=None):
        if listoffiles == None:
            listoffiles = self.filelist

        if destination == None:
            destination = self.dest

        if not os.path.exists(destination):
            os.makedirs(destination)

        for f in listoffiles:
            try:
                shutil.copy(f, destination)
            except shutil.SameFileError as e:
                print("{}".format(e))
                continue



if __name__ == '__main__':
    collector = Filecollector('/Users/gostendorf/Downloads', '/Users/gostendorf/Downloads/Testfolder', ".pdf")
    collector.findAllFiles()
    files = collector.filelist
    filteredlist = list(collector.filterFiles(files, ".pdf"))
    collector.copyFiles(filteredlist)