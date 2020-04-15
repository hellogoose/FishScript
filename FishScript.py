import itertools
user_input = input()

fish = '<><'
fish_end = '><>'
wave = '~'
current = 0

result = ''
for token, group in itertools.groupby(user_input.split()):
    number = len(list(group))
    if token == fish:
        current += number
    elif token == wave:
        current *= number
    elif token == fish_end:
        result += chr(current)
        current = 0
print(result)
