#!/usr/bin/env python3
"""Exact finite tests for phase-shifted occupied-bin covariance on a circle."""
from fractions import Fraction as Q
from itertools import product
from math import comb, exp, pi

checks=0

def exact_covariance(m,n,a):
    t=Q(1,m)
    return (m*((1-(1+a)*t)**n + (1-(2-a)*t)**n)
            +m*(m-2)*(1-2*t)**n -m*m*(1-t)**(2*n))

def microcell_covariance(m,n,a):
    b=a.denominator
    atoms=m*b
    labels0=[j//b for j in range(atoms)]
    labels1=[((j-a.numerator)//b)%m for j in range(atoms)]
    s0=s1=s01=0
    for seq in product(range(atoms),repeat=n):
        k0=len({labels0[j] for j in seq})
        k1=len({labels1[j] for j in seq})
        s0+=k0;s1+=k1;s01+=k0*k1
    den=atoms**n
    return Q(s01,den)-Q(s0*s1,den*den)

for m in range(2,6):
    for n in range(0,5):
        for a in (Q(0),Q(1,2),Q(1,3),Q(2,3)):
            expect=exact_covariance(m,n,a)
            got=microcell_covariance(m,n,a)
            assert got==expect,(m,n,a,got,expect)
            checks+=1
            if n>=2 and m>=3:
                assert expect>0
                checks+=1
            if n>=2 and m==2 and a==Q(1,2):
                assert expect==0
                checks+=1
            if n>=2 and a!=Q(1,2):
                assert exact_covariance(m,n,Q(1,2))<expect
                checks+=1

# Exact independence of the two phase grids with two bins, not just covariance.
for n in range(0,7):
    # Each point's two labels are independent fair bits, one of four outcomes.
    joint={}
    mar0={};mar1={}
    for seq in product(range(4),repeat=n):
        b0=tuple(j//2 for j in seq)
        b1=tuple(((j-1)//2)%2 for j in seq)
        k0=len(set(b0));k1=len(set(b1))
        joint[k0,k1]=joint.get((k0,k1),0)+1
        mar0[k0]=mar0.get(k0,0)+1
        mar1[k1]=mar1.get(k1,0)+1
    den=4**n
    for (k0,k1),num in joint.items():
        assert Q(num,den)==Q(mar0[k0],den)*Q(mar1[k1],den)
        checks+=1

# Exact integral of K(phase) and the truncated-gap identity.
def phase_average(m,points):
    breaks=sorted({Q(0),Q(1)} | {(m*x)%1 for x in points})
    avg=Q(0)
    for l,r in zip(breaks,breaks[1:]):
        shift=(l+r)/2
        cnt=len({(m*x-shift)//1 % m for x in points})
        avg+=(r-l)*cnt
    return avg
for m in range(2,7):
    for n in range(1,5):
        points=[Q((3*j+1)%(5*m),5*m) for j in range(n)]
        xx=sorted(points)
        gaps=[xx[i+1]-xx[i] for i in range(len(xx)-1)]+[1+xx[0]-xx[-1]]
        rhs=m-sum((max(Q(0),m*g-1) for g in gaps),Q(0))
        assert phase_average(m,points)==rhs
        checks+=1

# Exact-phase-averaged variance via integration of the covariance formula.
for m in range(2,9):
 for n in range(0,9):
    t=Q(1,m)
    int_formula=(Q(2*m*m,n+1)*((1-t)**(n+1)-(1-2*t)**(n+1))
        +m*(m-2)*(1-2*t)**n -m*m*(1-t)**(2*n))
    # Expand with the binomial theorem and integrate each monomial exactly.
    a=1-2*t
    integral=(sum(Q(comb(n,k),k+1)*a**(n-k)*t**k for k in range(n+1))
            +sum(Q(comb(n,k),k+1)*a**(n-k)*t**k for k in range(n+1)))
    simple=m*integral +m*(m-2)*a**n-m*m*(1-t)**(2*n)
    assert simple==int_formula
    checks+=1

# Limiting covariance and its spectral coefficients are strictly positive.
for c in (0.1,0.5,1,2,5):
    f=lambda d: exp(-c*(1+d))+exp(-c*(2-d))-(2+c)*exp(-2*c)
    assert f(0)>f(.25)>f(.5)>0
    assert abs(f(.1)-f(.9))<1e-12
    v=2*exp(-c)*(1-exp(-c))/c-(2+c)*exp(-2*c)
    assert f(.5)<v<f(0)
    for k in range(1,11):
        assert 2*c*exp(-c)*(1-exp(-c))/(c*c+4*pi*pi*k*k)>0
        checks+=1
    checks+=3
print('PASS exact and analytic checks:',checks)
