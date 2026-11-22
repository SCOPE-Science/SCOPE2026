#!/usr/bin/env python3
"""Exact ordinary location-domination enumerators for two 20-vertex cubic graphs."""
from itertools import combinations
from math import comb

def gp(n,k):
    nbs=[set() for _ in range(2*n)]
    def add(a,b): nbs[a].add(b);nbs[b].add(a)
    for i in range(n):
        add(i,(i+1)%n); add(i,n+i); add(n+i,n+(i+k)%n)
    assert len(nbs)==20 and all(len(x)==3 for x in nbs)
    return tuple(sum(1<<j for j in v) for v in nbs)

def valid(s,nb):
    sigs=set()
    for i in range(20):
        if s>>i&1: continue
        t=nb[i]&s
        if t==0 or t in sigs: return False
        sigs.add(t)
    return True

def spectrum(nb):
    count=[0]*21
    for k in range(21):
        for a in combinations(range(20),k):
            s=sum(1<<i for i in a)
            count[k]+=valid(s,nb)
    assert all(0<=count[k]<=comb(20,k) for k in range(21))
    return count

def check_desargues_isomorphism():
    # Explicit isomorphism from GP(10,3) to the bipartite 2-subset Kneser model H(5,2).
    mapping=(0,17,6,11,9,10,7,16,1,19,18,3,12,5,14,8,13,2,15,4)
    from itertools import combinations
    E=tuple(combinations(range(5),2))
    H=[0]*20
    for i,a in enumerate(E):
        for j,b in enumerate(E):
            if not(set(a)&set(b)):
                H[i] |= 1 << (10+j)
                H[10+j] |= 1 << i
    GP=gp(10,3)
    assert set(mapping)==set(range(20))
    for v in range(20):
        mapped=sum(1<<mapping[w] for w in range(20) if GP[v]>>w&1)
        assert mapped == H[mapping[v]]

if __name__=='__main__':
    check_desargues_isomorphism()
    D=spectrum(gp(10,3));P=spectrum(gp(10,2))
    delta=[p-d for p,d in zip(P,D)]
    assert D==[0,0,0,0,0,0,0,0,1475,15100,49826,83840,88890,66020,36330,15184,4825,1140,190,20,1],D
    assert P==[0,0,0,0,0,0,0,220,3935,21760,57054,87720,89940,66140,36330,15184,4825,1140,190,20,1],P
    assert delta==[0]*7+[220,2460,6660,7228,3880,1050,120]+[0]*7,delta
    assert sum(D)>0 and sum(P)>0
    print('PYTHON_EXACT_PASS')
    print('DESARGUES:',D)
    print('DODECAHEDRON:',P)
    print('DIFFERENCE:',delta)
