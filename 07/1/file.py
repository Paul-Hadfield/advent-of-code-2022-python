class File:
    def __init__(self, line:str):
        parts = line.split(' ')
        self.name = parts[1]
        self.size =int(parts[0])

    def __repr__(self):
        return f"File - {self.name} ({self.size})"

    def __str__(self):
        return f"File - {self.name}, ({self.size})"