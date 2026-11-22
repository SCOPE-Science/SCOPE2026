#!/usr/bin/env python3
"""Exact checks for odd-prime super Catalan valuation spectra (stdlib)."""
from collections import Counter
from math import factorial

def vp_factorial(n,p):
    v=0
    while n:
        n//=p; v+=n
    return v

def score(m,n,p):
    return (vp_factorial(2*m,p)+vp_factorial(2*n,p)-vp_factorial(m,p)-vp_factorial(n,p)-vp_factorial(m+n,p))

def transfer_hist(p,r):
    h=(p-1)//2; L=p*(p+1)//2; H=p*(p-1)//2
    s0=[1];s1=[0]
    for _ in range(r):
        n0=[0]*(len(s0)+1);n1=[0]*(len(s1)+1)
        for j,x in enumerate(s0):
            n0[j]+=L*x;n1[j+1]+=H*x
        for j,x in enumerate(s1):
            n0[j]+=H*x;n1[j+1]+=L*x
        s0,s1=n0,n1
    return [a+b for a,b in zip(s0,s1)]

def formula_hist(p,r):
    L=p*(p+1)//2; H=p*(p-1)//2
    if r==0:return [1]
    a=[1];b=[L,H]
    for _ in range(2,r+1):
        c=[0]*(len(b)+1)
        for i,coef in enumerate(b):
            c[i]+=L*coef;c[i+1]+=L*coef
        for i,coef in enumerate(a):c[i+1]-=p**3*coef
        a,b=b,c
    return b

def full_carry_aggregation(p):
    states=[(0,0,0),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,1)]
    grp=lambda s: s[0]+s[1]-s[2]
    L=p*(p+1)//2;H=p*(p-1)//2
    for s in states:
        counts=[0,0]
        for a in range(p):
            for b in range(p):
                ss=((2*a+s[0])//p,(2*b+s[1])//p,(a+b+s[2])//p)
                assert ss in states, (p,s,a,b,ss)
                counts[grp(ss)]+=1
        assert counts==([L,H] if grp(s)==0 else [H,L]),(p,s,counts)
    return len(states)*p*p

def brute_hist(p,r):
    mod=p**r
    c=Counter(score(m,n,p) for m in range(mod) for n in range(mod))
    return [c[j] for j in range(r+1)]

def main():
    checks=0
    for p in [3,5,7,11,13,17,19]:
        checks+=full_carry_aggregation(p)
        for r in range(0,8):
            a=transfer_hist(p,r);b=formula_hist(p,r)
            assert a==b,(p,r,a,b)
            assert sum(a)==p**(2*r)
            assert a[0]==(p*(p+1)//2)**r
            if r>0: assert a[-1]==p*(p-1)//2*(p*(p+1)//2)**(r-1)
            checks+=len(a)
    for p,maxr in [(3,5),(5,3),(7,2),(11,2)]:
        for r in range(maxr+1):
            got=brute_hist(p,r);want=formula_hist(p,r)
            assert got==want,(p,r,got,want)
            checks+=(p**r)**2
    print('CHECK_OK',checks)

if __name__=='__main__': main()
