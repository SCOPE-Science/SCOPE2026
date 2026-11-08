"""Exact finite checks for the weighted periodic-orbit census of the full tent map.

This checks all branch-affine periodic solutions to periods 2..12, compares
fixed-iterate weighted counts and primitive-orbit Möbius counts. It is not an
infinite proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb, gcd

ZERO, HALF, A, ONE = Fraction(0), Fraction(1, 2), Fraction(2, 3), Fraction(1)


def tent(x):
    return 2*x if x <= HALF else 2-2*x


def mobius(n):
    ps = 0
    d = 2
    while d*d <= n:
        if n % d == 0:
            n //= d
            ps += 1
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ps += 1
    return (-1)**ps


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def e(n,k):
    if not 1 <= k <= n//2:
        return 0
    return (n*comb(n-k,k)*2**k)//(n-k) - (2 if n == 2*k else 0)


def cycles_formula(n,k):
    v = sum(mobius(d)*e(n//d,k//d) for d in divisors(gcd(n,k)))
    assert v%n == 0, (n,k,v)
    return v//n


def periodic_points(n):
    pts = set()
    for bits in range(1<<n):
        slope, intercept = 1, 0
        for j in range(n):
            if bits & (1<<j):
                slope, intercept = -2*slope, 2-2*intercept
            else:
                slope, intercept = 2*slope, 2*intercept
        if slope == 1:
            continue
        x = Fraction(-intercept,slope-1)
        if x < ZERO or x > ONE:
            continue
        y = x
        for j in range(n):
            if y != HALF and (y > HALF) != bool(bits & (1<<j)):
                break
            y = tent(y)
        else:
            if y == x:
                pts.add(x)
    assert len(pts) == 2**n, (n,len(pts))
    return pts


def height(x,n):
    y = x
    k = 0
    for j in range(n):
        nxt = tent(y)
        if y > A and nxt < A:
            k += 1
        y = nxt
    assert y == x
    return k


def least_period(x,n):
    y=x
    for j in range(1,n+1):
        y=tent(y)
        if y==x:
            return j
    raise AssertionError('not periodic')


def test():
    assertions = 0
    for n in range(2,13):
        pts = periodic_points(n)
        pts = pts.difference({ZERO,A})
        fixed_stat = Counter(height(x,n) for x in pts)
        assert fixed_stat == Counter({k:e(n,k) for k in range(1,n//2+1)})
        assertions += len(pts)
        prime_stat = Counter(height(x,n) for x in pts if least_period(x,n)==n)
        formula = {k:n*cycles_formula(n,k) for k in range(1,n//2+1)}
        assert prime_stat == Counter(formula), (n,prime_stat,formula)
        assertions += len(formula)
        assert sum(prime_stat.values()) == sum(formula.values())
    print('All exact-rational branch, weighted trace, and primitive-orbit tests passed.')
    print('Periods checked: 2..12; total comparisons:', assertions)

if __name__ == '__main__':
    test()
