"""Standalone exact checks for circular moving-maximum change indicators.
Run with: python verify.py
No third-party dependencies.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def indicator(order, k, i):
    n = len(order)
    window = [(i + j) % n for j in range(k + 1)]
    top = max(window, key=lambda a: order[a])
    return int(top == i % n or top == (i + k) % n)


def pair_formula(k, d):
    p = F(4, (k + 1) * (k + d + 1))
    if d == k:
        p += F(1, 2 * k + 1)
    return p


def cov_formula(k, d):
    if d < k:
        return F(-4 * d, (k + 1)**2 * (k + d + 1))
    return F((k - 1)**2, (k + 1)**2 * (2 * k + 1))


def variance_formula(k):
    p = F(2, k + 1)
    return p * (1 - p) + 2 * sum((cov_formula(k, d) for d in range(1, k + 1)), F(0))


def harmonic_formula(k):
    h = sum((F(1, j) for j in range(k + 2, 2*k + 2)), F(0))
    return F(2, k + 1) - F(4 * (2*k + 1), (k + 1)**2) + F(8, k + 1) * h + F(2, 2*k + 1)


def brute_local(k, d):
    n = k + d + 1
    count = 0
    for p in permutations(range(n)):
        count += indicator(p, k, 0) * indicator(p, k, d)
    return F(count, factorial(n))


def brute_circle(k, n):
    es = F(0)
    es2 = F(0)
    for p in permutations(range(n)):
        t = sum(indicator(p, k, i) for i in range(n))
        es += t
        es2 += t*t
    size = factorial(n)
    return es/size, es2/size-(es/size)**2


def run():
    cases = 0
    for k in range(2, 15):
        assert variance_formula(k) == harmonic_formula(k)
        assert variance_formula(k) > F(2*k*(k-1), 3*(k+1)**2*(2*k+1)) or k==2
        assert all(cov_formula(k, d) < 0 for d in range(1, k))
        assert cov_formula(k, k) > 0
        cases += 4
    for k in range(2, 5):
        for d in range(1, k+1):
            observed = brute_local(k, d)
            assert observed == pair_formula(k, d), (k, d, observed, pair_formula(k,d))
            assert observed - F(4, (k+1)**2) == cov_formula(k,d)
            cases += 2
    for k,n in ((2,7),(3,8),(4,9)):
        m,v=brute_circle(k,n)
        assert m == F(2*n,k+1), (k,n,m)
        assert v == n*variance_formula(k), (k,n,v)
        cases+=2
    print('PASS',cases,'exact identities, including exhaustive local orders and cyclic permutations')

if __name__ == '__main__':
    run()
