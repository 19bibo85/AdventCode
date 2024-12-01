list = list()
dic = dict()
with open("2024\\01\\files\\02.txt") as f:
    while(True):
        line = f.readline().split()
        if(len(line) <= 1):
            break

        col1 = int(line[0])
        list.append(col1)

        col2 = int(line[1])
        if (not(dic.get(col2))):
            dic[col2] = col2
        else:
            dic[col2] += col2

sum = 0
for l in list:
    if(dic.get(l)):
        sum += dic[l]

print(sum)