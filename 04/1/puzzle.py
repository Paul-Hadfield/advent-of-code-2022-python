from functools import reduce
def parsePart(part):
    bounds = part.split('-')
    return set(range(int(bounds[0]), int(bounds[1]) + 1))

def findEncompassing(encompassing, line):
    parts = line.split(',')
    part1 = parsePart(parts[0])
    part2 = parsePart(parts[1])
    if part1.issubset(part2) or part2.issubset(part1):
        encompassing.append(line)

    return encompassing

with open('data.txt') as f:
    lines = f.read().splitlines()

print(len(reduce(findEncompassing, lines, [])))