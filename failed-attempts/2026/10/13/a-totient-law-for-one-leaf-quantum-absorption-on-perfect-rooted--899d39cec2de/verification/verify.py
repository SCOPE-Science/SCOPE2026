#!/usr/bin/env python3
"""Check finite exact Krylov ranks for adjacency walks on perfect b-ary trees.

The code uses two prime fields. Its finite checks support, but do not replace,
the all-parameter proof of the totient law.
"""
from math import gcd

PRIMES=(1000000007,998244353)

def phi(n):
    return sum(1 for k in range(1,n) if gcd(k,n)==1)

def tree(b,h):
    neighbors=[[]]
    levels=[[0]]
    for _ in range(h):
        nodes=[]
        for parent in levels[-1]:
            for _ in range(b):
                child=len(neighbors)
                neighbors.append([parent])
                neighbors[parent].append(child)
                nodes.append(child)
        levels.append(nodes)
    return neighbors,levels

def krylov_rank(neighbors,site,prime):
    n=len(neighbors)
    original=[0]*n
    original[site]=1
    pivots={}
    rank=0
    while True:
        reduced=original.copy()
        while True:
            pivot=next((i for i,value in enumerate(reduced) if value),None)
            if pivot is None:
                return rank
            if pivot not in pivots:
                scale=pow(reduced[pivot],-1,prime)
                pivots[pivot]=[(scale*a)%prime for a in reduced]
                rank+=1
                break
            column=pivots[pivot]
            coefficient=reduced[pivot]
            reduced=[(a-coefficient*z)%prime for a,z in zip(reduced,column)]
        original=[sum(original[u] for u in neighbors[i])%prime for i in range(n)]

cases=[(2,h) for h in range(1,9)]
cases +=[(3,h) for h in range(1,6)]
cases +=[(4,h) for h in range(1,5)]
count=0
for b,h in cases:
    graph,levels=tree(b,h)
    predicted=sum(phi(q) for q in range(2,h+3))
    for p in PRIMES:
        assert krylov_rank(graph,0,p)==h+1,(b,h,p,'root')
        assert krylov_rank(graph,levels[-1][0],p)==predicted,(b,h,p,'leaf')
        count+=2
print('VERIFY_OK finite_rank_comparisons=%d branching_depth_cases=%d fields=%d'%(
    count,len(cases),len(PRIMES)))
