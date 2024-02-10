'''This is a python program to print first n Fibonacci Series'''

#list and varibale
list_1=[0]
n=0
n1,n2=0,1
#input
n = int(input("Enter the no. for first n Fibonacci Series : "))

#loop to add Fibonacci numbers
if n==2:
        list_1=[0,1]

for i in range (2,n):
      n3=n1+n2
      list_1.append(n3)
      n1=n2
      n2=n3

print(list_1)