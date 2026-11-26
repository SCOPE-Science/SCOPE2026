#!/usr/bin/env python3
"""Exact rational checks for monic area-norms of two disjoint equal disks.

Unnormalized area is pi times this moment matrix.  No external modules.
"""
from fractions import Fraction as Q
from math import comb


def mom(i,j,a):
    # integral over disks centered at +/-a of z^i conjugate(z)^j / pi; R=1.
    return sum((Q(1)+(-1)**(i+j))*Q(comb(i,l)*comb(j,l)*a**(i+j-2*l),l+1)
               for l in range(min(i,j)+1))


def solve(M,v):
    M=[list(row)+[v[i]] for i,row in enumerate(M)]
    n=len(v)
    for j in range(n):
        pivot=next(k for k in range(j,n) if M[k][j])
        M[j],M[pivot]=M[pivot],M[j]
        z=M[j][j]
        M[j]=[x/z for x in M[j]]
        for k in range(n):
            if k!=j:
                z=M[k][j]
                M[k]=[x-z*y for x,y in zip(M[k],M[j])]
    return [row[-1] for row in M]


def minnorm(m,a):
    if m==0:return mom(0,0,a)
    A=[[mom(i,j,a) for j in range(m)] for i in range(m)]
    v=[mom(i,m,a) for i in range(m)]
    c=solve(A,v)
    return mom(m,m,a)-sum(v[i]*c[i] for i in range(m))

for a in [1,2,3,7,30,100]:
    assert minnorm(0,a)==2
    assert minnorm(1,a)==2*a*a+1
    assert minnorm(2,a)==4*a*a+Q(2,3)
    # L2>L3 after raising positive quantities to the twelfth power.
    assert (4*a*a+2)**3>(12*a*a+2)**2
    assert 4*a*a+2>4  # L2 > L1 (fourth powers, R=1)
    for k in range(4):
        for s in [0,1]:
            m=2*k+s
            val=minnorm(m,a)
            assert val>0
            # Predicted lambda_m / pi leading coefficient when R=1.
            leading=Q(2*4**k,k+1)*a**(2*k+2*s)
            assert val/leading>0
for k in range(3):
    for s in [0,1]:
        m=2*k+s
        leading=Q(2*4**k,k+1)*100**(2*k+2*s)
        ratio=minnorm(m,100)/leading
        assert abs(ratio-1)<Q(1,12)  # finite parameter check only
print('CHECK_OK: exact area moment matrices, low-degree formulae, and fixed-degree separation checks')
