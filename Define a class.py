'''Python class Person with instance object variable name and age. Set instance object 
variable in __init__() method. Also define show() method to display name and age of person'''

#class creation
class person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

              #receive the data
    def setdata(self,name,age):
        self.name=name
        self.age=age
    
              #returing the data value
    def show(self,name,age):
        return self.age , self.name

t1=person('ram',50)
t2=person()
t2.setdata('shyam',25)
print(t1.show(t1.name,t1.age))
print(t2.show(t2.name,t2.age))