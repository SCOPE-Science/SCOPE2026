"""Standalone checks for finite rank-one boundary perturbations of shifts.

Finite tests exercise algebraic identities and sample limits; the infinite
operator and asymptotic assertions are proved separately in RESULT.md.
"""
from fractions import Fraction as Q
from math import cos, pi, sinh, sqrt, exp, acos


def add(a,b):
    return [ (a[i] if i<len(a) else Q(0)) + (b[i] if i<len(b) else Q(0)) for i in range(max(len(a),len(b)))]

def mulx(a): return [Q(0)]+a

def scale(a,v): return [v*x for x in a]

def sub(a,b): return add(a,scale(b,-1))

def u_poly(n):
    if n==0:return [Q(1)]
    u0=[Q(1)];u1=[Q(0),Q(2)]
    for i in range(2,n+1):u0,u1=u1,sub(scale(mulx(u1),Q(2)),u0)
    return u1

def det_poly(n,t):
    # monic determinant of lambda I minus tridiagonal H_{n,t}
    p0=[Q(1)];p1=[-t,Q(1)]
    if n==1:return p1
    for i in range(2,n+1):p0,p1=p1,sub(mulx(p1),scale(p0,Q(1,4)))
    return p1

checks=0
for n in range(1,19):
    for t in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(4,3),Q(n+1,2*n)]:
        rhs=scale(sub(u_poly(n),scale(u_poly(n-1),2*t)),Q(1,2**n))
        assert det_poly(n,t)==rhs,(n,t)
        checks+=1
        # lambda = 1 precisely at finite edge threshold, via U_m(1)=m+1
        p=det_poly(n,t)
        ev=sum(p)
        assert ev == Q(1,2**n)*((n+1)-2*t*n)
        checks+=1

from scipy.linalg import eigh_tridiagonal
import numpy as np
from scipy.optimize import brentq

def top(n,t):
    d=np.zeros(n);d[0]=t
    return float(eigh_tridiagonal(d,np.full(n-1,.5),select='i',select_range=(n-1,n-1))[0][0])

for n in [8,18,39,100]:
    tcrit=(n+1)/(2*n)
    assert abs(top(n,tcrit)-1)<1e-12
    checks+=1
    for t in [0.,.18,.5,.7,1.1]:
        x=top(n,t)
        if t<tcrit:assert x<1
        if t>tcrit:assert x>1
        checks+=1

for alpha in [-1.,0.,.25,.5,.75,1.2]:
    if alpha<.5:
        k=brentq(lambda z:z/np.tan(z)-2*alpha,1.e-8,pi-1.e-8)
        target=-k*k/2
    elif alpha==.5:target=0.
    else:
        k=brentq(lambda z:z/np.tanh(z)-2*alpha,1.e-8,20.)
        target=k*k/2
    for n in [200,500]:
        actual=n*n*(top(n,.5+alpha/n)-1)
        assert abs(actual-target)<.13,(alpha,n,actual,target)
        checks+=1

for t in [.7,.8,1.0]:
    r=2*t
    exact=t+1/(4*t)
    coefficient=(r*r-1)**2/(2*r**3)
    for n in [11,14,17]:
        diff=exact-top(n,t)
        assert diff>0
        assert abs(diff*(r**(2*n))-coefficient)<.012
        checks+=1

print('CHECKS_PASSED',checks)
