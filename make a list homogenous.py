'''This is a program to remove all the non integer values from a list'''
list1=['a','b',1,3,5,'d']
list2=[]
#list has been creatred

for i in list1:
    if type(i)==int:
        #compare data type

        list2.append(i)
        #crete a second list with same data type

#print the commonlist
list1=list(set(list1) & set(list2))
print(list1)