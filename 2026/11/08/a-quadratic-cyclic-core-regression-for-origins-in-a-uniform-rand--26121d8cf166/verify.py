#!/usr/bin/env python3
"""Exact finite verification for the cyclic-core/leaf law of a uniform random mapping.

Run: python3 verify.py
Uses only the Python standard library. Exhaustive enumeration through n=6
is a finite check, not a proof of the all-n identities or asymptotics.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def cyclic_count(f):
    n = len(f)
    cyclic = set()
    done = set()
    for start in range(n):
        if start in done:
            continue
        local = {}
        v = start
        while v not in local and v not in done:
            local[v] = len(local)
            v = f[v]
        if v in local:
            cyclic.update(w for w, j in local.items() if j >= local[v])
        done.update(local)
    return len(cyclic)


def joint_counts(n):
    h = Counter()
    for f in product(range(n), repeat=n):
        indegree = [0] * n
        for v in f:
            indegree[v] += 1
        leaf_count = indegree.count(0)
        h[(cyclic_count(f), leaf_count)] += 1
    return h


def formula_count(n, m, ell):
    if m == n:
        return factorial(n) if ell == 0 else 0
    t = n - m
    if not 0 <= ell <= t:
        return 0
    surj = sum((-1)**j * comb(t-ell,j) * (n-ell-j)**(t-1)
               for j in range(t-ell+1))
    return factorial(n)//factorial(n-m) * m * comb(t,ell) * surj


def expected_cyclic(n):
    return sum(Fraction(k * k * factorial(n),
                        factorial(n-k) * n**(k+1))
               for k in range(1,n+1))


def verify():
    checks = 0
    for n in range(1,7):
        hist = joint_counts(n)
        assert sum(hist.values()) == n**n
        checks += 1
        for m in range(1,n+1):
            for ell in range(n+1):
                assert hist.get((m,ell),0) == formula_count(n,m,ell), (n,m,ell)
                checks += 1
        E_L = sum(Fraction(ell*count,n**n) for (m,ell),count in hist.items())
        E_C = sum(Fraction(m*count,n**n) for (m,ell),count in hist.items())
        E_CL = sum(Fraction(m*ell*count,n**n) for (m,ell),count in hist.items())
        assert E_C == expected_cyclic(n)
        checks += 1
        a = Fraction(n-1,n)
        assert E_L == n*a**n
        checks += 1
        if n >= 2:
            covariance = E_CL-E_C*E_L
            formula = n*a**n * (expected_cyclic(n-1) - expected_cyclic(n))
            assert covariance == formula < 0
            checks += 1
            for m in range(1,n):
                total = sum(c for (k,ell),c in hist.items() if k==m)
                mean = sum(Fraction(ell*c,total) for (k,ell),c in hist.items() if k==m)
                assert mean == (n-m)*a**(n-m-1)
                checks += 1
                for r in range(n-m+1):
                    falling = lambda v,r: factorial(v)//factorial(v-r) if v >= r else 0
                    fmean = sum(Fraction(falling(ell,r)*c,total)
                               for (k,ell),c in hist.items() if k==m)
                    assert fmean == falling(n-m,r)*(1-Fraction(r,n))**(n-m-1)
                    checks += 1
        print(f'n={n}: {n**n} maps; all exact identities match')
    print(f'PASS: {checks} exact comparisons')


if __name__ == '__main__':
    verify()
