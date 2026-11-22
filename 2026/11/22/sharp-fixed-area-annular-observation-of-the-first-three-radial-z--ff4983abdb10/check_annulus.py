"""Supplementary finite-moment checks for radial-quartic annular concentration.

Requires Python 3, sympy, numpy. Numerical checks are supplementary to
an analytic proof valid for every area fraction and annulus placement.
"""
import math
import random
from fractions import Fraction
import numpy as np
import sympy as sp

u, q, a = sp.symbols('u q a', real=True)
phis = (sp.Integer(1), sp.sqrt(3) * (2*u-1), sp.sqrt(5) * (6*u*u-6*u+1))
G = sp.Matrix(3, 3, lambda i,j: sp.expand(sp.integrate(phis[i]*phis[j], (u,a,a+q))))
assert sp.simplify(G.subs({a:0,q:1})-sp.eye(3))==sp.zeros(3)
center = sp.simplify(G.subs(a,(1-q)/2))
assert sp.simplify(center[0,1])==0
assert sp.simplify(center[1,2])==0
assert sp.simplify(center[1,1]-q**3)==0
T = q*(9*q**4-10*q*q+9)/4
assert sp.simplify(center[0,0]+center[2,2]-T)==0
assert sp.simplify(center[0,0]*center[2,2]-center[0,2]**2-q**6)==0
assert sp.simplify(T-2*q**3-9*q*(1-q*q)**2/4)==0

random.seed(20260517)
checked=0
for qq in [0.01, .03,.1,.2,.33,.5,.67,.8,.91,.97,.99]+[random.uniform(.03,.97) for _ in range(25)]:
    tc=float(T.subs(q,qq))
    lam=(tc-math.sqrt(max(0,tc*tc-4*qq**6)))/2
    # stable root for q << 1
    lam=2*qq**6/(tc+math.sqrt(max(0,tc*tc-4*qq**6)))
    beta=(qq**3-lam)/(12*(qq-lam))
    assert 0<beta<.25
    Gnum=sp.lambdify((q,a), G, modules='numpy')
    C=np.array(Gnum(qq,(1-qq)/2),dtype=float)
    val0=np.linalg.eigvalsh(C)[0]
    assert abs(val0-lam)<2e-12
    for f in [0, .1,.25,.49,.65,.75,.9,1]:
        aa=f*(1-qq)
        eig=np.linalg.eigvalsh(np.array(Gnum(qq,aa),float))[0]
        delta=aa-(1-qq)/2
        D0=1/80-beta/6+beta**2
        ub=lam*D0/(D0+(1/2-2*beta)*delta**2+delta**4)
        assert eig<=ub+3e-11, (qq,aa,eig,ub)
        checked+=1
# Independently integrate the original two-dimensional polar-area Gram,
# without using the symbolic antiderivatives in G.
from numpy.polynomial.legendre import leggauss
nodes, weights=leggauss(16)
Gfast=sp.lambdify((q,a),G,modules='numpy')
polar_checks=0
for qq,aa in [(0.1,0.0),(0.1,0.45),(0.25,0.15),(0.4,0.1),(0.5,0.25),
              (0.6,0.0),(0.75,0.2),(0.85,0.1),(0.95,0.02)]:
    r0,r1=np.sqrt(aa),np.sqrt(aa+qq)
    radii=(r1-r0)*nodes/2+(r1+r0)/2
    wr=(r1-r0)*weights/2
    vals=np.column_stack([np.ones_like(radii),
           np.sqrt(3)*(2*radii**2-1),
           np.sqrt(5)*(6*radii**4-6*radii**2+1)])
    independent=vals.T @ ((2*radii*wr)[:,None]*vals)
    symbolic=np.array(Gfast(qq,aa),float)
    assert np.max(np.abs(independent-symbolic))<2e-12
    polar_checks+=1
print('Symbolic Gram checks passed: 7 identities')
print('Independent original-disk polar quadrature checks passed:',polar_checks)
print('Placement eigenvalue checks passed:',checked)
print('Q=1/2 exact limiting lower eigenvalue:',(113-9*sp.sqrt(145))/256)
print('Q=1/2 decimal:',float((113-9*sp.sqrt(145))/256))
print('All finite numerical tests passed; continuum proof is analytic.')
