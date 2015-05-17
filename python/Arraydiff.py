__author__ = 'Su Lei'

def array_diff(c, d):
    return [x for x in c if x not in d]


a = [1, 2, 3]
b = [1, 2]
print array_diff(a, b)