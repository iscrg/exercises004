lst = [3]

nums = input().split()
nums = list(map(int, nums))

lst += nums

del lst[0]

print(lst)
