# Time Complexity  = Big O of n square and linear for Best Case scenerio 
# Space Complexity = n
# In Place Algorithm, meaning no need of extra memory

def insertionSort(arr):
    for i in range(0, (len(arr))):
        value = arr[i]
        hole = i
        
        while hole > 0 and arr[hole-1] > value:
            arr[hole] = arr[hole-1]
            hole = hole - 1 
                
        arr[hole] = value    
        
    return arr

arr = [2,3,4,1,9,8,6,5]
print("Given Array : ")
print(arr)

sorted_array = insertionSort(arr)
print("Sorted Array : ")
print(sorted_array)

             