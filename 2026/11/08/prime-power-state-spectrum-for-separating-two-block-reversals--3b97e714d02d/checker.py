"""Direct exhaustive finite checks for a two-block permutation separation theorem."""
from itertools import permutations, product
from math import lcm


def first_nondivisor(a):
    j = 2
    while a % j == 0:
        j += 1
    return j


def prediction(a, b):
    da, db = first_nondivisor(a), first_nondivisor(b)
    return max(da, db) + int(da == db and da in (2, 3, 4))


def compose(p, q):
    return tuple(q[p[i]] for i in range(len(p)))


def power(p, k):
    n = len(p)
    accum = tuple(range(n))
    while k:
        if k & 1:
            accum = compose(accum, p)
        p = compose(p, p)
        k >>= 1
    return accum


def can_distinguish(n, a, b):
    perms = list(permutations(range(n)))
    pa = set(power(p, a) for p in perms)
    pb = set(power(p, b) for p in perms)
    for x in pa:
        for y in pb:
            if compose(x, y) != compose(y, x):
                return True
    return False


def run():
    count = 0
    for n in range(1, 6):
        # All exponent pairs through 24, including every low-order exceptional case.
        for a, b in product(range(1, 25), repeat=2):
            expected = prediction(a, b) <= n
            actual = can_distinguish(n, a, b)
            assert actual == expected, (n, a, b, actual, expected)
            count += 1
    # Boundary cases beyond degree five, where the two power-word exponent
    # values are multiples of every cycle length through degree five.
    boundary = [(6, 60, 60), (6, 420, 60), (6, 120, 60),
                (6, 6, 6), (6, 60, 1), (6, 1, 60),
                (6, 12, 12), (6, 840, 420), (6, 2, 60)]
    for n, a, b in boundary:
        expected = prediction(a, b) <= n
        actual = can_distinguish(n, a, b)
        assert actual == expected, (n, a, b, actual, expected)
        count += 1
    # All first nondivisors through 19 are prime powers.
    for a in range(1, 20000):
        d = first_nondivisor(a)
        for c in range(2, d):
            assert a % c == 0
        if d == 2:
            continue
        prime_power = any(d == p**k for p in range(2, d+1) if all(p % z for z in range(2, int(p**.5)+1)) for k in range(1, 20))
        assert prime_power, (a, d)
    print('PASS: all', count, 'symmetric-group cases and 19,999 arithmetic cases')

if __name__ == '__main__':
    run()
