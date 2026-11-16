#!/usr/bin/env python3
"""Reproducibility tests for pure-degree spherical-harmonic tight latitude sampling.
Scientific tests only; proof of the all-degree statement is in RESULT.md.
Requires Python 3, NumPy, SciPy, and SymPy.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.special import roots_jacobi, sph_harm_y
import sympy as sp

u,t=sp.symbols('u t')

def normalized_ring(l):
    r=(l+2)//2
    x,v=roots_jacobi(r,0,-0.5)
    return (x+1)/2, v / (2*math.sqrt(2))


def intensity_poly(l,m):
    # Remove the positive spherical-normalization factor; prove linear independence.
    p=sp.legendre(l,t)
    q=sp.diff(p,t,m)**2 * (1-t*t)**m
    poly=sp.Poly(sp.expand(q),t)
    assert all(e[0]%2==0 for e,c in poly.terms())
    return sp.Poly(sum(c*u**(e[0]//2) for e,c in poly.terms()),u)

for l in range(1,11):
    fs=[intensity_poly(l,m) for m in range(l+1)]
    assert all(f.degree()==l for f in fs)
    M=sp.Matrix([[f.nth(j) for j in range(l+1)] for f in fs])
    assert M.det()!=0, (l,'intensity span')
    for m,f in enumerate(fs):
        assert sp.diff(f.as_expr(),u,m).subs(u,1)!=0
        assert all(sp.diff(f.as_expr(),u,j).subs(u,1)==0 for j in range(m))

    nodes,weights=normalized_ring(l)
    r=len(nodes)
    assert r==(l+2)//2
    assert np.all(nodes>0) and np.all(nodes<1) and np.all(weights>0)
    assert abs(weights.sum()-1)<2e-14
    for k in range(l+1):
        assert abs(weights@nodes**k-1/(2*k+1))<2e-13, (l,k)
    n=2*l+1
    gram=np.zeros((n,n),dtype=complex)
    for z,w in zip(np.sqrt(nodes),weights):
        theta=math.acos(z)
        for j in range(n):
            phi=2*math.pi*j/n
            vec=np.array([sph_harm_y(l,m,theta,phi) for m in range(-l,l+1)])
            gram += (4*math.pi*w/n)*np.outer(np.conj(vec),vec)
    assert np.max(np.abs(gram-np.eye(n)))<4e-12, (l,'Gram')

# Exact Gauss-Jacobi polynomial moment orthogonality for r <= 6.
def monic_orthogonal(n):
    if n==0: return sp.Poly(1,u)
    A=sp.Matrix([[sp.Rational(1,2*(i+j)+1) for j in range(n)] for i in range(n)])
    b=sp.Matrix([-sp.Rational(1,2*(i+n)+1) for i in range(n)])
    sol=A.inv()*b
    return sp.Poly(u**n+sum(sol[j]*u**j for j in range(n)),u)

for r in range(1,7):
    q=monic_orthogonal(r)
    for k in range(r):
        assert sum(q.nth(j)*sp.Rational(1,2*(j+k)+1) for j in range(r+1))==0
    if r>=2:
        p=monic_orthogonal(r-1)
        q_alt=q+sp.Rational(1,100)*p
        for k in range(r-1):
            assert sum(q_alt.nth(j)*sp.Rational(1,2*(j+k)+1) for j in range(r+1))==0
        assert all(0<x<1 for x in sp.nroots(q_alt,maxsteps=250)), (r,q_alt)
        den=(4*r-1)*(4*r-3)
        c_left=sp.Rational(-2*r*(2*r-1),den)
        c_right=sp.Rational((2*r-1)**2,den)
        assert (q+c_left*p).eval(1)==0
        assert (q+c_right*p).eval(0)==0
        assert c_left<0<c_right

# For the first nontrivial even-degree case, equal-mass quadrature is distinct.
u_lo=sp.Rational(1,3)-sp.Rational(2,3)/sp.sqrt(5)
u_hi=sp.Rational(1,3)+sp.Rational(2,3)/sp.sqrt(5)
for k in (0,1,2):
    assert sp.simplify((u_lo**k+u_hi**k)/2-sp.Rational(1,2*k+1))==0
assert sp.simplify((u_lo**3+u_hi**3)/2-sp.Rational(1,7))!=0
print('PURE_DEGREE_LATITUDE_PASS exact_spans=1..10 exact_gauss_polys=1..6')
print('PURE_DEGREE_LATITUDE_GRAM_PASS sample_degrees=1..10 parity_class=checked')
