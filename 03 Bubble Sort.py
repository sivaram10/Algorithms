#Bubble Sort

#Function to sort integers in ascending order
def Abubblesort(A):
    limitindex = len(A)
    for i in range(len(A)):
        for j in range(1,limitindex):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
            print(A)
        limitindex = limitindex-1
        print(A)
        
A = [100, 2, 101, 1, 2, -4, 18, 55, 0]  
Abubblesort(A)


#Function to sort integers in descending order
def Dbubblesort(A):
    limitindex = len(A)
    for i in range(len(A)):
        for j in range(1,limitindex):
            if A[j-1] < A[j]:
                A[j-1], A[j] = A[j], A[j-1]
            print(A)
        limitindex = limitindex-1
        print(A)
        
A = [100, 2, 101, 1, 2, 4, 18, 55, 0]  
Dbubblesort(A)