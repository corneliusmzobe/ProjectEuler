import math

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            x = 0
            break
        else:
            x = n
    return x

def listSize(list):
    count = 0
    for x in list:
        count += 1

    return count

def quadraticPrimes(n):
    prime = n**2 - 79*n + 1601
    return prime

n = 0
primeList = []
while n <= 79:
    if(isPrime(quadraticPrimes(n)) != 0):
        primeList.append(quadraticPrimes(n))
    n += 1
print(primeList)
print(listSize(primeList))