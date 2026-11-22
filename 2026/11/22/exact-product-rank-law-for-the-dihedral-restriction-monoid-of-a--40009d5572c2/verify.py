#!/usr/bin/env python3
"""Exact-arithmetic checks of product ranks in dihedral restriction monoids."""
from collections import Counter
from fractions import Fraction
from math import comb


def cyclic_restrictions(n):
    maps = set()
    for sign in (1, -1):
        for shift in range(n):
            group_map = tuple((sign * x + shift) % n for x in range(n))
            for mask in range(1 << n):
                maps.add(tuple(group_map[x] if mask & (1 << x) else -1 for x in range(n)))
    return tuple(sorted(maps))


def polynomial(n):
    # Polynomial operations, with Fractions to certify integer coefficients.
    def mul(A, B):
        C = [Fraction(0)] * (len(A) + len(B) - 1)
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                C[i+j] += a*b
        return C
    def power(A, k):
        X = [Fraction(1)]
        for _ in range(k):
            X = mul(X, A)
        return X
    even = n % 2 == 0
    a = Fraction(1) - Fraction(1, 2*n)
    S = a + Fraction(n, 2) + (Fraction(n, 4) if even else 0)
    v = Fraction(1 + int(even), 2)
    B = [Fraction(2**n)*a]
    def add(A, B, factor=1):
        C = list(A) + [Fraction(0)] * max(0, len(B) - len(A))
        for i, b in enumerate(B):
            C[i] += factor*b
        return C
    B = add(B, [Fraction(n*2**(n-2)),Fraction(n*2**(n-2))])
    if even:
        B = add(B, [Fraction(n*2**(n-4)),Fraction(n*2**(n-3)),Fraction(n*2**(n-4))])
    C = add([S*S], [-n*v*v, n*v*v])
    if even:
        C = add(C,[Fraction(n,8),Fraction(-n,4),Fraction(n,8)])
    total = add(add(power([3,1], n), B, -2), C)
    return [4*n*n*z for z in total], S, v


def brute(n):
    maps = cyclic_restrictions(n)
    actual = Counter()
    for f in maps:
        for g in maps:
            rank = sum(1 for x in range(n) if g[x] != -1 and f[g[x]] != -1)
            actual[rank] += 1
    theoretical, S, v = polynomial(n)
    assert all(x.denominator == 1 for x in theoretical)
    assert [actual[k] for k in range(n+1)] == [int(x) for x in theoretical], (n, actual, theoretical)
    assert sum(actual.values()) == len(maps)**2 == 4*n*n*(2**n-S)**2
    mean = sum(k*actual[k] for k in range(n+1))/len(maps)**2
    predicted_mean = n*float((Fraction(2**(n-1))-v)/(Fraction(2**n)-S))**2
    assert abs(mean-predicted_mean) < 1e-10
    print('n=%d size=%d coefficients=%s PASS' % (n,len(maps),[actual[k] for k in range(n+1)]))

if __name__ == '__main__':
    for n in range(3,8):
        brute(n)
    print('VERIFY_OK_CYCLE_RESTRICTION_PRODUCT_RANKS')
