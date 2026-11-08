#!/usr/bin/env python3
"""Exact independent finite checks for two-sample binary pairwise empirical models."""
from itertools import combinations, product
from math import comb

def components(vertices, edges):
    p = {v:v for v in vertices}
    def find(a):
        while p[a]!=a:a=p[a]
        return a
    for x,y in edges:
        if x in p and y in p:
            p[find(x)] = find(y)
    return len({find(v) for v in vertices})

def closed_counts(n, edges):
    count = local = 0
    for mask in range(1 << n):
        U = {x for x in range(n) if mask>>x & 1}
        e = sum(x in U and y in U for x,y in edges)
        c = components(U, edges)
        count += 2 ** (n-len(U)+e)
        local += 2 ** (n-c)
    return count,local

def direct_counts(n, edges):
    # Each context is a two-sample multiset of binary pairs, giving 10 total tables.
    # Tables use row counts (00,01,10,11) and have total 2.
    tables = []
    for i in range(4):
        for j in range(i,4):
            x=[0]*4; x[i]+=1; x[j]+=1; tables.append(tuple(x))
    assert len(tables)==10
    total=local=0
    for ts in product(tables, repeat=len(edges)):
        marg = {}
        ok=True
        for (u,v),t in zip(edges,ts):
            for vert,one in ((u,t[2]+t[3]),(v,t[1]+t[3])):
                if vert in marg and marg[vert]!=one:ok=False;break
                marg[vert]=one
            if not ok:break
        if not ok:continue
        total+=1
        # Existence of a global assignment whose restriction belongs to the
        # support of every empirical context (support-level test).
        support_found=False
        for assignment in product((0,1),repeat=n):
            if all(t[2*assignment[u]+assignment[v]] for (u,v),t in zip(edges,ts)):
                support_found=True;break
        local += support_found
    return total,local

if __name__=='__main__':
    graphs={
        'triangle':(3,[(0,1),(1,2),(0,2)]),
        'cycle4_K22':(4,[(0,2),(0,3),(1,2),(1,3)]),
        'path4':(4,[(0,1),(1,2),(2,3)]),
        'triangle_tail':(4,[(0,1),(1,2),(0,2),(2,3)]),
        'cycle5':(5,[(0,1),(1,2),(2,3),(3,4),(0,4)])
    }
    for label,(n,edges) in graphs.items():
        predicted=closed_counts(n,edges)
        observed=direct_counts(n,edges)
        print(label, 'formula',predicted,'direct',observed,'contextual',predicted[0]-predicted[1])
        assert observed==predicted
    print('CHECK_OK')
