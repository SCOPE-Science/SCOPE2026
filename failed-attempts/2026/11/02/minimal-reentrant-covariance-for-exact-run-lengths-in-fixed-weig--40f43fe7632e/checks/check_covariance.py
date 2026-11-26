#!/usr/bin/env python3
"""Exact checks for the covariance of distinct exact run-length counts in fixed-weight binary words."""
from fractions import Fraction
from math import comb
from itertools import combinations

assertions=0

def ck(cond):
    global assertions
    assert cond
    assertions+=1

def fall(v,j):
    if j<0 or j>v:
        return 0
    z=1
    for i in range(j): z*=v-i
    return z

def exact(a,b,r,s):
    """Closed factorial-moment formula for r!=s, positive run lengths."""
    n=a+b
    m=b+1
    p=lambda k: Fraction(b*fall(a,k),fall(n,k+1))
    p12=Fraction(b*(b-1)*fall(a,r+s),fall(n,r+s+2)) if n>=r+s+2 else Fraction(0)
    return m*(m-1)*p12-m*m*p(r)*p(s)

def enum(a,b):
    n=a+b
    counts={}
    for ones in combinations(range(n),a):
        bits=[0]*n
        for i in ones:bits[i]=1
        gaps=[];cur=0
        for v in bits:
            if v:cur+=1
            else:gaps.append(cur);cur=0
        gaps.append(cur)
        assert len(gaps)==b+1
        for r in range(1,a+1):
            for s in range(r+1,a+1):
                old=counts.setdefault((r,s),[0,0,0])
                x=gaps.count(r);y=gaps.count(s)
                old[0]+=x;old[1]+=y;old[2]+=x*y
    c=comb(n,a)
    for (r,s),(sx,sy,sxy) in counts.items():
        ck(Fraction(sxy,c)-Fraction(sx*sy,c*c)==exact(a,b,r,s))

for a in range(2,8):
    for b in range(2,7):
        enum(a,b)

# Positivity of the formula is controlled by the following integer polynomial when r=1, s=9.
def F(a,b):
    n=a+b
    return (b-1)*(a-9)*n*(n-1)-(b+1)*a*(n-10)*(n-11)

for t in range(10,141):
    ck(F(t,t)==-4*t*(t*t+3*t+32))
    ck(F(2*t,t)==t*(t+13)*(3*t-19))
    ck(F(4*t,t)==-5*t*(5*t*t-54*t+97))
    ck(exact(t,t,1,9)<0)
    ck(exact(2*t,t,1,9)>0)
    ck(exact(4*t,t,1,9)<0)

# General fixed-r,s covariance asymptotic, numerically but exactly check finite sign away from boundaries.
for r in range(1,5):
    for s in range(r+1,13):
        for k in (1,2,3,4,6,10):
            if k*250>=r+s:
                q=2*k*k+(1-r-s)*k+r*s
                if q:
                    ck((exact(k*250,250,r,s)<0)==(q>0))

print('PASS assertions:',assertions)
