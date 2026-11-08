#!/usr/bin/env python3
"""Standalone exhaustive Prüfer enumeration and exact moment checks."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
import heapq


def decode_statistics(code, n):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    leaves = degree.count(1)
    pending = degree.copy()
    heap = [i for i, d in enumerate(pending) if d == 1]
    heapq.heapify(heap)
    edges = []
    for x in code:
        u = heapq.heappop(heap)
        edges.append((u, x))
        pending[u] -= 1
        pending[x] -= 1
        if pending[x] == 1:
            heapq.heappush(heap, x)
    u, v = [i for i, d in enumerate(pending) if d == 1]
    edges.append((u, v))
    leaf_neighbor_count = [0] * n
    for u, v in edges:
        if degree[u] == 1:
            leaf_neighbor_count[v] += 1
        if degree[v] == 1:
            leaf_neighbor_count[u] += 1
    cherries = sum(comb(t, 2) for t in leaf_neighbor_count if t >= 2)
    return leaves, cherries


def formulas(n):
    N = n ** (n - 2)
    M = n * comb(n-1, 2)
    ec = Fraction(M * (n-2)**(n-4), N)
    el = Fraction(n * (n-1)**(n-2), N)
    elc = ec * 2 + Fraction(M * (n-3)**(n-3), N)
    eccm1 = Fraction(n * (n-1)*(n-2)*(n-3)**(n-4), N)
    if n >= 5:
        eccm1 += Fraction(n*(n-1)*(n-2)*(n-3)*(n-4)**(n-4), 4*N)
    ellm1 = Fraction(n*(n-1)*(n-2)**(n-2), N)
    return ec, el, elc, eccm1, ellm1


def verify():
    nchecks = 0
    for n in range(4, 9):
        N = n**(n-2)
        totC = totL = totLC = totCCm1 = totLLm1 = 0
        totmixed = [0]*(n-2)
        for code in product(range(n), repeat=n-2):
            L,C = decode_statistics(code, n)
            totC += C
            totL += L
            totLC += L*C
            totCCm1 += C*(C-1)
            totLLm1 += L*(L-1)
            for r in range(n-2):
                totmixed[r] += C*comb(L-2, r)
        observed = tuple(Fraction(t, N) for t in (totC,totL,totLC,totCCm1,totLLm1))
        predicted = formulas(n)
        assert observed == predicted, (n, observed, predicted)
        nchecks += 5
        for r in range(n-2):
            P = Fraction(comb(n-3,r)*(n-2-r)**(n-4), (n-2)**(n-4)) * predicted[0]
            assert Fraction(totmixed[r], N) == P,(n,r)
            nchecks += 1
        assert predicted[2] > predicted[0]*predicted[1]
        nchecks += 1
        print(f'n={n}: {N} trees; moments and factorial size-bias PASS')
    for n in range(9, 351):
        ec,el,elc,ecc,ell = formulas(n)
        assert elc > el*ec
        assert ecc + ec - ec*ec > 0
        assert ell + el - el*el > 0
        nchecks += 3
    print('VERIFY_OK', nchecks)

if __name__ == '__main__':
    verify()
