#! /usr/bin/python3
# Functions which searches for compressed files and deletes them

import re
import os


def findCompressedFiles(path):

    filesRegex = re.compile(r'.*\.zip|.*\.rar|.*\.tgz|.*\.tar\.gz')
    compressedFiles = []
    allFiles = os.listdir(path)

    for filename in range(len(allFiles)):

        matchObject = filesRegex.search(allFiles[filename])

        if matchObject != None:
            compressedFiles.append(matchObject.group())

    return compressedFiles


def deleteCompressedFiles(listOfFiles):
    for filename in range(len(listOfFiles)):
        if os.path.exists(listOfFiles[filename]):
            os.remove(listOfFiles[filename])


files = findCompressedFiles(
    '/media/mjgoncalves/hd1/development/python/teste')

print(files)
deleteCompressedFiles(files)
