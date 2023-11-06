nums = input().split()
nums = list(map(int, nums))

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f'Even: {even}, Odd: {odd}')
