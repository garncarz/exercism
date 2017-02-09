import re


def encode(decoded):
    if not decoded:
        return ''

    encoded = ''
    last_char = decoded[0]
    count = 1

    for char in decoded[1:]:
        if char == last_char:
            count += 1
        else:
            encoded += '%d%s' % (count, last_char) if count > 1 \
                       else last_char
            last_char = char
            count = 1

    encoded += '%d%s' % (count, last_char) if count > 1 \
               else last_char

    return encoded


def decode(encoded):
    decoded = ''

    for match in re.finditer(r'(?P<count>\d+)?(?P<char>[^\d])', encoded):
        count = int(match.group('count')) if match.group('count') \
                else 1
        decoded += match.group('char') * count

    return decoded
