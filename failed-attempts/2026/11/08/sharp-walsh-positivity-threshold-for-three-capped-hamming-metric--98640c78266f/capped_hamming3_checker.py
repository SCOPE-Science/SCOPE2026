#!/usr/bin/env python3
"""Reproducible checks of the radius-three capped Boolean Hamming result.

Uses only the Python standard library. Finite checks corroborate the exact
Walsh calculation; the all-dimension conclusion follows from the proof.
"""
import math
from math import comb

def eigenvalue(n, s, exponent):
    z = n - 2*s
    return -3.0**exponent + (1.0-3.0**exponent)*z + (2.0**exponent-3.0**exponent)*(z*z-n)/2

def critical(n):
    assert n >= 4
    if n % 2 == 0:
        f = lambda a: (n-2)*3.0**a-(n-4)*2.0**a-4
        level = n//2 + 1
    else:
        f = lambda a: (n-5)*3.0**a-(n-9)*2.0**a-6
        level = (n+3)//2
    lo,hi = 0.,1.
    assert f(lo)<0<f(hi)
    for _ in range(90):
        mid = (lo+hi)/2
        if f(mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2,level

for n in range(4,15):
    b,s0 = critical(n)
    all_modes = [eigenvalue(n,s,b) for s in range(1,n+1)]
    assert abs(all_modes[s0-1]) < 1e-10
    assert all(lam < -1e-8 for s,lam in enumerate(all_modes,1) if s!=s0)
    for factor,expected_sign in ((0.99,-1),(1.01,+1)):
        x=eigenvalue(n,s0,factor*b)
        assert expected_sign*x > 0,(n,factor,x)
    if n<=10:
        # Independent direct sum over the entire binary group.
        # The character has support {0,...,s-1}.
        for s in range(1,n+1):
            mask=(1<<s)-1
            total=0.
            for x in range(1<<n):
                chi=-1 if (x&mask).bit_count()%2 else +1
                total += chi*min(x.bit_count(),3)**b
            assert abs(total-eigenvalue(n,s,b))<1e-8,(n,s,total)
    print(n,format(b,'.12f'),s0,comb(n,s0),2**n-1-comb(n,s0))

L=math.log(3./2.)
a,b=math.log(3.),math.log(2.)
for n in [1000,1001,2000,2001]:
    beta,level=critical(n)
    correction=(2*a-10*b)/L**2 if n%2==0 else (8*a-20*b)/L**2
    approximation=2/(L*n)+correction/n**2
    assert abs(beta-approximation)<600/n**3,(n,beta,approximation)
    print('asymptotic',n,beta,approximation,level)
print('CAPPED_HAMMING3_WALSH_CHECKS_OK')
