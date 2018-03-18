#Selection Sort

def Aselectionsort(A):
    for i in range(len(A)):
        minindex = i
        for j in range(minindex+1, len(A)):
            if A[j] < A[minindex]:
                minindex = j
        print(A)
        A[minindex], A[i] = A[i], A[minindex]
    print(A)
    
A = [10, 0, 10, 1, 4, 4, 8, 5, 0]
Aselectionsort(A) 


def Dselectionsort(A):
    for i in range(len(A)):
        maxindex = i
        for j in range(maxindex+1, len(A)):
            if A[j] > A[maxindex]:
                maxindex = j
                print(A)
        A[maxindex], A[i] = A[i], A[maxindex]
    print(A)
            

A = [10, 0, -10, 1, 4, 4, 8, 5, 0]
Dselectionsort(A)

