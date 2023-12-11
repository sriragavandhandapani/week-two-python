class vechicle:
    def __init__(self,name):
        self.n=name
    def getdetails(self):
        print("Name of the vehicle is",self.n)
class bus(vechicle):
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def getbus(self):
        print("color",self.color)
        print("model",self.model)
b1=bus("volvo","red")
b1.getbus()