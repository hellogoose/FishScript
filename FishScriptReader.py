import itertools
with open('fishes.ocean', 'r') as reader:
    file = reader.read()

    fish = '<><'
    fish_end = '><>'
    wave = '~'
    div = '/\<
    current = 0

    result = ''
    for token, group in itertools.groupby(file.split()):
        number = len(list(group))
        if token == fish:
            current += number
        elif token == wave:
            current *= number
        elif token == div:
            current /= number
        elif token == fish_end:
            result += chr(current)
            current = 0
    print(result)
