from __future__ import annotations
from folder import Folder

def printTree(folder: Folder, depth:int = 0) -> None:
    print(f'Folder: {folder.name} ({folder.totalDirectorySize})')
    for childFolder in folder.folders:
        printTree(folder.folders[childFolder], depth + 1)
    for file in folder.files:
        print(file)

def getAllFolders(folder: Folder) -> list[Folder]:
    folders:list[Folder] = []
    folders.append(folder)
    for key in folder.folders:
        for childFolder in getAllFolders(folder.folders[key]):
            folders.append(childFolder)
    return folders