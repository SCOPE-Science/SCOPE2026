#!/usr/bin/env python3
"""Exact, reproducible checks for regular-graph missing-edge hypergraphic polytopes.

Exhaustive vertex-exposure enumeration for small graphs; not an infinite proof.
Only Python standard library is needed except graph-atlas optional tests.
"""
from itertools import permutations, combinations
from collections import Counter


def edge_set(n, edges):
    return {tuple(sorted(e)) for e in edges}


def predicted(n, edges):
    edges=edge_set(n,edges)
    r=2*len(edges)//n
    assert all(sum(1 for e in edges if t in e)==r for t in range(n))
    m=len(edges);a=m-r
    outer=set();inner=set()
    for t in range(n):
        for s in range(n):
            if t==s:continue
            if tuple(sorted((t,s))) not in edges:
                v=[0]*n;v[t]=a;v[s]=r;outer.add(tuple(v))
            else:
                for u in range(n):
                    if u in (t,s):continue
                    v=[0]*n;v[t]=a;v[s]=r-1;v[u]=1
                    inner.add(tuple(v))
    return outer,inner


def observed(n,edges):
    edges=edge_set(n,edges)
    out=set()
    for ranks in permutations(range(n)):
        v=[0]*n
        for i,j in edges:
            v[next(t for t in ranks if t!=i and t!=j)]+=1
        out.add(tuple(v))
    return out


def sqdist(v,w):return sum((x-y)**2 for x,y in zip(v,w))


def check(n,edges,large_pairs=True):
    ed=edge_set(n,edges);r=2*len(ed)//n;q=n-1-r;m=len(ed)
    assert 2<=r<=n-2 and n>=5
    assert all(sum(1 for e in ed if v in e)==r for v in range(n))
    outer,inner=predicted(n,ed)
    assert observed(n,ed)==(outer|inner)
    assert outer.isdisjoint(inner)
    assert len(outer)==n*q
    assert len(inner)==(n*(2*n-5) if r==2 else n*r*(n-2))
    avg=m/n
    assert all(sum(v[i] for v in outer)==m*q for i in range(n))
    assert all(sum((x-avg)**2 for x in v)==r*r*(n*n-5*n+8)/4 for v in outer)
    assert all(sum((x-avg)**2 for x in v)==r*r*(n*n-5*n+8)/4-2*(r-1) for v in inner)
    if large_pairs:
        D=2*((m-r)**2+r*r)
        allv=sorted(outer|inner)
        pairs=0
        for v,w in combinations(allv,2):
            d=sqdist(v,w)
            assert d<=D
            if d==D:
                assert v in outer and w in outer
                assert not any(v[i]*w[i] for i in range(n))
                pairs+=1
        assert pairs==n*q*(q*(n-4)+2)//2,(n,r,pairs)
        outverts=sorted(outer)
        for v,w in combinations(outverts,2):
            disjoint=not any(v[i]*w[i] for i in range(n))
            assert (sqdist(v,w)==D)==disjoint
        return pairs
    return None


def special_graphs():
    # All degree-relevant examples, including disconnected and matching complements.
    return [
      (5,[(i,(i+1)%5) for i in range(5)]),
      (6,[(i,(i+1)%6) for i in range(6)]),
      (6,[(i,(i+1)%3) for i in range(3)]+[(i+3,3+(i+1)%3) for i in range(3)]),
      (6,[(i,j) for i in range(3) for j in range(3,6)]),
      (6,[(i,j) for i in range(6) for j in range(i+1,6) if (i+j)%2 != 1 or (i,j) not in [(0,1),(2,3),(4,5)]]),
      (7,[(i,(i+1)%7) for i in range(7)]),
    ]

if __name__=='__main__':
    checked=0
    for n,edges in special_graphs():
        ed=edge_set(n,edges)
        r=2*len(ed)//n
        if all(sum(1 for e in ed if v in e)==r for v in range(n)) and 2<=r<=n-2:
            pairs=check(n,ed,large_pairs=n<=6)
            print('special graph n,r,edgecount,diameter_pairs:',n,r,len(ed),pairs)
            checked+=1
    try:
        import networkx as nx
    except ImportError:
        print('networkx unavailable; running standalone checks only')
    else:
        for g in nx.graph_atlas_g():
            n=len(g)
            if n<5 or n>7:continue
            degrees=[d for v,d in g.degree()]
            if not degrees or len(set(degrees))!=1:continue
            r=degrees[0]
            if not 2<=r<=n-2:continue
            check(n,list(g.edges()),large_pairs=n<=6)
            checked+=1
        print('including all regular graph-atlas instances, verified graphs:',checked)
    print('All finite exact checks passed; mathematical proof is required for all n.')
