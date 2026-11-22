#!/usr/bin/env python3
"""Independent finite arithmetic and asymptotic diagnostics (not infinite proof)."""
from fractions import Fraction as Q
from math import log, floor, isclose

def pooled(i, a, b, q):
    moment=lambda j: q*a**j+(1-q)*b**j
    return i*moment(i)/moment(i-1)

def formula(i, a, b, q):
    th=a/b; c=q/(1-q); z=c*th**(i-1)
    return b+(b-a)*z*(i*(1-th)-1-z)/((th+z)*(1+z))

def cutoff_sign(i, a, b, q):
    th=a/b;c=q/(1-q)
    return i*(1-th)-1-c*th**(i-1)

checks=0
for a,b in [(Q(1),Q(3)),(Q(2),Q(5)),(Q(4),Q(7))]:
    for q in [Q(1,5),Q(1,2),Q(3,4),Q(99,100),Q(999,1000)]:
        for i in range(2,25):
            delta=pooled(i,a,b,q)-pooled(i-1,a,b,q)
            assert delta==formula(i,a,b,q), (a,b,q,i,delta,formula(i,a,b,q))
            assert (delta>b)==(cutoff_sign(i,a,b,q)>0)
            checks+=1
        for group_size in range(3,19):
            feasible=any(pooled(i,a,b,q)-pooled(i-1,a,b,q)>b for i in range(2,group_size))
            assert feasible==(cutoff_sign(group_size-1,a,b,q)>0)
            checks+=1

a,b,q=Q(1),Q(3),Q(99,100)
assert pooled(4,a,b,q)-pooled(3,a,b,q)==Q(31,14)
assert pooled(5,a,b,q)-pooled(4,a,b,q)==Q(53,14)
assert pooled(6,a,b,q)-pooled(5,a,b,q)==Q(191,38)
assert not any(pooled(i,a,b,q)-pooled(i-1,a,b,q)>b for i in range(2,6-1))
assert pooled(5,a,b,q)-pooled(4,a,b,q)>b

# The following checks are asymptotic diagnostics at fixed logarithmic phases.
for theta in (1/3, 2/5):
    a,b=theta,1.0
    h=-log(theta)
    for phase in (0.0,0.25,0.5,0.75):
        for m in (25,45,65):
            zmax=theta**(1-phase)
            target=(b-a)*(1-theta)/h * zmax/((zmax+theta)*(zmax+1))
            vals=[]
            # j=-5...+6 captures the leading maximum for these large m.
            for j in range(-5,7):
                i=m+1+j
                z=theta**(j-phase)
                gap=(b-a)*z*(i*(1-theta)-1-z)/((z+theta)*(z+1))
                vals.append(gap)
            actual=max(vals)/((m+phase)*h)
            assert abs(actual-target)<1.0/m, (theta,phase,m,actual,target)
            checks+=1

print('PASS:',checks,'exact finite/rational and asymptotic diagnostic checks')
