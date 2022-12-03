from functools import reduce

def getElvesFood(elvesFood, line):
    if(line == ''):
        elvesFood.append(0)
    else:
        pos = len(elvesFood) - 1
        if(pos < 0):
            pos = 0
            elvesFood.append(0)

        elvesFood[pos] = elvesFood[pos] + int(line)
    return elvesFood

with open('data.txt') as f:
    lines = f.read().splitlines()
elvesFood = reduce(getElvesFood, lines, [])

print(max(elvesFood))