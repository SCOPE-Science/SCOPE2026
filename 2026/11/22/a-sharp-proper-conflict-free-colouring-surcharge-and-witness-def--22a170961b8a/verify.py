#!/usr/bin/env python3
"""Direct finite checks for the proper-conflict-free defect census of two-subset disjointness graphs."""
from itertools import combinations
from collections import Counter
from math import comb, factorial


def model(n):
    edges=list(combinations(range(n),2))
    adj=[tuple(j for j,f in enumerate(edges) if not(set(e)&set(f))) for e in edges]
    return edges,adj

def bad_count(colors,adj):
    return sum(1 for neighbors in adj if 1 not in Counter(colors[v] for v in neighbors).values())

def normalized_proper_colorings(n,k):
    edges,adj=model(n)
    m=len(edges)
    coloring=[-1]*m
    coloring[0]=0
    # A dynamic deterministic order is legal under color-canonicalization.
    def recurse(used,unassigned):
        if not unassigned:
            if used==k:
                yield tuple(coloring)
            return
        v=max(unassigned,key=lambda v:(len({coloring[w] for w in adj[v] if coloring[w]>=0}), sum(coloring[w]>=0 for w in adj[v]),len(adj[v]),-v))
        rest=unassigned-{v}
        forbid={coloring[w] for w in adj[v] if coloring[w]>=0}
        for c in range(min(k,used+1)):
            if c not in forbid:
                coloring[v]=c
                yield from recurse(max(used,c+1),rest)
                coloring[v]=-1
    yield from recurse(1,set(range(1,m)))

def predicted(n):
    s=n-3
    total=comb(n,3)*2**comb(s,2)
    source=comb(n,3)*s*2**comb(s-1,2)
    return {comb(s,2):source,comb(s,2)+3:total-source}

def canonical_pcf(n):
    e,adj=model(n)
    colors=tuple(a for a,b in e)
    assert len(set(colors))==n-1
    assert all(colors[i]!=colors[j] for i in range(len(e)) for j in adj[i])
    return bad_count(colors,adj)

def main():
    # Direct enumeration is independent of the tournament argument.
    for n in range(5,8):
        _,adj=model(n)
        histogram=Counter(bad_count(c,adj) for c in normalized_proper_colorings(n,n-2))
        target=Counter({k:v for k,v in predicted(n).items() if v})
        assert histogram==target,(n,histogram,target)
        assert canonical_pcf(n)==0
        print('EXHAUSTIVE_OPTIMAL_COLORINGS',n,dict(sorted(histogram.items())))
    for n in range(5,31):
        assert canonical_pcf(n)==0,n
    # Exceptional graphs: KG(3,2) is edgeless, KG(4,2) is three independent edges.
    for n in (3,4):
        edges,adj=model(n)
        assert (n==3 and all(not a for a in adj)) or (n==4 and all(len(a)==1 for a in adj))
    print('CONSTRUCTIVE_UPPER_BOUND_OK n=5..30')
    print('VERIFY_OK')

if __name__=='__main__':main()
