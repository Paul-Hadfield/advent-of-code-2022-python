class Instruction:
    def __init__(self, index:int, data: str):
        
        self.index = index

        parts = data.replace("move ", "").replace(" from ", "|").replace(" to ", "|").split('|')
        self.howMany = int(parts[0])
        self.fromStack = int(parts[1])
        self.toStack = int(parts[2])

    def __repr__(self):
        return f"Instruction: {self.index} - howMany:{self.howMany} fromStack:{self.fromStack} toStack:{self.toStack}"

    def __str__(self):
        return f"Instruction: {self.index} - howMany:{self.howMany} fromStack:{self.fromStack} toStack:{self.toStack}"