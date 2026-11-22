"""Exact independent reconstruction of the helm hard-core two-point function.
Run with Python 3 standard library. No external files required.
"""
from fractions import Fraction as F
from math import comb, sqrt

def path(k,t):
    if k < 1: return F(1)
    return sum(comb(k-j+1,j)*t**j for j in range((k+1)//2+1))

def cycle(n,t):
    return sum(F(n,n-j)*comb(n-j,j)*t**j for j in range(n//2+1))

def analytic(n,z):
    t=z/(1+z)
    A=cycle(n,t); W1=t*path(n-3,t); W2=t*t*path(n-6,t)
    p=z/(1+z)
    return p*p*((A+z)*W2-W1*W1)/(A+z)**2

def direct(n,z):
    # Independent rim subsets, then independently sum permitted pendant states.
    norm=F(0); a=F(0); b=F(0)
    for mask in range(1<<n):
        if mask & ((mask<<1 | mask>>(n-1))&((1<<n)-1)):
            continue
        cnt=mask.bit_count()
        weight=z**cnt*(1+z)**(n-cnt)
        norm+=weight
        # Full pendant generating factor for 0 and 3 occupied together.
        if not (mask&1):
            a+=weight*z/(1+z)
        if not (mask&1 or mask&(1<<3)):
            b+=weight*(z/(1+z))**2
    # hub occupied: no rim occupied and leaves arbitrary
    wh=z*(1+z)**n
    norm+=wh; a+=wh*z/(1+z); b+=wh*(z/(1+z))**2
    return b/norm-(a/norm)**2

checks=0
for n in [6,8,10,12,14]:
    for z in [F(1,20),F(1,4),F(1),F(2),F(10),F(100)]:
        if n<=12:
            assert analytic(n,z)==direct(n,z),(n,z)
            checks+=1
    assert analytic(n,F(1,100000))>0
    assert analytic(n,F(10**12))>0
    assert analytic(n,F(1))<0
    checks+=3
assert analytic(6,F(1))<0 and analytic(8,F(1))<0
checks+=2
for n in [16,20,30,40,60]:
    for z in [F(1,100000),F(1),F(10**30)]:
        q=analytic(n,z)
        assert (q>0 if z!=1 else q<0)
        checks+=1
# Check the explicit closed-form ratio against exact partition counts.
for n in [6,8,10,12,20]:
    for z in [F(1,10),F(1),F(3),F(20)]:
        t=z/(1+z)
        a=sqrt(1+4*float(t));u=(a-1)/(a+1)
        A=float(cycle(n,t));rho=float(t*path(n-3,t)/cycle(n,t))
        two=float(t*t*path(n-6,t)/cycle(n,t))
        C=two/(rho*rho)
        rhs=(1-u*u)*(1+u**n)*(1-u**(n-4))/(1+u**(n-1))**2
        assert abs(C-rhs)<1e-8,(n,z,C,rhs)
        checks+=1
print('NEW_HELM_CHECKS_PASSED',checks)
