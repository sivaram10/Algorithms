# Insertion Sort

#Function to sort integers in ascending order
def Ainsertionsort(A):
    print(A)
    for i in range(1,len(A)):
        key = A[i]
        sortedindex = i-1
        while sortedindex>=0 and A[sortedindex] > key:
            A[sortedindex+1]= A[sortedindex]
            sortedindex = sortedindex-1
            print(A)
        A[sortedindex+1] = key
    print(A)
    

A = [100, 55, 101, 1, 3, 4, 18, 55, 0]
Ainsertionsort(A)


#Function to sort integers in descending order
def Dinsertionsort(A):
    print(A)
    for i in range(1,len(A)):
        key = A[i]
        sortedindex = i-1
        while sortedindex>=0 and A[sortedindex] < key:
            A[sortedindex+1]= A[sortedindex]
            sortedindex = sortedindex-1
            print(A)
        A[sortedindex+1] = key
    print(A)
    
A = [100, 55, 101, 1, 3, 4, 18, 55, 0]
Dinsertionsort(A)