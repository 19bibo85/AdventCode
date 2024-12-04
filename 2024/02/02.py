c = 0

with open("2024\\02\\files\\01.txt") as f:
    while(True):
        nums = list(map(int, f.readline().split()))
        if(len(nums) <= 0):
            break

        i = 0
        v = 1
        while(i < len(nums) - 1):
            if (nums[0] < nums[1]):
                if (not(nums[i+1] >= nums[i] + 1 and nums[i+1] <= nums[i] + 3)):
                    v = 0
                    break
            else:                
                if (not(nums[i+1] >= nums[i] - 3 and nums[i+1] <= nums[i] - 1)):
                    v = 0
                    break
            i += 1
        c += v

print(c)