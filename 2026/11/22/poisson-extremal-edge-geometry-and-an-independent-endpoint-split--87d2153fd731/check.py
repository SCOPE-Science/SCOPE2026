"""Finite exact checks for extreme ordered edges of uniform Cayley trees.

Uses only the Python standard library; run with: python check.py.
Checks exact forest extension formula against enumerated trees and
all factorial moments through order three of long-edge counts.
"""
from collections import Counter
from itertools import product, combinations, permutations
from fractions import Fraction
from math import factorial
import heapq


def prufer_edges(code, n):
    if n == 2:
        return ((1, 2),)
    deg = [1] * n
    for x in code:
        deg[x-1] += 1
    leaves = [i for i in range(n) if deg[i] == 1]
    heapq.heapify(leaves)
    out = []
    for x in code:
        v = heapq.heappop(leaves)
        out.append((min(v+1,x), max(v+1,x)))
        deg[v] -= 1
        deg[x-1] -= 1
        if deg[x-1] == 1:
            heapq.heappush(leaves, x-1)
    a = heapq.heappop(leaves)+1
    b = heapq.heappop(leaves)+1
    out.append((min(a,b), max(a,b)))
    return tuple(out)


def inclusion(n, selected_edges):
    parent = list(range(n+1))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i,j in selected_edges:
        u,v = root(i),root(j)
        if u == v:
            return Fraction(0)
        parent[u] = v
    size=Counter(root(i) for i in range(1,n+1))
    numer=1
    for s in size.values(): numer *= s
    return Fraction(numer,n**len(selected_edges))


def falling(x,r):
    z=1
    for i in range(r): z*=x-i
    return z


def verify():
    assertions=0
    for n in range(2,9):
        family = list(product(range(1,n+1), repeat=n-2))
        E = list(combinations(range(1,n+1),2))
        tree_list = [frozenset(prufer_edges(c,n)) for c in family]
        assert len(tree_list) == n**(n-2);assertions+=1
        assert all(len(t)==n-1 for t in tree_list);assertions+=1
        edgefreq=Counter(e for t in tree_list for e in t)
        for e in E:
            assert Fraction(edgefreq[e],len(tree_list)) == inclusion(n,[e]);assertions+=1
        for e,f in combinations(E,2):
            actual=sum(e in T and f in T for T in tree_list)
            assert Fraction(actual,len(tree_list))==inclusion(n,[e,f]);assertions+=1
        # The first three falling factorial moments of edge counts
        # near the anti-diagonal must match forest inclusion enumeration.
        for r in range(1,min(n-1,4)+1):
            corner=[e for e in E if n-(e[1]-e[0])<=r]
            for k in range(1,min(3,len(corner))+1):
                observed = Fraction(sum(falling(sum(e in T for e in corner),k) for T in tree_list),len(tree_list))
                predicted = factorial(k)*sum((inclusion(n,C) for C in combinations(corner,k)),Fraction(0))
                assert observed==predicted, (n,r,k,observed,predicted)
                assertions+=1
        print(f'n={n}, trees={len(tree_list):,}, checks cumulative={assertions}')
    print(f'PASS: {assertions} exact assertions, including 262,144 labelled trees at n=8')

if __name__=='__main__':
    verify()
