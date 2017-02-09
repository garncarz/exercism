from collections import defaultdict
import re


def word_count(sentence):
    count = defaultdict(lambda: 0)
    for word in re.findall(r'(\w+)', sentence.replace('_', ' ')):
        word = word.lower()
        count[word] += 1
    return count
