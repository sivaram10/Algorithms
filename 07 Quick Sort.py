#Quick Sort

#This will sort array A in ascending order
def Aquicksort(A, start, end):
    if start < end:
        pindex = Apartition(A, start, end)
        Aquicksort(A, start, pindex-1)
        Aquicksort(A, pindex+1, end)

def Apartition(A, start, end):
    pivot = A[end]
    pindex = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[pindex] = A[pindex], A[i]
            pindex = pindex+1
    A[pindex], A[end] = A[end], A[pindex]
    return pindex

#This will sort array A in descending order
def Dquicksort(A, start, end):
    if start < end:
        pindex = Dpartition(A, start, end)
        Dquicksort(A, start, pindex-1)
        Dquicksort(A, pindex+1, end)    
 
def Dpartition(A, start, end):
    pivot = A[end]
    pindex = start
    for i in range(start, end):
        if A[i] >= pivot:
            A[i], A[pindex] = A[pindex], A[i]
            pindex = pindex+1
    A[pindex], A[end] = A[end], A[pindex]
    return pindex

A = [10, 3, 11, 1, 4, 2, 8, 5]
Aquicksort(A, 0, 7)
print(A)
Dquicksort(A, 0, 7)
print(A)


#Randomized Quick Sort

#This will sort array A in ascending order
import random

def Arandomizedpartition(A, start, end):
    replace = random.randint(start, end)
    A[replace], A[end] = A[end], A[replace]
    return Apartition(A, start, end)

def Arandomizedquicksort(A, start, end):
    if start < end:
        pindex = Arandomizedpartition(A, start, end)
        Arandomizedquicksort(A, start, pindex-1)
        Arandomizedquicksort(A, pindex+1, end)


#This will sort array A in descending order
def Drandomizedpartition(A, start, end):
    replace = random.randint(start, end)
    A[replace], A[end] = A[end], A[replace]
    return Dpartition(A, start, end)

def Drandomizedquicksort(A, start, end):
    if start < end:
        pindex = Drandomizedpartition(A, start, end)
        Drandomizedquicksort(A, start, pindex-1)
        Drandomizedquicksort(A, pindex+1, end)

A = [10, 3, 11, 1, 4, 2, 8, 5]
Arandomizedquicksort(A, 0, 7)
print(A)
Drandomizedquicksort(A, 0, 7)
print(A)