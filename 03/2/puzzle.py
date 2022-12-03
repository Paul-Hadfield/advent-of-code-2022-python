from functools import reduce

def splitIntoGroups(groups, contents):
    if len(groups) == 0:
        groups.append([])
    elif len(groups[len(groups)-1]) == 3:
        groups.append([])

    groups[len(groups)-1].append(contents)
    return groups

def getDuplicates(group):
    set1 = set(group[0])
    set2 = set(group[1])
    set3 = set(group[2])
    return set1.intersection(set2).intersection(set3)

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

groups = list(reduce(splitIntoGroups, backpacks, []))
duplicates = list(map(getDuplicates, groups))
priorities = list(map(getPriorities, duplicates))
print(sum(priorities))