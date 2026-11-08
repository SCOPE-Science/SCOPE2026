#!/usr/bin/env python3
"""Standalone all-length arithmetic formula and independent small graph edge checks."""
from collections import defaultdict

def interval(r,p,q):
    s=p+q
    lower=0 if s<r or p==0 or q==0 else (1 if s==r else 2*(s-r))
    upper=2*r if s==2*r else (0 if s==0 else min(2*p,2*q,s-1))
    return lower,upper

def run_options(r,m,u):
    if u==r:
        return int(m==r)
    count=int(m==2*r-u)
    v_low=max(0,3*r-2*u-m)
    count+=max(0,r-u-v_low)
    return count

def profiles(n):
    total=2
    for r in range(1,n//2+1):
        for ones in range(r,n-r+1):
            v1=[run_options(r,ones,u) for u in range(r+1)]
            v0=[run_options(r,n-ones,u) for u in range(r+1)]
            for u0 in range(r+1):
                if not v0[u0]:continue
                for u1 in range(r+1):
                    if not v1[u1]:continue
                    lo,hi=interval(r,u0,u1)
                    total+=v0[u0]*v1[u1]*(hi-lo+1)
    return total

def independently_enumerated_edges(r,p,q):
    values=set()
    mask=(1<<r)-1
    for a in range(1<<r):
        if a.bit_count()!=p:continue
        for b in range(1<<r):
            if b.bit_count()!=q:continue
            values.add((a&b).bit_count()+(a&(((b<<1)|(b>>(r-1)))&mask)).bit_count())
    return values

if __name__=='__main__':
    for r in range(1,9):
        for p in range(r+1):
            for q in range(r+1):
                lo,hi=interval(r,p,q)
                got=independently_enumerated_edges(r,p,q)
                assert got==set(range(lo,hi+1)),(r,p,q,lo,hi,got)
    print('EDGE_INTERVAL_OK r<=8')
    values=[profiles(n) for n in range(1,31)]
    print('COUNTS',values)
    assert values[:17]==[2,3,4,6,8,13,18,30,46,72,110,169,250,369,534,764,1074]
    print('FORMULA_CHECK_OK')
