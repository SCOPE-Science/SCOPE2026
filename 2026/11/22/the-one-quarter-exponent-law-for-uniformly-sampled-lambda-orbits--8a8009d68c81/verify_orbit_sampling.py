#!/usr/bin/env python3
"""Exact finite checks for the equal-orbit lambda-sampling theorem.

No external packages; full orbit partitions and independent rank-increment
subset census are compared over small prime fields. The unbounded L1 result
is proved mathematically in RESULT.md, not inferred from these checks.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def subset_census(q, n):
    out=Counter()
    for mask in product((0, 1), repeat=n-1):
        k=0
        weight=1
        exponent=0
        for m, b in enumerate(mask, 1):
            exponent+=k
            if b:
                weight*=q**(m-k)-1
                k+=1
        out[(k, exponent)]+=weight
    return out


def rank(M,p):
    rows=[r[:] for r in M]
    if not rows:return 0
    h=len(rows); w=len(rows[0]); rk=0
    for j in range(w):
        piv=next((i for i in range(rk,h) if rows[i][j]%p),None)
        if piv is None:continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        inv=pow(rows[rk][j],-1,p)
        rows[rk]=[(u*inv)%p for u in rows[rk]]
        for i in range(rk+1,h):
            if rows[i][j]:
                a=rows[i][j]
                rows[i]=[(u-a*v)%p for u,v in zip(rows[i],rows[rk])]
        rk+=1
        if rk==h:break
    return rk


def exhaustive_census(q,n):
    pos=[(i,j) for i in range(n) for j in range(i+1,n)]
    ind={v:i for i,v in enumerate(pos)}
    triple=[(ind[(i,k)],ind[(k,j)],t) for t,(i,j) in enumerate(pos) for k in range(i+1,j)]
    mats=list(product(range(q),repeat=len(pos)))
    unseen=set(mats)
    seen=Counter()
    while unseen:
        b=next(iter(unseen))
        mat=[[0]*n for _ in range(n)]
        for (i,j),v in zip(pos,b):mat[i][j]=v
        rk=rank(mat,q)
        orbit=set()
        for a in mats:
            w=list(b)
            for i,j,t in triple:w[t]=(w[t]+a[i]*b[j])%q
            orbit.add(tuple(w))
        assert orbit<=unseen, 'overlap between distinct group-action orbits'
        unseen.difference_update(orbit)
        ell=0
        while q**ell<len(orbit):ell+=1
        assert q**ell==len(orbit), 'non-power-of-q orbit'
        for item in orbit:
            mm=[[0]*n for _ in range(n)]
            for (i,j),v in zip(pos,item):mm[i][j]=v
            assert rank(mm,q)==rk, 'rank is not orbit-invariant'
        seen[(rk,ell)]+=1
    return seen


def matrix_rank_recursion(q,n):
    # Counts of individual matrices by (matrix rank, lambda orbit exponent).
    m={(0,0):1}
    for s in range(1,n):
        nxt=defaultdict(int)
        for (r,ell),v in m.items():
            nxt[(r,ell+r)]+=v*q**r
            nxt[(r+1,ell+r)]+=v*(q**s-q**r)
        m=dict(nxt)
    return Counter({(r,ell):v//q**ell for (r,ell),v in m.items() if v})


def main():
    for q,n in [(2,2),(2,3),(3,3),(5,3),(2,4),(3,4),(2,5)]:
        expected=subset_census(q,n)
        direct=exhaustive_census(q,n)
        assert expected==direct, (q,n,expected,direct)
        assert direct==matrix_rank_recursion(q,n)
        print('exhaustive q=%d n=%d orbits=%d'%(q,n,sum(direct.values())))
    for q in (2,3,4,5,7):
        for n in range(2,16):
            a=subset_census(q,n)
            b=matrix_rank_recursion(q,n)
            assert a==b,(q,n)
            K=sum(a.values())
            D=comb(n-1,2)
            assert sum(v for (k,ell),v in a.items() if ell==0)==q**(n-1)
            if n>=3:
                assert sum(v for (k,ell),v in a.items() if ell==D)==q*(q-1)**(n-2)
                assert set(ell for k,ell in a)==set(range(D+1))
            mu=sum(ell*v for (k,ell),v in a.items())/K
            print('moments q=%d n=%d K=%d mean_exponent=%.6f'%(q,n,K,mu)) if n in (6,10,14) else None
    print('EQUAL_ORBIT_LAMBDA_BIAS_CHECKS_PASSED')

if __name__=='__main__':main()
