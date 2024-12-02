correctLevelsCount=0
def validateLevel(results):
    isSafe=True
    isDecreasing = int(results[1])<int(results[0])
    for index in range(0,len(results)):
            if(index<(len(results)-1)):
                itemOne=int(results[index])
                itemTwo=int(results[index+1])
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
    return isSafe

with open("input.txt", "r") as file:
    for line in file:
        splitResults = line.split()
        isSafe=validateLevel(splitResults)
        if(isSafe is True):
             correctLevelsCount+=1
        else:
            for index in range(0,len(splitResults)):
                dublicateList = list(splitResults)
                del dublicateList[index]
                if(validateLevel(dublicateList) is True):
                    correctLevelsCount+=1
                    break
            
            
      
            
print(f"result:{correctLevelsCount}")