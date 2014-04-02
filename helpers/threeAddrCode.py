# An array to store the three address code
import pprint
code = []
quad = -1
nextQuad = 0

tempBase = "t"
tempCount = 0
printCodeValue = True

# Function to create new temporaries
def newTemp():
    global tempBase, tempCount
    tempCount = tempCount + 1
    return tempBase + str(tempCount)

# Function to emit code
def emit(regDest, regSrc1, regSrc2, op):
    global code, quad, nextQuad
    quad = nextQuad
    code.append([regDest, regSrc1, regSrc2, op])
    nextQuad = nextQuad + 1

# Function to print code
def printCode():
    if printCodeValue:
        pprint.pprint(code)

# Function to merge two lists
def merge(list1, list2):
    return list1.extend(list2)

# Function to backpatch
def backPatch(locationList, location):
    global code
    for position in locationList:
        code[position][2] = location
    
