#SUM OF PRIMES
#PROBLEM10

def prime(n):
    sumOfPrimes = 2
    for i in range(3,n):
        if isPrime(i) != 0:
            sumOfPrimes += isPrime(i)
            print(i, ' : ',sumOfPrimes)
    return sumOfPrimes

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            x = 0
            break
        else:
            x = n  
    return x

prime(10)
