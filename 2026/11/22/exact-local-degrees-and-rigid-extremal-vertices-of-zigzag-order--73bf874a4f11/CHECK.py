#!/usr/bin/env python3
"""Standalone exact finite checks of zigzag-order-polytope local degree classification.
Scientific checks use integer arithmetic and rational matrix rank; finite checks are not infinite proofs.
"""
from itertools import combinations
from math import comb
import json
from fractions import Fraction

def words(n):
    return [tuple((b >> i) & 1 for i in range(n)) for b in range(1 << n)
            if not (b & (b >> 1))]

def clusters(w):
    idx = [i for i, v in enumerate(w) if v]
    out=[]
    for i in idx:
        if not out or i - out[-1][-1] != 2: out.append([i])
        else: out[-1].append(i)
    return out

def predicted_degree(w):
    n=len(w)
    return n+sum(comb(len(c)+(c[0]>0)+(c[-1]<n-1)-1,2)
                 for c in clusters(w))

def adjacent_by_difference(u,v):
    d=[i for i in range(len(u)) if u[i]!=v[i]]
    return bool(d) and d[-1]-d[0]+1==len(d)

def polytope_edge_rank(u,v):
    n=len(u)
    facets=[]
    for i in range(n):
        if u[i]==v[i]==0:
            facets.append([int(j==i) for j in range(n)])
    for i in range(n-1):
        if u[i]+u[i+1]==v[i]+v[i+1]==1:
            facets.append([int(j==i or j==i+1) for j in range(n)])
    # Exact rational row reduction; no floating-point or external packages.
    a=[[Fraction(x) for x in row] for row in facets]
    rank=0
    for col in range(n):
        piv=next((r for r in range(rank,len(a)) if a[r][col]),None)
        if piv is None: continue
        a[rank],a[piv]=a[piv],a[rank]
        d=a[rank][col]
        a[rank]=[x/d for x in a[rank]]
        for r in range(rank+1,len(a)):
            mul=a[r][col]
            if mul:
                a[r]=[x-mul*y for x,y in zip(a[r],a[rank])]
        rank+=1
    return rank==n-1

def main():
    audits=[]
    for n in range(3,12):
        ww=words(n)
        deg={w:sum(adjacent_by_difference(w,v) for v in ww) for w in ww}
        assert all(deg[w]==predicted_degree(w) for w in ww), n
        maxdegree=max(deg.values())
        assert maxdegree==n+comb((n+1)//2,2),(n,maxdegree)
        extrema=[w for w in ww if deg[w]==maxdegree]
        assert len(extrema)==(1 if n%2 else 4),(n,extrema)
        simple=[w for w in ww if deg[w]==n]
        assert len(simple)==4,(n,simple)
        assert set(simple)=={(0,)*n,(1,)+(0,)*(n-1),(0,)*(n-1)+(1,),
                              (1,)+(0,)*(n-2)+(1,)},n
        if n<=7:
            for u,v in combinations(ww,2):
                assert polytope_edge_rank(u,v)==adjacent_by_difference(u,v),(n,u,v)
        audits.append(dict(n=n,vertices=len(ww),simple=len(simple),maximum_degree=maxdegree,
                           maximizers=len(extrema),graph_edges=sum(deg.values())//2,
                           polytope_face_rank_checked=n<=7))
    print('FENCE_LOCAL_DEGREE_EXACT_PASS')
    print(json.dumps(audits,separators=(',',':')))
if __name__=='__main__':main()
