"""Reproduce centroidal-chord formulas for a regular tetrahedron.
Only deterministic finite checks; not an infinite proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
V=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)

def direct(u):
    s=V@u
    return 1/max(s)+1/(-min(s))

def sorted_formula(u):
    x,y,z=sorted(map(abs,u),reverse=True)
    a=x+y
    return 2*a/(a*a-z*z)

def cdf(ell):
    if ell<=math.sqrt(2): return 0.
    if ell>=4/math.sqrt(3): return 1.
    def g(phi):
        A=math.cos(phi)+math.sin(phi)
        if ell<=2/A: return 0.
        w=(ell*ell*A**4-4*A*A)/(A*A*(ell*ell+2)+2*A*math.sqrt(A*A*(ell*ell+1)+ell*ell))
        q=min(math.sin(phi),math.sqrt(max(0.,w)))
        return q/math.sqrt(1+q*q)
    return 12/math.pi*quad(g,0,math.pi/4,epsabs=2e-12,epsrel=2e-12,limit=300)[0]

rng=np.random.default_rng(1922005)
U=rng.normal(size=(120000,3));U/=np.linalg.norm(U,axis=1)[:,None]
s=U@V.T
ld=1/s.max(axis=1)+1/(-s.min(axis=1))
ls=np.array([sorted_formula(u) for u in U]); assert np.max(np.abs(ld-ls))<1e-12
print('direct-vs-sorted maximum error:',np.max(np.abs(ld-ls)))
print('simulated range:',ld.min(),ld.max())
for e in [1.50,1.70,1.90,2.00,2.10,2.20,2.28]:
    F=cdf(e); empirical=np.mean(ld<=e)
    print(f'CDF at {e:.2f}: quad {F:.9f}, simulation {empirical:.9f}')
    assert abs(F-empirical)<.006
def upper_survival(ell):
    def lmax(phi):
        t=math.tan(phi)
        return 2*(1+t)*math.sqrt(1+2*t*t)/(1+2*t)
    a=brentq(lambda phi:lmax(phi)-ell,0.5,math.pi/4)
    def integrand(phi):
        A=math.cos(phi)+math.sin(phi)
        qm=math.sin(phi)
        w=(ell*ell*A**4-4*A*A)/(A*A*(ell*ell+2)+2*A*math.sqrt(A*A*(ell*ell+1)+ell*ell))
        q=math.sqrt(max(0,w))
        return qm/math.sqrt(1+qm*qm)-q/math.sqrt(1+q*q)
    return 12/math.pi*quad(integrand,a,math.pi/4,epsabs=1e-14,limit=200)[0]
for eps in [0.001,0.003,0.01,0.03]:
    lo=cdf(math.sqrt(2)+eps)
    hi=upper_survival(4/math.sqrt(3)-eps)
    print(f'epsilon {eps}: lower/epsilon {lo/eps:.8f}, upper/epsilon^2 {hi/eps**2:.8f}; targets 3 and {math.sqrt(3)/(4*math.pi):.8f}')
    assert abs(lo/eps-3)<.25
    assert abs(hi/eps**2-math.sqrt(3)/(4*math.pi))<.25
print('PASS: finite numeric diagnostics')
