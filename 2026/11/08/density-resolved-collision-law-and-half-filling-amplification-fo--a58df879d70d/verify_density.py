#!/usr/bin/env python3
"""Exact bivariate Newton recurrence and central-density local-limit sanity checks."""
from math import sqrt,pi,comb

def shift(a,j):return [0]*j+a

def add(*args):
    out=[0]*max(map(len,args))
    for a in args:
        for i,x in enumerate(a):out[i]+=x
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):out[i+j]+=x*y
    return out

def scale(a,c):return [x*c for x in a]

a=[1,1];b=[0,1];c=[0,1,1];d=[0,0,2]
q=[[4],a,add(mul(a,a),scale(b,2))]
q+=[add(mul(a,q[2]),mul(b,q[1]),scale(c,-3))]
q+=[add(mul(a,q[3]),mul(b,q[2]),scale(mul(c,q[1]),-1),scale(d,4))]
lam=.5+sqrt(5/4+sqrt(3))
var=(lam*lam-1)/(4*(2*lam-1)*(lam*lam-lam-1))
for n in range(5,201):
    q.append(add(mul(a,q[n-1]),mul(b,q[n-2]),scale(mul(c,q[n-3]),-1),mul(d,q[n-4])))
for n in [20,40,80,120,160,200]:
    mid=q[n][n//2]+2*((-1)**(n//2)) if n%2==0 else q[n][n//2]
    approx=lam**n/sqrt(2*pi*n*var)
    ratio=mid/approx
    p_cond=mid/comb(n,n//2)**2
    approx_cond=(lam/4)**n*sqrt(pi*n/(8*var))
    print('n',n,'central',mid,'localCLT_ratio',f'{ratio:.9f}','conditional_ratio',f'{p_cond/approx_cond:.9f}')
    assert abs(ratio-1)<.1
print('DENSITY_CHECK_OK')
