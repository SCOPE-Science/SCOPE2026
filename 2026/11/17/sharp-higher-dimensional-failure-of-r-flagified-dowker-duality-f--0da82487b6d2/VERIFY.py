#!/usr/bin/env python3
"""Finite checks for uniform-incidence higher-flagified Dowker complexes.
The general classification is proved separately using attaching maps.
"""
from itertools import combinations
from math import comb

def build(n,r):
    y=list(combinations(range(n),r)); vid={s:i for i,s in enumerate(y)}
    d={tuple()}
    for i in range(n):
        star=[vid[s] for s in y if i in s]
        for s in range(1,len(star)+1):
            d.update(combinations(star,s))
    specials=set()
    for t in combinations(range(n),r+1):
        face=tuple(sorted(vid[tuple(x for x in t if x!=i)] for i in t))
        assert face not in d
        specials.add(face)
        assert all(face[:j]+face[j+1:] in d for j in range(r+1))
    out=d|specials
    # Direct relation check through size r+2, independent of structural classification.
    upto=min(r+2,len(y))
    for sz in range(1,upto+1):
        for v in combinations(range(len(y)),sz):
            direct=(bool(set.intersection(*(set(y[j]) for j in v))) if sz<=r
                    else all(set.intersection(*(set(y[j]) for j in sub)) for sub in combinations(v,r)))
            assert (v in out)==direct,(n,r,v,direct)
    return y,out,len(specials)

def rank_mod_2(rows):
    piv={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in piv:x ^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def betti(faces):
    mx=max(map(len,faces))-1
    layers={d:sorted(f for f in faces if len(f)==d+1) for d in range(mx+1)}
    ranks={}
    for d in range(1,mx+1):
        idx={f:i for i,f in enumerate(layers[d-1])}
        columns=[]
        for f in layers[d]:
            x=0
            for j in range(len(f)):x ^=1<<idx[f[:j]+f[j+1:]]
            columns.append(x)
        ranks[d]=rank_mod_2(columns)
    b={d:len(layers[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(mx+1)}
    b[0]-=1
    return {d:v for d,v in b.items() if v}

if __name__=='__main__':
    total=0
    for n,r in [(4,2),(5,2),(6,2),(5,3),(6,3)]:
        y,faces,new=build(n,r)
        expected=comb(n-1,r+1)
        assert new==comb(n,r+1)
        b=betti(faces)
        assert b=={r:expected},(n,r,b)
        print(f'n={n} r={r} vertices={len(y)} nonempty_faces={len(faces)-1} new_r_faces={new} reduced_betti={b}')
        total+=len(faces)-1
    print('CHECK_HIGHER_FLAG_DOWKER_PASS',total)
