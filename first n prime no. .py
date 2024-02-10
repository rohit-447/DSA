'''This is a program to create list of first n prime natural no'''

#variable and list
list_1=[]               #variable to store value
n=0                     ##take the input of upto which the list is created

#input from user
n=int(input("Enter the no. upto which prime no. u want :"))

#loop to check prime no.
for num in range(0,n+1):
    if num>1:
        for i in range (2,num):
            if num%i==0:
                break
        else:
          list_1.append(num)

print(list_1)