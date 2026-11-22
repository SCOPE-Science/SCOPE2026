#!/usr/bin/env python3
"""Finite, independently reconstructible sanity check for prime cyclic Kneser neighborhood quotients."""
from itertools import combinations
from math import comb

def fvector_and_boundary(p):
    assert p>=5
    subsets=[sum(1<<i for i in I) for s in range(2,p-1) for I in combinations(range(p),s)]
    size=lambda a:a.bit_count()
    ranks={a:size(a) for a in subsets}
    levels={k:[v for v in subsets if ranks[v]==k] for k in range(2,p-1)}
    rotate=lambda a:sum(((a>>i)&1) << ((i+1)%p) for i in range(p))
    def norm(t):
        w=t; best=t
        for _ in range(1,p):
            w=tuple(rotate(a) for a in w)
            if w<best:best=w
        return best
    out=[set() for _ in range(p-3)]
    def step(chain,mask,start):
        if chain:out[len(chain)-1].add(norm(tuple(chain)))
        for j in range(start,p-1):
            if j not in levels:continue
            for x in levels[j]:
                if (x&mask)==mask:step(chain+[x],x,j+1)
    step([],0,2)
    cell=[sorted(x) for x in out]
    idx=[{v:i for i,v in enumerate(vs)} for vs in cell]
    boundaries=[None]
    for d in range(1,len(cell)):
        cols=[]
        for ch in cell[d]:
            data={}
            for k in range(d+1):
                face=norm(ch[:k]+ch[k+1:]);i=idx[d-1][face]
                data[i]=data.get(i,0)+(-1 if k%2 else 1)
            cols.append({i:v for i,v in data.items() if v})
        boundaries.append(cols)
    for d in range(2,len(cell)):
        for col in boundaries[d]:
            accum={}
            for mid,a in col.items():
                for j,b in boundaries[d-1][mid].items():accum[j]=accum.get(j,0)+a*b
            assert all(x==0 for x in accum.values()),('boundary square !=0',d)
    return list(map(len,cell)),boundaries

def modrank(cols,p):
    basis={}
    for col in cols:
        v={k:a%p for k,a in col.items() if a%p}
        while v:
            k=min(v)
            if k not in basis:
                c=pow(v[k],-1,p);basis[k]={i:(x*c)%p for i,x in v.items() if x*c%p};break
            r=basis[k];z=v[k]
            for j,t in r.items():
                nv=(v.get(j,0)-z*t)%p
                if nv:v[j]=nv
                else:v.pop(j,None)
    return len(basis)

if __name__=='__main__':
    for p in (5,7):
        cells,boundaries=fvector_and_boundary(p)
        print('p',p,'cells',cells,'Euler',sum((-1)**i*c for i,c in enumerate(cells)))
        for prime in (2,3,5,7,11):
            ranks=[0]+[modrank(cols,prime) for cols in boundaries[1:]]+[0]
            betti=[cells[i]-ranks[i]-ranks[i+1] for i in range(len(cells))]
            print('  characteristic',prime,'boundary ranks',ranks[1:-1], 'homology dimensions',betti)
        assert sum((-1)**i*c for i,c in enumerate(cells))==-(p-3)
    q=[(a,b) for a in range(7) for b in range(7) if a!=b]
    by_diff={((b-a)%7) for a,b in q}
    assert by_diff==set(range(1,7))
    # A cycle consisting of edge a and reversed edge b has voltage a-b mod 7.
    assert set(((a-1)%7 for a in by_diff if a!=1))==set(range(1,6))
    assert 1 in {((a-1)%7) for a in by_diff if a!=1}
    print('CHECK_RANK_SELECTED_KNESER_ROTATION_OK')
