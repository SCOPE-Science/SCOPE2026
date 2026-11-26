#!/usr/bin/env python3
"""Independent finite-field tests for group unit-conjugacy strata of square-zero quiver algebras."""
from itertools import product,combinations
from collections import Counter

def ff_add(q,a,b): return (a^b) if q==4 else (a+b)%q

def ff_neg(q,a): return a if q==4 else (-a)%q

def ff_mul(q,a,b):
    if q!=4:return a*b%q
    z=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:z ^= 1<<(i+j)
    for i in (2,):
        if z&(1<<i):z ^= 0b111<<(i-2)
    return z

def add_edges(q,g,h,edges):
    d,x=g;e,y=h
    return (tuple(ff_mul(q,a,b) for a,b in zip(d,e)),
            tuple(ff_add(q, ff_mul(q,d[i],y[z]),ff_mul(q,x[z],e[j])) for z,(i,j) in enumerate(edges)))

def group_elems(q,n,edges):
    nonzero=range(1,q)
    return [(d,x) for d in product(nonzero,repeat=n) for x in product(range(q),repeat=len(edges))]

def rank_edges(n,eds):
    par=list(range(n))
    def find(x):
        while par[x]!=x:x=par[x]
        return x
    for a,b in eds:
        a=find(a);b=find(b)
        if a!=b:par[a]=b
    return n-len({find(i) for i in range(n)})

def pred_classes(q,n,edges):
    out=Counter()
    for d in product(range(1,q),repeat=n):
        equal=[e for e,(i,j) in enumerate(edges) if d[i]==d[j]]
        unequal=len(edges)-len(equal)
        for mask in range(1<<len(equal)):
            F=[edges[equal[z]] for z in range(len(equal)) if mask>>z&1]
            r=rank_edges(n,F)
            assert len(F)>=r
            orbit_count=(q-1)**(len(F)-r)
            cls_size=(q**unequal)*(q-1)**r
            out[cls_size]+=orbit_count
    return out

def direct_classes(q,n,edges):
    elems=group_elems(q,n,edges)
    N=len(elems)
    counts=Counter()
    for g in elems:
        cent=sum(add_edges(q,g,h,edges)==add_edges(q,h,g,edges) for h in elems)
        size=N//cent
        assert cent*size==N
        counts[size]+=1
    assert all(v%s==0 for s,v in counts.items())
    return Counter({s:v//s for s,v in counts.items()})


def pred_classes_by_flats(q,n,edges):
    m=len(edges); lam=q-1; out=Counter()
    for Hmask in range(1<<m):
        H=[edges[j] for j in range(m) if Hmask>>j&1]
        rH=rank_edges(n,H)
        # Matroid-flat criterion: adding any omitted edge must increase rank.
        if any(rank_edges(n,H+[edges[j]])==rH for j in range(m) if not Hmask>>j&1):
            continue
        outside=[edges[j] for j in range(m) if not Hmask>>j&1]
        # Chromatic polynomial of contraction by inclusion-exclusion.
        colourings=0
        for mask in range(1<<len(outside)):
            subset=[outside[j] for j in range(len(outside)) if mask>>j&1]
            colourings+=(-1)**len(subset)*lam**(n-rank_edges(n,H+subset))
        assert colourings>=0
        for Smask in range(1<<len(H)):
            S=[H[j] for j in range(len(H)) if Smask>>j&1]
            rS=rank_edges(n,S)
            assert len(S)>=rS
            out[q**(m-len(H))*lam**rS]+=colourings*lam**(len(S)-rS)
    return out

def predicted_total_tutte(q,n,edges):
    z=0
    for mask in range(1<<len(edges)):
        F=[edges[i] for i in range(len(edges)) if mask>>i&1]
        exponent=2*(n-rank_edges(n,F))+len(F)-n
        # may be negative for pathological graph? actual exponent >=0 if loopless.
        assert exponent>=0
        z+=(q-1)**exponent
    return z

def main():
    configs=[
      (2,2,[(0,1)]), (3,2,[(0,1)]), (4,2,[(1,0)]),
      (3,3,[(0,1),(1,2)]), (3,3,[(0,1),(0,2)]),
      (3,3,[(0,1),(1,2),(2,0)]),
      (2,4,[(0,1),(1,2),(2,3)]),
      (3,2,[(0,1),(0,1)]),
      (3,3,[(0,1),(1,0)]),
      (4,2,[(0,1),(0,1)]),
      (3,3,[]),
      (3,1,[(0,0)]),
      (3,2,[(0,1),(1,1)]),
      (4,2,[(0,0),(0,1)]),
    ]
    for q,n,edges in configs:
        p=pred_classes(q,n,edges)
        d=direct_classes(q,n,edges)
        assert p==d,(q,n,edges,p,d)
        assert p==pred_classes_by_flats(q,n,edges)
        assert sum(p.values())==predicted_total_tutte(q,n,edges)
        assert sum(size*count for size,count in p.items())==(q-1)**n*q**len(edges)
        print('OK',q,n,edges,'|G|',(q-1)**n*q**len(edges),'class-profile',sorted(p.items()))
    print('VERIFY_OK_QUIVER_UNIT_GROUP_CONJUGACY')
if __name__=='__main__':main()
