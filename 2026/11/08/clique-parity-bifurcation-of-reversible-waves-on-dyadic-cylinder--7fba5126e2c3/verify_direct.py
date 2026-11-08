#!/usr/bin/env python3
"""Independent bitwise orbit checks for periodic clique cylinders."""
import random
from collections import Counter

def neighbours(r,m):
    n=1<<r
    out=[]
    for x in range(n):
        for j in range(m):
            s=set()
            for xp in ((x-1)%n,(x+1)%n):s.add(xp*m+j)
            for jp in range(m):
                if jp!=j:s.add(x*m+jp)
            out.append(sum(1<<i for i in s))
    return out

def advance(state,N,nb):
    mask=(1<<N)-1
    u=state&mask; v=(state>>N)&mask
    w=v
    for i,row in enumerate(nb):
        if (u&row).bit_count()&1:w^=1<<i
    return (u<<N)|w

def least_period(st,N,nb,limit):
    a=st
    for t in range(1,limit+1):
        a=advance(a,N,nb)
        if a==st:return t
    raise AssertionError(('order not attained',st,N,limit))

def check():
    # A complete small boundary census verifies orbit multiplicities directly.
    r,m=2,2; nb=neighbours(r,m); N=len(nb); out=Counter()
    for st in range(1<<(2*N)):
        out[least_period(st,N,nb,6)]+=1
    assert dict(out)=={1:1,3:255,6:65280},out
    print('complete_boundary_census vertices=8 states=65536 periods='+str(sorted(out.items())))
    rng=random.Random(20261104)
    for r,m,k in ((3,3,20000),(3,4,20000),(4,3,10000),(4,4,10000)):
        nb=neighbours(r,m); N=len(nb); period=3*(1<<r) if m%2 else 3*(1<<(r-1))
        allowed={1}
        if m%2:
            allowed.update(1<<j for j in range(1,r+1))
            allowed.update(3*(1<<j) for j in range(r+1))
        else:allowed.update(3*(1<<j) for j in range(r))
        vals=Counter()
        for i in range(k):
            st=rng.getrandbits(2*N)
            t=least_period(st,N,nb,period)
            assert t in allowed,(r,m,t)
            vals[t]+=1
        print('in_scope_sample r=%d m=%d states=%d order=%d observed=%s'%(r,m,k,period,str(sorted(vals.items()))))
    print('SUCCESS direct neighbor updates and temporal return tests')

if __name__=='__main__': check()
