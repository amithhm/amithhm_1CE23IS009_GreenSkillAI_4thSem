from abc import ABC,abstractmethod

class Animals(ABC):
    @abstractmethod
    def heart_chambs(self):
        pass

class Fish(Animals):
    def heart_chambs(self):
        return 2

class Frog(Animals):
    def heart_chambs(self):
        return 3
    
class Human(Animals):
    def heart_chambs(self):
        return 4

f2=Fish()
f3=Frog()
h4=Human()

print(f"Fish has {f2.heart_chambs()} chambers")
print(f"Frog has {f3.heart_chambs()} chambers")
print(f"Human has {h4.heart_chambs()} chambers")

'''OUTPUT:
Fish has 2 chambers
Frog has 3 chambers
Human has 4 chambers
'''