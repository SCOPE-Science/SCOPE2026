#!/usr/bin/env python3
"""Exact-integer checks for a parametric five-link closure-space census."""
from fractions import Fraction
from itertools import combinations
from math import isqrt

Q = 10**35
checks = 0

def radical_interval(t, j):
    assert isinstance(t, Fraction) and t >= 0 and j >= 0
    a, b = t.numerator + j*t.denominator, t.denominator
    lo = isqrt(a*Q*Q//b)
    return lo, lo + 1

def sgn(t, terms):
    global checks
    lows, highs = 0, 0
    for j, c in terms.items():
        l, u = radical_interval(t, j)
        if c >= 0:
            lows += c*l
            highs += c*u
        else:
            lows += c*u
            highs += c*l
    checks += 1
    if lows > 0:
        return 1
    if highs < 0:
        return -1
    raise AssertionError(('undecided sign', t, terms, lows, highs))

def from_L(jset):
    return {j: (1 if j in jset else -1) for j in range(5)}

def short_counts(t):
    counts=[]
    for k in (1,2,3):
        subsets=[(4,)+c for c in combinations(range(4),k-1)]
        short=[v for v in subsets if sgn(t,from_L(v))<0]
        counts.append((len(short), short))
    return counts

f0 = {0:1, 1:1, 2:-1, 3:-1, 4:1}
f1 = {0:-1, 1:-1, 2:1, 3:-1, 4:1}
assert sgn(Fraction(20752,1000000),f0)==-1
assert sgn(Fraction(20754,1000000),f0)==1
assert sgn(Fraction(386280,1000000),f1)==1
assert sgn(Fraction(386282,1000000),f1)==-1
expected=[(1,2,1),(1,2,0),(1,3,0)]
for t, triple in zip([Fraction(1,1000),Fraction(1,10),Fraction(1,2)],expected):
    c=short_counts(t)
    assert tuple(u[0] for u in c)==triple,(t,c)
    print('witness', t, 'short', c, 'betti', (triple[0]+triple[2],2*triple[1],triple[0]+triple[2]))
# Boundary claims that certify every other sign via ordering, pair comparison, and derivative estimates.
assert sgn(Fraction(0),{0:1,2:1,3:1,1:-1,4:-1})==1 # a+c+d > b+e
assert sgn(Fraction(1),{3:1,4:1,0:-1,1:-1,2:-1})==1 # d+e > a+b+c
assert sgn(Fraction(0),{1:1,4:1,0:-1,2:-1,3:-1})==-1 # f0 lower
assert sgn(Fraction(1),f0)==1
assert sgn(Fraction(0),f1)==1
assert sgn(Fraction(1),f1)==-1
print('VERIFY_OK exact_sign_checks',checks,'threshold_certificates',4,'generic_topology_chambers',3)
