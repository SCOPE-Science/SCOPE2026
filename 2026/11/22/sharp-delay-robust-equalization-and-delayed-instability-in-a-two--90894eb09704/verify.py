#!/usr/bin/env python3
"""Supplementary standard-library checks for a two-agent influence-share theorem."""
from fractions import Fraction as F
from math import log, pi
import cmath

def reduced(v, w, c, beta):
    return (4*v-beta*(1-v*v)*w)/(4+(2*c-beta)*(1-v*v))

def original(v, w, c, beta):
    p1=(1+v)/2; p2=(1-v)/2
    wd1=p1*(1+(c-beta*(1+w)/2)*p2)
    wd2=p2*(1+(c-beta*(1-w)/2)*p1)
    return (wd1-wd2)/(wd1+wd2)

checks=0
for c in [F(1,5),F(3,5),F(9,10),F(1)]:
    for beta in [F(0), c/2, c, c*F(6,5), c*F(19,10)]:
        for v in [F(-3,4),F(-1,3),F(0),F(2,7),F(4,5)]:
            for w in [F(-4,5),F(-1,2),F(0),F(1,4),F(5,6)]:
                assert original(v,w,c,beta)==reduced(v,w,c,beta)
                assert F(-1)<reduced(v,w,c,beta)<F(1)
                checks+=2
for c in [F(1,5),F(3,5),F(1)]:
    for beta in [F(0),c/4,c*F(3,4)]:
        for delay in [0,1,3,6]:
            past=[float(F((i*7+3)%15-7,10)) for i in range(delay+1)]
            rho=max(abs(z) for z in past)
            cc=float(c); bb=float(beta)
            q=(4+bb*(1-rho*rho))/(4+(2*cc-bb)*(1-rho*rho))
            assert q<1
            window=past[:]
            start=max(map(abs,window))
            for step in range(6*(delay+1)):
                nxt=reduced(window[-1],window[0],cc,bb)
                assert abs(nxt)<=q*max(map(abs,window))+1e-12
                window=window[1:]+[nxt]
                checks+=1
            assert max(map(abs,window))<=start*q**6+1e-12
            checks+=1

# Analytic root continuation r=exp(z/delay) near z0.
for c,beta,delay in [(0.9,1.2,40),(0.7,1.0,60),(1.,1.5,100)]:
    a=4/(4+2*c-beta); h=beta/(4+2*c-beta)
    z=complex(log(h/(1-a)),pi)
    for _ in range(40):
        E=cmath.exp(z); r=cmath.exp(z/delay)
        f=E*(r-a)+h
        fp=E*(r-a+r/delay)
        z-=f/fp
    r=cmath.exp(z/delay)
    assert abs(r)>1
    assert abs(r**delay*(r-a)+h)<1e-8
    assert abs((r-1)*delay-complex(log(h/(1-a)),pi))<0.5
    checks+=3
print('PASS',checks,'supplementary checks')
