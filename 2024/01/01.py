list1 = list()
list2 = list()
with open("2024\\01\\files\\01.txt") as f:
    while(True):
        line = f.readline().split()
        if(len(line) <= 1):
            break
        list1.append(int(line[0]))
        list2.append(int(line[1]))

list1.sort()
list2.sort()
sum = 0
for num1, num2 in zip(list1, list2):
    if(num1 > num2):
        sum += num1 - num2
    else:
        sum += num2 - num1
print(sum)
