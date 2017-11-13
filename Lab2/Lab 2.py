a = [5, 10, 15, 20, 25]

# Exercise one

def returnFirstAndLast(givenList):
    return [givenList[0], givenList[-1]]

# Exercise two

def printLessThanFive(list1):
    newList=[]
    chosenOne = int(input("Choose a number for the limit: "))
    chosenList=[]
    for value in list1:
        if(value<5):
            print(value)
            newList.append(value)
        if(value<chosenOne):
            chosenList.append(value)
    print(newList)
    return chosenList

# Exercise three

def returnCommon(list1, list2):
    newList=[]
    for value in list1:
        if(value in list2):
            newList.append(value)

    return newList

# Exercise four

# Test cases

a1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(printLessThanFive(a))

print(returnCommon(a1, b))
