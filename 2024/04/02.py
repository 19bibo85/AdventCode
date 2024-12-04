
matrix = list()
with open("2024\\04\\files\\02.txt") as f:
    while(True):
        letters = list(f.readline().strip())
        if(len(letters) <= 0):
            break

        matrix.append(letters)

def findWord(i, j, x, y, m):
    if (i >= len(matrix) or i < 0 or j >= len(matrix[i]) or j < 0):
        return ""
    
    if (i + x >= len(matrix) or i + x < 0 or j + y >= len(matrix[i]) or j + y < 0):
        if(m > 0):
            return matrix[i][j]
        else:
            return ""      
        
    if (m == 0):
        return ""
        
    return matrix[i][j] + findWord(i+x, j+y, x, y, m-1)

def isXmas(word1, word2):    
    if (not(word1.lower() in ("mas", "sam") or word2.lower() in ("mas", "sam"))):
        return 0
   
    if (not(word1 == word2[::-1] or word1 == word2)):
        return 0
    
    return 1    

r = 0
i = 0
while (i < len(matrix)):
    j = 0
    while (j < len(matrix[i])):
        r += isXmas(findWord(i, j, 1, 1, 3), findWord(i, j + 2, 1, -1, 3))
        j += 1
    i += 1

print(r)


        