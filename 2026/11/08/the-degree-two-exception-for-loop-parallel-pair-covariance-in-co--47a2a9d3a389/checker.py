#!/usr/bin/env python3
"""Exact validation for finite matching-model loop/multiplicity covariances."""
from fractions import Fraction
from math import comb
from itertools import product


def formula(degrees):
    N = sum(degrees)
    assert N >= 6 and N % 2 == 0 and all(d >= 0 for d in degrees)
    a = [comb(d, 2) for d in degrees]
    S = sum(a)
    T = sum(a[i] * a[j] for i in range(len(a)) for j in range(i + 1, len(a)))
    W = sum(a[i] * a[j] * (2 * degrees[i] + 2 * degrees[j] - 6)
            for i in range(len(a)) for j in range(i + 1, len(a)))
    return Fraction(2 * (4 * S * T - (N - 1) * W),
                    (N - 1)**2 * (N - 3) * (N - 5))


def predicted_sign(degrees):
    high = [d for d in degrees if d >= 2]
    if len(high) < 2:
        return 0
    if len(high) >= 3 and set(high) == {2} and all(d != 1 for d in degrees):
        return 1
    return -1


def brute(degrees):
    N = sum(degrees)
    label = [i for i, d in enumerate(degrees) for _ in range(d)]
    counts = [0, 0, 0, 0]
    def rec(stubs, edgelist):
        if not stubs:
            L = sum(x == y for x, y in edgelist)
            mult = {}
            for x, y in edgelist:
                if x != y:
                    mult[(x, y)] = mult.get((x, y), 0) + 1
            P = sum(k*(k-1)//2 for k in mult.values())
            counts[0] += 1
            counts[1] += L
            counts[2] += P
            counts[3] += L*P
            return
        first = stubs[0]
        for j in range(1, len(stubs)):
            second = stubs[j]
            rec(stubs[1:j] + stubs[j+1:],
                edgelist + [tuple(sorted((label[first], label[second])))] )
    rec(tuple(range(N)), [])
    C, SL, SP, SLP = counts
    return Fraction(SLP, C) - Fraction(SL * SP, C*C)


def regformula(n, d):
    N = n*d
    a = comb(d, 2)
    return Fraction(n*(n-1)*a*a*(2*N*(2-d)+4*d-6),
                    (N-1)**2*(N-3)*(N-5))


def run():
    checks = 0
    for n in range(2, 6):
        for ds in product(range(0, 7), repeat=n):
            N = sum(ds)
            if N < 6 or N > 10 or N % 2:
                continue
            expected = formula(ds)
            observed = brute(ds)
            assert observed == expected, (ds, observed, expected)
            checks += 1
    for n in range(2, 7):
        for ds in product(range(0, 7), repeat=n):
            N = sum(ds)
            if N < 6 or N % 2:
                continue
            val = formula(ds)
            sign = (val > 0) - (val < 0)
            assert sign == predicted_sign(ds), (ds, val, sign)
            checks += 1
    for d in range(2, 8):
        for n in range(2, 16):
            if n*d < 6 or n*d % 2:
                continue
            assert formula([d]*n) == regformula(n, d)
            checks += 1
    for x, y, z in product(range(0, 8), repeat=3):
        q = ((x+1)*(y+1)*(x+y-z)
             +(x+1)*(z+1)*(x+z-y)
             +(y+1)*(z+1)*(y+z-x))
        p = (x+y+z + 2*(x*x+y*y+z*z)
             +x*x*y+x*x*z+x*y*y+x*z*z+y*y*z+y*z*z-3*x*y*z)
        assert q == p and q >= 0
        checks += 1
    print('PASS:', checks, 'exact assertions')

if __name__ == '__main__':
    run()
