import re

with open("2024\\03\\files\\01.txt") as f:
    line = str(f.readlines())
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line, flags=re.IGNORECASE)

    total_sum = 0
    for match in matches:
        total_sum += int(match[0]) * int(match[1])
    
    print(total_sum)