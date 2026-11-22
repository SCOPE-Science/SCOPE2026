#!/usr/bin/env python3
"""Exact finite checks for the canonical skew Hochschild polytope.

This checks representative finite dimensions; the all-dimensional statement
follows from the block-merging and simplex-projection proof in RESULT.md.
"""
from fractions import Fraction
from math import comb
from itertools import product


def vertices(n):
    # A vertex is indexed by a composition of [n], encoded by break positions.
    weights = [n - j for j in range(1, n + 1)]
    for cuts in product((False, True), repeat=n-1):
        endpoints = [i for i, b in enumerate(cuts, start=1) if b] + [n]
        last = 0
        v = [0] * n
        for end in endpoints:
            v[end-1] = sum(weights[last:end])
            last = end
        yield tuple(v)


def exact_formula(n):
    assert n >= 2
    T = n * (n-1) // 2
    possible = [k for k in range(1, n+1)
                if k*(k-1)*(k-2) < 3*T <= k*(k*k-1)]
    assert len(possible) == 1, (n, possible)
    k = possible[0]
    lam = Fraction(T + comb(k, 3), k)
    a = [comb(n-i, 2) for i in range(1, n+1)]
    c = [max(Fraction(0), lam-ai) for ai in a]
    R2 = Fraction(T*T) + sum(comb(j,2)**2 for j in range(k)) - k*lam*lam
    eligible = sum(ai <= lam for ai in a)
    expected_contacts = 1 << (eligible-1)
    return T, k, lam, a, c, R2, expected_contacts


def check(n):
    T,k,lam,a,c,R2,expected_contacts = exact_formula(n)
    assert sum(c) == T
    assert c == sorted(c)
    for j in range(1,n):
        assert sum(c[:j]) <= sum(n-i for i in range(1,j+1))
    V = list(vertices(n))
    assert len(V) == 2**(n-1) == len(set(V))
    contacts = 0
    for v in V:
        assert sum(v) == T
        assert sum(vi*vi+2*ai*vi for vi,ai in zip(v,a)) == T*T
        d2 = sum((Fraction(vi)-ci)**2 for vi,ci in zip(v,c))
        assert d2 <= R2, (n,v,d2,R2)
        if d2 == R2:
            contacts += 1
            assert all(vi==0 for vi,ai in zip(v,a) if ai>lam)
        else:
            assert any(vi>0 and ai>lam for vi,ai in zip(v,a))
    assert contacts==expected_contacts, (n,contacts,expected_contacts)
    return k,lam,R2,contacts


if __name__=='__main__':
    for n in range(2,13):
        k,lam,R2,contacts=check(n)
        print(f'n={n:2d} k={k:2d} lambda={lam} R2={R2} contacts={contacts}')
    print('HOCHSCHILD_SKEW_CIRCUMSPHERE_EXACT_PASS')
