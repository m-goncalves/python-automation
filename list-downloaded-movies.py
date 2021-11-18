#! /usr/bin/python3
# A function that returns all movies or folders containing movies of a given directory

import os
import re


def listDownloadedMovies(path):

    foldersList = []
    moviesList = []
    count = 0

    os.chdir(targetFolder)
    foldersContent = os.listdir(targetFolder)
    extensionsRegex = re.compile(r'.*\.avi|.*\.mkv|.*\.mp4')

    for item in range(len(foldersContent)):
        if os.path.isdir(foldersContent[item]):
            foldersList.append(foldersContent[item])

        matchObjetc = extensionsRegex.search(foldersContent[item])

        if matchObjetc != None:
            moviesList.append(matchObjetc.group())

    while count < len(foldersList):
        for foldername, _, filenames in os.walk(foldersList[count]):
            for filename in range(len(filenames)):
                if filenames[filename].endswith('.part'):
                    continue

                matchObjetc = extensionsRegex.search(filenames[filename])

                if matchObjetc != None:
                    moviesList.append(foldername)

        count += 1
    return moviesList


targetFolder = '/media/mjgoncalves/hd1/development/python/donwloads'
listOfmovies = listDownloadedMovies(targetFolder)
print(listOfmovies)
