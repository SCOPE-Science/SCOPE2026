#!/usr/bin/env python3
"""Standalone exact and numerical checks for a greedy matching law on complete split graphs."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import exp, factorial

checks = 0

def assert_equal(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def check(cond):
    global checks
    assert cond
    checks += 1

@lru_cache(None)
def deficit_law(a, b):
    """Distribution of the number of chosen internal edges; rational recursion."""
    if a == 0 or (a == 1 and b == 0):
        return ((0, Fraction(1)),)
    edges = a*(a-1)//2 + a*b
    if not edges:
        return ((0, Fraction(1)),)
    p_internal = Fraction(a*(a-1)//2, edges)
    result = defaultdict(Fraction)
    if a >= 2:
        for k, p in deficit_law(a-2, b):
            result[k+1] += p_internal*p
    if b > 0:
        for k, p in deficit_law(a-1, b-1):
            result[k] += (1-p_internal)*p
    return tuple(sorted(result.items()))


def no_internal_product(a, b):
    z = Fraction(1)
    for x in range(1, a+1):
        z *= Fraction(2*(b-a+x), 2*(b-a+x)+x-1)
    return z

@lru_cache(None)
def labeled_law(a, b, used_mask=0):
    """Independent labeled-edge exploration, no part-count transition used."""
    edge_list = [(i, j) for i in range(a) for j in range(i+1, a)]
    edge_list += [(i, a+j) for i in range(a) for j in range(b)]
    available = [(i,j) for i,j in edge_list if not ((used_mask>>i)&1 or (used_mask>>j)&1)]
    if not available:
        return ((0, Fraction(1)),)
    result = defaultdict(Fraction)
    weight = Fraction(1, len(available))
    for i,j in available:
        extra = int(j<a)
        for k,p in labeled_law(a,b,used_mask | (1<<i) | (1<<j)):
            result[k+extra] += p*weight
    return tuple(sorted(result.items()))


def tv_to_poisson(law, lam):
    d = dict(law)
    count = max(d, default=0)
    tv = 0.5*sum(abs(float(d.get(k,0))-exp(-lam)*lam**k/factorial(k)) for k in range(count+1))
    tv += 0.5*(1-sum(exp(-lam)*lam**k/factorial(k) for k in range(count+1)))
    return tv

# Independent finite-state and labeled-vertex recursions.
for a in range(2,7):
    for b in range(a, min(a+5, 9)):
        rational = dict(deficit_law(a,b))
        assert_equal(sum(rational.values()), Fraction(1))
        assert_equal(rational.get(0, Fraction(0)), no_internal_product(a,b))
        assert_equal(deficit_law(a,b), labeled_law(a,b))
        check(all(0 <= k <= a//2 for k in rational))
        check(all(p > 0 for p in rational.values()))
        check(sum((a-k)*p for k,p in rational.items()) >= Fraction(a,2))

# Directly verify each Bernoulli comparison used in the total-variation coupling.
for a in range(2,24):
    for b in (4*a, 5*a, a*a+4*a):
        q_sum = Fraction(0)
        for x in range(1,a+1):
            q = Fraction(x-1,2*b)
            q_sum += q
            for k in range((a-x)//2+1):
                D = 2*b-2*a+3*x+4*k-1
                p = Fraction(x-1,D)
                check(abs(D-2*b) <= 2*a)
                check(D >= Fraction(3*b,2))
                check(abs(p-q) <= Fraction(2*a*(x-1), 3*b*b))
        assert_equal(q_sum, Fraction(a*(a-1),4*b))

# The finite-law error is bounded by the stated all-parameter theorem.
for a in range(2,55):
    for b in (4*a, 5*a, 8*a, max(4*a, a*a), 3*a*a):
        law = deficit_law(a,b)
        lam = a*(a-1)/(4*b)
        check(tv_to_poisson(law,lam) <= a*(a-1)*(14*a-5)/(24*b*b) + 1e-14)
        check(0 <= float(no_internal_product(a,b)) <= 1)

print(f'VERIFY_OK {checks} assertions')
