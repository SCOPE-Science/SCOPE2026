#!/usr/bin/env python3
"""Independent enumeration checks for decompositions of binary dependence teams.

Execute: python verify_split.py
No packages beyond the Python standard library are required.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial
import random


def brute_split(p, q, mask):
    edges = [(i, j) for i in range(p) for j in range(q) if (mask >> (i*q+j)) & 1]
    total = 0
    for labels in range(1 << len(edges)):
        first, second = {}, {}
        good = True
        for k, (i,j) in enumerate(edges):
            if (labels >> k) & 1:
                if j in second and second[j] != i:
                    good = False
                    break
                second[j] = i
            else:
                if i in first and first[i] != j:
                    good = False
                    break
                first[i] = j
        total += int(good)
    return total


def graph_split(p, q, mask):
    par = list(range(p+q))
    def root(i):
        while i != par[i]:
            par[i] = par[par[i]]
            i = par[i]
        return i
    edges = []
    for i in range(p):
        for j in range(q):
            if (mask >> (i*q+j)) & 1:
                a, b = i, p+j
                ra, rb = root(a), root(b)
                par[ra] = rb
                edges.append((a,b))
    vertices = Counter(root(i) for i in range(p+q))
    edge_ct = Counter(root(a) for a,b in edges)
    value = 1
    for r, nv in vertices.items():
        ne = edge_ct[r]
        if ne > nv:
            return 0
        if ne == nv:
            value *= 2
        elif ne == nv-1:
            value *= nv
        else:
            raise AssertionError('connected component count inconsistent')
    return value


def max_formula(d):
    m = 2*d
    if m % 3 == 0:
        return 3**(m//3)
    if m % 3 == 1:
        return 4*3**((m-4)//3)
    return 2*3**((m-2)//3)


def global_formula(p,q):
    return sum((-1)**k*comb(p,k)*comb(q,k)*factorial(k)
               *(q+1)**(p-k)*(p+1)**(q-k)
               for k in range(min(p,q)+1))


def run():
    checked = 0
    for p in range(1,4):
        for q in range(1,4):
            subtotal = 0
            for mask in range(1 << (p*q)):
                a = brute_split(p,q,mask)
                b = graph_split(p,q,mask)
                assert a == b, (p,q,mask,a,b)
                subtotal += b
                checked += 1
            assert subtotal == global_formula(p,q), (p,q,subtotal,global_formula(p,q))
            print('EXHAUSTIVE',p,q,'teams',1<<(p*q),'all witnesses',subtotal)
    for d in range(1,5):
        by_formula = [graph_split(d,d,mask) for mask in range(1 << (d*d))]
        mx = max(by_formula)
        assert mx == max_formula(d), (d,mx,max_formula(d))
        assert sum(by_formula) == global_formula(d,d)
        sat = sum(v>0 for v in by_formula)
        assert sat == {1:2,2:16,3:460,4:33959}[d]
        print('ALL_GRAPHS',d,'teams',len(by_formula),'satisfying',sat,'maximum',mx,'sum',sum(by_formula))
    rng=random.Random(271828)
    for _ in range(200):
        mask=rng.randrange(1 << 16)
        assert graph_split(4,4,mask)==brute_split(4,4,mask), mask
    print('RANDOM_4X4',200,'OK')
    print('EXHAUSTIVE_BRUTE_TOTAL',checked,'OK')
    print('PASS')

if __name__ == '__main__':
    run()
