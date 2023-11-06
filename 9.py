import string

sentence = ''
words_dict = {}

while True:
    add_sentence = input()

    if add_sentence == '':
        break
    else:
        sentence += add_sentence

for point in string.punctuation:
    sentence = sentence.replace(point, '')

words = sentence.split()

for word in words:
    if word in words_dict.keys():
        words_dict[word] += 1
    else:
        words_dict[word] = 1

words = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

for word in words:
    print(word[0], word[1])
