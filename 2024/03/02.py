import re

with open("2024\\03\\files\\02.txt") as f:
    line = str(f.readlines())
    matches = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", line, flags=re.IGNORECASE)

    total_sum = 0
    enabled = True
    for match in matches:
        val = match[0]
        if (val == "do()"):
            enabled = True
        elif (val == "don't()"):
            enabled = False
        else:
            if(enabled):
                total_sum += int(match[1]) * int(match[2])
    
    print(total_sum)