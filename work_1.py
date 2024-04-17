nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
sum_even = 0
index = 0

while index < len(nums):
    if nums[index] % 2 == 0:
        sum_even += nums[index]
    index += 1

print(sum_even)