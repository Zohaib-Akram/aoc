import re
with open("input.txt", "r") as file:
    text = file.read().replace("\n", "")

    multPatern = r"mul\((\d+),(\d+)\)"
    actionPatern = r"do\(\)|don't\(\)"
    results = re.finditer(fr"{actionPatern}|{multPatern}", text)

    isMultiply = True 
    sum=0

    for item in results:
        # print(item.group(0),item.group(1),item.group(2))
        if item.group(0) == "do()":
            isMultiply = True 
        elif item.group(0) == "don't()":
            isMultiply = False  
        elif isMultiply and item.group(1) and item.group(2):  
            sum+=int(item.group(1)) * int(item.group(2))

print("sum :", sum)