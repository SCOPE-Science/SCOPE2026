#!/usr/bin/env python3
"""Exact checks for a four-distance Katetov near-leaf spectrum."""
from itertools import product
from math import comb

def coefficients(n):
    assert n >= 1
    c = [comb(n, j) * (1 + 3 * (1 << (n-j))) for j in range(n+1)]
    c[1] += n * (1 + (1 << n))
    return c

def enumerate_types(n):
    """Independent full diagram enumeration; old center-leaf edges 2, leaf-leaf edges 4."""
    totals = [0] * (n + 1)
    for vector in product((1, 2, 3, 4), repeat=n+1):
        cx, leaves = vector[0], vector[1:]
        if any(not (abs(cx-y) <= 2 <= cx+y) for y in leaves):
            continue
        if any(not (abs(leaves[i]-leaves[j]) <= 4 <= leaves[i]+leaves[j])
               for i in range(n) for j in range(i+1, n)):
            continue
        totals[sum(y <= 2 for y in leaves)] += 1
    return totals

def log_concave_at(c, j):
    return c[j] * c[j] >= c[j-1] * c[j+1]

def unimodal(c):
    mode = max(range(len(c)), key=c.__getitem__)
    return all(c[i] <= c[i+1] for i in range(mode)) and all(
        c[i] >= c[i+1] for i in range(mode, len(c)-1))

def check():
    for n in range(1, 8):
        expect = coefficients(n)
        observed = enumerate_types(n)
        assert observed == expect, (n, observed, expect)
    for n in range(1, 301):
        c = coefficients(n)
        assert sum(c) == (1 << n) + 3 * (3**n) + n*(1+(1 << n))
        assert unimodal(c), n
        faults = [j for j in range(1, n) if not log_concave_at(c, j)]
        assert faults == ([] if n <= 10 else [2]), (n, faults)
        if n >= 3:
            Q = 1 << n
            D = c[2]**2 - c[1]*c[3]
            expression = (n*n*(n-1)*((33-3*n)*Q*Q+(136-32*n)*Q+80-16*n))//192
            assert D == expression, (n,D,expression)
    n=11
    c=coefficients(n)
    print('n=11: c0,c1,c2,c3,c4=',c[:5])
    print('n=11: c2^2 - c1*c3=',c[2]**2-c[1]*c[3])
    print('Brute-force diagram checks: 1..7 leaves')
    print('Shape and exact identity checks: 1..300 leaves')
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
