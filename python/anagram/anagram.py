from collections import defaultdict


def detect_anagrams(word, possibilities):
    word = word.lower()

    chars = defaultdict(lambda: 0)
    for char in word:
        chars[char] += 1

    anagrams = []

    for word2 in possibilities:
        word2l = word2.lower()

        if word == word2l:
            continue

        chars2 = chars.copy()
        for char in word2l:
            chars2[char] -= 1

        for char_count in chars2.values():
            if char_count != 0:
                break
        else:
            anagrams.append(word2)

    return anagrams
