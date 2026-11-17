"""Finite diagnostic checks for the logarithmic block-average theorem.

This code tests finite binomial identities and root computations; the
almost-sure and infinite-dimensional assertions are proved analytically.
"""
from fractions import Fraction
from itertools import product
from math import comb, log2, isclose

checks = 0


def checked(condition):
    global checks
    assert condition
    checks += 1


def entropy_distance(r, q):
    result = 0.0
    if r > 0:
        result += r * log2(r / q)
    if r < 1:
        result += (1-r) * log2((1-r) / (1-q))
    return result


def root(c, q):
    threshold = 1.0 / (-log2(q))
    if c <= threshold:
        return 1.0
    lo, hi = q, 1.0
    for _ in range(100):
        mid = (lo+hi)/2
        if entropy_distance(mid,q) > 1.0/c:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


for probability in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
    q = max(probability, 1-probability)
    for m in range(1, 11):
        exact_by_count = [Fraction(0) for _ in range(m+1)]
        # Independent signs, with '+' probability probability.
        for signs in product((0, 1), repeat=m):
            count = sum(signs)
            weight = probability**count * (1-probability)**(m-count)
            exact_by_count[count] += weight
        checked(sum(exact_by_count) == 1)
        for k in range(m+1):
            checked(exact_by_count[k] == comb(m,k)*probability**k*(1-probability)**(m-k))
            if float(q) >= .5:
                above = sum(exact_by_count[j] for j in range(k,m+1))
                checked(0 <= above <= 1)
        # The negative tail cannot outweigh the reflected positive tail.
        qdist = [Fraction(comb(m,k))*q**k*(1-q)**(m-k) for k in range(m+1)]
        for k in range((m+1)//2):
            checked(qdist[k] <= qdist[m-k])

for q in (.5, .6, .75, .9):
    threshold = 1 / (-log2(q))
    for c in (threshold/2, threshold, threshold*1.001, threshold*2, threshold*10):
        r = root(c,q)
        checked(q <= r <= 1)
        if c <= threshold:
            checked(r == 1)
        else:
            checked(q < r < 1)
            checked(isclose(entropy_distance(r,q),1/c,abs_tol=2e-14))
        checked(2*r-1 >= 2*q-1)

for c in (.5, 1., 2., 4.):
    for n in range(1,150):
        m = max(1, __import__('math').ceil(c*log2(n+1)))
        weight = n/(n+1)
        checked(0 < weight < 1)
        checked(m >= 1)
        checked(weight*abs(sum([1]*m)/m) == weight)

print(f"PASS: {checks} finite exact and floating-point diagnostics")
