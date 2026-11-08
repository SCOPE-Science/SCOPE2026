"""Exact checks for integer reciprocal-mean pair counts; standard library only."""
from math import gcd, isqrt, log, pi
from fractions import Fraction


def by_pairs(n, m):
    return sum(1 for a in range(1, n) for b in range(a + 1, n + 1)
               if (m * a * b) % (a + b) == 0)


def by_primitive(n, m):
    s = 0
    for y in range(2, isqrt(m * n) + 2):
        for x in range(1, y):
            if gcd(x, y) == 1:
                q = (x + y) // gcd(m, x + y)
                s += n // (q * y)
    return s


def local_factor(m):
    value = Fraction(1)
    p = 2
    while p * p <= m:
        if m % p == 0:
            k = 0
            while m % p == 0:
                m //= p
                k += 1
            value *= 1 + Fraction(k * (p - 1), p + 1)
        p += 1
    if m > 1:
        value *= 1 + Fraction(m - 1, m + 1)
    return value


for m in range(1, 9):
    for n in (8, 20, 50, 100, 300):
        direct = by_pairs(n, m)
        primitive = by_primitive(n, m)
        assert direct == primitive, (n, m, direct, primitive)
    print('EXACT_IDENTITY', 'm', m, 'N', 300,
          'pairs', by_primitive(300, m), 'factor', str(local_factor(m)))

for m in (1, 2, 3, 4, 6):
    n = 100_000
    exact = by_primitive(n, m)
    constant = 3 * log(2) / pi ** 2 * local_factor(m)
    print('ASYMPTOTIC_CHECK', 'm', m, 'N', n,
          'edges', exact, 'leading_C', f'{float(constant):.12f}',
          'normalized_error', f'{float(exact/n - constant*log(n)):.8f}')

assert local_factor(1) == 1
assert local_factor(2) == Fraction(4, 3)
print('VERIFY_OK exact_formulas=true independent_enumerations=true')
