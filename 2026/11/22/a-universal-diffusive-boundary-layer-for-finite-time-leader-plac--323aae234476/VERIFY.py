"""Exact-rational interval certificate and independent finite matrix checks.

Run: python VERIFY.py
Requires Python standard library, numpy, scipy for optional matrix comparison.
"""
from fractions import Fraction as Q
from math import exp, cos, pi, sqrt


def expneg_bounds(z):
    """Rational enclosure of exp(-z) for 0 <= z <= 25."""
    assert 0 <= z <= 25
    n = 100
    term = Q(1)
    s = term
    for j in range(1,n+1):
        term = term*z/j
        s += term
    first_omitted = term*z/(n+1)
    upper_tail = first_omitted/(1-z/Q(n+2))
    return Q(1)/(s+upper_tail), Q(1)/s


def imul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)


def iadd(a,b): return (a[0]+b[0],a[1]+b[1])


def derivative_bounds(x):
    out=(Q(0),Q(0))
    for k in range(1,6):
        z=k*k*x*x
        pol=Q(1)-2*k*k*x*x
        e=expneg_bounds(z)
        iv=imul((pol,pol),e)
        if k%2: iv=(-iv[1],-iv[0])
        out=iadd(out,iv)
    return out


def curvature_bounds(a,b):
    out=(Q(0),Q(0))
    for k in range(1,6):
        poly=imul((a,b), (4*k**4*a*a-6*k*k,4*k**4*b*b-6*k*k))
        e=(expneg_bounds(k*k*b*b)[0],expneg_bounds(k*k*a*a)[1])
        iv=imul(poly,e)
        if k%2: iv=(-iv[1],-iv[0])
        out=iadd(out,iv)
    return out

# Curvature is sqrt(pi)*G''(x); the k>=6 remainder has
# absolute value < 1/1000 for 0.7<=x<=1.
low=Q(100)
for i in range(40):
    a=Q(7,10)+Q(3*i,400)
    b=Q(7,10)+Q(3*(i+1),400)
    bound=curvature_bounds(a,b)[0]
    assert bound>1, ('curvature',i,float(bound))
    low=min(low,bound)
print('CERTIFIED sqrt(pi)*G_doubleprime lower, five terms:',float(low))

# For x in these brackets, derivative-tail absolute value < 1/1000000.
l=Q(86518,100000)
r=Q(86519,100000)
dl=derivative_bounds(l)
dr=derivative_bounds(r)
assert dl[1]<-Q(1,1000000),float(dl[1])
assert dr[0]>Q(1,1000000),float(dr[0])
print('CERTIFIED unique root bracket:',float(l),float(r))

# Independent exact spectral characteristic polynomial checks of DN blocks.
import sympy as sp
z=sp.Symbol('z')
for length in range(1,13):
    A=sp.diag(*([1]+[2]*(length-1)))
    for i in range(length-1):
        A[i,i+1]=A[i+1,i]=-1
    p=A.charpoly(z).as_expr()
    # p_0=1, p_1=z-1, p_l=(z-2)p_{l-1}-p_{l-2}.
    p0,p1=sp.Integer(1),z-1
    for i in range(2,length+1):
        p0,p1=p1,sp.expand((z-2)*p1-p0)
    assert sp.expand(p-p1)==0
print('CERTIFIED 12 DN characteristic-polynomial recurrences')

# Floating-point sanity check of the finite path optimizer; not part of
# the proof of any infinite or asymptotic assertion.
import numpy as np
from scipy.linalg import eigh_tridiagonal
for n,t in [(9,0.2),(9,2),(9,10),(80,50),(300,600),(1000,1000)]:
    a=[0.]
    for length in range(1,n):
        ev=2-2*np.cos((2*np.arange(1,length+1)-1)*pi/(2*length+1))
        formula=float(np.exp(-t*ev).sum())
        if n <= 80:
            diag=np.array([1.]+[2.]*(length-1))
            direct=np.exp(-t*eigh_tridiagonal(diag,-np.ones(length-1),eigvals_only=True)).sum() if length>1 else exp(-t)
            assert abs(formula-direct) < 1e-10
        a.append(formula)
    scores=[a[j]+a[n-1-j] for j in range((n+1)//2)]
    j=min(range(len(scores)),key=scores.__getitem__)
    print('path',n,'horizon',t,'leader-distance',j,'distance/sqrt(t)',round(j/sqrt(t),5))
print('PASS')
