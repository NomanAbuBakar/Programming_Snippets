# Time Complexity  = Big O of n square.
# Space Complexity = n
# In Place Algorithm, meaning no need of extra memory

def simpleBubbleSort(arr):
    
    for i in range(0, (len(arr) - 1)): # 0 to n-2 loop
        for j in range(0, (len(arr) - 2)): 
            if arr[j] > arr[j+1]:
                # Swap
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp         
    
    return arr

# It will avoid check the last sorted elements in nested loop
def modifiedBubbleSort(arr):
    avoidingSortedArray = 1

    for i in range(0, (len(arr) - 1)): # 0 to n-2 loop
        for j in range(0, (len(arr) - avoidingSortedArray)): 
            if arr[j] > arr[j+1]:
                # Swap
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        avoidingSortedArray = avoidingSortedArray + 1         
    return arr

# It will avoid check the last sorted elements in nested loop and will check if any pass goes without any swap then terminate the sorting means array is already sorted
# Best Case for this Algo would O(n)
def furtherModifiedBubbleSort(arr):
    avoidingSortedArray = 1
    isSwap = False

    for i in range(0, (len(arr) - 1)): # 0 to n-2 loop
        for j in range(0, (len(arr) - avoidingSortedArray)): 
            if arr[j] > arr[j+1]:
                isSwap = True
                # Swap
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

        avoidingSortedArray = avoidingSortedArray + 1        
        if isSwap == False:
            return arr        
                 
    return arr

arr = [2,3,4,1,9,8,6,5]
print("Given Array : ")
print(arr)

sorted_array = simpleBubbleSort(arr)
print("Sorted Array from Simple Bubble Sort : ")
print(sorted_array)

sorted_array = modifiedBubbleSort(arr)
print("Sorted Array from Modified Bubble Sort: ")
print(sorted_array)
             
sorted_array = furtherModifiedBubbleSort(arr)
print("Sorted Array from Further Modified Bubble Sort: ")
print(sorted_array)             