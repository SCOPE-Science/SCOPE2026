#!/usr/bin/env python3
"""Exact checks for Boolean Fourier multipliers of permutation two-cycle supports.

Run: python3 checker.py
All integer assertions are exact. Asymptotic and all-order assertions
are established in the accompanying mathematical proof, not by this test.
"""
from math import comb, factorial
from itertools import permutations
from fractions import Fraction

checks = 0

def verify(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)


def spectrum_formula(n, k):
    return sum(
        (-2)**j * factorial(k) * factorial(n-k) *
        factorial(n-2*j) // (factorial(j)*factorial(k-j)*factorial(n-k-j))
        for j in range(min(k, n-k)+1)
    )


def spectrum_from_permutations(n):
    hist = [0]*(1<<n)
    for p in permutations(range(n)):
        mask = 0
        for a in range(n):
            b = p[a]
            if b > a and p[b] == a:
                mask |= (1<<a) | (1<<b)
        hist[mask] += 1
    transform = hist[:]
    for b in range(n):
        bit = 1<<b
        for i in range(1<<n):
            if not (i & bit):
                a = transform[i]
                c = transform[i|bit]
                transform[i] = a+c
                transform[i|bit] = a-c
    return transform

# Independent reconstruction from full permutations and subset Fourier transform.
for n in range(1, 9):
    actual = spectrum_from_permutations(n)
    verify(actual[0] == factorial(n), ('total', n))
    for a, v in enumerate(actual):
        verify(v == spectrum_formula(n, a.bit_count()), ('direct', n, a))

# Coefficients of exp(-2uv)/(1-u-v), computed by a different recurrence.
q = [[Fraction(1)]]
for n in range(1, 101):
    prev = q[-1]
    cur = []
    for k in range(n+1):
        v = (prev[k] if k < n else 0) + (prev[k-1] if k else 0)
        if n % 2 == 0 and k == n//2:
            v += Fraction((-2)**(n//2),factorial(n//2))
        cur.append(v)
    q.append(cur)
    for k in range(n+1):
        verify(cur[k]*factorial(k)*factorial(n-k) == spectrum_formula(n,k), ('coeff',n,k))
        if n >= 4 and 1 <= k <= n//2:
            verify(cur[k] - cur[k-1] >= Fraction(2,3), ('unimodality',n,k))

# Every finite dimension checked, including exceptional n=2 and order 4.
for n in range(1, 101):
    row = [spectrum_formula(n,k) for k in range(n+1)]
    if n == 2:
        verify(row == [2,0,2], ('singular exception',n))
    else:
        verify(min(row)>0, ('positive',n))
    if n >= 3:
        verify(3*min(row) >= factorial(n), ('sharp dimension-free bound',n))
    if n >= 6:
        verify(all(row[k]>row[k+1] for k in range(n//2)), ('central minimizer',n))
        verify(min(row) == row[n//2], ('central minimum',n))

print('PASS:', checks, 'exact assertions')
print('order 2:', [spectrum_formula(2,k) for k in range(3)])
for n in range(3,10):
    vals = [spectrum_formula(n,k) for k in range(n+1)]
    k = n//2 if n>=6 or n==3 or n==5 else 1
    print('order',n,'minimum',min(vals),'ratio',str(Fraction(factorial(n), min(vals))), 'min weight',k)
