#!/usr/bin/env python3
"""Exhaustive finite corroboration for a closed-neighborhood collapse theorem.

Run: python3 verify_closed_square.py
This does not substitute for the unrestricted mathematical argument.
"""
from itertools import combinations
from random import Random
from collections import Counter


def connected(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    seen={0}; todo=[0]
    for a in todo:
        for b in adj[a]-seen:
            seen.add(b);todo.append(b)
    return len(seen)==n


def squares(n, edges):
    ee={tuple(sorted(x)) for x in edges}
    if any(all(tuple(sorted(p)) in ee for p in combinations(t,2)) for t in combinations(range(n),3)):
        return None
    sqs={}
    for a,b,c,d in combinations(range(n),4):
        for cy in [(a,b,c,d),(a,b,d,c),(a,c,b,d)]:
            es=frozenset(tuple(sorted(p)) for p in zip(cy,cy[1:]+cy[:1]))
            if es<=ee: sqs[es]=frozenset(cy)
    if len(set().union(*sqs)) != sum(map(len,sqs)) if sqs else False:
        return None
    return list(sqs.values())


def complex_faces(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    faces={frozenset()}
    for v in range(n):
        vs=sorted(adj[v]|{v})
        for s in range(1,len(vs)+1):
            for t in combinations(vs,s):faces.add(frozenset(t))
    return adj,faces


def check(n,edges,require_connected=True):
    edges=frozenset(tuple(sorted(x)) for x in edges)
    if require_connected and not connected(n,edges):return False
    sqs=squares(n,edges)
    if sqs is None:return False
    adj,faces=complex_faces(n,edges)
    original=len(faces); pairs=0
    opposites=set()
    for Q in sqs:
        for a,b in combinations(Q,2):
            if (min(a,b),max(a,b)) not in edges:
                opposites.add(frozenset((a,b)))
    for v in range(n):
        ns=sorted(adj[v]); candidates=[]
        for size in range(len(ns),1,-1):
            for sigma in combinations(ns,size):
                s=frozenset(sigma)
                if len(s)==2 and s in opposites:continue
                candidates.append(s)
        for s in candidates:
            top=s|{v}
            assert s in faces and top in faces,(n,edges,v,s)
            larger={t for t in faces if s<t}
            assert larger=={top},(n,edges,v,s,larger)
            faces.remove(s);faces.remove(top);pairs+=1
    expected={frozenset()}
    for v in range(n):expected.add(frozenset((v,)))
    expected.update(frozenset(e) for e in edges)
    for Q in sqs:
        for m in range(1,4):
            expected.update(frozenset(t) for t in combinations(sorted(Q),m))
    assert faces==expected,(n,edges,sqs,faces^expected)
    assert original==len(faces)+2*pairs
    q=len(sqs); b=len(edges)-n+1
    assert b>=q,(n,edges,q,b)
    # Independent mod-2 boundary reduction on the leftover two-complex.
    def rank(columns):
        pivots={}
        for z in columns:
            while z:
                k=z.bit_length()-1
                if k in pivots:z^=pivots[k]
                else:pivots[k]=z;break
        return len(pivots)
    vertices=[frozenset((i,)) for i in range(n)]
    one=sorted((s for s in faces if len(s)==2),key=lambda s:tuple(sorted(s)))
    two=sorted((s for s in faces if len(s)==3),key=lambda s:tuple(sorted(s)))
    vidx={v:i for i,v in enumerate(vertices)}
    eidx={s:i for i,s in enumerate(one)}
    d1=rank([sum(1<<vidx[frozenset((v,))] for v in s) for s in one])
    d2=rank([sum(1<<eidx[frozenset(p)] for p in combinations(s,2)) for s in two])
    assert len(one)-d1-d2==b-q,(n,edges,len(one),d1,d2,b,q)
    assert len(two)-d2==q
    return True


def main():
    total=0; with_squares=0; stats=Counter()
    for n in range(3,7):
        all_edges=list(combinations(range(n),2))
        for bitset in range(1<<len(all_edges)):
            E=[e for i,e in enumerate(all_edges) if bitset>>i&1]
            if check(n,E):
                total+=1; q=len(squares(n,E)); stats[(n,q)]+=1
                if q:with_squares+=1
    rnd=Random(7)
    samples=0
    for n in [7,8,9]:
        all_edges=list(combinations(range(n),2))
        for _ in range(300):
            E=[e for e in all_edges if rnd.random()<0.24]
            if check(n,E):samples+=1
    extra=[(8,[(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(2,6)]),
           (9,[(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(2,6),(8,7)])]
    for n,E in extra:
        assert check(n,E)
        assert len(squares(n,E))==2
    print('CONNECTED_LABELED_GRAPHS_N3_TO_N6',total)
    print('WITH_NONZERO_SQUARES',with_squares)
    print('CUTOFF_DISTRIBUTION',sorted((n,q,c) for (n,q),c in stats.items()))
    print('RANDOM_HIGHER_VALID_INSTANCES',samples)
    print('NONCACTUS_TWO_SQUARE_CASES',len(extra))
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
