def check(name):
    if name=="city123":
        return True

def display():
    name=input("Enter name: ")
    if check(name):
        print("Good Morning",name)

display()