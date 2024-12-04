word = "XMAS"

def check_word(lines, row, col, dr, dc):
    for i in range(4):
        r = row + dr * i
        c = col + dc * i
        if not (0 <= r < len(lines) and 0 <= c < len(lines[0])): 
            return False
        if lines[r][c] != word[i]:  
            return False
    return True

with open("input.txt", "r") as file:
    lines = [list(line.strip()) for line in file]
    count = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == 'X':
                #  horizontal right direction
                if check_word(lines, row, col, 0, 1):
                    count += 1
                # horizontal left direction
                if check_word(lines, row, col, 0, -1):
                    count += 1
                # vertical down direction
                if check_word(lines, row, col, 1, 0):
                    count += 1
                # vertical up direction
                if check_word(lines, row, col, -1, 0):
                    count += 1
                # diagonal top-left direction
                if check_word(lines, row, col, -1, -1):
                    count += 1
                # diagonal top-right direction
                if check_word(lines, row, col, -1, 1):
                    count += 1
                # diagonal bottom-left direction
                if check_word(lines, row, col, 1, -1):
                    count += 1
                # diagonal bottom-right direction
                if check_word(lines, row, col, 1, 1):
                    count += 1


print("result:", count)