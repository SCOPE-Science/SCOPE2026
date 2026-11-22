#!/usr/bin/env python3
"""Finite checks of the ordered-DAG shortcut witness correspondence.
Only finite arithmetic checks; the Poisson limit is proved separately.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial, comb


def witness_counts(n, edges):
    edges = set(edges)
    counts = [0]*(n+1)
    for u in range(n):
        for v in range(u+1,n):
            if (u,v) not in edges:
                continue
            def visit(k, depth):
                if k == v:
                    if depth>=2:
                        counts[depth+1]+=1
                    return
                for z in range(k+1,v+1):
                    if (k,z) in edges and not (k==u and z==v):
                        visit(z,depth+1)
            visit(u,0)
    return counts

def reduced_count(n,edges):
    es=set(edges); ans=0
    for u,v in es:
        reachable={u}
        for k in range(u,v):
            if k in reachable:
                for z in range(k+1,v+1):
                    if (k,z) in es and (k,z)!=(u,v): reachable.add(z)
        ans += (v in reachable)
    return ans

def cycle_is_witness(order):
    # input cycle vertices in cyclic order, values are total ranks
    E={tuple(sorted((order[k],order[(k+1)%len(order)]))) for k in range(len(order))}
    return sum(witness_counts(len(order),E))

checks=0
for r in range(3,9):
    cnt=sum(cycle_is_witness(perm)>0 for perm in permutations(range(r)))
    assert cnt==2*r, (r,cnt)
    checks +=1

for n in range(3,7):
    all_edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    hist=[0]*(n+1)
    for mask in range(1<<len(all_edges)):
        es=[e for i,e in enumerate(all_edges) if mask>>i&1]
        counts=witness_counts(n,es)
        w=sum(counts)
        r=reduced_count(n,es)
        assert r<=w
        assert (r==0)==(w==0)  # no witness iff no redundant edge
        for length in range(3,n+1): hist[length]+=counts[length]
        checks+=2
    expected = sum(Fraction(comb(n,k),2**k) for k in range(3,n+1))
    empirical = Fraction(sum(hist),2**len(all_edges))
    assert expected==empirical,(n,expected,empirical)
    checks+=1
print('PASS finite checks',checks,'; all cyclic-order checks 3..8 and all ordered digraphs 3..6')
