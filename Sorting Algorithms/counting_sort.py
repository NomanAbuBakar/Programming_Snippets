# For Calculating Simple Frequency of Numbers
def countFrequency(A, C):
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    return C

# For Calculating Commulative Frequency
def comulativeFrequency(C):
    i = 1
    for i in range(1, len(C)):
        C[i] = C[i] + C[i -1]
    return C   

def counting_sort(A):
    # Since max is 9, PC will create array of size 9, actually it's size of 10(0-9)
    rnge = max(A) + 1

    # B array would be used at the end to get value after hashing commulative frequency 
    B = [0] * len(A)

    # C would be used to hold frequency of numbers and their commulative frequency
    C = [0] * rnge

    
    C = countFrequency(A, C)
    C = comulativeFrequency(C)

    # Getting values by hashing commulative frequency
    for i in range(len(A)-1, -1, -1):
        # -1 is again being used because loop start from 0
        B[C[A[i]]-1] = A[i]
        # Reducing commulative frequency after getting value
        C[A[i]] = C[A[i]] -1
        
    return B    


# Testing
A = [5,9,4,5,3,6,8,5,4,8,7,4,6,9,7]
A = counting_sort(A)
print (A)