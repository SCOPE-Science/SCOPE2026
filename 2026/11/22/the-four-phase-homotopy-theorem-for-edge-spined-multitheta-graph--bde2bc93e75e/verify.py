#!/usr/bin/env python3
"""Exact finite-field simplicial chain tests for edge-spined multitheta graphs."""
from itertools import product
from collections import defaultdict

def edges(lengths):
    e=[(0,1)]
    v=2
    for length in lengths:
        prev=0
        for _ in range(length-1):
            e.append((prev,v)); prev=v; v+=1
        e.append((prev,1))
    return v,e

def independent_faces(n,edges):
    adj=[0]*n
    for i,j in edges:
        adj[i]|=1<<j; adj[j]|=1<<i
    bysize=[[] for _ in range(n+1)]
    def rec(left,chosen):
        if not left:
            bysize[chosen.bit_count()].append(chosen);return
        bit=left&-left; idx=bit.bit_length()-1
        rec(left^bit,chosen)
        rec((left^bit)&~adj[idx],chosen|bit)
    rec((1<<n)-1,0)
    while bysize and not bysize[-1]:bysize.pop()
    return bysize

def rank_mod2(columns):
    pivots={}
    for v in columns:
        while v:
            h=v.bit_length()-1
            if h not in pivots:
                pivots[h]=v;break
            v^=pivots[h]
    return len(pivots)

def reduced_betti(by):
    # boundary of 0-faces onto the empty face is included
    ranks=[0]*len(by)
    for k in range(1,len(by)):
        rowidx={mask:i for i,mask in enumerate(by[k-1])}
        columns=[]
        for face in by[k]:
            vec=0; left=face
            while left:
                bit=left&-left; left^=bit
                vec^=1<<rowidx[face^bit]
            columns.append(vec)
        ranks[k]=rank_mod2(columns)
    betti={}
    for k in range(1,len(by)):
        h= len(by[k]) - ranks[k] - (ranks[k+1] if k+1<len(by) else 0)
        if h:betti[k-1]=h
    return betti

def prediction(lengths):
    residues={p%3 for p in lengths}
    r=sum(p//3 for p in lengths)
    if 0 in residues and 2 in residues:return {}
    if 0 in residues:return {r-1:1}
    if 2 in residues:return {r:2}
    return {r:1}

def main():
    tested=0; groups=[]
    for m, domain in ((2,(2,3,4,5,6,7,8)),(3,(2,3,4,5)),(4,(2,3,4))):
        local=0
        # symmetric multisets avoid repetitions of isomorphic arm permutations
        from itertools import combinations_with_replacement
        for lens in combinations_with_replacement(domain,m):
            n,e=edges(lens)
            by=independent_faces(n,e)
            actual=reduced_betti(by)
            expected=prediction(lens)
            assert actual==expected,(lens,actual,expected)
            tested+=1;local+=1
        groups.append((m,local))
    extra=((2,2,2,2,2),(3,3,3,3,3),(4,4,4,4,4),(2,3,4,5,2),(5,5,5,5),(2,2,2,2,2,2),(3,3,3,3,3,3))
    for lens in extra:
        n,e=edges(lens)
        actual=reduced_betti(independent_faces(n,e))
        assert actual==prediction(lens),(lens,actual,prediction(lens))
    print('PASS: mod-2 reduced chain homology matches the uniform prediction')
    for m,num in groups:print(f' {m} arms: {num} symmetry-reduced length tuples')
    print(f' extra four-to-six-arm stress cases: {len(extra)}')
    print(f' total: {tested+len(extra)} graph complexes; exact face generation, boundary ranks')
    for L in ((2,2),(3,3),(4,4),(2,4),(3,5),(4,5),(3,3,5),(4,4,4),(3,4,5)):
        print(L,prediction(L))
if __name__=='__main__': main()
