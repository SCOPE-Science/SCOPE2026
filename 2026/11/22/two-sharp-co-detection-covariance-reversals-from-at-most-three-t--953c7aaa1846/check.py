#!/usr/bin/env python3
"""Exact rational checks for the finite-template aliquot covariance theorem.

The analytic argument is stated in RESULT.md; the finite assertions below are
supplementary and do not replace the proof for all probability distributions.
"""
from fractions import Fraction as Q
from itertools import product

checks = 0

def check(cond, why):
    global checks
    assert cond, why
    checks += 1

def h_law(pmf, x):
    return sum((p * (1-x)**n for n,p in enumerate(pmf)), Q(0))

def covariance(pmf, x):
    return h_law(pmf,2*x) - h_law(pmf,x)**2

def moms(pmf):
    mu = sum(n*p for n,p in enumerate(pmf))
    v = sum(n*(n-1)*p for n,p in enumerate(pmf))
    w = sum(n*(n-1)*(n-2)*p for n,p in enumerate(pmf))
    return mu,v,w

def reduced(pmf, x):
    mu,v,w=moms(pmf)
    return v-mu**2 + (mu*v-w)*x - (mu*w/Q(3) + v*v/Q(4))*x**2 + v*w*x**3/Q(6) - w*w*x**4/Q(36)

def curvature(pmf,x):
    mu,v,w=moms(pmf)
    return -v*v/Q(2) - 2*mu*w/Q(3) + v*w*x - w*w*x*x/Q(3)

probes=[Q(1,37),Q(1,12),Q(1,9),Q(1,8),Q(1,4),Q(3,8),Q(2,5),Q(1,2)]
for den in range(1,16):
    for n0 in range(den+1):
        for n1 in range(den-n0+1):
            for n2 in range(den-n0-n1+1):
                n3=den-n0-n1-n2
                pmf=tuple(Q(z,den) for z in (n0,n1,n2,n3))
                mu,v,w=moms(pmf)
                check(v>=w>=0, 'factorial moment ordering')
                for x in probes:
                    check(covariance(pmf,x)==x*x*reduced(pmf,x),'PGF polynomial identity')
                    check(curvature(pmf,x)<=0,'concavity inequality')
                    if n2+n3>0:
                        check(curvature(pmf,x)<0,'strict concavity')
                if n3==0:
                    a,b,c,_=pmf
                    for x in probes:
                        check(reduced(pmf,x)==2*c-(b+2*c-c*x)**2,'two-copy factorization')

p3=(Q(1,4),Q(7,16),Q(1,32),Q(9,32))
for x in probes:
    factored=-(9*x-1)*(9*x**3-55*x**2+167*x-57)/1024
    check(reduced(p3,x)==factored,'three-copy witness factorization')
check(reduced(p3,Q(1,12))<0,'low-volume sign')
check(reduced(p3,Q(1,9))==0,'exact first root')
check(reduced(p3,Q(1,8))>0,'middle positive sign')
check(reduced(p3,Q(3,8))>0,'second root lower bracket')
check(reduced(p3,Q(2,5))<0,'second root upper bracket')
check(reduced(p3,Q(1,2))<0,'high-volume negative sign')

p2=(Q(3,10),Q(1,5),Q(1,2),Q(0))
check(reduced(p2,Q(1,5))<0,'two-copy negative witness')
check(reduced(p2,Q(2,5))==0,'exact two-copy transition')
check(reduced(p2,Q(9,20))>0,'two-copy positive witness')

# Independent per-molecule amplification with efficiency e replaces x by e*x.
for e in (Q(1,4),Q(2,3),Q(1)):
    for x in probes:
        check(covariance(p3,e*x)==(e*x)**2*reduced(p3,e*x), 'amplification thinning')

print('PASS',checks,'exact-rational assertions')
