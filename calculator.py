#input at the beginning initials and the percent they will pay from 0-1
#then it will repeat with input (cost, initials)

def getInitials(i1, i2, i3, p1, p2, p3):
   # allData=[]
   # allData = input("Type in initals of people followed by how much they will contribute from 0-1")
    peopleDict = {}
    peopleDict[i1] = p1
    peopleDict[i2] = p2
    peopleDict[i3] = p3
    return peopleDict

def costCalculator():
    peopleDict = {}

    i = int(1)
    while i != "-1":
        initial = input("Enter a person's 'letter': (or -1 to stop) ")
        i = initial
        if i == "-1":
            break
        percentPayed = input("Enter how much they pay from 0-1: ")
        peopleDict[initial] = percentPayed

    pTot = {}
    for totInitial in peopleDict:
        pTot[totInitial] = 0

    cost = 1
    while cost != 0:
        totPeople = float(0)
        peopleList = []
        cost = float(input("Cost: "))
        people = input("People: ")
        if people == "all":
            for person in peopleDict:
                pTot[person] += cost/3
            #pTot[i1] += cost/3
            #pTot[i2] += cost / 3
            #pTot[i3] += cost / 3
        else:
            for character in people:
                peopleList.append(character)
            #print(peopleList, "is people list", peopleDict)
            for person in peopleList:
                totPeople += float(peopleDict[person])

            for people in peopleList:
                tempCost = ((cost/(totPeople))*(float(peopleDict[people])))
                #print(tempCost)
                pTot[people] += tempCost
        print(pTot)


def receiptCalculator(fileName: str):
    costList = []
    with open(fileName) as myFile:
        for line in myFile:
            line = line[:-1]
            line = line.split(',')
            costList.append(line)
    peopleDict = {}
    for i in range(2,5):
        pp = costList[0] #pp stands for percent percent
        pp = pp[i].split('!')
        peopleDict[pp[0]] = pp[1]
        i += 1
    pTot = {}
    for initial in peopleDict:
        pTot[initial] = 0
    for line in costList:
        if line[0] == 'Price':
            continue
        totPeople = float(0)
        peopleList = []
        cost = float(line[0])
        people = line[1]
        if people == "all":
            for person in peopleDict:
                pTot[person] += cost / 3
        else:
            for character in people:
                peopleList.append(character)
            for person in peopleList:
                totPeople += float(peopleDict[person])
            for people in peopleList:
                tempCost = ((cost / (totPeople)) * (float(peopleDict[people])))
                pTot[people] += tempCost
    for name, total in pTot.items():
        total = round(total, 2)
        print(f'{name} pays ${total}')

receiptCalculator("receipts.csv")