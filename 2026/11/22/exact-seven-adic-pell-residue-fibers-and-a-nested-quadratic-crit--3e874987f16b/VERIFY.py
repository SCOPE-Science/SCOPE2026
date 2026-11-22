#!/usr/bin/env python3
"""Independent finite recurrence and modular-root verification of the stated Pell fiber law."""
from collections import Counter

def root_c(k):
    c=5
    for j in range(1,k):
        unit=7**j
        c=next(c+a*unit for a in range(7) if (2*(c+a*unit)**2-1)%(7*unit)==0)
    return c

def square_roots(z,m):
    if m==0: return 1
    mod=7**m
    return sum((u*u-z)%mod==0 for u in range(mod))

def proof_predicted(y,k):
    base={0:1,1:2,2:1,5:1}.get(y%7,0)
    if k==1: return base+int(y==5)
    mod=7**k
    c=root_c(k)
    if (y-c)%49: return base
    modsmall=7**(k-2)
    d=(c*pow(2,-1,mod))%mod
    z=((y-c)//49)*pow(d,-1,modsmall) % modsmall if modsmall>1 else 0
    return base+7*square_roots(z,k-2)

def verify():
    checked=0
    for k in range(1,6):
        m=7**k; T=6*7**(k-1)
        seen=set(); freq=[0]*m; a,b=0,1
        for n in range(T):
            assert (a,b) not in seen
            seen.add((a,b));freq[a]+=1
            a,b=b,(2*b+a)%m
        assert (a,b)==(0,1) and len(seen)==T
        assert (2*root_c(k)**2-1)%m==0
        for y in range(m):
            assert freq[y]==proof_predicted(y,k),(k,y,freq[y],proof_predicted(y,k))
            checked+=1
        assert {y%7 for y,n in enumerate(freq) if n}=={0,1,2,5}
        print('PASS depth',k,'period',T,'image',sum(bool(n) for n in freq),'histogram',dict(Counter(freq)))
    print('PASS:',checked,'complete target-fiber equalities')
if __name__=='__main__': verify()
