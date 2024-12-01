leftLocations = []
rightLocations=[]
sum=0

with open("input.txt", "r") as file:
    for line in file:
        splitResults = line.split()
        leftLocations.append(int(splitResults[0]))
        rightLocations.append(int(splitResults[1]))

for item in leftLocations:
    count=rightLocations.count(item)
    sum+=count*item

print(sum)