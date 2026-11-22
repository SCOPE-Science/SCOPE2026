"""Standalone mathematics checks for a uniform-history-reset driven dephasing qubit.

Run: python check.py
Dependencies: sympy, mpmath, numpy, scipy.
Only finite checks and exact algebra are performed; the all-parameter proof is written separately.
"""
import math
import sympy as sp
import numpy as np
import mpmath as mp
from scipy.integrate import solve_ivp

q,k,w=sp.symbols('q k w',positive=True,real=True)
bx=2*k/(q+2*k)
bo=(k*q+w*w)/(q*q+2*k*q+w*w)
assert sp.simplify((bo-bx)-q*(w*w-2*k*k-k*q)/((q+2*k)*(q*q+2*k*q+w*w)))==0
Om=sp.symbols('Om',positive=True,real=True)
lam=-k+sp.I*Om
u=sp.factor(sp.im(lam/(q-lam)))
beta=sp.factor(-sp.re(lam/(q-lam)))
assert sp.simplify(u-q*Om/((q+k)**2+Om**2))==0
assert sp.simplify(beta-(k*q+k*k+Om*Om)/((q+k)**2+Om**2))==0
assert sp.simplify(sp.det(sp.Matrix([[-2*k,-w],[w,0]])-lam*sp.eye(2)).subs(Om**2,w*w-k*k))==0

mp.mp.dps=45

def scalar(lam,q,t):
    z=q-lam
    return mp.exp(-z*t)*mp.hyp1f1(q/z,1,z*t)

def spectral_bloch(k,w,q,b0,t):
    om=math.sqrt(w*w-k*k)
    b0=np.array(b0, dtype=float)
    M=np.array([[-2*k,-w],[w,0]], dtype=complex)
    lp=-k+1j*om; lm=lp.conjugate()
    Pp=(M-lm*np.eye(2))/(lp-lm)
    Pm=np.eye(2)-Pp
    yz=(complex(scalar(lp,q,t))*Pp+complex(scalar(lm,q,t))*Pm)@b0[1:]
    return np.array([float(mp.re(scalar(-2*k,q,t)))*b0[0],yz[0].real,yz[1].real])

def direct_bloch(k,w,q,b0,t):
    B=np.array([[-2*k,0,0],[0,-2*k,-w],[0,w,0]],float)
    b0=np.array(b0,float)
    t0=1e-7
    der=B@b0
    # Taylor at t0. Integral mean = b0 + t0*B*b0/2 + O(t0^2).
    yy=np.r_[b0+t0*der,b0+t0*der/2]
    def rhs(s,y):
        b=y[:3];avg=y[3:]
        return np.r_[(B-q*np.eye(3))@b+q*avg, (b-avg)/s]
    sol=solve_ivp(rhs,(t0,t),yy,rtol=1e-11,atol=1e-12,method='DOP853')
    assert sol.success
    return sol.y[:3,-1]

b0=(0.34,0.43,-0.26)
for k,w in [(1.,2.),(1.,1.2),(0.5,2.0)]:
    for qv in [0.17,0.7,3.0,6.0]:
        for t in [0.3,1.7,7.0]:
            e=spectral_bloch(k,w,qv,b0,t)
            d=direct_bloch(k,w,qv,b0,t)
            assert np.max(np.abs(e-d))<1.3e-7,(k,w,qv,t,e,d)

# Exponent dominance is checked independently of the exact subtraction formula.
for kv,wv in [(1.,1.1),(1.,math.sqrt(2)),(1.,2.),(2.,4.)]:
    critical=(wv*wv-2*kv*kv)/kv
    for qv in [0.01,0.2,1.0,2.0,4.5,12.0]:
        bxv=2*kv/(qv+2*kv)
        bov=(kv*qv+wv*wv)/(qv*qv+2*kv*qv+wv*wv)
        assert (bov>bxv)==(qv<critical) if abs(qv-critical)>1e-10 else True
print('PASS: exact characteristic polynomial; exponent difference; log frequency; 36 independent numerical vector trajectory comparisons (108 components); sign classification')
