#!/usr/bin/env python3
"""Finite exact checks of confluence relations on pairs of chains.

Run with Python 3.9+. No non-standard dependencies are required.
"""
from collections import Counter
from itertools import combinations_with_replacement


def confluence_direct(mask, m, n):
    def edge(i, j):
        return bool(mask & (1 << (i*n+j)))
    for i in range(m):
        for j in range(n):
            if not edge(i, j):
                continue
            for ip in range(i, m):
                if not any(edge(ip, jp) for jp in range(j, n)):
                    return False
            for jp in range(j, n):
                if not any(edge(ip, jp) for ip in range(i, m)):
                    return False
    return True


def profile(mask, m, n):
    row = tuple(max((j for j in range(n) if mask & (1 << (i*n+j))), default=-1) for i in range(m))
    col = tuple(max((i for i in range(m) if mask & (1 << (i*n+j))), default=-1) for j in range(n))
    return row, col


def monotone(xs):
    return all(xs[i] <= xs[i+1] for i in range(len(xs)-1))


def cube_polynomial(m, n):
    """Polynomial coefficient map: number of confluent matrices by arrow count."""
    coeff = Counter()
    cubes = 0
    max_free = 0
    max_skeleton = 0
    for r in combinations_with_replacement(range(-1,n),m):
        for c in combinations_with_replacement(range(-1,m),n):
            if any(c[r[i]] < i for i in range(m) if r[i]>=0):
                continue
            if any(r[c[j]] < j for j in range(n) if c[j]>=0):
                continue
            low = {(i,r[i]) for i in range(m) if r[i]>=0}
            low.update((c[j],j) for j in range(n) if c[j]>=0)
            upper = {(i,j) for i in range(m) for j in range(n) if j<=r[i] and i<=c[j]}
            assert low <= upper
            free = upper - low
            assert free == {(i,j) for i in range(m) for j in range(n) if j<r[i] and i<c[j]}
            cubes += 1
            max_free = max(max_free,len(free))
            max_skeleton = max(max_skeleton,len(low))
            # Every element of a Boolean cube is an arbitrary subset of the free cells.
            from math import comb
            for t in range(len(free)+1):
                coeff[len(low)+t] += comb(len(free),t)
    return coeff,cubes,max_free,max_skeleton


def check():
    checks = 0
    for m,n in [(1,1),(1,3),(2,2),(2,3),(3,2),(2,4),(3,3),(3,4),(4,3),(4,4)]:
        actual = Counter()
        for mask in range(1<<(m*n)):
            b = confluence_direct(mask,m,n)
            r,c = profile(mask,m,n)
            assert b == (monotone(r) and monotone(c)),(m,n,mask,r,c,b)
            if b:
                actual[mask.bit_count()] += 1
            checks += 1
        predicted,cubes,max_free,max_skeleton = cube_polynomial(m,n)
        assert actual == predicted,(m,n,actual,predicted)
        assert max_free == (m-1)*(n-1)
        assert max_skeleton == m+n-1
        print('RECTANGULAR_OK',m,n,sum(actual.values()),'cubes',cubes)
    counts = [2,9,118,4849,697066,378458905]
    for n,want in enumerate(counts,1):
        predicted,cubes,max_free,max_skeleton = cube_polynomial(n,n)
        assert sum(predicted.values()) == want,(n,sum(predicted.values()))
        assert max_free==(n-1)**2 and max_skeleton==2*n-1
        print('SQUARE_OK',n,want,'cubes',cubes)
    print('VERIFY_OK',checks,'directly examined relation matrices')

if __name__ == '__main__':
    check()
