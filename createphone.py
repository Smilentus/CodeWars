# My implementation
def create_phone_number(n):
    number = ''
    for c in n:
        number += str(c)
    return '(' + number[:3] + ') ' + number[3:6] + '-' + number[6:10]

# Best Solution
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)