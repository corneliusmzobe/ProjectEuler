#Largest prime factor
#problem3

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            x = 0
            break
        else:
            x = n
    return x

def largestFactor(n):
    x = 2
    myList = []
    for i in range(3,n):
        x = isPrime(i)
        if x != 0:
             if n%x == 0:
                    n = n/x
                    myList.append(x)
                    print(x, sep=", ")
    return myList[-1]
largestFactor(600851475143)
