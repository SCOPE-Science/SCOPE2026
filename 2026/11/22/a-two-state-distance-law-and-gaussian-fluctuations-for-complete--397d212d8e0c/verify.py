#!/usr/bin/env python3
"""Independent vertex-pair distance checks for the unit-flow polytope of a complete DAG.

Usage: python3 verify.py
Uses Python's standard library, integer histograms, and exact rational arithmetic.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def path_edges(mask, m):
    vertices = [0] + [i+1 for i in range(m) if mask & (1 << i)] + [m+1]
    return frozenset(zip(vertices, vertices[1:]))


def brute_histogram(m):
    paths = [path_edges(mask, m) for mask in range(1 << m)]
    hist = Counter()
    for p in paths:
        for q in paths:
            hist[len(p ^ q)] += 1
    return hist


def transfer_histogram(m):
    states = [Counter(), Counter({0: 1})]
    for _ in range(m):
        a,b = states
        na,nb = Counter(),Counter()
        for e,c in a.items():
            na[e] += c
            na[e+1] += 2*c
            nb[e+2] += c
        for e,c in b.items():
            na[e+1] += 2*c
            nb[e] += 2*c
        states = [na,nb]
    a,b=states
    hist = Counter(b)
    for e,c in a.items():
        hist[e+2] += c
    return hist


def mean_exact(m):
    return Fraction(5*m,6) + Fraction(8,9)*(1 - Fraction(1,4**m))


def moment(hist,degree):
    total=sum(hist.values())
    return sum(Fraction(k**degree*v,total) for k,v in hist.items())


def checks():
    for m in range(8):
        a=brute_histogram(m)
        b=transfer_histogram(m)
        assert a == b, (m,a,b)
        assert sum(a.values()) == 4**m
        assert moment(a,1)==mean_exact(m), (m,moment(a,1),mean_exact(m))
        print(f"m={m} paths={2**m} pairs={4**m} mean={moment(a,1)} var={moment(a,2)-moment(a,1)**2} support={sorted(a)}")
    # Larger parameter checks use polynomial recurrence, without enumerating path pairs.
    for m in (8,9,10,12,20,40):
        hist=transfer_histogram(m)
        assert sum(hist.values())==4**m
        assert moment(hist,1)==mean_exact(m)
        var=moment(hist,2)-moment(hist,1)**2
        print(f"m={m} variance_per_site={float(var/m):.12f} target={43/108:.12f}")
    print("CRY_PATH_DISTANCE_EXACT_PASS m=0..7 exhaustive and m<=40 polynomial checks")

if __name__=='__main__':
    checks()
