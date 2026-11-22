"""Reproducible finite checks for the parabolic-arc chord diameter theorem.
The analytic proof is in RESULT.md; grids and quadrature do not replace it.
Needs Python 3.10+, scipy and numpy.
"""
from math import sqrt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

PHI = (1 + sqrt(5)) / 2
AC = sqrt((11 + 5 * sqrt(5)) / 8)

def chord(u, v):
    return (v-u) * sqrt(1+(u+v)**2)

def branch(a):
    if a <= sqrt(2):
        return None
    w=(a+sqrt(a*a-2))/2
    x=w-a
    return (w, x, chord(x,a))

def diameter(a):
    b=branch(a)
    return max(2*a, b[2] if b else 0)

def constant(a):
    if a<AC:
        return 1/(4*a*a)
    w, _, _=branch(a)
    A=2*sqrt(1+w*w)
    B=(2*w*w-1)/(2*w*sqrt(1+w*w))
    return 4/(3*a*a*A*sqrt(B))

def numerical_tail(a, eps):
    b=branch(a)
    D=diameter(a)
    if a>=AC:
        w,xstar,_=b
        B=(2*w*w-1)/(2*w*sqrt(1+w*w))
        lo=max(-a,xstar-2*sqrt(eps/B))
        hi=min(a,xstar+2*sqrt(eps/B))
        def strip(u):
            if chord(u,a)<=D-eps:
                return 0.0
            v=brentq(lambda v:chord(u,v)-D+eps,a-0.3,a,xtol=2e-14)
            return a-v
        return 2*quad(strip,lo,hi,epsabs=1e-11,limit=400,points=[xstar])[0]/(2*a*a)
    def strip(u):
        if chord(u,a)<=D-eps:
            return 0.0
        v=brentq(lambda v:chord(u,v)-D+eps,a-0.3,a,xtol=2e-14)
        return a-v
    return quad(strip,-a,-a+1.2*eps,epsabs=1e-11,limit=200)[0]/(2*a*a)

assert abs(AC**2-(11+5*sqrt(5))/8)<1e-14
w,_,ell=branch(AC)
assert abs(w*w-PHI)<1e-12 and abs(ell-2*AC)<1e-12
for a in (1.15,1.4,1.58,1.9,2.5):
    u=np.linspace(-a,a,801)
    best=0
    for v in np.linspace(-a,a,101):
        d=(v-u)*np.sqrt(1+(v+u)**2)
        best=max(best,float(np.max(d[v>u])) if np.any(v>u) else 0)
    assert best<=diameter(a)+1e-9
for a in (1.4,1.9):
    e=0.003
    p=numerical_tail(a,e)
    q=constant(a)*e**(2 if a<AC else 1.5)
    assert abs(p/q-1)<0.012,(a,p,q)
print('PARABOLIC_DIAMETER_GOLDEN_TRANSITION_CHECKS_OK')
