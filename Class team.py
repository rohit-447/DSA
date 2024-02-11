'''This is program to create a class team with instance object variable a list of member names.
    Provide method to input member names and display member names'''
p_list=[]
name=''
#class created
class team:
    p_list=[]
    def __init__(self,name,p_list):
        self.p_list=p_list
        self.name=name

    def entry_names(self):
        def entry(self):
            en=''
            en=input("Do u want to enter names (y/n):")
            if en.upper()=='Y':
                name=input("Enter the name :")
                p_list.append(name)
                entry(self)
            else:
             return self.p_list
        entry(self)
        


    def display(self):
        print("list of members are : ",self.p_list)

p=team(name,p_list)
p.entry_names()
p.display()