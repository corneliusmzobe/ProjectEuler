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
    while (index > i):
        temp = Pm(n-i)
        diff = pentNum - temp
        if (isPenNumber(diff)):
            if (getPenIndex(temp) != getPenIndex(diff)):
                newIndex = getPenIndex(diff)
                if(Pm(newIndex) + Pm(n-i) == pentNum):
                    count += 1
                    print('Pn(', index, ') = ', Pm(newIndex), ' + ', Pm(n-i), ' = ', Pm(index), ' Count: ', int(count/2))
        i = i+1
    return int(count/2)
m = 1
count = 1
LIMIT = 5
while (count < LIMIT):
    count = getNumberOfSumOfTwos(Pm(m), m)
    if(count >= LIMIT):
        print('Pn(', m, '): ', Pm(m), 'Count: ', count)
    m += 1
    # print('Count: ', count, 'm: ', m)

#print('Index: ',getPenIndex(107602))