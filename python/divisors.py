__author__ = 'Su Lei'

def isPrime(n):
    for x in xrange(1, n):
        if x is not 2 and n % x is 0 and x is not 1:
            return False
    return True



def divisors(integer):
    if integer is 1:
        return []
    if not isPrime(integer):
        return [i for i in xrange(2, integer) if integer % i is 0]
    else:
        return '%d is prime'%(integer)


print divisors(13)