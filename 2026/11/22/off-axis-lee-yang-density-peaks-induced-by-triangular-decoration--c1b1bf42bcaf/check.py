"""Reproducibility checks for Ising Lee--Yang zeros on triangular bouquets.

Requirements: Python >=3.10, sympy, numpy, mpmath.
Run: python check.py
"""
from itertools import product
import numpy as np
import sympy as sp
import mpmath as mp

z=sp.Symbol('z')

def exact_poly(m,q):
    u=sp.Rational(q)**2
    a=1+2*u*z+u*z*z
    b=u+2*u*z+z*z
    return sp.Poly(sp.expand(a**m+z*b**m),z)

def enumerated_poly(m,q):
    q=sp.Rational(q)
    coeff=[sp.Rational(0) for _ in range(2*m+2)]
    edges=[(0,2*j+1) for j in range(m)]+[(0,2*j+2) for j in range(m)]+[(2*j+1,2*j+2) for j in range(m)]
    for bits in product((0,1),repeat=2*m+1):
        disagree=sum(bits[i]!=bits[j] for i,j in edges)
        coeff[sum(bits)]+=q**disagree
    return sp.Poly(sum(coeff[k]*z**k for k in range(2*m+2)),z)

def w(theta,u):
    return 2*u+(1+u)*np.cos(theta)-1j*(1-u)*np.sin(theta)

def phase_derivative(theta,u):
    return -(1-u)*(1+u+2*u*np.cos(theta))/(abs(w(theta,u))**2)

def positive_angles(m,u):
    # f(theta) from continuously unwrapped ellipse angle, in (-pi,0) on (0,pi)
    def f(t):
        return np.angle(w(t,u)) if t<np.pi-1e-12 else -np.pi
    ans=[]
    from scipy.optimize import brentq
    for j in range(m+1):
        target=-(2*j+1)*np.pi
        def fun(t):return 2*m*f(t)-t-target
        # Last root is pi, independent of m.
        if j==m: ans.append(np.pi)
        else: ans.append(brentq(fun,0,np.pi-1e-10,xtol=1e-13))
    return ans

cnt=0
for m in range(1,7):
    for q in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(2,3)]:
        pp=exact_poly(m,q)
        assert pp==enumerated_poly(m,q),(m,q)
        cnt+=1
print('EXACT_PARTITION_ENUMERATIONS',cnt)

# Polynomial roots and exact phase equation, all orientations.
cnt=0
for m in range(1,7):
    for q in [0.1,0.3,0.6]:
        pp=exact_poly(m,sp.Rational(str(q)))
        roots=np.roots(np.array([float(c) for c in pp.all_coeffs()]))
        assert max(abs(abs(v)-1) for v in roots)<5e-6,(m,q,roots)
        assert len(set(round(np.angle(v),7) for v in roots))==2*m+1
        for th in positive_angles(m,q*q):
            assert abs(complex(pp.eval(np.exp(1j*th))))/sum(abs(complex(c)) for c in pp.all_coeffs())<1e-8,(m,q,th)
        cnt+=1
print('ROOT_AND_PHASE_CASES',cnt)

# Algebraic derivative identity & unique density peak.
u,c=sp.symbols('u c',real=True)
D=1-2*u+5*u**2+4*u*(1+u)*c+4*u*c**2
R=(1-u)*(1+u+2*u*c)/D
assert sp.factor(sp.diff(R,c)*D**2/(2*u*(1-u)))==(-4*u*c*c-4*u*c-4*c+3*u*u-6*u-1)
for v in [0.01,0.1,0.5,0.9,0.99]:
    cpeak=(-(1+v)+(1-v)*np.sqrt(1+3*v))/(2*v)
    assert -1<cpeak<1
    assert abs(-4*v*cpeak**2-4*(v+1)*cpeak+3*v*v-6*v-1)<1e-8
print('PEAK_DERIVATIVE_AND_LOCATION_OK')
# Every star Poisson-kernel density has derivative >0 on (0,pi),
# unlike the strict interior maximum of the decorated triangles.
for v in [0.05,0.2,0.6,0.9]:
    for th in np.linspace(0.05,np.pi-0.05,25):
        q=np.sqrt(v)
        star_derivative=(1-v)*2*q*np.sin(th)/(2*np.pi*(1+v+2*q*np.cos(th))**2)
        assert star_derivative>0
print('STAR_UNIMODALITY_CONTRAST_OK')

# Positive normalized limiting density and leading first-zero scale.
for q in [0.1,0.25,0.5,0.9]:
    val=mp.quad(lambda t: (1-q*q)*(1+q*q+2*q*q*mp.cos(t))/abs(2*q*q+(1+q*q)*mp.cos(t)-1j*(1-q*q)*mp.sin(t))**2/(2*mp.pi),[-mp.pi,0,mp.pi])
    assert abs(val-1)<1e-10,(q,val)
    cs=(1-q*q)/(1+3*q*q)
    for m in [1000,2000,4000]:
        theta=positive_angles(m,q*q)[0]
        assert abs(theta*(2*m*cs+1)/np.pi-1)<0.005,(m,q,theta)
print('DENSITY_NORMALIZATION_AND_FIRST_ZERO_OK')
print('ALL_CHECKS_PASSED')
