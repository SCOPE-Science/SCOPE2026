"""Numerical checks for the fixed-area flat-cylinder distance-moment theorem.
Run: python CHECK.py (requires numpy and scipy). Numerical tests support, not replace, proof.
"""
import math
import numpy as np
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

def quadrature(order=180):
    t,w=leggauss(order)
    z=(t+1)/2
    w=w/2
    u=z[:,None]
    v=z[None,:]
    weights=2*w[:,None]*w[None,:]*(1-v)
    return u,v,weights

U,V,W=quadrature()

def score(q,p):
    # Divide the integrand by its positive maximum to avoid overflow.
    a=q*U*U
    b=V*V/q
    s=a+b
    scale=q+1/q
    return float(np.sum(W*(a-b)/s*(s/scale)**(p/2)))

def root(p):
    return brentq(lambda q: score(q,p), .35, 1.01, xtol=2e-13)

q2=root(2)
q4=root(4)
assert abs(q2-1/math.sqrt(2))<2e-11,(q2,1/math.sqrt(2))
assert abs(q4-3**(-.25))<2e-11,(q4,3**(-.25))
for p in [.5,1,2,4,8,20,50,100]:
    q=root(p)
    assert 0<q<1
    assert score(q-.0001,p)<0<score(q+.0001,p), (p,q)
q100=root(100)
assert abs(100*(1-q100)-2)<.12,(q100,100*(1-q100))

rng=np.random.default_rng(123456)
N=350000
x1=rng.uniform(size=N);x2=rng.uniform(size=N)
y1=rng.uniform(size=N);y2=rng.uniform(size=N)
U_sim=2*np.minimum(np.abs(x1-x2),1-np.abs(x1-x2))
V_sim=np.abs(y1-y2)
assert abs(np.mean(U_sim**2)-1/3)<.003
assert abs(np.mean(V_sim**2)-1/6)<.003
for q in [.5,1/math.sqrt(2),1.,1.6]:
    empirical=np.mean((q*U_sim**2+V_sim**2/q)/2)
    formula=q/6+1/(12*q)
    assert abs(empirical-formula)<.003,(q,empirical,formula)
print('FLAT_CYLINDER_LP_OPTIMIZATION_OK',N)
print('q_p_2',q2,'q_p_4',q4,'q_p_100',q100,'p100_deficit',100*(1-q100))
