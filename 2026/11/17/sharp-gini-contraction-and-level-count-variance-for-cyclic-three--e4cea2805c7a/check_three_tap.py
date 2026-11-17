#!/usr/bin/env python3
"""Standalone exact-integer finite checks for cyclic three-point averaging.

Run with Python 3. The all-order proof is mathematical, not computational.
"""
from fractions import Fraction
from random import Random


def gini3_window_counts(mask, n):
    digits = [(mask >> i) & 1 for i in range(n)]
    q = [digits[(i - 1) % n] + digits[i] + digits[(i + 1) % n]
         for i in range(n)]
    hist = [q.count(j) for j in range(4)]
    numerator = sum((j-i)*hist[i]*hist[j]
                    for i in range(4) for j in range(i+1, 4))
    return digits, q, hist, numerator


def is_one_cyclic_arc(digits):
    n = len(digits)
    return sum(digits[i] and not digits[i-1] for i in range(n)) == 1


count = 0
for n in range(3, 17):
    F = (n*n)//4
    sharp_found = False
    for mask in range(1, 2**n-1):
        x, q, h, numerator = gini3_window_counts(mask, n)
        k = sum(x)
        deficit3 = 3*k*(n-k) - numerator
        d = h[1] + h[2] + h[3]
        b = h[2] + h[3]
        e = h[3]
        assert deficit3 == (d-k)**2 + (b-k)**2 + (e-k)**2
        if n == 3:
            assert numerator == 0
        else:
            assert numerator * F <= (3*F-8)*k*(n-k)
            if numerator * F == (3*F-8)*k*(n-k):
                sharp_found = True
                if n >= 5:
                    assert k in ((n//2), ((n+1)//2))
                    assert is_one_cyclic_arc(x)
        if 2 <= k <= n-2:
            assert deficit3 >= 8
            if deficit3 == 8 and n >= 5:
                assert is_one_cyclic_arc(x)
        else:
            assert deficit3 == 6
        count += 1
    assert (n == 3 or sharp_found)
print('ALL_CUTS_EXHAUSTIVE_EXACT_N3_TO_N16_PASSED',count)

# Values for general vectors have denominator 3 and are tested without roundoff.
rng=Random(271828)
nonbin_count=0
for n in range(3, 20):
    F=n*n//4
    for _ in range(450):
        x=[rng.randrange(-20, 21) for _ in range(n)]
        before=sum(abs(x[i]-x[j]) for i in range(n) for j in range(i+1,n))
        y=[x[(i-1)%n]+x[i]+x[(i+1)%n] for i in range(n)]
        after3=sum(abs(y[i]-y[j]) for i in range(n) for j in range(i+1,n))
        if n==3:
            assert after3==0
        else:
            assert after3*F <= (3*F-8)*before
        nonbin_count+=1
print('EXACT_INTEGER_NONBINARY_INPUTS_PASSED',nonbin_count)

# Structural exceptional case: on 4 sites the smoother is a centered
# antipodal reversal scaled by -1/3, so the Gini ratio is always 1/3.
for _ in range(1000):
    x=[rng.randrange(-100,101) for i in range(4)]
    y=[x[(i-1)%4]+x[i]+x[(i+1)%4] for i in range(4)]
    assert sum(abs(y[i]-y[j]) for i in range(4) for j in range(i+1,4)) == sum(abs(x[i]-x[j]) for i in range(4) for j in range(i+1,4))
print('FOUR_SITE_EXACT_GINI_SIMILARITY_PASSED')

# Explicit symbolic-equivalent integer comparison with the Dobrushin
# coefficient: for n >= 6, rows centered three positions apart have
# disjoint supports, so oscillation norm equals one.
for n in range(6,100):
    supp0={(n-1)%n,0,1}
    supp3={2,3,4}
    assert not(supp0 & supp3)
print('DOBRUSHIN_SEPARATION_N6_TO_N99_PASSED')
print('ALL_THREE_TAP_GINI_CHECKS_PASSED')
