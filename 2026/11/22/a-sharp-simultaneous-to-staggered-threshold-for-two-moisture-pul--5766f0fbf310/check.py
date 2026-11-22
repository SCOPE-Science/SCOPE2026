#!/usr/bin/env python3
"""Supplementary symbolic, quadrature, and numerical tests for an ideal two-pulse reservoir response."""
import math
import random
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq

x,q,a=sp.symbols('x q a', positive=True)
H=sp.log(1+a*a)-sp.log(1+a*a*x*x)+sp.log(1+a*a*(1+x)**2)-sp.log(1+a*a*q*q*(1+1/x)**2)
D=a*a*(3*x**3+6*x**2+4*x+1)+x+1
N=x**3*(a*a*x*(x+1)-1)
den=x*(1+a*a*x*x)*(1+a*a*(1+x)**2)*(x*x+a*a*q*q*(1+x)**2)
assert sp.cancel(sp.diff(H,x)-2*a*a*(q*q*D-N)/den)==0


def closed(A,k,T,t):
    xx=math.exp(-k*t);qq=math.exp(-k*T)
    return (math.log1p(A*A)-math.log1p(A*A*xx*xx)+ math.log1p(A*A*(1+xx)**2)- math.log1p(A*A*qq*qq*(1+1/xx)**2))/(2*k)

def integral(A,k,T,t):
    def f(y):return y*y/(1+y*y)
    before=quad(lambda u:f(A*math.exp(-k*u)),0,t,epsabs=1e-11)[0]
    after=quad(lambda u:f(A*(math.exp(-k*u)+math.exp(-k*(u-t)))),t,T,epsabs=1e-11)[0]
    return before+after

def optimal(A,k,T):
    aa=A*A
    if 2*aa<=1:return 0.0
    qc=math.sqrt((2*aa-1)/(14*aa+2))
    qv=math.exp(-k*T)
    if qv>=qc:return 0.0
    root_min=(math.sqrt(1+4/aa)-1)/2
    def equ(v):
        N=v**3*(aa*v*(v+1)-1)
        D=aa*(3*v**3+6*v*v+4*v+1)+v+1
        return N-qv*qv*D
    if qv*qv<1e-14: return -math.log(root_min)/k  # asymptotic numerical guard
    r=brentq(equ,max(qv,root_min),1,xtol=1e-14)
    return -math.log(r)/k

rng=random.Random(5162024)
checks=0
for i in range(1500):
    A=math.exp(rng.uniform(-2.5,2.5))
    k=math.exp(rng.uniform(-1.2,1.2))
    Hh=rng.uniform(.025,11)
    T=Hh/k
    tau=T*rng.random()
    c=closed(A,k,T,tau)
    d=integral(A,k,T,tau)
    assert abs(c-d)<2e-9*(1+abs(d)),(A,k,T,tau,c,d)
    checks+=1
for i in range(1500):
    A=math.exp(rng.uniform(-1.8,2.2))
    k=math.exp(rng.uniform(-1.2,1.2))
    T=rng.uniform(.2,12)/k
    tau=optimal(A,k,T)
    assert 0<=tau<=T
    cand=minimize_scalar(lambda z:-closed(A,k,T,z),bounds=(0,T),method='bounded',options={'xatol':1e-12})
    assert closed(A,k,T,tau) >= -cand.fun-1e-9
    for z in [0,T,T*rng.random(),T*rng.random()]:
        assert closed(A,k,T,tau)>=closed(A,k,T,z)-3e-9
        checks+=1
# The exact a=1 boundary and an infinite-horizon golden-ratio lag.
a1=1.0
hc=math.log(4)
assert optimal(a1,1,hc-1e-8)==0
assert optimal(a1,1,hc+1e-8)>0
lim=-math.log((math.sqrt(5)-1)/2)
assert abs(optimal(1,1,40)-lim)<1e-7
# Uniform weak-pulse bound: strictly simultaneous for all horizons.
for A in [.01,.2,1/math.sqrt(2)]:
    for h in [.01,1,5,20]: assert optimal(A,1,h)==0
print('PASS',checks,'quadratures and optimization comparisons; symbolic derivative confirmed', 'golden-lag',lim)
