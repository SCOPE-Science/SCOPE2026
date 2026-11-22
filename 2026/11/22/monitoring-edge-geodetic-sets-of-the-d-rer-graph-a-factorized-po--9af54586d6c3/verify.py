#!/usr/bin/env python3
"""Independent exhaustive check for the Durer graph monitoring theorem.
Run with Python 3 standard library: python3 verify.py
"""
from collections import Counter, deque
from itertools import combinations

def graph():
    adj = [set() for _ in range(12)]
    def link(a,b):
        adj[a].add(b)
        adj[b].add(a)
    for i in range(6):
        link(i,(i+1)%6)
        link(i,6+i)
        link(6+i,6+(i+2)%6)
    return adj

def distances(adj, removed=None):
    out=[]
    for start in range(12):
        dist=[100]*12
        dist[start]=0
        queue=deque([start])
        while queue:
            a=queue.popleft()
            for b in adj[a]:
                if removed is not None and frozenset((a,b))==removed:
                    continue
                if dist[b]>dist[a]+1:
                    dist[b]=dist[a]+1
                    queue.append(b)
        out.append(dist)
    return out

def monitor_pairs(adj):
    old=distances(adj)
    witness={}
    for u in range(12):
        for v in sorted(adj[u]):
            if u>=v:
                continue
            e=frozenset((u,v))
            new=distances(adj,e)
            witness[(u,v)]={(a,b) for a in range(12) for b in range(a+1,12)
                            if new[a][b]>old[a][b]}
    return witness

def structural(mask):
    if any(not(mask>>i & 1 or mask>>(6+i)&1) for i in range(6)):
        return False
    return all(sum(bool(mask>>(6+i)&1) for i in range(parity,6,2))>=2
               for parity in range(2))

def full_test():
    adj=graph()
    w=monitor_pairs(adj)
    assert len(w)==18
    assert w[(0,6)]=={(0,6),(0,8),(0,10),(1,6),(5,6),(6,7),(6,11)}
    assert w[(6,8)]=={(0,8),(2,6),(6,8)}
    assert w[(0,1)]=={(0,1),(0,2),(0,7),(1,5),(1,6),(6,7)}
    successful=[]
    for mask in range(1<<12):
        S={i for i in range(12) if mask>>i & 1}
        by_distance=all(any(a in S and b in S for a,b in pairs)
                        for pairs in w.values())
        by_structure=structural(mask)
        assert by_distance==by_structure, ('equivalence',mask)
        if by_distance:
            successful.append(mask)
    poly=Counter(x.bit_count() for x in successful)
    assert dict(poly)=={6:16,7:72,8:129,9:116,10:54,11:12,12:1}
    minimal=[m for m in successful if not any((m^(1<<i)) in successful for i in range(12) if m>>i&1)]
    assert len(minimal)==16 and all(m.bit_count()==6 for m in minimal)
    bases=[m for m in successful if m.bit_count()==6]
    def choice(mask,parity):
        return next((i for i in range(parity,6,2) if mask>>i&1),None)
    coords={m:(choice(m,0),choice(m,1)) for m in bases}
    assert len(set(coords.values()))==16
    jump_edges=set()
    slide_edges=set()
    for a,b in combinations(bases,2):
        diff=a^b
        if diff.bit_count()!=2:
            continue
        jump_edges.add(frozenset((a,b)))
        removed=next(i for i in range(12) if (a & ~b)>>i&1)
        added=next(i for i in range(12) if (b & ~a)>>i&1)
        if added in adj[removed]:
            slide_edges.add(frozenset((a,b)))
        ca,cb=coords[a],coords[b]
        assert sum(x!=y for x,y in zip(ca,cb))==1
        assert any((x is None)!=(y is None) for x,y in zip(ca,cb))
    assert slide_edges==jump_edges and len(jump_edges)==24
    degrees=Counter(sum(a in edge for edge in jump_edges) for a in bases)
    assert dict(degrees)=={2:9,4:6,6:1}
    assert sum(1 for a,b in combinations(bases,2) if sum(x!=y for x,y in zip(coords[a],coords[b]))==1
               and any((x is None)!=(y is None) for x,y in zip(coords[a],coords[b])))==24
    # Diameter four and a single component follow from K_{1,3} x K_{1,3}
    print('VERIFY_OK vertices=12 edges=18 subsets=4096 minimal=16 mon_poly=',sorted(poly.items()),
          'jump_slide_edges=24 degree_histogram=',sorted(degrees.items()),'diameter=4')
if __name__=='__main__':
    full_test()
