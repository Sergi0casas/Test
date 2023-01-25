
class Archivo:

    def __init__(self, weight, type, lenguage, name):
        self.weight = weight
        self.type = type
        self.lenguage = lenguage
        self.name = name

    
    def __str__(self):
        s = f"{self.name}\nProgram lenguage: {self.lenguage}\nType of file: {self.type}\nWeight: {self.weight}\n"
        return s


class Directory(Archivo):

    def __init__(self):
        self.list = []
        

    def add_file(self, name, weight, type, lenguage):
        file = Archivo(name, weight, type, lenguage)
        file.name = name
        file.lenguage = lenguage
        file.type = type
        file.lenguage = lenguage
        self.list.append(file)

    def delete_user(self,user):
        if user in self.list:
            self.list.remove(user)
    
    def __str__(self):
        for i in self.list:
            print(i.__str__())
    
    def user(self, name):
        print("Hello world mi leader you are the beest of the world MR. ", name)
        print("This a change on branch development in github ", name)
        print("This is a change of branch origin")
        print("Gomy Gomy this is a gomy")

development = Directory()

development.add_file("juego.py",12,"TXT","Python")
development.add_file("algoritmo.cpp", 23,"TXT","C++")
development.add_file("web.js", 43,"ORG","Js")
development.user("pedro")
development.__str__()
