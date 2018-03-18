#Bucket sort

#This only takes values between 0 and 1, 1 not included
import numpy as np
A = [0.7, 0.29, 0.27, 0.75, 0.01, 0.8, 0.6]

def Ainsertionsort(A):
    for i in range(1,len(A)):
        key = A[i]
        sortedindex = i-1
        while sortedindex>=0 and A[sortedindex] > key:
            A[sortedindex+1]= A[sortedindex]
            sortedindex = sortedindex-1
        A[sortedindex+1] = key

Ainsertionsort(A)

def Abucketsort(A):
    temp = [0] * int(np.floor(max(A) * 10)+1)
    bucket = [[] for _ in temp]
    for i in A:
        index = int(np.floor(i*10))
        bucket[index].append(i)
        
    for i in bucket:
        Ainsertionsort(i)

    output = [item for sublist in bucket for item in sublist]
    print(output)
        
        
A = [0.7, 0.29, 0.27, 0.75, 0.01, 0.8, 0.6]
Abucketsort(A)