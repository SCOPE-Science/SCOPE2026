"""Finite exact and numerical checks for the root-doubling-tree size limit.

Run: python verify.py
The theorem's weak convergence and Harris recurrence use analytic arguments;
this script does not certify infinite assertions.
"""
from fractions import Fraction
import math
import random

checks=0
# Exact discrete transition probabilities and the martingale drift.
P={0:Fraction(1)}
for n in range(1,14):
    Q={}
    for b,w in P.items():
        p=Fraction(1,b+1)
        Q[2*b+2]=Q.get(2*b+2,Fraction(0))+w*p
        Q[b+1]=Q.get(b+1,Fraction(0))+w*(1-p)
        assert p*(2*b+2-b)+(1-p)*1==2
        checks+=1
    P=Q
    assert sum(P.values())==1
    assert all(b>=n for b in P)
    assert sum(Fraction(b)*w for b,w in P.items())==2*n
    checks+=3

# Generator polynomial identity, checked as exact rational coefficients.
# L(y^r)=(r+2^r-1)y^(r-1)-r y^r.
for r in range(1,31):
    a= r+2**r-1
    for y in [Fraction(1),Fraction(3,2),Fraction(2),Fraction(5),Fraction(17,4)]:
        drift=r*y**(r-1)*(1-y)
        jump=( (2*y)**r-y**r )/y
        assert drift+jump == a*y**(r-1)-r*y**r
        checks+=1

# Exact one-jump hazard relation, sampled on a wide grid of (k,z).
# Integral_0^log(1+1/k) dt/phi_t(z) = log(1+1/(kz)).
for k in [1,2,3,5,10,31,100,1000]:
    for z in [1,1.1,1.5,2,3.75,10,101]:
        delta=math.log1p(1/k)
        hazard=math.log((math.exp(delta)+z-1)/z)
        p=-math.expm1(-hazard)
        assert math.isclose(p,1/(k*z+1),rel_tol=2e-12,abs_tol=2e-13)
        checks+=1
        for v in [0,delta/4,delta/2,delta]:
            flow=lambda x,s:1+(x-1)*math.exp(-s)
            one=flow(2*flow(z,v),delta-v)
            sur=2*flow(z,delta)
            assert -2e-12<=sur-one<=delta+2e-12
            checks+=1

# Small-set common density support for any compact [1,R] after enough time.
for R in [1,2,3,10,100]:
    T=max(2, math.ceil(math.log(2*R-1))+1)
    assert 1+(2*R-1)*math.exp(-T)<2
    checks+=1

# Exactly simulate the PDMP over fixed time using integrated hazard inversion.
def pdmp(z,T,rr):
    remaining=T
    while remaining>0:
        E=-math.log1p(-rr.random())
        # first-jump time solves log((exp(t)+z-1)/z)=E
        h=math.log1p(z*math.expm1(E))
        if h>=remaining:
            z=1+(z-1)*math.exp(-remaining)
            break
        z=2*(1+(z-1)*math.exp(-h))
        remaining-=h
    return z

rr=random.Random(28011)
samples=[pdmp(2.0,35.0,rr) for _ in range(25000)]
mean=sum(samples)/len(samples)
m2=sum(x*x for x in samples)/len(samples)
# Analytic π moments are E[Y]=2, E[Y²]=5. Loose Monte Carlo diagnostic.
assert abs(mean-2)<0.085, mean
assert abs(m2-5)<0.45, m2
checks+=2

# Event-driven exact simulation of discrete B_n at large n.
def simulate_B(n,rr):
    b=0
    t=0
    while t<n:
        if b==0:
            b=2;t+=1;continue
        # Geometric-ish waiting: P(no root in next x steps)=b/(b+x).
        u=rr.random()
        gap=math.ceil(u*b/(1-u))
        if gap>n-t:
            b+=n-t
            break
        # gap-1 ordinary steps followed by a doubling.
        b+=gap-1
        b=2*(b+1)
        t+=gap
    return b
rr=random.Random(28012)
values=[simulate_B(100000,rr)/100000 for _ in range(22000)]
mean2=sum(values)/len(values)
assert abs(mean2-2)<0.09,mean2
checks+=1
print('PASS finite assertions:',checks)
print('PDMP simulation E[Y], E[Y²]:',round(mean,5),round(m2,5))
print('Discrete B_100000/100000 simulation mean:',round(mean2,5))
print('Limit moments from generator: m1=2, m2=5, var=1')
