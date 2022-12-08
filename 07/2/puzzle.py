from folderUtils import getAllFolders
from folder import Folder
from file import File

def getFolderSize(folder: Folder) -> int:
    return folder.totalDirectorySize

with open('data.txt') as f:
    output = f.read().splitlines()

root = Folder('/')
current: Folder = root

readingADirectory = False
for line in output:
    if line == "$ ls":
        readingADirectory = True
    elif line == "$ cd ..":
        readingADirectory = False
        if current.parent:
            current = current.parent
    elif line.startswith('$ cd '):
        readingADirectory = False        
        dir = line[5:]
        if dir == '/':
            current = root
        else: 
            current = current.folders[dir]
    elif readingADirectory:
        if line.startswith('dir '):
            dir = line[4:]
            current.addFolder(dir)
        else:
            current.addFile(File(line))
    else:
        raise NameError('Unknown line')

available = 70000000 - root.totalDirectorySize
needed = 30000000 - available

folders = filter(lambda x:(x.totalDirectorySize > needed), getAllFolders(root))
folderSizes: list[int] = list(map(getFolderSize, folders))

print(min(folderSizes))