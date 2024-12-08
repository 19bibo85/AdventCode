column1 = list()
column2 = list()
sequences = list()
with open("2024\\05\\files\\01.txt") as f:
    while(True):
        line = f.readline()
        if (len(line) <= 0):
            break
        
        if line.strip() == "":
            continue

        if ("|" in line):
            maps = list(map(int,line.split("|")))
            column1.append(maps[0])
            column2.append(maps[1])
            continue
        
        if ("," in line):            
            sequence = list(map(int,line.split(",")))
            sequences.append(sequence)
            continue

r = 0
for sequence in sequences:
    for c1, c2 in zip(column1, column2):
         if (c2 not in sequence or c1 not in sequence):
             continue
         
         if(sequence.index(c2) < sequence.index(c1)): 
             break
    else:
        r += sequence[(len(sequence) // 2)]

print(r)