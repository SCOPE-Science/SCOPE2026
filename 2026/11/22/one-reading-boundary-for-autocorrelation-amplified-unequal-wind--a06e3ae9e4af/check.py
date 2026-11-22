#!/usr/bin/env python3
"""Exact checks for a stationary two-window covariance calculation."""
from fractions import Fraction as F
from math import erfc,sqrt

def coefficients(m,n):
    if m>n: m,n=n,m
    z=[]
    for k in range(1,m+n):
        if k<m: c=F(m-k,m*m)+F(n-k,n*n)-F(k,m*n)
        elif k<n: c=-F(k,n*n)
        else: c=-F(m+n-k,m*n)
        z.append(c)
    return z

def var(m,n,r):
    cs=coefficients(m,n)
    return 1/m+1/n+2*sum(float(c)*r**k for k,c in enumerate(cs,1))

def deriv(m,n,r):
    return 2*sum(k*float(c)*r**(k-1) for k,c in enumerate(coefficients(m,n),1))

def bisect_root(m,n):
    l,h=0.0,1.0
    assert deriv(m,n,l)>0 and deriv(m,n,h)<0
    for _ in range(120):
        c=(l+h)/2
        if deriv(m,n,c)>0: l=c
        else: h=c
    return (l+h)/2

checks=0
for m in range(1,21):
 for n in range(1,21):
    ws=[F(1,m)]*m+[-F(1,n)]*n
    cs=coefficients(m,n)
    for k,c in enumerate(cs,1):
        direct=sum((ws[i]*ws[i+k] for i in range(m+n-k)),F(0))
        assert c==direct, (m,n,k,c,direct)
        checks+=1
    # The prefix-cut identity is checked independently of the symbolic derivation.
    prefixes=[sum(ws[:k],F(0)) for k in range(1,m+n)]
    deriv1=2*sum((k*c for k,c in enumerate(cs,1)),F(0))
    assert deriv1==-2*sum((v*v for v in prefixes),F(0))<0
    assert sum(ws,F(0))==0
    assert F(1,m)+F(1,n)+2*sum(cs,F(0))==0
    checks+=3
    if min(m,n)==1:
        assert all(c<0 for c in cs)
        assert deriv(m,n,0)<0 and deriv(m,n,1)<0
    else:
        assert cs[0]>0
        signs=[1 if c>0 else -1 for c in cs if c]
        assert signs.count(1)>=1 and signs.count(-1)>=1
        assert sum(a!=b for a,b in zip(signs,signs[1:]))==1
        r=bisect_root(m,n)
        assert 0<r<1 and deriv(m,n,0)>0 and deriv(m,n,1)<0
        assert var(m,n,r)>var(m,n,0) and var(m,n,r)>0
    checks+=6

r=bisect_root(2,10)
assert abs(r-0.638158678162176)<1e-11
peak=var(2,10,r)
assert abs(peak-0.8897419730372291)<1e-11
base=var(2,10,0)
assert abs(base-0.6)<1e-14
p0=erfc(1/sqrt(2*base)); p1=erfc(1/sqrt(2*peak))
assert abs(p0-0.19670560245894686)<1e-11
assert abs(p1-0.28907564989383217)<1e-11
checks+=5
print(f"PASS: {checks} exact/analytic-identity and supplementary numeric assertions")
print(f"(m,n)=(2,10): rho={r:.15f}; variance0={base:.15f}; variance_peak={peak:.15f}; p0={p0:.12f}; p_peak={p1:.12f}")
