#Shell Sort

import numpy as np

#Function to sort input array to ascending order
def Ashellsort(A):
    print(A)
    n = len(A)
    gap = int(np.floor(n/2))
    while gap > 0:
        for i in range(n-gap):
            if A[i] >= A[i+gap]:
                A[i], A[i+gap] = A[i+gap], A[i]
            j = i   
            while j-gap >= 0:
                if A[j-gap] >= A[j]:
                    A[j], A[j-gap] = A[j-gap], A[j]
                    j = j-gap
                else:
                    j = 0
        gap = int(np.floor(gap/2))
    print(A)

A = [700, 2, 101, 1, 3, 4, 54, 0,  -3]
Ashellsort(A)

#Function to sort input array to descending order
def Dshellsort(A):
    print(A)
    n = len(A)
    gap = int(np.floor(n/2))
    while gap > 0:
        for i in range(n-gap):
            if A[i] <= A[i+gap]:
                A[i], A[i+gap] = A[i+gap], A[i]
            j = i   
            while j-gap >= 0:
                if A[j-gap] <= A[j]:
                    A[j], A[j-gap] = A[j-gap], A[j]
                    j = j-gap
                else:
                    j = 0
        gap = int(np.floor(gap/2))
    print(A)

A = [700, 2, 101, 1, 3, 4, 54, 0,  -3]
Dshellsort(A)