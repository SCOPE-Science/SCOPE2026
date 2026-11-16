"""Reproduce exact first-band paired spherical Fourier variance calculations.
Run: python checker.py (requires numpy and sympy).
"""
import math
import numpy as np
import sympy as sp

D,t,u,v=sp.symbols('D t u v', positive=True, real=True)
A=D*(1+t)/2
B=(D-1+t+D*t*t)/2
assert sp.simplify((A-B)+(t-1)*(D*t+1)/2)==0
assert sp.simplify(A.subs(t,-1/D)-(D-1)/2)==0
assert sp.simplify(B.subs(t,-1/D)-(D-1)/2)==0
assert sp.simplify(A.subs(t,0)-D/2)==0
assert sp.simplify(B.subs(t,0)-(D-1)/2)==0
assert sp.simplify(B.subs(t,-1)-(D-1))==0
print('Exact symbolic factorization, optimum, and comparison cases: PASS')

def angle_pair(rng,d,t):
    x=rng.normal(size=d);x/=np.linalg.norm(x)
    z=rng.normal(size=d);z-=z.dot(x)*x;z/=np.linalg.norm(z)
    y=t*x+np.sqrt(max(0,1-t*t))*z
    return x,y

def empirical_loss(d,t,draws=12000,seed=314):
    rng=np.random.default_rng(seed)
    # Input coefficient a or b_1, output coefficients [h0,h1,...,hd]
    err=np.zeros((d+1,d+1))
    # collect covariance/mean squared operator of the paired kernel estimator.
    for _ in range(draws):
        x,y=angle_pair(rng,d,t)
        F=np.r_[1.,np.sqrt(d)*x]
        G=np.r_[1.,np.sqrt(d)*y]
        # Kernel expansion vector = feature vector F_x times sampled function f(x).
        L=(np.outer(F,F)+np.outer(G,G))/2-np.eye(d+1)
        err+=L.T@L/draws
    return np.linalg.eigvalsh(err)

checks=0
for d in [3,4,5,8]:
  for tval in [-1,-1/d,0,0.4,1]:
    ev=empirical_loss(d,tval,draws=24000,seed=18+d)
    a=float(A.subs({D:d,t:tval}));b=float(B.subs({D:d,t:tval}))
    expected=np.array(sorted([a]+[b]*d))
    # concentration numerical tolerance
    err=np.max(np.abs(ev-expected))
    assert err<0.32,(d,tval,err,ev,expected)
    checks+=1
print(f'Numerical checks across {checks} dimension-angle families: PASS')
print('Eigenspectra are Monte Carlo corroboration; universality is proved algebraically.')
