#!/usr/bin/env python3
"""Finite checks for a moving pairwise-difference theorem.

All exact tests use rational arithmetic; finite tests do not replace
its all-window proof by the complete-graph cut argument.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
from random import Random

def variation(a):
    return sum(abs(a[i + 1] - a[i]) for i in range(len(a) - 1))

def gini(x, m):
    c = Q(comb(m, 2))
    return [sum(abs(x[p] - x[q]) for p in range(i, i + m)
                for q in range(p + 1, i + m)) / c
            for i in range(len(x) - m + 1)]

def clipped_pair(x, m, bound):
    c = Q(comb(m, 2))
    return [sum(min(abs(x[p] - x[q]), bound) for p in range(i, i + m)
                for q in range(p + 1, i + m)) / c
            for i in range(len(x) - m + 1)]

def sharp(m):
    return Q(2 * (m * m // 4), comb(m, 2))

# Exhaustively test the robust algebraic bound even when cross-pair
# responses are independently arbitrary signs (a larger class than rank orders).
for m in range(2, 7):
    pairs = [(a, b) for a in range(1, m) for b in range(1, m - a + 1)]
    max_seen = 0
    for signs in product((-1, 1), repeat=len(pairs)):
        s = [0] * (m + 1)
        for (a, b), e in zip(pairs, signs):
            for l in range(a, m - b + 1):
                s[l] += e
        val = variation(s)
        assert val <= 2 * (m * m // 4), (m, signs, s, val)
        max_seen = max(max_seen, val)
    assert max_seen == 2 * (m * m // 4), (m, max_seen)
print('EXHAUSTIVE_ARBITRARY_PAIR_SIGNS_AND_COMPLETE_GRAPH_CUT_PASS m=2..6')

# Exact attained sharpness; insert extra samples after the window.
for m in range(2, 33):
    for n in (2*m, 2*m+3):
        x = [Q(i) for i in range(1, n+1)]
        y = [z + (Q(1) if i >= m else 0) for i,z in enumerate(x)]
        base = variation([a - b for a,b in zip(y,x)])
        gain = variation([a-b for a,b in zip(gini(y,m),gini(x,m))])
        assert base == 1 and gain == sharp(m), (m,n,base,gain,sharp(m))
print('EXACT_ATTAINING_WITNESSES_PASS m=2..32 n=2m,2m+3')

rng=Random(240117)
for k in range(1200):
    m = rng.randint(2, 8)
    n = rng.randint(m, m+12)
    x = [Q(rng.randint(-25, 25), rng.randint(1, 9)) for _ in range(n)]
    y = [Q(rng.randint(-25, 25), rng.randint(1, 9)) for _ in range(n)]
    dx = variation([a-b for a,b in zip(x,y)])
    dg = variation([a-b for a,b in zip(gini(x,m),gini(y,m))])
    assert dg <= sharp(m) * dx, (m,n,k,dg,dx,sharp(m))
    if k % 4 == 0:
        bound = Q(rng.randint(1, 15), 5)
        dc = variation([a-b for a,b in zip(clipped_pair(x,m,bound),clipped_pair(y,m,bound))])
        assert dc <= sharp(m) * dx, (m,n,k,dc,dx,sharp(m))
print('EXACT_RANDOM_TWO_INPUT_GINI_AND_CLIPPED_PAIR_VARIATION_PASS 1200,300')

# Exercise a general pairwise nonlinearity over an isolated single edge.
for k in range(200):
    m=rng.randint(2,9)
    n=rng.randint(m,m+14)
    j=rng.randrange(1,n)
    t=Q(rng.randint(-20,20) or 1, 7)
    x=[Q(rng.randint(-12,12),5) for _ in range(n)]
    z=[v+(t if i>=j else Q(0)) for i,v in enumerate(x)]
    a=clipped_pair(x,m,Q(5,2));b=clipped_pair(z,m,Q(5,2))
    assert variation([c-d for c,d in zip(a,b)]) <= abs(t)*sharp(m)
print('EXACT_ONE_EDGE_TELESCOPING_TESTS_PASS 200')
print('ALL_MOVING_PAIRWISE_GINI_CHECKS_PASS')
