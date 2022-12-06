
with open('data.txt') as f:
    data = f.read()

index = 0
packetLength = len(data)
buffer: list[str] = []
while index < packetLength:
    buffer.append(data[index])
    if len(buffer) > 4:
        buffer.pop(0)
        print(buffer)
        uniqueChars = set(buffer)
        if len(uniqueChars) == 4:
            print(index + 1)
            break
    index += 1