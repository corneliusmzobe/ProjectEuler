def divisor(n):
    counter = 0
    for i in range(1,n):
        if n % i == 0:
            counter += 1
  
    return counter

def triNumber(n):
    triNo = 0
    for i in range(1,n+1):
        triNo += i
    return triNo

n = 5
tri = triNumber(n)
while divisor(tri) < 500:
    tri = triNumber(n)
    n += 1
else:
    print(f"{tri} has {divisor(tri)} divisors") 
    
