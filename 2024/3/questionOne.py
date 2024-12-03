import re

pattern = r"mul\((\d+),(\d+)\)"
sum=0

with open("input.txt", "r") as file:
    text = file.read().replace("\n", "")
    matches = re.findall(pattern, text)
    for a,b in matches:
        sum+=int(a)*int(b)

print("Sum of results:", sum)