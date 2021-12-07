#! /usr/bin/python3
# A function that returns all movies or folders containing movies of a given directory

import os
import re
import shutil


def listDownloadedMovies(path):

    foldersList = []
    moviesList = []
    unfinishedDownloads = []

    os.chdir(downloadsFolder)
    foldersContent = os.listdir(downloadsFolder)
    extensionsRegex = re.compile(r'.*\.avi|.*\.mkv|.*\.mp4')

    # Loops through foldersContent and adds directories to
    # foldersList and movies to moviesList.

    for item in range(len(foldersContent)):
        if os.path.isdir(foldersContent[item]):
            foldersList.append(foldersContent[item])

        matchObject = extensionsRegex.search(foldersContent[item])

        if matchObject != None:
            moviesList.append(matchObject.group())

    # Loops through foldersList and checks to see which folders contains
    # finished movie downloads and adds them to moviesList. Unfinished movie
    # downloads are added to unfinishedDownloads.

    for folder in range(len(foldersList)):
        for foldername, _, filenames in os.walk(foldersList[folder]):
            for filename in range(len(filenames)):

                matchObject = extensionsRegex.search(filenames[filename])

                if matchObject != None and foldername not in moviesList:
                    moviesList.append(foldername)

                if filenames[filename].endswith('.part'):
                    unfinishedDownloads.append(foldername)

    # Checks to see if there are folders with unfinished downloads in
    # in the moviesList and removes them.

    for downloads in range(len(unfinishedDownloads)):
        if unfinishedDownloads[downloads] in moviesList:
            moviesList.remove(unfinishedDownloads[downloads])

    return moviesList

# Moves completely donwloaded movies to a specified folder


def moveFiles(destinationFolder, moviesList):

    os.chdir(downloadsFolder)
    for movie in range(len(moviesList)):
        shutil.move(moviesList[movie], destinationFolder)


downloadsFolder = '/media/mjgoncalves/hd1/development/python/donwloads'
destinationFolder = '/media/mjgoncalves/hd1/development/python/destination'
listOfmovies = listDownloadedMovies(downloadsFolder)
moveFiles(destinationFolder, listOfmovies)
