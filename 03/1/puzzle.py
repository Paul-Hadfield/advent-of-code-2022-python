def splitContents(contents):
    midPoint = int(len(contents) / 2)
    compartment1 = contents[0:midPoint]
    compartment2 = contents[midPoint:]
    return {"compartment1": compartment1,"compartment2":compartment2}

def getDuplicates(backpack):
    set1 = set(backpack["compartment1"])
    set2 = set(backpack["compartment2"])
    return set1.intersection(set2)

def getPriorities(duplicates):
    if len(duplicates) != 1:
        raise NameError('Not handled')

    duplicate = ord(list(duplicates)[0])
    if(duplicate >= 97):
        return duplicate - 96
    else:
        return duplicate - 38
    
with open('data.txt') as f:
    backpacks = f.read().splitlines()

contents = list(map(splitContents, backpacks))
duplicates = list(map(getDuplicates, contents))
priorities = list(map(getPriorities, duplicates))
print(sum(priorities))