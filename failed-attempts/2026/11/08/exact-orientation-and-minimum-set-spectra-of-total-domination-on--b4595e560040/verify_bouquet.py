#!/usr/bin/env python3
"""Independently enumerate valid orientations and directed total dominating sets
of cycle bouquets, using edge bit orientations and direct subset tests.
Only the standard-library is required.
"""
from itertools import product
from collections import Counter
from math import prod

def bouquet(lengths):
    assert lengths and all(L>=3 for L in lengths)
    edges=[]; petals=[]; v=1
    for L in lengths:
        internal=list(range(v,v+L-1)); v+=L-1
        chain=[0]+internal+[0]
        edges.extend(zip(chain[:-1],chain[1:]))
        petals.append(tuple(range(len(edges)-L,len(edges))))
    return v,edges,petals

def brute(lengths):
    nv, edges, petals=bouquet(lengths)
    cnt=Counter(); mincnt=Counter(); nvalid=0
    for orientation in range(1<<len(edges)):
        inp=[0]*nv; out=[0]*nv
        for ei,(a,b) in enumerate(edges):
            if orientation>>ei&1: a,b=b,a
            inp[b] |= 1<<a
            out[a] |= 1<<b
        if any(x==0 for x in inp): continue
        nvalid+=1
        best=nv+1; ways=0
        for chosen in range(1<<nv):
            if chosen.bit_count()>best: continue
            if all(inp[v]&chosen for v in range(nv)):
                if chosen.bit_count()<best:best=chosen.bit_count(); ways=1
                else:ways+=1
        assert best<=nv
        cnt[best]+=1
        mincnt[best]+=ways
    return cnt,mincnt,nvalid

def predicted(lengths):
    offset=2+sum(L-3 for L in lengths)
    counts=Counter({0:1})
    for L in lengths:
        nxt=Counter()
        for c,num in counts.items():
            nxt[c]+=num*(L-1)
            nxt[c+1]+=num*2
        counts=nxt
    counts.pop(0,0)
    return Counter({offset+c:n for c,n in counts.items() if n})

def predicted_min_sets(lengths):
    off=2+sum(L-3 for L in lengths)
    dp=Counter({0:1})
    for L in lengths:
        nx=Counter()
        for k,v in dp.items():
            nx[k]+=v*2*(L-2)
            nx[k+1]+=v*2
        dp=nx
    return Counter({off+c:c*v for c,v in dp.items() if c})

def main():
    profiles=[(3,), (4,), (6,), (3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5),(3,3,3),(3,3,4),(3,4,4),(4,4,4)]
    total=0
    for lens in profiles:
        got,gm,n=brute(lens); expect=predicted(lens); emm=predicted_min_sets(lens)
        assert got==expect, (lens,got,expect)
        assert gm==emm, (lens,gm,emm)
        assert sum(got.values())==n
        total+=n
        print('CHECK',lens,'valid_orientations',n,'scores',dict(sorted(got.items())),'minimum_sets',dict(sorted(gm.items())))
    print('VERIFY_OK', 'profiles',len(profiles),'valid_orientations',total, 'all_signed_edge_orientations_and_directed_total_domination=PASS', 'minimum_set_enumerator=PASS')
if __name__=='__main__':main()
