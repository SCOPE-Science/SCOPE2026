#!/usr/bin/env python3
"""Exact finite-sample checks of endpoint input rank transfer on replicated pendant paths.
Uses only the Python standard library; the infinite statement has a separate proof.
Run: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations
from random import Random


def matrix_rank(A):
    if not A: return 0
    a = [[Fraction(x) for x in row] for row in A]
    m, n = len(a), len(a[0]); r = 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if a[i][col]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][col]
        a[r] = [x/q for x in a[r]]
        for i in range(r+1, m):
            v = a[i][col]
            if v:
                a[i] = [a[i][j]-v*a[r][j] for j in range(n)]
        r += 1
        if r == m: break
    return r


def laplacian(n, edges):
    L = [[0]*n for _ in range(n)]
    for i, j, w in edges:
        assert 0 <= i < n and 0 <= j < n and i != j and w > 0
        L[i][i] += w; L[j][j] += w
        L[i][j] -= w; L[j][i] -= w
    return L


def controllability_rank(L, chosen):
    n = len(L)
    if not chosen: return 0
    p = len(chosen)
    C = [[] for _ in range(n)]
    V = [[int(i==k) for k in chosen] for i in range(n)]
    for _ in range(n):
        for i in range(n): C[i].extend(V[i])
        V = [[sum(L[i][j]*V[j][k] for j in range(n)) for k in range(p)] for i in range(n)]
    return matrix_rank(C)


def expanded(n, base_edges, weights):
    q = len(weights)+1
    edges = [(i*q, j*q, w) for i,j,w in base_edges]
    for i in range(n):
        edges.extend((i*q+d, i*q+d+1, w) for d,w in enumerate(weights))
    return laplacian(n*q, edges)


def graph_cases():
    rng=Random(20261107)
    for n in range(2,6):
        edges=[(i,i+1,rng.randint(1,3)) for i in range(n-1)]
        yield n,edges
        if n>=3:
            yield n, edges+[(0,n-1,rng.randint(1,4))]
        yield n, [(i,j,rng.randint(1,4)) for i in range(n) for j in range(i+1,n)]


def main():
    rng=Random(20261107)
    checks=0
    for n, edges in graph_cases():
        G=laplacian(n,edges)
        choices = list(combinations(range(n),1)) + list(combinations(range(n),2))
        for depth in range(1,4):
            weights=[rng.randint(1,4) for _ in range(depth)]
            E=expanded(n,edges,weights); q=depth+1
            for J in choices:
                base_rank = controllability_rank(G,J)
                for choice in range(3):
                    if choice==0: S=[i*q for i in J]
                    elif choice==1: S=[i*q+depth for i in J]
                    else: S=[i*q+(depth if k%2 else 0) for k,i in enumerate(J)]
                    actual=controllability_rank(E,S)
                    expect=q*base_rank
                    assert actual==expect, (n,edges,weights,J,S,actual,expect)
                    checks+=1
            # Root and tip of the same fiber must not simulate two distinct indices.
            S=[0,depth]
            assert controllability_rank(E,S)==q*controllability_rank(G,[0])
            checks+=1
    # Internal sensors need not satisfy endpoint transfer.
    E=expanded(2,[(0,1,1)],[1,1])
    ifail=controllability_rank(E,[1])
    b=controllability_rank(laplacian(2,[(0,1,1)]),[0])
    assert ifail < 3*b, (ifail,b)
    checks+=1
    print('VERIFY_OK',checks)

if __name__=='__main__':main()
