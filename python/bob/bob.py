def hey(what):
    what = what.strip()

    if not what:
        return 'Fine. Be that way!'

    if what == what.upper() and what != what.lower():
        return 'Whoa, chill out!'

    if what.endswith('?'):
        return 'Sure.'

    return 'Whatever.'
