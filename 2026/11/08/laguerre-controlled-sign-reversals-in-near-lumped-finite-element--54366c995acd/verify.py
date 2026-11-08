#!/usr/bin/env python3
"""Supplementary numerical and exact-algebra consistency checks for the finite-element semigroup formulas.
Run with: python verify.py. Finite checks supplement the analytic proof and do not certify it.
"""
import math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.special import roots_genlaguerre

checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

z, x = sp.symbols('z x')
for degree in range(1, 9):
    actual = sp.assoc_laguerre(degree, -1, z)
    identity = -z * sp.assoc_laguerre(degree-1, 1, z) / degree
    require(sp.expand(actual-identity) == 0, ('Laguerre identity', degree))
    require(sp.expand(actual).coeff(z, degree) == (-1)**degree/sp.factorial(degree), ('top coefficient', degree))
    if degree >= 2:
        roots, weights = roots_genlaguerre(degree-1, 1)
        require(len(roots) == degree-1 and np.all(roots > 0), ('positive roots', degree))
        require(np.all(np.diff(roots) > 0), ('simple roots', degree))

for n in range(3, 10):
    C = 2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
    for p in [0.08,0.25,0.6,1.0]:
        B = 6*np.eye(n)-p*C
        G = -6*np.linalg.solve(B,C)
        require(np.allclose(B, B.T), 'symmetric mass')
        require(G[0,2] < 0, ('generator distance-two negativity', n, p))
        for tau in [0.002,0.05,0.2,0.9]:
            A = expm(tau*G)
            require(np.allclose(A,A.T,atol=2e-13), ('symmetry',n,p,tau))
            require(np.all(np.isfinite(A)), 'finite exponential')

for n in range(3, 8):
    mp.mp.dps = 80
    degree = n-1
    roots = list(roots_genlaguerre(degree-1, 1)[0])
    root_edges = [0.] + roots + [roots[-1]+3.]
    # All sign intervals for the far-end entry match the Laguerre leading term.
    for p0 in [0.01,0.002]:
        p=mp.mpf(str(p0))
        for a,b in zip(root_edges[:-1], root_edges[1:]):
            zz=mp.mpf(str((a+b)/2))
            tau=p*zz/6
            terms=[]
            for k in range(1,n+1):
                angle=mp.pi*k/(n+1)
                lam=2-2*mp.cos(angle)
                mu=lam/(1-p*lam/6)
                weight=mp.mpf(2)/(n+1)*(-1)**(k+1)*mp.sin(angle)**2
                terms.append(weight*mp.exp(-mu*tau))
            val=mp.fsum(terms)
            leading=(-1)**degree*mp.mpf(str(sp.N(sp.assoc_laguerre(degree,-1,z).subs(z,float(zz)),45)))
            require(mp.sign(val)==mp.sign(leading), ('boundary-layer sign', n,p0,zz))
            scaled=val/(p/6)**degree
            require(abs(scaled-leading)<mp.mpf('0.50')*(1+abs(leading)), ('scaled asymptotic',n,p0,zz,str(scaled),str(leading)))

# Exact three-node spectral formula: positivity changes exactly once for p>0.
for p in [0.02,0.1,0.4,0.8,1.0]:
    d=6-2*p
    s1=6*(2-math.sqrt(2))/(d+math.sqrt(2)*p)
    s2=12/d
    s3=6*(2+math.sqrt(2))/(d-math.sqrt(2)*p)
    require(s1<s2<s3, ('ordered eigenvalues',p))
    require(s1+s3>2*s2, ('nonconvex eigenvalues',p))
    alpha=s2-s1;beta=s3-s2
    fun=lambda tau: math.expm1(alpha*tau)+math.expm1(-beta*tau)
    root=brentq(fun,1e-9,3)
    require(fun(root/2)<0 and fun(2*root)>0, ('unique sign crossing check',p))
    C=2*np.eye(3)-np.eye(3,k=1)-np.eye(3,k=-1)
    G=-6*np.linalg.solve(6*np.eye(3)-p*C,C)
    for tau in [0.01,root/2,root,root*1.2,1.0]:
        predicted=(math.exp(-s1*tau)+math.exp(-s3*tau)-2*math.exp(-s2*tau))/4
        actual=expm(tau*G)[0,2]
        require(abs(actual-predicted)<3e-13, ('spectral entry',p,tau))
    if p==1:
        require(abs(root-0.2128117769214)<1e-10, 'consistent mass root')

print(f'PASS {checks} finite consistency assertions; analytic proofs remain separate.')
