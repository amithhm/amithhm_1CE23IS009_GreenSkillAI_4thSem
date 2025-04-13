class Box:
    def __init__(self,w,d,h):
        self.w=w
        self.d=d
        self.h=h
    def volume(self): #Method Overridden
        v=self.w*self.d*self.h
        print(f"The Volume = {v}")
class Amazon(Box):
    def volume(self):
        v=self.w*self.d*self.h
        print(f"The Volume = {v} cubic cm")
    def display(self):
        print(f"Width = {self.w} cm\nHeight = {self.h} cm\nDepth = {self.d} cm")

a=Amazon(8,3,4)
a.display()
a.volume()

'''OUTPUT:
Width = 8 cm 
Height = 4 cm
Depth = 3 cm 
The Volume = 96 cubic cm
'''
    