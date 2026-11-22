#!/usr/bin/env python3
"""Numerical diagnostics for exact random-acceleration crossing-clock theorem.

Uses independently specified Gaussian conditional velocity and Kac--Rice;
no numerical finite grid is treated as a proof of global uniqueness.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

root2pi=math.sqrt(2*math.pi)
C=math.sqrt(3)/(2*math.pi)
assertions=0

def check(cond,why):
    global assertions
    assertions += 1
    if not cond: raise AssertionError(why)

def g(s):
    z=3/(math.sqrt(2)*s**1.5)
    return C/s*math.exp(-z*z/3)*(math.exp(-z*z)+math.sqrt(math.pi)*z*math.erf(z))

def gaussian_reconstruction(s):
    # k=|u|=1, hence tau=1; direct Rice p_X(u) E(|V| | X=u).
    varx=s**3/3
    mu=3/(2*s)
    sig=math.sqrt(s)/2
    px=math.exp(-1/(2*varx))/math.sqrt(2*math.pi*varx)
    eabs=sig*math.sqrt(2/math.pi)*math.exp(-mu*mu/(2*sig*sig))+mu*math.erf(mu/(math.sqrt(2)*sig))
    return px*eabs

def H(s):
    return quad(g,0,s,epsabs=2e-12,epsrel=2e-12,limit=180)[0]

def Q(s):return s*g(s)-H(s)

for s in np.geomspace(0.17,80,73):
    check(abs(g(s)-gaussian_reconstruction(s))<=2e-12*max(1,g(s)),f'Gaussian Rice {s}')

s0=brentq(lambda s:(g(s+1e-5)-g(s-1e-5)),0.7,2)
a=brentq(Q,1.5,5)
check(1.22<s0<1.23,'single kernel peak location')
check(2.31788<a<2.31789,'tangent root location')
check(abs(Q(a))<1e-11,'tangent equation')
check(abs(g(a)-0.1413932986053531)<2e-11,'optimal flux')

for s in np.geomspace(.23,85,71):
    check((g(s)<=g(s0)+3e-11),'peak envelope')
    check(H(s)/s <= g(a)+2e-11,'global tangent slope')
    check(Q(s)>0 if s<a-1e-5 else (Q(s)<0 if s>a+1e-5 else True),'Q sign')

for mean in [0.25,0.8,1.4,2,2.318,2.5,3.4,6]:
    cap = g(a) if mean<=a else H(mean)/mean
    # enumerate families of positive two-point clocks; no finite enumeration proves global optimality
    for lower in np.geomspace(.1,min(0.99*mean,2),15):
        if lower>=mean: continue
        for upper in [mean*1.02,mean*1.3,mean*2, max(7,2*mean), 25]:
            if upper<=mean:continue
            p=(mean-lower)/(upper-lower)
            val=(p*H(upper)+(1-p)*H(lower))/mean
            check(val<=cap+1.4e-10,f'concave bound at {mean,lower,upper}: {val,cap}')
for mean in [0.4,1,2]:
    for eps in [1e-2,1e-3,1e-4]:
        p=(mean-eps)/(a-eps)
        val=(p*H(a)+(1-p)*H(eps))/mean
        check(val<=g(a)+1e-12,'bursty upper bound')
        if eps<=1e-4:check(abs(val-g(a))<4e-5,'bursty limit')

print(f'checks passed: {assertions}; peak={s0:.12f}; tangency={a:.12f}; flux={g(a):.12f}')
