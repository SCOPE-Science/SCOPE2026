#!/usr/bin/env python3
"""Independent bounded checks for maximal-geodesic edge-transversal theorem."""
from itertools import product,combinations,permutations
from math import comb,prod

def graph(qs):
    V=list(product(*(range(q) for q in qs)))
    E=[]; where={}
    for u in V:
        for i,qi in enumerate(qs):
            for b in range(u[i]+1,qi):
                v=list(u);v[i]=b;v=tuple(v)
                where[frozenset((u,v))]=len(E)
                E.append((u,v,i))
    paths=set()
    for a in V:
        for b in V:
            if all(x!=y for x,y in zip(a,b)) and a<b:
                for pi in permutations(range(len(qs))):
                    v=a; pp=[]
                    for i in pi:
                        w=list(v);w[i]=b[i];w=tuple(w)
                        pp.append(where[frozenset((v,w))]);v=w
                    paths.add(tuple(sorted(pp)))
    return E,paths

def check(qs):
    E,paths=graph(qs)
    n=prod(qs);target=n*(min(qs)-1)//2
    full_by_coord=[frozenset(k for k,e in enumerate(E) if e[2]==i) for i in range(len(qs))]
    expected={s for s in full_by_coord if len(s)==target}
    masks=[sum(1<<k for k in p) for p in paths]
    found=[]
    for subset in combinations(range(len(E)),target):
        s=sum(1<<k for k in subset)
        if all(s&m for m in masks):found.append(frozenset(subset))
    assert set(found)==expected,(qs,len(found),len(expected))
    assert all(all(sum(k in S for k in p)==1 for p in paths) for S in found)
    print('EXHAUSTIVE',qs,'vertices',n,'edges',len(E),'max_geodesics',len(paths),'minimum',target,'optimizers',len(found))

def check_exact_one(qs):
    E,paths=graph(qs)
    full_by_coord=[frozenset(k for k,e in enumerate(E) if e[2]==i) for i in range(len(qs))]
    assert all(all(sum(k in S for k in p)==1 for p in paths) for S in full_by_coord)
    print('COORDINATE_CLASS_TEST',qs,'coordinate_sizes',[len(s) for s in full_by_coord])

if __name__=='__main__':
    for qs in [(2,), (3,), (2,2), (2,3), (3,3), (2,2,2), (2,2,3)]:check(qs)
    for qs in [(2,3,3),(3,3,3),(2,3,4),(2,2,2,2),(2,3,4,5)]:check_exact_one(qs)
    print('VERIFY_OK')
