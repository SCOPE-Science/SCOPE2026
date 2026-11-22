"""Reproducibility checks for Poisson interrogations of a chiral triangle.

Run with Python 3, NumPy, SciPy, and SymPy.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import expm

r=sp.symbols('r',positive=True,real=True)
rt=sp.sqrt(3)
H=sp.Matrix([[0,-sp.I,-1],[sp.I,0,1],[-1,1,0]])
assert H==H.conjugate().T
assert H**3==3*H
assert H[2,0]==-1 and (H**2)[2,0]==sp.I
x=sp.symbols('x',real=True)
U=sp.eye(3)-sp.I*sp.sin(rt*x)/rt*H+(sp.cos(rt*x)-1)/3*H**2
amp=sp.simplify(U[2,0])
assert sp.simplify(amp-sp.I*(sp.sin(rt*x)/rt+(sp.cos(rt*x)-1)/3))==0
amp2=sp.expand_trig(sp.expand(amp*sp.conjugate(amp)))
# A sine/cosine Fourier form permits an elementary Laplace transform.
prob=sp.expand_trig(sp.expand(amp*sp.conjugate(amp)))
expected=2*(r*r-3*r+6)/((r*r+3)*(r*r+12))
Lap=lambda k,w: r*r/(r*r+w*w) if k=='cos' else r*w/(r*r+w*w)
# Laplace identities for sin^2, cos^2, sin cos and linear terms.
p_expr=sp.expand((sp.sin(rt*x)/rt+(sp.cos(rt*x)-1)/3)**2)
const=(sp.Rational(1,6)+sp.Rational(1,9)+sp.Rational(1,18))
cos1=-sp.Rational(2,9)
cos2=-sp.Rational(1,6)+sp.Rational(1,18)
sin1=-2*rt/sp.Integer(9)
sin2=rt/sp.Integer(9)
p_from_trig=const+cos1*Lap('cos',rt)+cos2*Lap('cos',2*rt)+sin1*Lap('sin',rt)+sin2*Lap('sin',2*rt)
assert sp.simplify(p_from_trig-expected)==0,sp.simplify(p_from_trig-expected)
q=sp.factor(r*expected)
s=3+2*rt
c=2/rt-1
assert sp.simplify(c-q-c*(r*r-s*r+6)**2/((r*r+3)*(r*r+12)))==0
rminus=(s-sp.sqrt(s*s-24))/2
rplus=(s+sp.sqrt(s*s-24))/2
assert sp.simplify(rminus*rplus-6)==0
assert sp.simplify(rminus+rplus-s)==0
assert sp.simplify(q.subs(r,rminus)-c)==0
assert sp.simplify(q.subs(r,rplus)-c)==0
q_rev=2*r*(r*r+3*r+6)/((r*r+3)*(r*r+12))
rev_d=-2*(r*r-6)*(r**4+6*r**3+9*r*r+36*r+36)/((r*r+3)**2*(r*r+12)**2)
assert sp.simplify(sp.diff(q_rev,r)-rev_d)==0
assert sp.simplify(q_rev.subs(r,sp.sqrt(6)) - (6+4*sp.sqrt(6))/27)==0
assert sp.simplify(q_rev.subs(r,sp.sqrt(6)) - (sp.sqrt(6)*(sp.sqrt(6)+4))/27)==0

Hnp=np.array(H,dtype=complex)
assert np.allclose(Hnp,Hnp.conj().T)
eigvals, eigvecs=np.linalg.eigh(Hnp)
assert np.allclose(sorted(eigvals),[-math.sqrt(3),0,math.sqrt(3)],atol=1e-12)
checks=0
for sign in (1,-1):
    matrix=Hnp if sign==1 else Hnp.conj()
    for rr in (0.27,0.63,1.123460657,1.91,3.7,5.340640958,9.35):
        pred=float((expected if sign==1 else q_rev/r).subs(r,rr))
        # Directly integrate the probability computed from a full 3x3 unitary matrix.
        def integrand(t):
            psi=expm(-1j*matrix*t)[:,0]
            return rr*math.exp(-rr*t)*abs(psi[2])**2
        estimate,error=quad(integrand,0,100/rr,epsabs=1e-10,epsrel=1e-10,limit=700)
        assert abs(estimate-pred)<max(1e-8,20*error),(rr,sign,estimate,pred,error)
        checks+=1
for rr in np.geomspace(0.04,50,150):
    v=float(q.subs(r,float(rr)))
    w=float(q_rev.subs(r,float(rr)))
    assert v<=float(c)+1e-11 and w<=float(q_rev.subs(r,sp.sqrt(6)))+1e-11
    assert v>0 and w>0
    checks+=4
print(f'PASS: exact symbolic identities and {checks} direct numerical assertions;')
print('two rates',float(rminus),float(rplus),'minimum mean',float(1/c))
print('reverse optimum',float(sp.sqrt(6)),'reverse minimum mean',float(1/q_rev.subs(r,sp.sqrt(6))))
