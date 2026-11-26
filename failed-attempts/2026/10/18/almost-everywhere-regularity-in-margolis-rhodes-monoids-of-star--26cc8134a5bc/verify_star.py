#!/usr/bin/env python3
"""Independent exhaustive checks for MR(star) maps (mathematical data only)."""
from itertools import product
from math import comb, factorial

def rook(n):
    return sum(comb(n,k)**2*factorial(k) for k in range(n+1))

def continuous(f,m):
    n=m+1
    # A simplex of a star contains at most two vertices; if two, one is 0.
    for target in range(n):
        fiber={i for i,x in enumerate(f) if x==target}
        if len(fiber)>2 or (len(fiber)==2 and 0 not in fiber):
            return False
    for leaf in range(1,n):
        fiber={i for i,x in enumerate(f) if x==0 or x==leaf}
        if len(fiber)>2 or (len(fiber)==2 and 0 not in fiber):
            return False
    return True

def regular_by_sections(f,m):
    n=m+1
    image=sorted(x for x in set(f) if x>=0)
    fibers=[[i for i,x in enumerate(f) if x==y] for y in image]
    for chosen in product(*fibers):
        g=[-1]*n
        for y,x in zip(image,chosen):g[y]=x
        if continuous(g,m):return True
    return False

def actual(m):
    n=m+1
    totals={'total':0,'regular':0,'idempotents':0,'noninjective':0,'nonregular':0}
    rank_totals={k:0 for k in range(n+1)}
    rank_nonregular={k:0 for k in range(n+1)}
    for f in product(range(-1,n),repeat=n):
        if not continuous(f,m):continue
        totals['total']+=1
        image=[y for y in f if y>=0]
        k=len(set(image))
        rank_totals[k]+=1
        inj=len(image)==k
        reg=regular_by_sections(f,m)
        totals['regular']+=reg
        totals['nonregular']+=not reg
        totals['noninjective']+=not inj
        totals['idempotents']+=all(y<0 or f[y]==y for y in f)
        rank_nonregular[k]+=not reg
    return totals,rank_totals,rank_nonregular

def expected(m):
    r=rook(m)
    rprev=rook(m-1)
    total=(m+2)*(r+m)
    noninj=m+m*m*rprev
    nonreg=m*(r-m*rprev-1)
    idem=2**(m+1)+m+m*2**(m-1)
    rank_totals={}
    nonreg_ranks={}
    for k in range(m+2):
        inj=0
        if k<=m: inj+=comb(m,k)*factorial(m+1)//factorial(m+1-k)
        if 1<=k<=m+1:inj+=comb(m,k-1)*factorial(m)//factorial(m-k+1)
        if k==1:inj+=m
        if k==2:inj+=m*m
        noninj_k=0
        if k==1:noninj_k=m
        if 1<=k<=m:noninj_k+=m*m*comb(m-1,k-1)**2*factorial(k-1)
        rank_totals[k]=inj+noninj_k
        nonreg_ranks[k]=comb(m,k-1)*comb(m,k)*factorial(k) if 2<=k<=m else 0
    return {'total':total,'regular':total-nonreg,'nonregular':nonreg,'noninjective':noninj,'idempotents':idem},rank_totals,nonreg_ranks

if __name__=='__main__':
    for m in range(1,6):
        x=actual(m);y=expected(m)
        if x!=y:raise AssertionError((m,x,y))
        print('m=',m, 'actual=',x[0], 'rank_counts=',list(x[1].values()), 'nonregular_by_rank=',list(x[2].values()))
    # independent rook recurrence and finite ratio diagnostics
    for n in range(1,150):
        assert rook(n+1)==2*(n+1)*rook(n)-n*n*rook(n-1)
    print('VERIFY_OK: exhaustive continuous maps on stars m=1..5, regular sections, idempotents, rank distributions, Laguerre recurrence.')
