correctLevelsCount=0
with open("input.txt", "r") as file:
    for line in file:
        splitResults = line.split()
        isDecreasing = int(splitResults[1])<int(splitResults[0])
        isSafe=True
        for index in range(0,len(splitResults)):
            if(index<(len(splitResults)-1)):
                itemOne=int(splitResults[index])
                itemTwo=int(splitResults[index+1])
                difference=abs(itemOne-itemTwo)
                if(difference>3 or difference<1):
                    isSafe=False
                    break
                if(isDecreasing is True and itemTwo>itemOne):
                    isSafe=False
                    break
                if(isDecreasing is False and itemTwo<itemOne):
                    isSafe=False
                    break
        if(isSafe is True): 
            correctLevelsCount+=1
print(f"result:{correctLevelsCount}")