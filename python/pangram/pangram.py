from string import ascii_lowercase


def is_pangram(sentence):
    count = {}
    for char in ascii_lowercase:
        count[char] = 0

    for char in sentence.lower():
        if char in count:
            count[char] += 1

    return all(count.values())
