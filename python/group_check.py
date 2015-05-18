__author__ = 'Su Lei'


def group_check(s):
    a = {'}': '{', ']': '[', ')': '('}
    b = [')', '}', ']']
    i = 0
    c = []
    while i < len(s):
        t = s[i]
        if t in b:
            if len(c) is 0:
                return False
            else:
                tc = c.pop()
                if tc is not a[t]:
                    return False
        else:
            c.append(t)
        i += 1
    if len(c) is 0:
        return True
    else:
        return False

st = '{()'
print group_check(st)