# Time Complexity  = Big O of n square.
# Space Complexity = n
# In Place Algorithm, meaning no need of extra memory

def selectionSort(arr):
    for i in range(0, (len(arr) - 2)):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = temp
    return arr

arr = [2,3,4,1,9,8,6,5]
print("Given Array : ")
print(arr)

sorted_array = selectionSort(arr)
print("Sorted Array : ")
print(sorted_array)

             