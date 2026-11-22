#!/usr/bin/env python3
"""Reproducible algebraic and independent numerical checks for a magnetic quantum trimer.
Requires sympy and numpy.  Exact symbolic identities establish the resolvent formulas;
the analytic uniqueness/limit arguments are given in RESULT.md.
"""
import math
import numpy as np
import sympy as sp

r,z,x,h=sp.symbols('r z x h', nonzero=True)
I=sp.I
H=sp.Matrix([[0,1,z],[1,0,1],[1/z,1,0]])
K=r*sp.eye(9)
for i in range(3):
    for j in range(3):
        krow=3*i+j
        for k in range(3):
            K[krow,3*k+j] += I*H[i,k]
            K[krow,3*i+k] -= I*H[k,j]
b=sp.zeros(9,1)
b[0]=r
sol=K.inv()*b
D=r**2*(r**2+9)**2-27*(z-1/z)**2
# D = r^2(r^2+9)^2+108 sin^2(Phi) on |z|=1
pred_p0=(r**6+14*r**4+45*r**2-9*(z-1/z)**2)/D
pred_delta=6*I*r*(r**2+3)*(z-1/z)/D # = -12 r (r^2+3)sin(Phi)/D
assert sp.cancel(sol[0]-pred_p0)==0
assert sp.cancel(sol[4]-sol[8]-pred_delta)==0
assert sp.cancel(sol[0]+sol[4]+sol[8]-1)==0
assert sp.cancel((K*sol-b)[0])==0
assert sp.factor(sp.det(K)-r**3*D)==0
F=x**4+11*x**3+27*x**2+(81-108*h)*x-108*h
# derivative of absolute imbalance with respect to r is -36*s*F/D^2
s=sp.symbols('s', positive=True)
f=12*r*(r*r+3)*s/(r*r*(r*r+9)**2+108*s*s)
N=sp.factor(sp.diff(f,r)*(r*r*(r*r+9)**2+108*s*s)**2)
assert sp.simplify(N+36*s*F.subs({x:r*r,h:s*s}))==0
assert sp.factor(F.subs(h,1)-(x+3)**2*(x**2+5*x-12))==0
hoptimal=(x**4+11*x**3+27*x**2+81*x)/(108*(x+1))
assert sp.factor(x*(x+9)**2-108*hoptimal)==8*x*x*(x+9)/(x+1)
# independently verify the matrix equation and closed formula for a 3x3 Hermitian Hamiltonian
count=8
for flux in [-2.4,-1.1,-0.19,0.003,0.7,math.pi/2,2.4,math.pi-.001]:
    for rate in [.002,.015,.07,.3,1,3,12]:
        hn=np.array([[0,1,np.exp(1j*flux)],[1,0,1],[np.exp(-1j*flux),1,0]], complex)
        kn=rate*np.eye(9)+1j*(np.kron(hn,np.eye(3))-np.kron(np.eye(3),hn.T))
        bn=np.zeros(9,complex);bn[0]=rate
        rhon=np.linalg.solve(kn,bn).reshape(3,3)
        sn=math.sin(flux)
        dn=rate**2*(rate**2+9)**2+108*sn**2
        dtarget=-12*rate*(rate**2+3)*sn/dn
        ptarget=(rate**6+14*rate**4+45*rate**2+36*sn**2)/dn
        assert abs((rhon[1,1]-rhon[2,2]).real-dtarget)<2e-10
        assert abs(rhon[0,0].real-ptarget)<2e-10
        assert np.linalg.norm(rhon-rhon.conj().T)<2e-10
        assert abs(np.trace(rhon)-1)<2e-10
        assert np.linalg.eigvalsh(rhon).min()>-1e-10
        count+=5
# independent numerical root/maximum checks
for flux in [.01,.1,.4,.9,math.pi/2]:
    hh=math.sin(flux)**2
    coeff=[1,11,27,81-108*hh,-108*hh]
    roots=np.roots(coeff)
    positives=[w.real for w in roots if abs(w.imag)<1e-8 and w.real>0]
    assert len(positives)==1
    optimal=math.sqrt(positives[0])
    y=lambda rr:abs(-12*rr*(rr*rr+3)*math.sin(flux)/(rr*rr*(rr*rr+9)**2+108*hh))
    assert y(optimal)>y(optimal*.999) and y(optimal)>y(optimal*1.001)
    count+=2
# near-degeneracy scaling: rate/sin(flux) converges to 2/sqrt(3), maximum to 1/(3sqrt(3))
for flux in [1e-3,2e-4,1e-4]:
    ss=math.sin(flux)
    rr=math.sqrt(max(float(w.real) for w in np.roots([1,11,27,81-108*ss**2,-108*ss**2]) if abs(w.imag)<1e-8 and w.real>0))
    qq=12*rr*(rr*rr+3)*ss/(rr*rr*(rr*rr+9)**2+108*ss**2)
    assert abs(rr/ss-2/math.sqrt(3))<1e-5
    assert abs(qq-1/(3*math.sqrt(3)))<1e-6
    count+=2
print('PASS: exact 9x9 resolvent identities, characteristic determinant, optimizer polynomial,')
print('factorization, flux envelope identity,',count,'independent scalar numerical assertions')
