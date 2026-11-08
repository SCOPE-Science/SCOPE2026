#!/usr/bin/env python3
"""Exact S6 rational homology character of the bidirected K(2,6) multipath complex."""
from verify_k2_6 import build_faces
from functools import lru_cache
from collections import Counter
from math import factorial

def partitions(n,cap=None):
    if n==0:
        yield (); return
    if cap is None:cap=n
    for a in range(min(n,cap),1-1,-1):
        for tail in partitions(n-a,a):yield (a,)+tail

def fixedperm(mu):
    s=[];k=0
    for length in mu:
        for i in range(length):s.append(k+(i+1)%length)
        k+=length
    return s

def perm_sign(arr):
    inversions=sum(arr[i]>arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))
    return -1 if inversions%2 else 1

def lefschetz(mu,faces):
    perm=fixedperm(mu)
    trace=[0]*5
    for f in faces:
        if not f:continue
        img=[x//6*6+perm[x%6] for x in f]
        if tuple(sorted(img))==f:trace[len(f)]+=perm_sign(img)
    return 1 - sum((-1)**(k-1)*trace[k] for k in range(1,5)), trace

def rim_removals(lam,r):
    n=sum(lam)
    for nu in partitions(n-r):
        if len(nu)>len(lam):continue
        if any(nu[i]>lam[i] for i in range(len(nu))):continue
        skew={(i,j) for i in range(len(lam)) for j in range((nu[i] if i<len(nu) else 0),lam[i])}
        if len(skew)!=r:continue
        if any(all((i+di,j+dj) in skew for di,dj in ((0,0),(0,1),(1,0),(1,1))) for i,j in skew):continue
        seen={next(iter(skew))}; stack=list(seen)
        while stack:
            i,j=stack.pop()
            for q in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if q in skew and q not in seen:seen.add(q);stack.append(q)
        if len(seen)==r:yield nu,(-1)**(len({i for i,j in skew})-1)

@lru_cache(None)
def char(lam,mu):
    if not mu:return 1 if not lam else 0
    return sum(sign*char(nu,mu[1:]) for nu,sign in rim_removals(lam,mu[0]))

def zval(mu):
    c=Counter(mu)
    z=1
    for i,m in c.items():z *= i**m *factorial(m)
    return z

def main():
    faces=build_faces()
    cl=list(partitions(6))
    chars={mu:lefschetz(mu,faces)[0] for mu in cl}
    assert chars[(1,1,1,1,1,1)]==169
    decomp={}
    for lam in cl:
        numerator=sum(chars[mu]*char(lam,mu)*(factorial(6)//zval(mu)) for mu in cl)
        assert numerator%factorial(6)==0,(lam,numerator)
        mult=numerator//factorial(6)
        assert mult>=0,(lam,mult)
        if mult:decomp[lam]=mult
    assert chars=={(6,):1,(5,1):-1,(4,2):1,(4,1,1):1,(3,3):1,(3,2,1):-1,(3,1,1,1):-5,(2,2,2):1,(2,2,1,1):1,(2,1,1,1,1):-7,(1,1,1,1,1,1):169}
    assert decomp=={(4,2):2,(4,1,1):2,(3,3):1,(3,2,1):4,(3,1,1,1):2,(2,2,2):2,(2,2,1,1):3,(2,1,1,1,1):1}
    # Verify the full symmetric-group character orthogonality relations.
    for a in cl:
        for b in cl:
            inner=sum(char(a,mu)*char(b,mu)*(factorial(6)//zval(mu)) for mu in cl)
            assert inner==(factorial(6) if a==b else 0)
    print('cycle_type -> top_homology_trace')
    for mu in cl:print(mu,chars[mu])
    print('Specht_partition -> multiplicity')
    for lam,mul in decomp.items():print(lam,mul)
    assert sum(mul*char(lam,(1,)*6) for lam,mul in decomp.items())==169
    # independent total orthogonality and character reconstruction checks
    for mu in cl:
        assert sum(mult*char(lam,mu) for lam,mult in decomp.items())==chars[mu]
    print('ALL_CHARACTER_OK')
if __name__=='__main__':main()
