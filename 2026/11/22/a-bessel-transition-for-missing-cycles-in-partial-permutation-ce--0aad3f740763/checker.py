#!/usr/bin/env python3
"""Finite independent centralizer enumeration and critical Bessel-limit checks."""
from itertools import combinations, permutations
from math import comb, factorial

def sigma_cycles(m, ell):
    return tuple(i//ell*ell+(i+1)%ell for i in range(m*ell))

def composition_partial(sigma, f):
    # output (sigma circ f, f circ sigma), undefined=-1
    return (tuple(sigma[y] if y>=0 else -1 for y in f),
            tuple(f[sigma[i]] for i in range(len(sigma))))

def direct_counts(m, ell):
    n=m*ell
    s=sigma_cycles(m,ell)
    counts={}
    for k in range(n+1):
        c=0
        for dom in combinations(range(n), k):
            for img in combinations(range(n), k):
                for p in permutations(img):
                    f=[-1]*n
                    for d,v in zip(dom,p):f[d]=v
                    l,r=composition_partial(s,f)
                    if l==r:c+=1
        counts[k]=c
    return counts

def formula_counts(m,ell):
    return {k*ell:comb(m,k)**2*factorial(k)*ell**k for k in range(m+1)}

for m,ell in [(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(1,4),(1,5)]:
    direct=direct_counts(m,ell)
    pred=formula_counts(m,ell)
    for k in range(m*ell+1):assert direct[k]==pred.get(k,0),(m,ell,k,direct[k],pred.get(k,0))
    print('PASS m=%d ell=%d counts=%s'%(m,ell,[direct[k] for k in range(0,m*ell+1)]))

# Numerically compare the omitted-cycle law with limiting Bessel limiting law
from math import exp
for lam, m, ell in [(1,40,40),(1,160,160),(2,40,20),(2,160,80)]:
    # stable recursive weights for j missing cycles
    w=[1.]
    for j in range(m):w.append(w[-1]*(m-j)/(ell*(j+1)**2))
    Z=sum(w)
    b=[1.]
    for j in range(100):b.append(b[-1]*lam/(j+1)**2)
    B=sum(b)
    TV=.5*sum(abs((w[j]/Z if j<=m else 0)-(b[j]/B)) for j in range(len(b)))
    print('CRITICAL lam=%g m=%d ell=%d TV=%.8f'%(lam,m,ell,TV))
    assert TV<.04
print('ALL CHECKS PASSED')
