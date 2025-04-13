class Car:
    color="Black"
    
    def __init__(self,name):
        self.name=name

    def start(self):
        print("Car has Started")

    def stop(self):
        print("Car has Stopped")

obj1=Car("BMW")
print(obj1.color)
print(obj1.name)
obj1.start()
obj1.stop()