#!/usr/bin/env python3
"""Independent binomial homogeneous-block rank check for modular Lefschetz partitions."""
from math import comb

def rank_mod(a,p):
    if not a:return 0
    a=[v[:] for v in a];rows=len(a);cols=len(a[0]);r=0
    for c in range(cols):
        k=next((i for i in range(r,rows) if a[i][c]%p),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];v=pow(a[r][c],-1,p)
        for j in range(c,cols):a[r][j]=a[r][j]*v%p
        for i in range(r+1,rows):
            z=a[i][c]
            if z:
                for j in range(c,cols):a[i][j]=(a[i][j]-z*a[r][j])%p
        r+=1
        if r==rows:break
    return r

def homogeneous_power_rank(p,m,t):
    result=0
    for deg in range(2*m-1-t):
        source=[i for i in range(m) if 0<=deg-i<m]
        target=[i for i in range(m) if 0<=deg+t-i<m]
        mat=[[comb(t,j-i)%p if 0<=j-i<=t else 0 for i in source] for j in target]
        result+=rank_mod(mat,p)
    return result

for p,r in [(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2)]:
    m=(p**r-1)//2
    for t in range(2*m):
        got=homogeneous_power_rank(p,m,t)
        expected=sum(max(0,2*j-1-t) for j in range(1,m+1))
        assert got==expected,(p,r,m,t,got,expected)
    print('PASS truncated-ring power ranks',p,r,m,'powers',2*m)
