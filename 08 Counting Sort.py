#Counting Sort

#As of now valid only for whole numbers in ascending order

A = [10, 3, 10, 1, 4, 2, 8, 5, 0]

def Acountingsort(A):
    output = [0] * len(A)
    count = [0] * (max(A)+1)
    print(A)
    print(count)
    print(output)
    print('')
   
    for i in A:
        count[i] = count[i] + 1
        print(count)

    for i in range(1,len(count)):
        count[i] = count[i]+count[i-1]
    print(count)
    print('')

    for i in A:
        index = count[i]-1
        output[index] = i
        count[i] = count[i]-1
        print(output)
    print(output)

A = [10, 3, 10, 1, 4, 4, 8, 5, 0]      
Acountingsort(A)