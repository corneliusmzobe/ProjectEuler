def getNextOddNumbers(n):
    if n < 1:
        return 1
    return n + 2

def getSumOfNumberSpiralDiagonals(n):
    spiral = [1]
    currentOddNumber = 0
    count = 0
    step = 0
    skipped = 0
    sum = 1
    for x in range(2, n):
        step = getNextOddNumbers(currentOddNumber)

        if step > skipped:
            skipped = skipped + 1
            continue
            
        if skipped == step:
            spiral.append(x)
            sum = sum + x
            skipped = 0
            count = count + 1

        if count == 4:
            currentOddNumber = step
            skipped = 0
            count = 0

    return sum

print(getSumOfNumberSpiralDiagonals(1002002))
