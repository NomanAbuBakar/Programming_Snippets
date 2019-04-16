# ---------------------------------|-MERGE SORT-|------------------------------------
# Code written in just more simpler way for easy Understanding
def mergeSort(Arr):
    size_Arr = len(Arr)

    if size_Arr < 2:
        return Arr

    mid = int(size_Arr / 2)

    Left = [0] * mid
    Right = [0] * (size_Arr - mid)

    for i in range(0, mid):
        Left[i] = Arr[i] 

    
    for i in range(mid, size_Arr):
        Right[i-mid] = Arr[i]    

    Left = mergeSort(Left)
    Right = mergeSort(Right)
    return merge(Left, Right)

# -----------------------------------------------------------------------------------------
# Efficiently written code using Python Tactics :)
def mergeSortEfficientWritten(Arr):
    size_Arr = len(Arr)

    if size_Arr < 2:
        return Arr

    mid = int(size_Arr / 2)

    Left = mergeSort(Arr[:mid])
    Right = mergeSort(Arr[mid:])
    return merge(Left, Right)

# -----------------------------------------------------------------------------------------
# Just to Merge any two give Arrays ...
def merge(left, right):
    size_L = len(left)
    size_R = len(right)
    arr = []

    i=0
    j=0
    k=0

    while (i < size_L and j < size_R):
        if (left[i] <= right[j]):
            arr.append(left[i])
            i = i + 1
            
        else:
            arr.append(right[j])
            j = j + 1
            
    while (i < size_L):
        arr.append(left[i])
        i = i + 1

    while (j < size_R):
        arr.append(right[j])
        j = j + 1
        
    return arr         

# -----------------------------------------------------------------------------------------
# Testing ...
A = [2,4,1,6,8,5,3,7]

print("Merged Sorted From Simple One : ", mergeSort(A))
print("Merged Sorted From Second One : ", mergeSortEfficientWritten(A))
