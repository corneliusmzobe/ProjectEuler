import math
#Problem799

def Pm(m):
    return int((m * (3*m - 1)) / 2)

def getPenIndex(Pm):
    return int((1+math.sqrt(1+24*Pm))/6)

def isPenNumber(n):
    index = getPenIndex(n)
    return Pm(index) == n

def getNumberOfSumOfTwos(pentNum, index):
    n = index
    i = 1
    count = 0
    
    for i in range(index-1, 1, -1):
        temp = Pm(i)
        diff = pentNum - temp
        if (temp < diff):
            break

        if (isPenNumber(diff)):
            newIndex = getPenIndex(diff)
            if(Pm(newIndex) + Pm(i) == pentNum):
                count += 1
                print('Pn(', index, ') = ', Pm(newIndex), ' + ', Pm(i), ' = ', Pm(index), ' Count: ', count)
    return count
m = 98873
count = 0
LIMIT = 20

while (count < LIMIT):
    count = getNumberOfSumOfTwos(Pm(m), m)
    if(count >= LIMIT):
        print('Pn(', m, '): ', Pm(m), 'Count: ', count)
    m += 1

#Pn( 157724 ):  37315211402 Count:  24