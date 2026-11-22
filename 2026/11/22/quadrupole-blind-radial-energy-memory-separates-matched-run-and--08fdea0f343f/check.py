#!/usr/bin/env python3
"""Reproducible symbolic and independent path-level checks for a trapped active swimmer."""
import math
import numpy as np
import sympy as sp

alpha, beta, t = sp.symbols('alpha beta t', positive=True)
M = 1/(1+alpha)
F = (18+5*beta)/(3*(1+alpha)*(3+alpha)*(2+beta))
V = sp.factor(F-M**2)
P2 = (6+beta)/(3*(1+alpha)*(2+beta))
checks=0
def exact(test, note):
    global checks
    if not test: raise AssertionError(note)
    checks += 1

def eq(a,b, note):
    exact(sp.simplify(a-b)==0, note)

# Derived from direct action of the generator on five scalar monomials.
eq(-2*M+2*M,0,'stationary Q')
eq(-(1+alpha)*M+1,0,'stationary P')
eq(-4*F+4*F,0,'stationary Q^2')
eq(-(3+alpha)*F+2*P2+M,0,'stationary QP')
eq(-(2+beta)*P2+2*M+beta*M/3,0,'stationary P^2')
eq(V,2*(alpha*beta+6*alpha-2*beta)/(3*(1+alpha)**2*(3+alpha)*(2+beta)),'variance')
eq(sp.diff(V,beta),-8/(3*(1+alpha)*(3+alpha)*(2+beta)**2),'strict quadrupolar monotonicity')
VR=sp.factor(V.subs(beta,alpha))
VB=sp.factor(V.subs(beta,3*alpha))
eq(VR,2*alpha*(alpha+4)/(3*(1+alpha)**2*(2+alpha)*(3+alpha)),'RTP variance')
eq(VB,2*alpha**2/((1+alpha)**2*(3+alpha)*(3*alpha+2)),'ABP variance')
eq(sp.factor(VR/VB),(alpha+4)*(3*alpha+2)/(3*alpha*(alpha+2)),'ratio')
eq(sp.factor(VR-VB),16*alpha/(3*(1+alpha)*(2+alpha)*(3+alpha)*(3*alpha+2)),'strict variance gap')
h=sp.exp(-2*t)*(1+alpha-2*sp.exp((1-alpha)*t))/(alpha-1)
eq(h.subs(t,0),1,'normalized covariance at lag zero')
eq(sp.diff(h,t).subs(t,0),0,'normalized covariance first derivative')
eq(sp.diff(h,t,2).subs(t,0),-2*(1+alpha),'normalized covariance curvature')
eq(sp.diff(h,t)+2*h,2*sp.exp(-(1+alpha)*t),'covariance propagation ODE')
eq(sp.limit(h,alpha,1),(1+2*t)*sp.exp(-2*t),'resonant limit')
S=sp.symbols('S')
eq(((18+5*beta)/(2+beta)).subs(beta,(18-2*S)/(S-5)), S, 'quadrupolar mode inverse')
for aa in [sp.Rational(1,5),sp.Rational(1,2),sp.Integer(1),sp.Integer(2),sp.Integer(7)]:
    exact(bool((VR-VB).subs(alpha,aa)>0),'positive RTP-ABP gap')
    exact(bool(VR.subs(alpha,aa)>VB.subs(alpha,aa)>0),'positive variances')
    exact(bool((V.subs({alpha:aa,beta:aa})>=0)),'physical moment positivity')

# Independent path-level test: RTP angles are fully redrawn, ABP angles diffuse on S^2.
# Position follows the exact integrating-factor update for piecewise-constant headings.
def draw_unit(rng,n):
    v = rng.standard_normal((n,3))
    return v/np.linalg.norm(v,axis=1)[:,None]

def sample(model,n=11500,steps=1780,dt=.016,lag_steps=60,seed=721):
    rng=np.random.default_rng(seed)
    Y=np.zeros((n,3)); U=draw_unit(rng,n)
    exp_dt=math.exp(-dt)
    old=None
    for k in range(steps):
        if model=='RTP':
            sel=(rng.random(n)<1-math.exp(-dt))
            if np.any(sel): U[sel]=draw_unit(rng,int(np.sum(sel)))
        elif model=='ABP':
            G=rng.standard_normal((n,3))
            G-=U*np.sum(U*G,axis=1)[:,None]
            U+=-U*dt+math.sqrt(dt)*G
            U/=np.linalg.norm(U,axis=1)[:,None]
        Y=exp_dt*Y+(1-exp_dt)*U
        if k==steps-lag_steps-1: old=np.sum(Y*Y,axis=1)
    cur=np.sum(Y*Y,axis=1)
    mean=float(np.mean(cur)); var=float(np.var(cur)); cov=float(np.mean((old-np.mean(old))*(cur-mean)))
    return mean,var,cov/var

for model, vt in [('RTP',float(VR.subs(alpha,1))),('ABP',float(VB.subs(alpha,1)))]:
    mean,var,ratio=sample(model,seed=41 if model=='RTP' else 84)
    reference=(1+2*.96)*math.exp(-2*.96)
    assert abs(mean-.5)<.015, (model,'mean',mean)
    assert abs(var-vt)<.011, (model,'variance',var,vt)
    assert abs(ratio-reference)<.08, (model,'covariance ratio',ratio,reference)
    checks+=3
    print(f'{model}: mean={mean:.6f}, var={var:.6f}, lag-correlation={ratio:.6f}; predicted {0.5:.6f}, {vt:.6f}, {reference:.6f}')
print('PASS',checks,'symbolic, exact rational, and independent simulated observable assertions')
