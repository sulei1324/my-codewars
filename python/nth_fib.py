__author__ = 'Su Lei'


def nth_fib(n):
    for i in xrange(n):
        if i is 0:
            r1 = 0
            r2 = 0
        elif i is 1:
            r1 = 1
            r2 = 0
        else:
            t = r2
            r2 = r1
            r1 += t
    return r1


def nth_fib1(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a


print nth_fib(6)

