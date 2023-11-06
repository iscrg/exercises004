num = int(input())
res = []

for i in range(1, int(num**0.5)+1):
    if num % i == 0:
        res.append(i)
        res.append(num//i)

print(res)
