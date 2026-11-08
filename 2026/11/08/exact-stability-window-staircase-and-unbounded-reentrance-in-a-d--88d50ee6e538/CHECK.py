#!/usr/bin/env python3
"""Reproducibility checks for the two-frequency delay-stability staircase.

Only finite algebraic and numerical checks are asserted; the all-delay theorem
is established analytically in RESULT.md.
Run: python CHECK.py (requires numpy and sympy).
"""
import math
import numpy as np
import sympy as sp

# Exact rational coefficients from the positive Holling-II parameter family.
r=sp.symbols('r', positive=True)
a,b,d,K,h=map(sp.Rational, ('1','5/4','1','4','1/4'))
x=d/(b-d*h)
y=(1+h*x)*r*(1-x/K)/a
alpha=sp.factor(a*h*x*y/(1+h*x)**2)
beta=sp.factor(r*x/K)
gamma=sp.factor(a*b*x*y/(1+h*x)**3)
assert (x,y,alpha,beta,gamma)==(1,15*r/16,3*r/20,r/4,3*r/5)
assert sp.factor(beta**2-alpha**2)==r**2/25
print('EXACT coefficients', x,y,alpha,beta,gamma)

theta=math.acos(3/5)
def info(rate):
    A=3*rate/20; B=rate/4; G=3*rate/5
    v=math.sqrt(B*B-A*A)
    wplus=(math.sqrt(v*v+4*G)+v)/2
    wminus=(math.sqrt(v*v+4*G)-v)/2
    assert abs(wplus*wminus-G)<3e-14
    assert abs(wplus-wminus-v)<3e-14
    t=(theta/(2*math.pi))*math.sqrt(1+60/rate)
    j=max(0,math.ceil(t)-1)
    Aevents=[(theta+2*math.pi*n)/wplus for n in range(j+2)]
    Bevents=[(2*math.pi-theta+2*math.pi*n)/wminus for n in range(j+2)]
    assert all(Aevents[n]< Bevents[n] for n in range(j+2))
    assert all((Bevents[n]<Aevents[n+1])==(n+1<t) for n in range(j+1))
    return A,B,G,wplus,wminus,t,j,Aevents,Bevents

for rr, expected in [(1,1),(.1,3),(.01,11),(.001,36)]:
    A,B,G,wp,wm,t,j,ae,be=info(rr)
    assert j==expected
    for w, delay in [(wp,ae[0]),(wm,be[0])]:
        lam=1j*w
        F=lam**2-A*lam+B*lam*np.exp(-lam*delay)+G
        Fprime=2*lam-A+B*np.exp(-lam*delay)*(1-lam*delay)
        dlambda=B*lam**2*np.exp(-lam*delay)/Fprime
        predicted=(w**4-G**2)/abs(Fprime)**2
        assert abs(F)<2e-12 and abs(dlambda.real-predicted)<1e-10
    print('rate',rr,'reentries',j,'T',format(t,'.12f'),'firstA',format(ae[0],'.12f'),'firstB',format(be[0],'.12f'))

# Independent argument-principle check: count unstable zeros of F inside
# a rectangle containing all possible zeros with nonnegative real part.
def right_half_plane_roots(rate,delay,mesh=0.002):
    A,B,G,*_=info(rate)
    bound=(A+B+math.sqrt((A+B)**2+4*G))/2
    R=max(3.,bound+1.)
    H=R
    eps=1e-7
    nx=round((R-eps)/mesh)+1
    ny=round(2*H/mesh)+1
    xx=np.linspace(eps,R,nx)
    yy=np.linspace(-H,H,ny)
    contour=np.concatenate((xx-1j*H,R+1j*yy,xx[::-1]+1j*H,eps+1j*yy[::-1]))
    F=contour*contour-A*contour+B*contour*np.exp(-contour*delay)+G
    phase=np.angle(F[1:]/F[:-1]).sum()/(2*np.pi)
    assert abs(phase-round(phase))<2e-3
    return round(phase)

for tau,expected in ((.5,0),(1.2,2),(7.5,2),(7.95,0),(8.1,0),(8.25,2),(15.,2)):
    count=right_half_plane_roots(1,tau)
    assert count==expected,(tau,count,expected)
    print('argument_principle tau',tau,'unstable_roots',count)

print('VERIFY_OK exact_family=1 frequencies=8 crossing_signs=8 staircase_sizes=4 argument_principle_cases=7')
