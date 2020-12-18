from math import factorial


# Function for the "multiplication" of two
# elements of the symetric group
def symElMerge(el1, el2):
    n = len(el1)
    result = [0 for i in range(n)]
    for i in range(n):
        result[i] = el1[el2[i]-1]
    return result


def isI(el):
    n = len(el)
    if el == [i+1 for i in range(n)]:
        return True
    else:
        return False


def getElOrder(el):
    n = 1
    baseEl = el
    while not(isI(el)):
        el = symElMerge(el, baseEl)
        n += 1
    return n

def isMagicSquare(el):
    if ((el[0]+el[1]+el[2]) == (el[3]+el[4]+el[5]) and
        (el[0]+el[1]+el[2]) == (el[6]+el[7]+el[8]) and
        (el[0]+el[1]+el[2]) == (el[0]+el[3]+el[6]) and
        (el[0]+el[1]+el[2]) == (el[1]+el[4]+el[7]) and
        (el[0]+el[1]+el[2]) == (el[2]+el[5]+el[8]) and
        (el[0]+el[1]+el[2]) == (el[0]+el[4]+el[8]) and
        (el[0]+el[1]+el[2]) == (el[2]+el[4]+el[6])
    ):
        return True
    else:
        return False


# Set the generators
# For S_9 the generators are (14)(28)(59) and (123)(456)(789)
genOrder2 = [4, 8, 3, 1, 9, 6, 7, 2, 5]
genOrder3 = [2, 3, 1, 5, 6, 4, 8, 9, 7]

# For S_36
# genOrder3 = [2, 3, 1, 5, 6, 4, 8, 9, 7, 11, 12, 10, 14, 15, 13, 17, 18, 16, 20, 21, 19, 23, 24, 22, 26, 27, 25, 29, 30, 28, 32, 33, 31, 34, 35, 36]
# genOrder2 = [4, 34, 35, 1, 5, 9, 10, 11, 6, 7, 8, 15, 16, 17, 12, 13, 14, 21, 22, 23, 18, 19, 20, 27, 28, 29, 24, 25, 26, 33, 36, 32, 30, 2, 3, 31]

# Initialise the element and the helper variables
el = genOrder3
baseEl = [i+1 for i in range(9)]
addEnd = False
caseNum = 0
counter = 1

# Let's see whether this loop will close or not
while not(isMagicSquare(el)):
    if counter == factorial(9):
        break
    if not addEnd:
        el = genOrder2
        caseInBinaryList = [int(x) for x in bin(caseNum)[2:]]
        for i in caseInBinaryList:
            el = symElMerge(el, genOrder2)
            el = symElMerge(el, genOrder3)
            if i == 1:
                el = symElMerge(el, genOrder3)
        caseNum += 1
    else:
        el = symElMerge(el, genOrder2)
    addEnd = not addEnd
    counter += 1
print(el)
print(counter)
print("That's all folks")
