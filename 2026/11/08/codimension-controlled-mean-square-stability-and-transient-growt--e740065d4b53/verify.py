"""Independent finite Gaussian-moment checks for the stated CV-ZOD quadratic recursion.
The general-dimensional claim is proved algebraically, not by these finite checks.
"""
import math
import numpy as np
from fractions import Fraction
from itertools import product


def gaussian_monomial(exp):
    out = 1
    for e in exp:
        if e % 2: return 0
        for j in range(1, e, 2): out *= j
    return out

def moment_poly(poly):
    return sum(c*gaussian_monomial(e) for e,c in poly.items())

def poly_mul(a,b):
    out={}
    for e,c in a.items():
        for f,v in b.items():
            k=tuple(x+y for x,y in zip(e,f));out[k]=out.get(k,0)+c*v
    return out

def poly_add(*args):
    out={}
    for a in args:
        for e,c in a.items():out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}

def poly_scale(a,c):return {e:c*v for e,v in a.items()}

def basis(d,i,p=1):return {tuple(p if j==i else 0 for j in range(d)):1}

for d in range(2,7):
    rr={tuple(0 for _ in range(d)):0}
    for i in range(d):rr=poly_add(rr,basis(d,i,2))
    r4=poly_mul(rr,rr)
    for k in range(1,d):
        m=d-k
        v={tuple(0 for _ in range(d)):0}
        for i in range(k):v=poly_add(v,basis(d,i,2))
        w={tuple(0 for _ in range(d)):0}
        for i in range(k,d):w=poly_add(w,basis(d,i,2))
        assert moment_poly(poly_mul(r4,v))==k*(d+2)*(d+4)
        assert moment_poly(poly_mul(r4,w))==m*(d+2)*(d+4)
        q=basis(d,d-1)
        wdotq=q
        wnorm=w
        assert moment_poly(poly_mul(poly_mul(wdotq,wdotq),wnorm))==m+2
        assert moment_poly(poly_mul(poly_mul(wdotq,wdotq),v))==k

rng=np.random.default_rng(20261101)
for d,k in [(2,1),(4,2),(5,4),(8,3)]:
    m=d-k; alpha=0.38; tau=0.04
    x=rng.standard_normal(d)
    u=rng.standard_normal((280000,d))
    p=x[:k];q=x[k:]; w=u[:,k:]; dot=w@q
    grad=np.concatenate([np.broadcast_to(p,(len(u),k)),np.zeros((len(u),m))],axis=1) + dot[:,None]*u + 0.5*tau*np.sum(u*u,axis=1)[:,None]*u
    y=x-alpha*grad
    empirical=np.array([np.mean(np.sum(y[:,:k]**2,axis=1)),np.mean(np.sum(y[:,k:]**2,axis=1))])
    a=sum(p*p);b=sum(q*q);mom=(d+2)*(d+4)
    analytic=np.array([(1-alpha)**2*a+alpha**2*k*b+alpha**2*tau**2*k*mom/4,
                       (1-2*alpha+alpha**2*(m+2))*b+alpha**2*tau**2*m*mom/4])
    assert np.all(np.abs(empirical-analytic)<=0.035*np.maximum(analytic,1e-6)),(d,k,empirical,analytic)
import sympy as sp
eta,k,m=sp.symbols('eta k m', positive=True)
A=(1-eta)**2
rho=1-2*eta+eta**2*(m+2)
B=eta**2*k
assert sp.simplify(rho-A-eta**2*(m+1))==0
assert sp.simplify(B/(rho-A)-k/(m+1))==0
assert sp.simplify(1-2*eta+eta**2*(m+2)).subs(eta,sp.Rational(2,1)/(m+2))==1
for mm in [1,2,3,7]:
    e=sp.Rational(2,mm+2)
    assert (1-2*e+e*e*(mm+2))==1
    assert 1-2*(e-sp.Rational(1,1000))+ (e-sp.Rational(1,1000))**2*(mm+2)<1
    assert 1-2*(e+sp.Rational(1,1000))+ (e+sp.Rational(1,1000))**2*(mm+2)>1
print('CHECKS_OK: exact Gaussian Wick moments in d=2..6, 4 Monte Carlo block recursions, exact stability/partition identities')
