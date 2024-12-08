# importing the sys module
import sys

sys.setrecursionlimit(10**6)

matrix = list()
x = 0; y = 0; symbol = ""
with open("2024\\06\\files\\01.txt") as f:
    while(True):
        line = f.readline()
        if (len(line) <= 0):
            break

        i = line.find("^")
        if (i != -1):           
            x = len(matrix); 
            y = i; 
            symbol = "^"
        
        matrix.append(list(line))

moves_map = { "^" : [-1, 0], ">" : [0, 1], "v" : [1, 0], "<" : [0, -1] }

symbol_map = { "^" : ">", ">" : "v", "v" : "<", "<" : "^" }

def rotating(symbol, x, y):
     x += moves_map[symbol][0]
     y += moves_map[symbol][1]
     if (x == -1 or x == len(matrix) or y == -1 or y == len(matrix[x]) or matrix[x][y] == "#"):
         return symbol_map[symbol]
     else:
         return symbol     

def moving(symbol, x, y, c):
    if ((symbol == "^" and x == 0) or (symbol == "v" and x == len(matrix) - 1) or (symbol == "<" and y == 0) or (symbol == ">" and y == len(matrix[x]) - 1)):
        matrix[x][y] = "X"
        return
    
    symbol = rotating(symbol, x, y)
    matrix[x][y] = "X"
    x += moves_map[symbol][0]
    y += moves_map[symbol][1]
    matrix[x][y] = symbol
    moving(symbol, x, y, c + 1)

moving(symbol, x, y, 0)

r = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if (matrix[x][y] == "X"):
            r += 1
print(r)