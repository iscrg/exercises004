nums = input('Type in the first numbers: ').split()
lst1 = list(map(int, nums))
nums = input('Type in the second numbers: ').split()
lst2 = list(map(int, nums))

lower_limit = int(input('Type in the lower limit: '))
upper_limit = int(input('Type in the upper limit: '))

cut = lst1[lower_limit-1:upper_limit]
cut.reverse()

lst2 += cut
del lst1[lower_limit-1:upper_limit]

print(lst1)
print(lst2)
