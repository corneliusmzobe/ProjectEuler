import math

def Tn(n):
   return int((n * (n + 1)) / 2)

def Pm(m):
    return int((m * (3*m - 1)) / 2)

def Hn(n):
    return int(n * (2*n - 1))
n = 286
m = 2
z =2
while (n > 1):
    m = int((1 + math.sqrt(1 + 24*Tn(n)))/6)

    z = int((1 + math.sqrt(1 + 8*Tn(n)))/4)

    if(Pm(m) == Hn(z) and Tn(n) == Hn(z)):
        print('Tn(', n, '): ', Tn(n))
        print('Pn(', m, '): ', Pm(m))
        print('Hn(', z, '): ', Hn(z))
        break


    n = n+1


#print('Pm(' + m + '): ' + Pm(m))
#print('Hn(' + z + '): ' + Hn(z))