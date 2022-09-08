
def getListOfOrderedNames():
    f = open("p022_names.txt", "r")
    namesFromFile = f.read()
    listOfNames = []
    listOfNamesWithDoubleQuotes = namesFromFile.split(",")
    for name in listOfNamesWithDoubleQuotes:
        nameWithNoQuotes = name.strip('\"')
        listOfNames.append(nameWithNoQuotes)
        listOfNames.sort()
    return listOfNames

def getNameValue(name):
    alphabetsDict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16, 
        "Q": 17, 
        "R": 18, 
        "S": 19, 
        "T": 20, 
        "U": 21, 
        "V": 22, 
        "W": 23,
        "X": 24, 
        "Y": 25,
        "Z": 26,
    }

    sum = 0

    for c in name:
        sum += alphabetsDict[c]

    return sum

def getNameScore():
    totalNameScore = 0
    listOfNames = getListOfOrderedNames()
    for i in range(len(listOfNames)):
        name = listOfNames[i]
        nameValue = getNameValue(name)
        totalNameScore += nameValue*(i+1)
    return totalNameScore

print(getNameScore())
