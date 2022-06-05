# Problem800


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            x = 0
            break
        x = n
    return x
