#!/usr/bin/env python3
"""Reproduce analytic identities and independent finite geometry checks."""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

k,t=sp.symbols('k t',positive=True)
u=t*t-t+1
f=(3*k+u)/(t*(3*k*t*t+u))
assert sp.simplify(sp.diff(f,t)+(3*k+1)*(9*k*t*t+u*u)/(t*t*(3*k*t*t+u)**2))==0
lam=(3+k)/(2*(1+3*k))
assert sp.simplify((3-2*lam)/(6*lam-1)-k)==0
s,a,B,C=sp.symbols('s a B C',positive=True)
A0=a**4*(s*(t+1)/2+s**3*(t**3+1)/6)
B0=a**4*(s**3+s/3)
C0=a**4*(s**3*t**3+s*t/3)
assert sp.simplify(A0/(B0+C0)-(3+s*s*u)/(2*(1+3*s*s*u)))==0
assert sp.simplify(B0/C0-f.subs(k,s*s*u))==0
print('Exact symbolic identities: PASS')

def facet_masses(a,b,c,d):
    return {
        'x+':(b**3*(c+d)+b*(c**3+d**3)/3)/2,
        'x-':(a**3*(c+d)+a*(c**3+d**3)/3)/2,
        'y+':(d**3*(a+b)+d*(a**3+b**3)/3)/2,
        'y-':(c**3*(a+b)+c*(a**3+b**3)/3)/2,
    }

def radial(phi,a,b,c,d):
    x,y=math.cos(phi),math.sin(phi)
    opts=[]
    if x>0: opts.append((b/x,'x+'))
    if x<0: opts.append((-a/x,'x-'))
    if y>0: opts.append((d/y,'y+'))
    if y<0: opts.append((-c/y,'y-'))
    return min(opts)

for a,b,c,d in [(1.3,1.3,.6,2.8),(.25,.25,4.,1.),(1.,2.,3.,4.),(2.,1.,1.,1.)]:
    masses=facet_masses(a,b,c,d)
    cuts=sorted(set([0,2*math.pi]+[math.atan2(y,x)%(2*math.pi) for x in (-a,b) for y in (-c,d)]))
    for side in masses:
        def weighted(phi):
            r,j=radial(phi,a,b,c,d)
            return (r**4/2) if j==side else 0
        actual=sum(quad(weighted,cuts[i],cuts[i+1],epsabs=1e-9)[0] for i in range(len(cuts)-1))
        assert math.isclose(actual,masses[side],rel_tol=1e-9,abs_tol=1e-7),(side,actual,masses[side])
print('Independent radial-sector integration: 16/16 PASS')

for lam0,beta0 in [(0.2,0.1),(0.9,10),(1.4,0.25),(0.75,3),(0.17,4)]:
    kap=(3-2*lam0)/(6*lam0-1)
    g=lambda tt:(3*kap+(tt*tt-tt+1))/(tt*(3*kap*tt*tt+tt*tt-tt+1))-beta0
    tt=brentq(g,1e-9,1e9)
    ss=math.sqrt(kap/(tt*tt-tt+1))
    aa=(1/(ss**3+ss/3))**.25
    masses=facet_masses(aa,aa,aa*ss*tt,aa*ss)
    assert math.isclose(masses['x+'],masses['x-'],rel_tol=1e-11)
    assert math.isclose(masses['x+']/(masses['y+']+masses['y-']),lam0,rel_tol=1e-11)
    assert math.isclose(masses['y+']/masses['y-'],beta0,rel_tol=1e-11)
print('Inverse reconstruction examples: 5/5 PASS')
