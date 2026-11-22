#!/usr/bin/env python3
"""Independent finite checks for the horizontal Pascal-quotient theorem.

Pure-Python, standard library only. Complete finite enumeration is a check,
not a proof of the all-depth statement.
"""
from math import comb

def lucas(n,k,p,digits):
    z=1
    while n or k:
        a,b=n%p,k%p
        if b>a:return 0
        z=z*digits[a][b]%p
        n//=p;k//=p
    return z

def predicted(p,r):
    q=p*(p+1)//2
    mult=sum(q**j for j in range(r))
    return {u:((p-1) if u==p-1 else (p-1)//2)*mult for u in range(1,p)}

def exhaustive(p,r):
    digits=[[comb(n,k)%p for k in range(n+1)] for n in range(p)]
    count={u:0 for u in range(1,p)}
    for n in range(p**r):
        previous=lucas(n,0,p,digits)
        for k in range(n):
            upcoming=lucas(n,k+1,p,digits)
            if previous and upcoming:
                u=previous*pow(upcoming,-1,p)%p
                count[u]+=1
            previous=upcoming
    return count

def chi(x,p):
    v=pow(x%p,(p-1)//2,p)
    return 0 if v==0 else (1 if v==1 else -1)

if __name__=='__main__':
    checks=0
    for p,max_r in [(2,8),(3,5),(5,4),(7,3),(11,3),(13,2)]:
        for r in range(1,max_r+1):
            seen=exhaustive(p,r); target=predicted(p,r)
            assert seen==target,(p,r,seen,target)
            total=sum(seen.values()); signed=sum(chi(u,p)*ct for u,ct in seen.items())
            if p>2:
                assert signed*p == chi(-1,p)*total
            checks+=p
            print(f'p={p}, r={r}, edges={total}, histogram={seen}')
    # Direct integer-binomial versus Lucas checks at each tested prime.
    for p in [3,5,7,11,13]:
        d=[[comb(n,k)%p for k in range(n+1)] for n in range(p)]
        for n in range(min(180,p**3)):
            for k in range(n+1):
                assert lucas(n,k,p,d) == comb(n,k)%p
                checks+=1
    print('CHECK_OK',checks)
