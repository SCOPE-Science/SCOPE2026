#!/usr/bin/env python3
"""Independent finite algebra and counting checks for random-cylinder covering."""
from itertools import combinations
from collections import Counter
from math import comb
from random import Random

def rank_mod(rows,p):
    if not rows:return 0
    a=[r[:] for r in rows]; h=len(a); w=len(a[0]); rk=0
    for col in range(w):
        pivot=next((i for i in range(rk,h) if a[i][col]%p),None)
        if pivot is None:continue
        a[rk],a[pivot]=a[pivot],a[rk]
        inv=pow(a[rk][col],-1,p)
        a[rk]=[(v*inv)%p for v in a[rk]]
        for i in range(h):
            if i!=rk and a[i][col]%p:
                fac=a[i][col]
                a[i]=[(v-fac*z)%p for v,z in zip(a[i],a[rk])]
        rk+=1
        if rk==h:break
    return rk

def predicted_rank(E,p,a,ell):
    b=p**a
    C=Counter(e%b for e in E)
    return sum(min(v,ell) for v in C.values())

def observed_rank(E,p,a,ell):
    t=ell*p**a
    return rank_mod([[comb(e,k)%p if k<=e else 0 for k in range(t)] for e in E],p)

def exact_deficiency_distribution(p,b,ell):
    # Each bucket has p distinct sites; build generating polynomial in marked count and deficit.
    dist={(0,0):1}
    for _ in range(b):
        nxt={}
        for (m,d),v in dist.items():
            for c in range(p+1):
                key=(m+c,d+max(0,c-ell))
                nxt[key]=nxt.get(key,0)+v*comb(p,c)
        dist=nxt
    for m in range(p*b+1):
        assert sum(v for (mm,d),v in dist.items() if mm==m)==comb(p*b,m)
    return dist

def finite_tests():
    checked=0
    for p,a in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)]:
        b=p**a; N=p*b
        for ell in range(1,p+1):
            if N<=9:
                samples=(E for m in range(N+1) for E in combinations(range(N),m))
            else:
                rng=Random(1000+N+ell)
                samples=([i for i in range(N) if rng.random()<0.28] for _ in range(500))
            for E in samples:
                assert observed_rank(E,p,a,ell)==predicted_rank(E,p,a,ell),(p,a,ell,E)
                checked+=1
        if b<=4:
            D=exact_deficiency_distribution(p,b,1)
            rng=Counter()
            for m in range(N+1):
                for E in combinations(range(N),m):
                    rng[(m,len(E)-predicted_rank(E,p,a,1))]+=1
            assert rng==Counter(D)
    print('PASS finite rank cases:',checked)
    print('PASS generating function coefficients for all subsets at p,b=(2,2),(3,3) and p,b=(2,4)')
    # Exact one-dimensional occupancy distribution for p=2, b=16, ell=1.
    p=2;b=16;ell=1;m=6
    dist=exact_deficiency_distribution(p,b,ell)
    prob0=dist.get((m,0),0)/comb(p*b,m)
    rng=Random(117); trials=20000
    estimates=[]
    for _ in range(trials):
        E=rng.sample(range(p*b),m)
        estimates.append(len(E)==predicted_rank(E,p,4,ell))
    assert abs(sum(estimates)/trials-prob0)<0.02
    print('PASS independent hypergeometric simulation; exact full-image probability:',format(prob0,'.9f'))

if __name__=='__main__':finite_tests()
