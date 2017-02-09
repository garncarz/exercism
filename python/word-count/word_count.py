import re


def word_count(sentence):
    count = {}
    for word in re.findall(r'(\w+)', sentence.replace('_', ' ')):
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count
