#Merge Sort
import numpy as np

#Function to sort an array in ascending order
def Amergesort(A, left, right):
    print(A[left:right])
    if left < right:
        mid = int(np.ceil((left+(right-1))/2))
        Amergesort(A, left, mid)
        Amergesort(A, mid+1, right)
        Amerge(A, left, mid, right)
    print(A)
        
def Amerge(A, left, mid, right):
    leftarraysize = mid - left +1
    rightarraysize = right - mid
    
    leftarray = [0] * leftarraysize
    rightarray = [0] * rightarraysize
    
    for i in range(0, leftarraysize):
        leftarray[i] = A[left + i]
        
    for i in range(0, rightarraysize):
        rightarray[i] = A[mid + i + 1]
        
    i = 0
    j = 0
    k = left
    
    while i < leftarraysize and j < rightarraysize:
        if leftarray[i] <= rightarray[j]:
            A[k] = leftarray[i]
            i = i+1
        else:
            A[k] = rightarray[j]
            j = j+1
        k = k+1
        
    while i < leftarraysize:
        A[k] = leftarray[i]
        i = i+1
        k = k+1
    while j < rightarraysize:
        A[k]= rightarray[j]
        j = j+1
        k = k+1
        
A = [100, 2, 100, 1, 3, 4, 18, 55, 0]
Amergesort(A, 0, 8)


#Function to sort an array in descending order
def Dmergesort(A, left, right):
    print(A[left:right])
    if left < right:
        mid = int(np.ceil((left+(right-1))/2))
        Dmergesort(A, left, mid)
        Dmergesort(A, mid+1, right)
        Dmerge(A, left, mid, right)
    print(A)
        
def Dmerge(A, left, mid, right):
    leftarraysize = mid - left +1
    rightarraysize = right - mid
    
    leftarray = [0] * leftarraysize
    rightarray = [0] * rightarraysize
    
    for i in range(0, leftarraysize):
        leftarray[i] = A[left + i]
        
    for i in range(0, rightarraysize):
        rightarray[i] = A[mid + i + 1]
        
    i = 0
    j = 0
    k = left
    
    while i < leftarraysize and j < rightarraysize:
        if leftarray[i] >= rightarray[j]:
            A[k] = leftarray[i]
            i = i+1
        else:
            A[k] = rightarray[j]
            j = j+1
        k = k+1
        
    while i < leftarraysize:
        A[k] = leftarray[i]
        i = i+1
        k = k+1
    while j < rightarraysize:
        A[k]= rightarray[j]
        j = j+1
        k = k+1
        
A = [100, 2, 100, 1, 3, 4, 18, 55, 0]
Dmergesort(A, 0, 8)