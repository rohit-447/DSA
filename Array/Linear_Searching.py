##time complexity: O(n)
# Space complexity: O(1)
# Linear Search Algorithm
def Linear_Search(array,search):
    if len(array)==0:
        print("array is empty")
    for i in range (len(array)):
        if array[i]==search:
            print("Element is at index:",i)
            return i
        else:
            continue
    return -1


#array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search=3
#function Call
Linear_Search(array, search)