#! /usr/bin/python3
# A function that returns all movies or folders containing movies of a given directory

import os
import re


def listDownloadedMovies(path):

    foldersList = []
    moviesList = []
    unfinishedDownloads = []

    os.chdir(targetFolder)
    foldersContent = os.listdir(targetFolder)
    extensionsRegex = re.compile(r'.*\.avi|.*\.mkv|.*\.mp4')

    for item in range(len(foldersContent)):
        if os.path.isdir(foldersContent[item]):
            foldersList.append(foldersContent[item])

        matchObject = extensionsRegex.search(foldersContent[item])

        if matchObject != None:
            moviesList.append(matchObject.group())

    for folder in range(len(foldersList)):
        for foldername, _, filenames in os.walk(foldersList[folder]):
            for filename in range(len(filenames)):

                matchObject = extensionsRegex.search(filenames[filename])

                if matchObject != None and foldername not in moviesList:
                    moviesList.append(foldername)

                if filenames[filename].endswith('.part'):
                    unfinishedDownloads.append(foldername)

    for downloads in range(len(unfinishedDownloads)):

        if unfinishedDownloads[downloads] in moviesList:
            moviesList.remove(unfinishedDownloads[downloads])

    return moviesList


targetFolder = '/media/mjgoncalves/hd1/development/python/donwloads'
listOfmovies = listDownloadedMovies(targetFolder)
print(listOfmovies)
