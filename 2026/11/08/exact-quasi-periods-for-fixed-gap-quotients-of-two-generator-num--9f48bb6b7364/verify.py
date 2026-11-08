#!/usr/bin/env python3
"""Exact integer cross-check of fixed-gap semigroup-quotient Frobenius formula."""
from math import gcd

def residues(p,h):
    inv=pow(h,-1,p)
    out=[]
    for r in range(p):
        for t in range(p):
            j=((r*r+(h-2)*r-h-t*r)*inv)%p
            if j<=t:
                out.append((t,j))
                break
        else: raise AssertionError('missing branch')
    return out

def independent_frobenius(a,h,p):
    # Direct semigroup membership using inverse of h modulo a.
    F=a*(a+h)-2*a-h
    ih=pow(h,-1,a)
    last=-1
    for n in range(F//p+1):
        m=p*n
        y=(m*ih)%a
        if m < y*(a+h):
            last=n
    return last

cases=0
for p in range(2,21):
    for h in range(1,11):
        if gcd(p,h)>1: continue
        B=residues(p,h)
        assert B[0]==(p-1,p-1)
        assert B.count(B[0])==1
        for a in range(max(p,h*(p-1))+1,max(p,h*(p-1))+24):
            if gcd(a,h)>1: continue
            t,j=B[a%p]
            num=a*a+(h-2-t)*a-h*(1+j)
            assert num%p==0,(p,h,a,num)
            expected=num//p
            direct=independent_frobenius(a,h,p)
            assert expected==direct,(p,h,a,expected,direct)
            cases+=1
print('EXACT_INDEPENDENT_DIRECT_CHECK_OK cases=',cases,'p=2..20 h=1..10')
print('ZERO_RESIDUE_RIGIDITY_CHECK_OK all tested p,h')
print('INFINITE_PERIOD_PROOF_REQUIRED true')
