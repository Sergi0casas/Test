
class Archivo:

    def __init__(self, weight, type, lenguage):
        self.weight = weight
        self.type = type
        self.lenguage = lenguage

    
    def __str__(self):
        s = f"Program lenguage: {self.lenguage}\nType of file: {self.type}\nWeight: {self.weight}\n"
        return s


class Directory(Archivo):

    def __init__(self):
        self.list = []
        

    def add_file(self, weight, type, lenguage):
        file = Archivo(weight, type, lenguage)
        file.lenguage = lenguage
        file.type = type
        file.lenguage = lenguage
        self.list.append(file)
    
    def __str__(self):
        for i in self.list:
            print(i.__str__())
    
    def user(self, name):
        print("Hello world, jajajajaj ", name)
        print("This a change on branch development ", name)

development = Directory()

development.add_file(12,"TXT","Python")
development.add_file(23,"TXT","C++")
development.add_file(43,"ORG","Js")
development.user("pedro")
development.__str__()