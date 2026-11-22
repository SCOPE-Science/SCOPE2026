#!/usr/bin/env python3
"""Exact finite checks for induced-edge and wedge statistics of uniform labelled trees.
Only the standard library is needed.  This finite checker supplements the proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations
from math import comb
import heapq


def edges_from_prufer(code, n):
    degrees = [1] * n
    for x in code:
        degrees[x] += 1
    leaves = [j for j, d in enumerate(degrees) if d == 1]
    heapq.heapify(leaves)
    out = []
    for x in code:
        y = heapq.heappop(leaves)
        out.append((min(x,y), max(x,y)))
        degrees[x] -= 1
        degrees[y] -= 1
        if degrees[x] == 1:
            heapq.heappush(leaves, x)
    a,b = [j for j,d in enumerate(degrees) if d==1]
    out.append((min(a,b),max(a,b)))
    return tuple(out)


def exact_checks():
    checks = 0
    for n in range(3, 8):
        total = n ** (n-2)
        hist = [Counter() for _ in range(n+1)]
        wedges = [0]*(n+1)
        pair_hist = Counter()
        graph_hist = [Counter() for _ in range(min(n, 5) + 1)]
        pair_index = {k: {edge: i for i,edge in enumerate(combinations(range(k), 2))}
                      for k in range(1, min(n, 5) + 1)}
        for code in product(range(n), repeat=n-2):
            edges = edges_from_prufer(code,n)
            edge_set = set(edges)
            for k in range(1, min(n, 5) + 1):
                mask = sum(1 << j for edge, j in pair_index[k].items() if edge in edge_set)
                graph_hist[k][mask] += 1
            pair_hist[(int((0,1) in edge_set), int((0,2) in edge_set),int((2,3) in edge_set))] += 1
            for k in range(1,n+1):
                internal = [(a,b) for a,b in edges if b<k]
                h=len(internal)
                hist[k][h] += 1
                degrees=[0]*k
                for a,b in internal:
                    degrees[a]+=1;degrees[b]+=1
                wedges[k] += sum(comb(d,2) for d in degrees if d>=2)
        for k in range(1,n+1):
            for r in range(k):
                expected = Fraction(comb(k-1,r)*k**r*(n-k)**(k-1-r), n**(k-1))
                observed = Fraction(hist[k][r],total)
                assert observed == expected, (n,k,r,observed,expected)
                checks += 1
            observed = Fraction(wedges[k],total)
            expected = Fraction(9*comb(k,3),n*n)
            assert observed == expected, (n,k,observed,expected)
            checks += 1
        p1 = sum(v for key,v in pair_hist.items() if key[0])
        pwedge = sum(v for key,v in pair_hist.items() if key[0] and key[1])
        pdisjoint = sum(v for key,v in pair_hist.items() if key[0] and key[2])
        assert Fraction(p1,total)==Fraction(2,n)
        assert Fraction(pwedge,total)==Fraction(3,n*n)
        if n >= 4:
            assert Fraction(pdisjoint,total)==Fraction(4,n*n)
        checks += 3
        # Whole-labelled-graph total variation, not only edge-count variation.
        for k in range(1, min(n, 5) + 1):
            M = comb(k, 2)
            p = Fraction(2, n)
            distance = Fraction(0)
            for mask in range(1 << M):
                edges = mask.bit_count()
                expected = p**edges * (1-p)**(M-edges)
                actual = Fraction(graph_hist[k][mask], total)
                distance += abs(actual-expected) / 2
            bound = Fraction(k*k*(k-1) + 2*k*(k-1) + 21*comb(k,3), n*n)
            assert distance <= min(1,bound), (n,k,distance,bound)
            checks += 1
    return checks

if __name__ == '__main__':
    count=exact_checks()
    print('PASS:',count,'exact rational checks, all Prüfer codes for n=3,...,7')
