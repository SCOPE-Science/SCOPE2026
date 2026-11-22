"""Independent symbolic and finite matrix-semigroup checks for the published covariance phase theorem.

Run: python verify.py. Requires numpy, scipy and sympy.
Finite checks are not a proof of the global phase diagram.
"""
import math
import random
import numpy as np
import sympy as sp
from scipy.linalg import expm

# State 0: attracting rate k; state 1: inverted rate -h.
a,b,k,h,d=sp.symbols('a b k h d', positive=True)
q=a+b
P=sp.Matrix([a/q,b/q])
Q=sp.Matrix([[-b,a],[b,-a]])
K=sp.diag(k,-h)
m=(2*K-Q).inv()*(2*d*P)
V=sp.factor(sum(m))
A=Q-K
T=sp.factor(-sp.trace(A)); J=sp.factor(A.det())
F=(a+b)**2-2*(a-b)*(k+h)+4*k*h
checks=0
def exact_check(x):
    global checks
    assert sp.factor(x)==0, sp.factor(x)
    checks+=1
exact_check(V - d*((a+b)**2+2*b*k-2*a*h)/((a+b)*(a*k-b*h-2*k*h)))
exact_check((sp.ones(1,2)*A*m)[0] + d)
exact_check(T-(a+b+k-h))
exact_check(J-(a*k-b*h-k*h))
exact_check((V*(sp.ones(1,2)*A*A*m)[0]-d**2)*q**2*(a*k-b*h-2*k*h)**2 + a*b*d**2*(k+h)**2*F)
L=h*(b+2*k)/k
exact_check(F.subs(a,L)-b*(b+2*k)*(k+h)**2/k**2)
exact_check(F.subs(a,k+h-b) - (4*b*(k+h)-(k-h)**2))
for seed in range(210):
    rng=random.Random(seed*139+17)
    kk=rng.uniform(0.35,5.0); hh=rng.uniform(.1,4.0)
    bb=rng.uniform(.025,2.4); aa=hh*(bb+2*kk)/kk+rng.uniform(.0001,6)
    dd=rng.uniform(.2,3)
    qv=aa+bb; pi=np.array([aa,bb])/qv
    Qt=np.array([[-bb,aa],[bb,-aa]])
    Kv=np.diag([kk,-hh]); M=Qt-Kv
    m2=np.linalg.solve(2*Kv-Qt,2*dd*pi)
    vv=float(m2.sum())
    assert np.all(m2>0) and vv>0
    assert abs(float(-np.ones(2)@M@m2)-dd)<1e-9
    eig=np.sort(-np.linalg.eigvals(M).real); rs,rf=map(float,eig)
    assert 0<rs<rf
    af=(dd-rs*vv)/(rf-rs); a_s=vv-af
    assert a_s>0
    polynomial=(aa+bb)**2-2*(aa-bb)*(kk+hh)+4*kk*hh
    if abs(polynomial)>1e-6:
        assert (af>0)==(polynomial<0)
    for t in (0.,.025,.3,1.,2.5,6.):
        cv=float(np.ones(2)@expm(M*t)@m2)
        pred=a_s*math.exp(-rs*t)+af*math.exp(-rf*t)
        assert abs(cv-pred)<4e-9, (seed,t,cv,pred)
        assert cv>0
        checks+=1
    checks+=6
# Exact example has two positive cancellation roots, both with infinite fourth moment.
kk,hh,bb=2.,1.,1/20
low=hh*(bb+2*kk)/kk
rootrad=math.sqrt((kk-hh)**2-4*bb*(kk+hh))
roots=[kk+hh-bb-rootrad,kk+hh-bb+rootrad]
assert low<roots[0]<roots[1]
for aa in roots:
    Qt=np.array([[-bb,aa],[bb,-aa]]); Kv=np.diag([kk,-hh]);
    pi=np.array([aa,bb])/(aa+bb)
    m2=np.linalg.solve(2*Kv-Qt,2*pi); vv=sum(m2)
    M=Qt-Kv; eig=np.sort(-np.linalg.eigvals(M).real); rho=1/vv
    assert min(abs(eig[0]-rho),abs(eig[1]-rho))<1e-11
    for t in (.1,.7,1.6,4):
        direct=np.ones(2)@expm(M*t)@m2
        assert abs(direct-vv*math.exp(-rho*t))<2e-11
        checks+=1
    exponent=aa/hh-bb/kk
    assert 2<exponent<4
    checks+=1
for aa,expected_sign in [(2.1,-1),(2.5,1),(4.,-1)]:
    Qt=np.array([[-bb,aa],[bb,-aa]]); Kv=np.diag([kk,-hh]); pi=np.array([aa,bb])/(aa+bb)
    m2=np.linalg.solve(2*Kv-Qt,2*pi); v=sum(m2)
    M=Qt-Kv; eig=np.sort(-np.linalg.eigvals(M).real)
    af=(1.-eig[0]*v)/(eig[1]-eig[0]); assert np.sign(af)==expected_sign
    checks+=1
assert checks>2500,checks
print(f'PASS {checks} symbolic identities, matrix semigroup comparisons and boundary checks')
