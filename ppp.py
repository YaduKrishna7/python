class Area:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        print(self.length*self.width)
A=Area(5,10)
B=Area(20,30)
C=Area(30,20)
A.display()
B.display()
C.display()
