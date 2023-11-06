def perforated(string):
    letters = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']
    for letter in letters:
        if letter in string:
            return True
    return False


res = {
    'perforated': 0,
    'non-perforated': 0
}

string = input().split()

for word in string:
    if perforated(word):
        res['perforated'] += 1
    else:
        res['non-perforated'] += 1

print(res)
