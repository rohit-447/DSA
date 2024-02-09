'''This is a program to  create a list of first n natural no.'''
#list and variable
list1=[]
n=0
a=1

n=int(input("Enter the no."))
for i in range(0, n):
    list1.append(a)
    a=a+1
print(list1)
