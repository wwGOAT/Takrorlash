nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
sum_even = 0
for num in nums:
    if num % 2 == 0:
        sum_even += num

print(sum_even)