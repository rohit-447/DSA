'''This is a program to create a Rectangle class with length and breadth its instance objec t
   variable .Provide setdimensions() ,shoedimensions() and getarea()'''

class Rectangle:
    def __init__(self,length=0,breadth=0):
        self.length  = length
        self.breadth = breadth


    def setdimensions(self,length,breadth):
        self.length  = length
        self.breadth = breadth
        return length, breadth


    def showdimension(self,length,breadth):
        print("Length of Rectangle is ",length)
        print("Length of Rectangle is ",breadth)

    def getarea(self,length,breadth):
        Rectangle.showdimension(self,length,breadth)
        area=length*breadth
        print("Area of rectangle is : ",area)
        
length  = int(input("Enter the length of rectangle : "))
breadth = int(input("Enter the breadth of rectangle : "))

t1=Rectangle()
t1.setdimensions(length,breadth)
t1.getarea(length,breadth)
