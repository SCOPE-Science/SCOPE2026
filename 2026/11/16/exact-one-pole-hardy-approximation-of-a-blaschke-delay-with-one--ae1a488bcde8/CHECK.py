#!/usr/bin/env python3
"""Finite consistency checks for the explicit H2 projection formula; not an infinite proof."""
import cmath
import math
import random

def fun(N, a, r):
    return (1-r*r)*r**(2*N-4)*((r+a)/(1+a*r))**2

def dlog(N, a, r):
    return (N-2)/r-r/(1-r*r)+(1-a*a)/((r+a)*(1+a*r))

def root(N, a):
    lo, hi = 1.e-13, 1-1.e-13
    for _ in range(100):
        mid = (lo+hi)/2
        if dlog(N,a,mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def B(N,a,z):
    return z**(N-1)*(z-a)/(1-a*z)

def captured(N,a,p):
    if abs(p)<1.e-12:
        if N>2: return 0.
        return a*a
    return (1-abs(p)**2)*abs(B(N,a,p)/p)**2

random.seed(1603)
count=0
for N in [2,3,4,6,9,20,80]:
    prev_r=1.
    prev_cap=-1.
    for a in [0.02,0.15,0.4,0.75,0.95]:
        r=root(N,a)
        assert 0<r<1 and abs(dlog(N,a,r))<1.e-5
        cap=fun(N,a,r)
        assert abs(cap-captured(N,a,-r))<1.e-11
        assert r<prev_r and cap>prev_cap
        prev_r=r; prev_cap=cap
        # Exact coefficient projection checked by partial geometric tail.
        coeff=[0j]*(N-1)
        coeff.append(-a)
        for k in range(1,1800): coeff.append((1-a*a)*a**(k-1))
        proj=sum(coeff[j]*((-r)**(j-1)) for j in range(1,len(coeff)))
        assert abs((1-r*r)*abs(proj)**2-cap)<1.e-9
        for _ in range(25):
            rr=random.random()*.99999
            ang=random.random()*2*math.pi
            p=rr*cmath.exp(1j*ang)
            assert captured(N,a,p)<=cap+1.e-10
            count+=1
        count+=5
for N in [200,500,2000,5000]:
    for a in [0.1,0.5,0.9]:
        r=root(N,a)
        approx_r=1-1/(2*N)+((1-a)/(2*(1+a))-5/8)/N**2
        assert abs(r-approx_r) < 5/N**3
        approx_f=1/(math.e*N)*(1+(5*a+1)/(2*(1+a)*N))
        assert abs(fun(N,a,r)/approx_f-1) < 10/N**2
        count+=2
for N in [2,3,5,10,100]:
    rad=math.sqrt((N-1)/N)
    exact=(1/N)*((N-1)/N)**(N-1)
    assert abs(captured(N,0,rad*cmath.exp(1j*.4))-exact)<1.e-12
    count+=1
print(f'PASS: {count} independent finite consistency assertions; infinite proof is analytical.')
