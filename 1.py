lst = []

for _ in range(10):
    num = int(input())
    lst.append(num)

res = [sum(lst)] * 9
print(res)
