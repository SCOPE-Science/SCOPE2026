#!/usr/bin/env python3
"""Exact finite checks for Euclidean deep holes of order polytopes.

No dependencies outside the Python standard library. The mathematical proof
covers every finite poset; the enumerations here are finite checks only.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb


def pava_distance(bits):
    blocks = []
    for bit in bits:
        blocks.append([bit, 1])
        while len(blocks) > 1 and F(*blocks[-2]) > F(*blocks[-1]):
            a, b = blocks.pop()
            blocks[-1][0] += a
            blocks[-1][1] += b
    fit = [F(s, n) for s, n in blocks for _ in range(n)]
    return sum((F(v)-y)**2 for v, y in zip(bits, fit))


def hall(bits, relation):
    n = len(bits)
    positives = [i for i, x in enumerate(bits) if x == 1]
    negatives = [i for i, x in enumerate(bits) if x == 0]
    k = len(positives)
    if k == 0 or k == n:
        return False
    for r in range(1, k+1):
        for ss in combinations(positives, r):
            reachable = {j for i in ss for j in negatives if relation[i][j]}
            if (n-k)*r > k*len(reachable):
                return False
    return True


def chain_rel(n):
    return [[i < j for j in range(n)] for i in range(n)]


def fence_rel(n):
    # Alternating height-two fence: every odd-indexed element is minimal.
    return [[(i % 2 == 0 and j % 2 == 1 and abs(i-j) == 1)
             for j in range(n)] for i in range(n)]


def target_count(n):
    if n % 2 == 0:
        m = n//2
        return comb(2*m, m)//(m+1)
    k = n//2
    return 2*comb(n, k)//n


def main():
    total = 0
    for n in range(2, 13):
        relation = chain_rel(n)
        maxdist = F((n*n)//4, n)
        deep = []
        for b in product([0,1], repeat=n):
            dist = pava_distance(b)
            assert dist <= maxdist, (n,b,dist,maxdist)
            expected = sum(b) in {n//2, (n+1)//2} and hall(b, relation)
            assert (dist == maxdist) == expected, (n,b,dist,expected)
            if dist == maxdist:
                deep.append(b)
            total += 1
        assert len(deep) == target_count(n), (n,len(deep),target_count(n))
    fencechecked = 0
    for n in range(2, 13):
        rel = fence_rel(n)
        maxdist = F((n*n)//4, n)
        satisfiers=[]
        for b in product([0,1],repeat=n):
            if sum(b) not in {n//2,(n+1)//2}:
                continue
            if hall(b,rel):
                satisfiers.append(b)
            fencechecked += 1
        assert len(satisfiers)==1,(n,satisfiers)
        b=satisfiers[0]
        assert all((b[i] == 1 if i%2 == 0 else b[i]==0) for i in range(n))
        # A rational nonnegative flow along every covering edge certifies that
        # the constant vector t = (#ones)/n is the closest order point.
        k=sum(b); flux=[F(0) for _ in range(n-1)]
        running=F(0)
        for i in range(n-1):
            running += F(b[i])-F(k,n)
            flux[i] = running if i%2==0 else -running
        assert all(x>=0 for x in flux),(n,flux)
        assert sum((F(v)-F(k,n))**2 for v in b)==maxdist
    print('ORDER_POLYTOPE_DEEP_HOLES_PASS chain_bits=%d fence_balanced=%d n=2..12' % (total,fencechecked))

if __name__=='__main__':
    main()
