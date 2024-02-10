'''Given an array of with some data integer type values. Write a python programm to sort array values '''
from array import *
#array module has been im imported

array1=array('i',[3,4,6,2,6,8,9])
#array has been created
'''Method 1 by converting array into list and then sort '''
a=array1.tolist()
#array has been coverted to list

a.sort()
#list has been shorted

print(a)

'''Method 2 by comparing each element'''

for i in range (0,len(array1)):
#it runs a loop to comapring the first value
    for j in range(i+1,len(array1)):
       #it runs a loop to compare the second value

       if array1[i]>array1[j]:
           #compares two value
           tem=array1[i]            #temp stores the greater value
           array1[i]=array1[j]      #replacing the short value first index
           array1[j]=tem            #replace the second value to temp
           
print(array1)