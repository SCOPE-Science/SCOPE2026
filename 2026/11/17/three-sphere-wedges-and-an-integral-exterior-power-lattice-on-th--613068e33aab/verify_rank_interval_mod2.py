#!/usr/bin/env python3
"""Independent boundary-matrix corroboration over F2, not an integral proof."""
from itertools import combinations
from collections import defaultdict
from math import comb

def run(n):
    words=[m for m in range(1,1<<n) if 1<=m.bit_count()<=3]
    # Find maximal cliques by depth-first Bron--Kerbosch independent of Morse code.
    adj={a:{b for b in words if b!=a and (a^b).bit_count()<=2} for a in words}
    facets=[]
    def BK(R,P,X):
        if not P and not X:
            facets.append(tuple(sorted(R)));return
        pivot=max(P|X,key=lambda u:len(P&adj[u])) if P or X else None
        for v in tuple(sorted(P-adj[pivot] if pivot is not None else P)):
            BK(R|{v},P&adj[v],X&adj[v]);P.remove(v);X.add(v)
    BK(set(),set(words),set())
    by_dim=defaultdict(set)
    for F in facets:
        for size in range(1,len(F)+1):
            by_dim[size-1].update(combinations(F,size))
    rank={}
    for k in range(1,max(by_dim)+1):
        prev={f:j for j,f in enumerate(sorted(by_dim[k-1]))}
        pivots={}
        for f in sorted(by_dim[k]):
            col=0
            for j in range(len(f)):
                sub=f[:j]+f[j+1:]
                col^=1<<prev[sub]
            while col:
                p=col.bit_length()-1
                if p in pivots:col^=pivots[p]
                else:pivots[p]=col;break
        rank[k]=len(pivots)
    betti={k:len(by_dim[k])-rank.get(k,0)-rank.get(k+1,0)-(k==0) for k in by_dim}
    assert {k:b for k,b in betti.items() if b}!={}
    assert {k:b for k,b in betti.items() if b}=={3:comb(n,4)}
    return n,len(words),sum(map(len,by_dim.values())),{k:b for k,b in betti.items() if b}

if __name__=='__main__':
    for n in range(4,8):print('n vertices faces nonzero_reduced_betti_F2',run(n))
    print('RANK_INTERVAL_1_3_MOD2_PASS')
