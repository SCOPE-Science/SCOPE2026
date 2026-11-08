#!/usr/bin/env python3
"""Direct finite checks for minimal forts of once-subdivided complete graphs.
No external packages needed. Run: python3 verify.py"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial

def graph(n):
    edges = list(combinations(range(n), 2))
    N = n + len(edges)
    adj = [0] * N
    for j, (a, b) in enumerate(edges):
        e = n + j
        adj[a] |= 1 << e
        adj[b] |= 1 << e
        adj[e] |= (1 << a) | (1 << b)
    return edges, adj

def fort(mask, adj):
    if not mask:
        return False
    for v, neighbors in enumerate(adj):
        if not ((mask >> v) & 1) and (neighbors & mask).bit_count() == 1:
            return False
    return True

def predicted(n, edges):
    eindex = {e: n + j for j,e in enumerate(edges)}
    full=(1<<n)-1
    answer={full}
    for v in range(n):
        select=full ^ (1<<v)
        select |= sum(1<<eindex[tuple(sorted((v,u)))] for u in range(n) if u!=v)
        answer.add(select)
    for k in range(3,n+1):
        for vertices in combinations(range(n), k):
            smallest = vertices[0]
            for tail in permutations(vertices[1:]):
                if tail[0] > tail[-1]:
                    continue
                cyc=(smallest,)+tail
                mask=0
                for a,b in zip(cyc,cyc[1:]+cyc[:1]):
                    mask |= 1 << eindex[tuple(sorted((a,b)))]
                answer.add(mask)
    return answer

def exhaustive(n):
    edges,adj=graph(n)
    expected=predicted(n,edges)
    actual=[]
    tested=0; forts_examined=0
    N=len(adj)
    # Process in order of increasing cardinality. A fort is inclusion-minimal
    # iff it contains no previously discovered minimal fort, even when no
    # single-vertex deletion is a fort.
    for k in range(1,N+1):
        for vs in combinations(range(N),k):
            tested+=1
            mask=sum(1<<v for v in vs)
            if any((mask&g)==g for g in actual):
                continue
            if fort(mask,adj):
                forts_examined+=1
                actual.append(mask)
    assert set(actual)==expected,(n,len(actual),len(expected),list(set(actual)^expected)[:8])
    poly=Counter(q.bit_count() for q in actual)
    want=Counter({k:factorial(n)//(2*k*factorial(n-k)) for k in range(3,n+1)})
    want[n]+=1
    want[2*n-2]+=n
    assert poly==want,(n,poly,want)
    return tested,len(actual),len(expected),forts_examined,dict(sorted(poly.items()))

if __name__=='__main__':
    nsets=0;min_forts=0
    for n in range(3,7):
        checks=exhaustive(n)
        nsets+=checks[0];min_forts+=checks[1]
        print('n=%d vertex_subsets=%d minimal_forts=%d polynomial=%s'%(n,checks[0],checks[1],checks[4]),flush=True)
    print(f'VERIFY_OK n=3..6 vertex_subsets={nsets} minimal_forts={min_forts} exact_minimality=PASS polynomial=PASS',flush=True)
