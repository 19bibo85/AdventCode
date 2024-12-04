
matrix = list()
with open("2024\\04\\files\\01.txt") as f:
    while(True):
        letters = list(f.readline().strip())
        if(len(letters) <= 0):
            break

        matrix.append(letters)

def findWord(i, j, x, y, m):
    if (i + x >= len(matrix) or i + x < 0 or j + y >= len(matrix[i]) or j + y < 0):
        if(m > 0):
            return matrix[i][j]
        else:
            return ""      
    if (m == 0):
        return ""
    
    return matrix[i][j] + findWord(i+x, j+y, x, y, m-1)

def isXmas(word):
    if(word.lower() == "xmas"):
        return 1
    else:
        return 0

r = 0
i = 0
while (i < len(matrix)):
    j = 0
    while (j < len(matrix[i])):
        r += isXmas(findWord(i, j, 0, 1, 4))        
        r += isXmas(findWord(i, j, 1, 0, 4))
        r += isXmas(findWord(i, j, 1, 1, 4))
        r += isXmas(findWord(i, j, 1, -1, 4))
        j += 1
    i += 1

i = len(matrix) - 1
while (i >= 0):
    j = len(matrix[i]) - 1
    while (j >= 0):
        r += isXmas(findWord(i, j, 0, -1, 4))
        r += isXmas(findWord(i, j, -1, 0, 4))
        r += isXmas(findWord(i, j, -1, 1, 4))
        r += isXmas(findWord(i, j, -1, -1, 4))
        j -= 1
    i -= 1

print(r)


        