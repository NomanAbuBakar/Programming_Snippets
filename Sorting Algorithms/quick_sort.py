# Best/Average Case Time Complexity Big O(nlogn)
# Worst Case Big O of n square but it could be avoided by randomized Quick Sort
def partition(Arr, start, end):
    pivot_value = Arr[end]
    pivot_index = start

    for i in range(start, end):
        if Arr[i] <= pivot_value:
            temp = Arr[pivot_index]
            Arr[pivot_index] = Arr[i]
            Arr[i] = temp
            pivot_index = pivot_index + 1

    temp = Arr[pivot_index]
    Arr[pivot_index] = Arr[end]
    Arr[end] = temp

    return pivot_index 

def quickSort(Arr, start, end):
    if start < end:    
        pivot_index = partition(Arr, start, end)
        quickSort(Arr, start, pivot_index-1)
        quickSort(Arr, pivot_index+1, end)

#Testing
A = [7,2,1,6,8,5,3,4]
quickSort(A, 0, (len(A)-1))
print(A)

       