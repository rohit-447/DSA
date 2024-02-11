'''This is a program to create class circle with instance object variable radius. Provide setter
   and getter for radius. Also define getArea() and  getCircumference() methods'''

#class creation
class circle:
    def __init__(self,radius):
        self.radius=radius

    def setter(self,radius):
        self.radius=radius

    def getcircumference(self,radius):
        self.radius=radius
        circumference=2*3.14*radius
        print("Circumference of circle with ",radius, "is :" , circumference)

    def getarea(self,radius):
        self.radius=radius
        area=3.14*(radius**2)
        print("Area of circle with ",radius, "is :" ,area)

radius = int(input("Enter the radius of circle : "))
r = circle(radius)
r.getarea(radius)
r.getcircumference(radius)