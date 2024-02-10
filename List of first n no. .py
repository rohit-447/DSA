'''This is a program to  create a list of first n natural no.'''
#list and variable
list1=[]              #Empty list to store value
n=0                   #take the input of upto which the list is created
a=1                   #append the value

#input from user
n=int(input("Enter the no."))

#loop to append the data
for i in range(0, n):
    list1.append(a)
    a=a+1

print(list1)
