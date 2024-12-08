column1 = list()
column2 = list()
sequences = list()
with open("2024\\05\\files\\02.txt") as f:
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

results = list()
for sequence in sequences:
    i = 0
    incorrect = False
    while i < len(sequence):
        for c1, c2 in zip(column1, column2):
            if (i+1 >= len(sequence)):
                continue

            if (sequence[i+1] == c1 and sequence[i] == c2):
                incorrect = True
                temp = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = temp
                i=0
                break
        i += 1

    if (incorrect):
        results.append(sequence)

r = 0
for result in results:
    r += result[(len(result) // 2)]

print(r)