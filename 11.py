nums = input('Type in numbers: ').split()
nums = list(map(int, nums))

command = input('Type in the command: ')

if command[0] == 'R':
    n = int(command[1:])
    res = nums[-n:] + nums[:-n]
else:
    n = int(command[1:])
    res = nums[n:] + nums[:n]

print(res)
