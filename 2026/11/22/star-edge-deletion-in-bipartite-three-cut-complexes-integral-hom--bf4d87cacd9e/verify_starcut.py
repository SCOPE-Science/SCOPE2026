#!/usr/bin/env python3
"""Finite, independent checks of the three-cut Alexander dual for star-deficient bicliques.

No scientific conclusions for unbounded parameters are inferred from these tests;
those follow from the explicit link and homotopy-pushout proof.
"""
from itertools import combinations
from math import comb
from collections import defaultdict


def C(n,k):
    return comb(n,k) if n>=k>=0 else 0


def graph_edges(a,b,t):
    # x=0, U=1..a-1, B=a..a+b-1; missing x--(first t B vertices)
    return {frozenset((u,a+j)) for u in range(a) for j in range(b)
            if u!=0 or j>=t}


def actual_dual(a,b,t):
    n=a+b
    edges=graph_edges(a,b,t)
    disconnected=[]
    for triple in combinations(range(n),3):
        ts=set(triple)
        # BFS connectivity of induced three-vertex subgraph
        seen={triple[0]}
        while True:
            nxt=seen|{v for v in ts for u in seen if frozenset((u,v)) in edges}
            if nxt==seen: break
            seen=nxt
        if len(seen)<3: disconnected.append(frozenset(triple))
    return {frozenset(S) for k in range(n+1) for S in combinations(range(n),k)
            if not any(T<=frozenset(S) for T in disconnected)}


def decomposed_dual(a,b,t):
    # L0 = sk1(U)*sk1(B), plus x*(sk0(U)*sk1(Q)), plus edges x--P
    U=range(1,a)
    B=range(a,a+b)
    Q=range(a+t,a+b)
    P=range(a,a+t)
    F=set()
    for k in range(3):
        for A in combinations(U,k):
            for l in range(3):
                for BB in combinations(B,l):F.add(frozenset(A+BB))
    for k in range(2):
        for A in combinations(U,k):
            for l in range(3):
                for QQ in combinations(Q,l):F.add(frozenset((0,)+A+QQ))
    for p in P:F.add(frozenset((0,p)))
    return F


def betti_mod2(F):
    bydim=defaultdict(list)
    for face in F:
        if face:bydim[len(face)-1].append(tuple(sorted(face)))
    for k in bydim:bydim[k].sort()
    ranks={}
    for k in sorted(bydim):
        if k==0:continue
        idx={f:i for i,f in enumerate(bydim[k-1])}
        pivots={}
        for f in bydim[k]:
            mask=0
            for j in range(len(f)):
                mask^=1<<idx[f[:j]+f[j+1:]]
            while mask:
                p=mask.bit_length()-1
                if p in pivots:mask^=pivots[p]
                else:pivots[p]=mask;break
        ranks[k]=len(pivots)
    return {k:len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in bydim}


def predicted(a,b,t):
    q=b-t
    beta3=C(a-2,2)*C(b-1,2)+(a-2)*C(q-1,2) if q else C(a-2,2)*C(b-1,2)
    beta1=t+(a-2 if q==0 else 0)
    return {0:1,1:beta1,2:0,3:beta3}


def main():
    cases=0
    for a in range(4,7):
        for b in range(4,7):
            for t in range(b+1):
                actual=actual_dual(a,b,t)
                expected=decomposed_dual(a,b,t)
                assert actual==expected,(a,b,t,len(actual^expected))
                hom=betti_mod2(actual)
                target=predicted(a,b,t)
                assert all(hom.get(k,0)==target.get(k,0) for k in set(hom)|set(target)),(a,b,t,hom,target)
                cases+=1
    print('PASS',cases,'full face-list identities and independent binary homology comparisons')
    a,b=5,6
    for t in range(b+1):
        F=actual_dual(a,b,t)
        print(f'K_{{{a},{b}}}-star({t}): dual faces={len(F)}, Betti={betti_mod2(F)}, predicted={predicted(a,b,t)}')
    return 0

if __name__=='__main__':raise SystemExit(main())
