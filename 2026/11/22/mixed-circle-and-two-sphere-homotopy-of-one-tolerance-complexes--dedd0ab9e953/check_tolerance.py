#!/usr/bin/env python3
"""Independent finite homology checks for one-tolerance of disjoint simplices.
All calculations over GF(p) use incidence faces, not the gluing theorem.
"""
from itertools import combinations, product
from math import comb


def faces(sizes):
    offs = []
    at = 0
    for sz in sizes:
        offs.append(tuple(range(at,at+sz)))
        at += sz
    groups={v:i for i,B in enumerate(offs) for v in B}
    result=[set() for _ in range(max(sizes)+2)]
    for k in range(1,max(sizes)+3):
        for s in combinations(range(at),k):
            counts = [0]*len(sizes)
            for v in s: counts[groups[v]]+=1
            if k-max(counts)<=1:
                result[k-1].add(s)
    while result and not result[-1]:result.pop()
    return [sorted(s) for s in result]


def rank_mod(Mrows,ncols,p):
    """Sparse row reduction over prime field."""
    pivots={}
    for row in Mrows:
        d=dict(row)
        while d:
            k=min(d)
            if k not in pivots:
                v=d[k]%p
                iv=pow(v,-1,p)
                pivots[k]={j:(val*iv)%p for j,val in d.items() if (val*iv)%p}
                break
            pv=pivots[k]
            factor=d[k]%p
            for j,val in pv.items():
                w=(d.get(j,0)-factor*val)%p
                if w:d[j]=w
                else:d.pop(j,None)
    return len(pivots)


def betti(sizes,p):
    groups=faces(sizes)
    ranks=[0]
    for i in range(1,len(groups)):
        rows={s:i for i,s in enumerate(groups[i-1])}
        boundaries={s:[] for s in groups[i-1]}
        for j,s in enumerate(groups[i]):
            for k in range(len(s)):
                face=s[:k]+s[k+1:]
                boundaries[face].append((j,(-1)**k%p))
        rank=rank_mod([dict(row) for row in boundaries.values()],len(groups[i]),p)
        ranks.append(rank)
    ranks.append(0)
    result=[len(groups[k])-ranks[k]-ranks[k+1] for k in range(len(groups))]
    return result, tuple(map(len,groups))


def predicted(sizes):
    r=len(sizes)
    h1=comb(r-1,2) if r>=2 else 0
    h2=sum((sizes[i]-1)*(sizes[j]-1) for i in range(r) for j in range(i+1,r))
    return (1,h1,h2)


def run():
    tests=[(2,2),(2,3),(1,3,2),(2,2,2),(3,2,3),(1,1,1,1),
           (2,2,2,2),(1,2,3,1),(3,3,3),(2,2,2,3)]
    total=0
    for sz in tests:
        x,y=predicted(sz),{}
        for p in (2,3,5):
            actual,f=betti(sz,p)
            expect=list(x)+[0]*max(0,len(actual)-len(x))
            if actual!=expect[:len(actual)]:
                raise AssertionError((sz,p,actual,x,f))
            y[p]=actual
            total+=1
        print(f'blocks={sz}, f_vector={f}, betti={y[2]}')
    print(f'PASS: {total} independent characteristic-field homology comparisons')

if __name__=='__main__':run()
