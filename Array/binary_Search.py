# Binary Search Algorithm
# Time Complexity: O(log n)
# Space Complexity: O(1)
def binary_Search(Array, search, low, high):
   
   #shorting of the array
    Array.sort()
    while low<= high:
        mid= low +(high -low)//2
        if search==Array[mid]:
            return mid
        
        #right search of array
        elif search > Array[mid]:
            #Recurssion call for right side of the array
            return binary_Search(Array, search, mid+1, high)

            #without the recursion 
            #low =mid +1
        
        #left search of array
        else:
            #recurssion call for left side of the array
            return binary_Search(Array,search, low , mid-1)
        
            #without the recursion
            #high = mid -1

    #if element is not found
    return -1





#array
Array= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#search element
search =10
#low and high bound
low = 0
high=len(Array)-1
if len(Array)==0:
    print("Array is empty")
    exit()
# Binary Search Algorithm
result=binary_Search(Array,search,low ,high)
print("Element is present at the index",result)