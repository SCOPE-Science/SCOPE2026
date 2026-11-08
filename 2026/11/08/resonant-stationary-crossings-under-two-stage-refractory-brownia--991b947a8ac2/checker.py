#!/usr/bin/env python3
"""Symbolic and numerical checks for the two-stage refractory Brownian resetting calculation.
Run: python checker.py (requires sympy, scipy, numpy)."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def normalized_components(x):
    assert 0 < x < 4
    a=(x+2)/2
    w=math.sqrt(x*(4-x))/2
    vstar=1/(x*(1+2*x))
    c=-(1-x)**2/x
    b=-vstar-c
    d=(1+x*c+a*b)/w
    return a,w,vstar,c,b,d

def explicit_m(t,r,q,D):
    x=r/q
    a,w,vstar,c,b,d=normalized_components(x)
    u=q*t
    return (2*D/q)*(vstar+c*math.exp(-x*u)+math.exp(-a*u)*(b*math.cos(w*u)+d*math.sin(w*u)))

def independent_m(t,r,q,D):
    def derivative(_,y):
        pa,p1,p2,m=y
        return [-r*pa+q*p2,r*pa-q*p1,q*p1-q*p2,2*D*pa-r*m]
    sol=solve_ivp(derivative,(0,t),[1.,0.,0.,0.],rtol=1e-12,atol=1e-13)
    assert sol.success
    return sol.y[3,-1]

def zeros_near_one(x):
    a,w,vstar,c,b,d=normalized_components(x)
    amp=math.hypot(b,d)
    delta=a-x
    if not (0<delta and c<0): raise ValueError(x)
    cap=math.log(amp/(-c))/delta
    # Root sign function with the common e^{-a t} factor divided out.
    def f(u): return c*math.exp(delta*u)+b*math.cos(w*u)+d*math.sin(w*u)
    up=cap+3*math.pi/w
    mesh=np.linspace(0,up,int(math.ceil(up*700))+1)
    vals=[f(u) for u in mesh]
    count=0
    for i in range(len(mesh)-1):
        if vals[i]*vals[i+1] < 0:
            brentq(f,mesh[i],mesh[i+1],xtol=1e-12)
            count+=1
    return count,cap

def main():
    s,r,q,D=sp.symbols('s r q D',positive=True)
    M=2*D*(s+q)**2/(s*(s+r)*((s+q)**2+r*(s+2*q)))
    assert sp.simplify(sp.limit(s*M,s,0)-2*D*q/(r*(q+2*r)))==0
    assert sp.simplify(sp.limit((s+r)*M,s,-r)+2*D*(q-r)**2/(r*q*q))==0
    y=sp.symbols('y',positive=True)
    H=(s+q)**2+r*(s+2*q)
    assert sp.factor(sp.discriminant(H,s)-r*(r-4*q))==0
    assert sp.simplify(H.subs(s,-r)-q**2)==0
    assert sp.simplify(H.subs(s,-q)-r*q)==0
    # Directly reconstruct the Laplace formula from the three-stage resolvent.
    z=sp.Matrix([[s+r,0,-q],[-r,s+q,0],[0,-q,s+q]])
    pa=sp.simplify(z.inv()[0,0])
    assert sp.simplify(pa-(s+q)**2/(s*H))==0
    assert sp.simplify(M-2*D*pa/(s+r))==0
    print('Seven symbolic/structural checks passed.')
    cases=[(0.4,1.,1.3),(1.,1.,2.),(1.7,1.,.7),(2.,1.,1.),(2.5,1.,1.),(3.9,1.,.4),(.99,1.,1.),(1.01,1.,1.)]
    n=0
    for r0,q0,d0 in cases:
        for t0 in [.05,.4,1.1,3.,6.,10.]:
            m1=explicit_m(t0,r0,q0,d0)
            m2=independent_m(t0,r0,q0,d0)
            assert abs(m1-m2) < 2e-10*(1+abs(m2)),(r0,q0,d0,t0,m1,m2)
            n+=1
    print(f'{n} separately integrated initial-value ODE comparisons passed.')
    x=2.; a,w,vs,c,b,d=normalized_components(x)
    assert np.allclose([a,w,vs,c,b,d],[2,1,.1,-.5,.4,.8])
    x=1.; a,w,vs,c,b,d=normalized_components(x)
    assert np.allclose([a,w,vs,c,b,d],[1.5,math.sqrt(3)/2,1/3,0,-1/3,1/math.sqrt(3)])
    print('Both resonance and equal-decay boundary coefficients passed.')
    for eps in [.05,.01,.002,.0002, .00001]:
        for side in [-1,1]:
            x=1+side*eps
            n,cutoff=zeros_near_one(x)
            target=2*math.sqrt(3)/math.pi*math.log(1/eps)
            print(f'x={x:.7f} crossings={n} leading={target:.2f} cutoff={cutoff:.3f}')
            assert abs(n-target)<6
    print('All zero-count consistency checks passed.')
if __name__=='__main__': main()
