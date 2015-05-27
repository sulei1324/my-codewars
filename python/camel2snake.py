__author__ = 'Su Lei'
import re


def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()


def camel2snake(s):
    r = ''
    s = str(s)
    for i in xrange(len(s)):
        if re.match('[A-Z]', s[i]) is not None and i is not 0:
            r += '_' + str(s[i]).lower()
        elif i is 0:
            r += str(s[i]).lower()
        else:
            r += s[i]
    return r


print camel2snake(111)
