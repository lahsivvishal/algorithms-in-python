# General
"""
if n == 2:
    return 1
elif n == 1:
    return 0
elif:
    return fib(n-1)+fib(n-2)
"""
# Memoize
"""
def getNthFib(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]
print(getNthFib(6))
"""
#Iterative method
def getNthfib(n):
    lasttwo = [0, 1]
    counter = 3
    while counter <=3:
        nextFib = lasttwo[0] + lasttwo [1]
        lasttwo[0] = lasttwo[1]
        lasttwo[1] = nextFib
        counter += 1
    return lasttwo[1] if n > 1 else lasttwo[0]

print(getNthfib(0)
