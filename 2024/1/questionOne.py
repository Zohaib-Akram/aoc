leftLocations = []
rightLocations=[]
sum=0

with open("inputOne.txt", "r") as file:
    for line in file:
        splitResults = line.split()
        leftLocations.append(int(splitResults[0]))
        rightLocations.append(int(splitResults[1]))

leftLocations=sorted(leftLocations)
rightLocations=sorted(rightLocations)
for index in range(0,len(leftLocations)):
    sum+=abs(leftLocations[index]-rightLocations[index])
    
print(sum)