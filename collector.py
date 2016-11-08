import os
from pprint import pprint
import shutil

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
            if os.path.isfile(file) and f.endswith(self.filter):
                self.filelist.append(file)
            if os.path.isdir(file):
                self.findAllFiles(directory=file)

    def copyFiles(self, listoffiles=None, destination=None):
        if listoffiles == None:
            listoffiles = self.filelist

        if destination == None:
            destination = self.dest

        for f in listoffiles:
            shutil.copy(f, destination)

if __name__ == '__main__':
    collector = Filecollector('/Users/gostendorf/Downloads', '/Users/gostendorf/Downloads/Testfolder', ".pdf")
    collector.findAllFiles()
    collector.copyFiles()
    #pprint(collector.filelist)