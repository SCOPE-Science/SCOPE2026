"""Independent finite tests for Domb quadratic-character correlations mod five.

Run: python3 CHECK.py
All statements about every index or shift require the proof in RESULT.md.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb

W = (1, 1, -1, 1, 1)


def domb_direct(n):
    return sum(comb(n, j) ** 2 * comb(2*j, j) *
               comb(2*(n-j), n-j) for j in range(n+1))


def digit_sign(n):
    a = 1
    while n:
        a *= W[n % 5]
        n //= 5
    return a


@lru_cache(None)
def finite_correlation(r, h):
    if r == 0:
        return Fraction(digit_sign(h))
    q, a = divmod(h, 5)
    l, u = finite_correlation(r-1, q), finite_correlation(r-1, q+1)
    if a == 0: return l
    if a == 1: return u/5
    if a == 2: return (-l+2*u)/5
    if a == 3: return (2*l-u)/5
    return l/5


@lru_cache(None)
def limit_correlation(h):
    if h == 0: return Fraction(1)
    if h == 1: return Fraction(0)
    q, a = divmod(h, 5)
    l = limit_correlation(q)
    if a == 0: return l
    if a == 4: return l/5
    u = limit_correlation(q+1)
    if a == 1: return u/5
    if a == 2: return (-l+2*u)/5
    return (2*l-u)/5


def test():
    assert [domb_direct(i) for i in range(5)] == [1, 4, 28, 256, 2716]
    for n in range(210):
        value = domb_direct(n) % 5
        character = 1 if value in (1,4) else -1 if value in (2,3) else 0
        assert character == digit_sign(n), (n, value, character)
    tested_blocks = 0
    for r, max_h in ((1,70),(2,70),(3,70),(4,70),(5,70),(6,28)):
        limit = 5**r
        data = [digit_sign(i) for i in range(limit+max_h)]
        for h in range(max_h+1):
            direct = sum(data[i]*data[i+h] for i in range(limit))
            predicted = finite_correlation(r,h)*limit
            assert predicted.denominator == 1 and direct == predicted, (r,h,direct,predicted)
            tested_blocks += 1
    for r in range(1,7):
        n = 5**r
        cells = {(s,t):0 for s in (-1,1) for t in (-1,1)}
        for i in range(n):
            cells[digit_sign(i), digit_sign(i+1)] += 1
        for s in (-1,1):
            for t in (-1,1):
                assert 4*cells[s,t] == n+(s+t)*3**r+s*t
        assert finite_correlation(r,1)*5**r == 1
        assert finite_correlation(r,2)*5**r == -5**(r-1)+2
        assert finite_correlation(r,3)*5**r == 2*5**(r-1)-1
    for h in range(1,100001):
        c = limit_correlation(h)
        assert Fraction(-1,5) <= c <= Fraction(2,5)
        t=h
        while t%5==0: t//=5
        if c == Fraction(-1,5): assert t == 2
        if c == Fraction(2,5): assert t == 3
    print('PASS: 210 independent Domb values; %d exact finite-block comparisons;' % tested_blocks)
    print('24 exact adjacent sign-pair cells, 18 finite low-shift identities, 100000 sharp-bound/equality tests.')

if __name__ == '__main__':
    test()
