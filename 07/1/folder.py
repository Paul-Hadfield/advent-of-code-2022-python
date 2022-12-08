from __future__ import annotations
from typing import Optional

from file import File

class Folder:
    def __init__(self, name:str, parent: Optional[Folder] = None):
        self.name = name
        self.parent = parent
        self.folders: dict[str, Folder] = {}
        self.files: list[File] = []
        self.totalDirectorySize = 0

    def addFolder(self, dirName: str) -> Folder:
        folder = Folder(dirName, self)
        self.folders[dirName] = folder
        return folder

    def addFile(self, file: File) -> None:
        self.files.append(file)
        self.updateTotalDirectorySize(file.size)

    def updateTotalDirectorySize(self, size: int) -> None:
        self.totalDirectorySize += size
        if self.parent:
            self.parent.updateTotalDirectorySize(size)
