#Heap Sort

#Function to create max heap
def max_heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    
    if left < n and arr[i] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

#Function to create min heap
def min_heapify(arr, n, i):
    smallest = i
    left = 2*i+1
    right = 2*i+2
    
    if left < n and arr[i] > arr[left]:
        smallest = left
    
    if right < n and arr[smallest] > arr[right]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

#This will sort array A in ascending order
arr = [12, 12, 13, 8, 6, 7]
def Aheapsort(arr):
    print(arr)
    n = len(arr)
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)
    print(arr)

Aheapsort(arr)


#This will sort array A in descending order
arr = [12, 12, 13, 8, 6, 7]
def Dheapsort(arr):
    print(arr)
    n = len(arr)
    for i in range(n, -1, -1):
        min_heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)   
    print(arr)

Dheapsort(arr)

#Function to extract maximum element from the heap

def heap_extract_max(arr):
    print(arr)
    n = len(arr)
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)
    print(arr)
    max = arr[0]
    arr[0] = arr[n-1]
    n = n-1
    arr = arr[:n]
    print(max)
    print(arr)

arr = [1, 26, 13, 5, 6, 7]
heap_extract_max(arr)

#Function to increase key of heap and still maintain max_heap property
import numpy as np

def heap_increase_key(arr, index, key):
    n = len(arr)
    print(arr)
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)
    print(arr)
    arr[index] = key
    print(arr)
    while index>1 and arr[int(np.ceil(index/2)-1)] < arr[index]:
        arr[index], arr[int(np.ceil(index/2)-1)] = arr[int(np.ceil(index/2)-1)], arr[index]
        index = int(np.ceil(n/2)-1)
    print(arr)

arr = [1, 26, 13, 5, 6, 7] 
heap_increase_key(arr, 4, 10)

#Function to insert a new element in the heap and still maintain max_heap property

def max_heap_insert(arr, key):
    n = len(arr)
    print(arr)
    arr.append(float("-inf"))
    heap_increase_key(arr, n, key)

arr = [1, 26, 13, 5, 6, 7]
max_heap_insert(arr, 14)