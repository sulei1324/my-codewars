__author__ = 'Su Lei'

def polybius(text):
    rs = ''
    for i in text:
        if i is ' ':
            rs += i
            continue
        else:
            o = ord(i)
            if o >= 74:
                o -= 1
            c = (o - 65) % 5 + 1
            r = (o - 65) / 5 + 1
            rn = r * 10 + c
            print rn
            rs += str(rn)
    return rs


key_array = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'IJ', 'K'],
    ['L', 'M',  'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

t = 'CODEWARS FD'

print polybius(t)