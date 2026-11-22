#!/usr/bin/env python3
"""Finite exact checks for symbolic-cylinder periodic closing and border counts.

Only finite instances are tested here; the infinite statements use the analytic proof.
"""
from collections import Counter
from fractions import Fraction


def words(B, n):
    q = len(B)
    curr = [(i,) for i in range(q)]
    for _ in range(1, n):
        curr = [w + (j,) for w in curr for j in range(q) if B[w[-1]][j]]
    return curr


def distance(B, a, b):
    q = len(B)
    frontier = [a]
    for d in range(1, q*q + 2):
        frontier = [v for u in frontier for v in range(q) if B[u][v]]
        if b in frontier:
            return d
    raise ValueError('Graph is not strongly connected')


def formula(B, w):
    n = len(w)
    for p in range(1, n):
        if all(w[i] == w[i+p] for i in range(n-p)):
            return p
    return n-1+distance(B, w[-1], w[0])


def exhaustive(B, w):
    n = len(w)
    q = len(B)
    for p in range(1, n + q*q + 2):
        for t in words(B, p):
            if not B[t[-1]][t[0]]:
                continue
            if all(w[i] == t[i % p] for i in range(n)):
                return p
    raise AssertionError('No periodic completion')


def border_count(w):
    n = len(w)
    return sum(w[:k] == w[n-k:] for k in range(1, n))


def longest_border(w):
    n = len(w)
    return max((k for k in range(1,n) if w[:k]==w[-k:]),default=0)


def test(B, name, nmax):
    print('GRAPH',name)
    for n in range(2,nmax+1):
        ww = words(B,n)
        values = Counter()
        border_events = Counter()
        for w in ww:
            e = formula(B,w)
            if n<=8:
                assert e == exhaustive(B,w), (n,w,e)
            L = longest_border(w)
            if L>0:
                assert e==n-L
            else:
                assert e==n-1+distance(B,w[-1],w[0])
            values[n-e] +=1
            for k in range(1,n):
                if w[:k] == w[-k:]: border_events[k]+=1
        count=len(ww)
        mean=Fraction(sum(v*c for v,c in values.items()),count)
        second=Fraction(sum(v*v*c for v,c in values.items()),count)
        variance=second-mean**2
        expected_borders=Fraction(sum(border_events.values()),count)
        if n in {3,5,9,12,15,nmax}:
            print(f'n={n}, words={count}, mean(n-eta)={float(mean):.8f}, var={float(variance):.8f}, E(number_of_borders)={float(expected_borders):.8f}, P(eta=n+1)={float(Fraction(values[-1],count)):.8f}')
        if name=='lazy_cycle3' and n>=8:
            for k in (1,2,3):
                if k<n: assert abs(Fraction(border_events[k],count)-Fraction(1,3*2**(k-1)))<=Fraction(3,2**(n//2))

if __name__ == '__main__':
    test([[1,1],[1,0]], 'golden_mean', 15)
    test([[1,1,0],[0,1,1],[1,0,1]], 'lazy_cycle3', 16)
    from math import sqrt
    phi=(1+sqrt(5))/2
    G=words([[1,1],[1,0]],15)
    E_G=sum(border_count(w) for w in G)/len(G)
    assert abs(E_G-(phi+2)/(phi*phi))<0.01
    C=words([[1,1,0],[0,1,1],[1,0,1]],16)
    E_C=sum(border_count(w) for w in C)/len(C)
    assert abs(E_C-2/3)<0.005
    print('PASS finite formula, directed closing, Perron-border convergence')
