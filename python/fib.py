__author__ = 'Su Lei'


def fibonacci1(m):
    cache = {0: 0, 1: 1}

    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1)+fib(n-2)
        return cache[n]
    return fib(m)


def doFib(n, f):
    if f[n] is -1:
        f[n] = doFib(n - 1, f) + doFib(n - 2, f)
    print f
    return f[n]


def fibonacci(n):
    fib = [-1] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    return doFib(n, fib)


def memoized(f):
    cache = {}

    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped


@memoized
def fibonacci2(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci(10)


