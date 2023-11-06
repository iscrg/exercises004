import string

sentence = input()

for point in string.punctuation:
    sentence = sentence.replace(point, '')

words = sentence.split()
print(words)
