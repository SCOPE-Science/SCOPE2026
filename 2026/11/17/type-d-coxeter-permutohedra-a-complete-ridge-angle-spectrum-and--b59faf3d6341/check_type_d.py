#!/usr/bin/env python3
"""Exact finite checks of a type-D Coxeter-fan Euclidean ridge-angle theorem.

The fan rays are orbit images of fundamental weights. All two-dimensional
cones of a simplicial Coxeter fan arise from unordered pairs of chamber rays.
This program needs only Python's standard library.
"""
import itertools
import math
from collections import Counter
from fractions import Fraction


def doubled_weights(n):
    w = [tuple(2 if j < k else 0 for j in range(n)) for k in range(1, n-1)]
    w.append(tuple(1 if j < n-1 else -1 for j in range(n)))
    w.append(tuple([1] * n))
    assert len(w) == n
    return w


def expected(n):
    h = Counter()
    for ell in range(2, n-1):
        for k in range(1, ell):
            h[Fraction(k, ell)] += 2**ell * math.comb(n, ell) * math.comb(ell, k)
    for k in range(1, n-1):
        h[Fraction(k, n)] += 2**n * math.comb(n, k)
    h[Fraction((n-2)**2, n**2)] += n * 2**(n-1)
    r = 5**n - 2*3**n + 1 - n*4**(n-1) + n*2**(n-1)
    assert r == sum(h.values())
    return r, h


def actual(n):
    rays = doubled_weights(n)
    pairs = set()
    for perm in itertools.permutations(range(n)):
        for signs in itertools.product((-1, 1), repeat=n):
            if math.prod(signs) != 1:
                continue
            vv = [tuple(signs[j] * ray[perm[j]] for j in range(n)) for ray in rays]
            for a, b in itertools.combinations(vv, 2):
                pairs.add((a, b) if a < b else (b, a))
    h = Counter()
    for a, b in pairs:
        dot = sum(x*y for x,y in zip(a,b))
        aa = sum(x*x for x in a)
        bb = sum(y*y for y in b)
        assert dot > 0, (a,b,dot)
        h[Fraction(dot*dot, aa*bb)] += 1
    return len(pairs), h


def mean_by_formula(n):
    r, _ = expected(n)
    raw = []
    for ell in range(2, n-1):
        for k in range(1, ell):
            raw.append((2**ell * math.comb(n,ell)*math.comb(ell,k),math.sqrt(k/ell)))
    for k in range(1, n-1):
        raw.append((2**n*math.comb(n,k),math.sqrt(k/n)))
    raw.append((n*2**(n-1),(n-2)/n))
    m = math.fsum(c*(math.pi-math.acos(z)) for c,z in raw) / r
    exact = 3*math.pi/4-math.pi*n*2**(n-3)/r
    assert abs(m-exact) < 1e-11


for n in (4,5,6):
    r, h=expected(n)
    ar, ah=actual(n)
    assert (ar,ah)==(r,h),(n,r,ar,h-ah,ah-h)
    print(f"rank={n} ridges={r} angle_levels={len(h)} rational_gram=PASS")
for n in range(4,31):
    mean_by_formula(n)
print('TYPE_D_RIDGE_ANGLE_PASS')
