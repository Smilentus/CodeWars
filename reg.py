import re

def abbreviate(s):  
    words = re.split('[^a-zA-Z]+', s)
    sep = re.split('[a-zA-Z]+', s)
    sep = list(filter(lambda x: x != '', sep))
    sepPos = 0
    data = ''

    for w in words:
        if len(w) <= 3:
            data += w + (sep[sepPos] if sepPos < len(sep) else '')
        else:
            data += w[0] + str(len(w) - 2) + w[-1] + (sep[sepPos] if sepPos < len(sep) else '')
        sepPos += 1

    return data

print(abbreviate('rerjkl'))
print(abbreviate('rerjkl5adas'))
print(abbreviate('rerjkl adas asd'))
print(abbreviate('rerjkl adas-asd'))