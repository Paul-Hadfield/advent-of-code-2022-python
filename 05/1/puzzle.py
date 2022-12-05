from functools import reduce
from instruction import Instruction

def readStartingState(data: list[str]) -> dict[int, list[str]]:
    stackHeight = 0
    while(data[stackHeight].startswith(" 1 ") == False):        
        stackHeight += 1
    numberOfStacks = int((len(data[stackHeight])+1)/4)

    heightIndex = stackHeight - 1

    stacks: dict[int, list[str]] = {}    
    while heightIndex >=0:        
        stackIndex = 0
        while stackIndex < numberOfStacks:

            value = data[heightIndex][(stackIndex * 4) + 1:(stackIndex * 4) + 2]
            if value != ' ':
                stack = stacks.get(stackIndex)
                if stack == None:
                    stack = []
                    stacks[stackIndex] = stack           

                stack.append(value)    

            stackIndex += 1
        heightIndex -= 1

    return stacks

def readInstructions(data: list[str]) -> list[Instruction]:
    
    processingInstructions = False        
    instructions: list[Instruction] = []
    index = 1
    for line in data:
        if line == '':
            processingInstructions = True
        elif processingInstructions: 
            instructions.append(Instruction(index, line))
            index += 1

    #instructions.sort(key=lambda x:x.index)
    return instructions

def applyInstructions(crates: dict[int, list[str]], instruction: Instruction) -> dict[int, list[str]]:
    index = 0
    while(index < instruction.howMany):
        fromStack = crates.get(instruction.fromStack-1)
        if fromStack != None:
            crate = fromStack.pop()
            toStack = crates.get(instruction.toStack-1)
            if toStack != None:
                toStack.append(crate)
        index += 1
    return crates

with open('data.txt') as f:
    lines = f.read().splitlines()

crates = readStartingState(lines)
instructions = readInstructions(lines)
crates = reduce(applyInstructions, instructions, crates)

topCrates = ''
for index in crates:
    stack = crates[index]
    if stack:
        topCrates += stack[len(stack)-1]

print(topCrates)