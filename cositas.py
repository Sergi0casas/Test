
class archivo:

    def __init__(self, weight, type, lenguage):
        self.weight = weight
        self.type = type
        self.lenguage = lenguage

    
    def __str__(self):
        s = f"Program lenguage: {self.lenguage}\nType of file: {self.type}\nWeight: {self.weight}"
        return s


class directory(archivo):

    def __init__(self, weight, n_files):
        