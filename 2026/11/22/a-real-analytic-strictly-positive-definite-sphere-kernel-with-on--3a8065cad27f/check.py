#!/usr/bin/env python3
"""Finite diagnostics for a real single-mode-per-degree spherical kernel.

This script does not constitute a proof of strict positive definiteness at
arbitrary finite configurations; the separate Vandermonde argument does.
"""
from math import sqrt, sin, cos, pi
import numpy as np
import sympy as sp


def family(n):
    if n == 0:
        return 'A'
    if n == 1:
        return 'C'
    j = 1
    start = 2
    while not start <= n < start + j:
        start += j
        j += 1
    return ('A', 'B', 'C', 'D')[(j - 1) % 4]


def harmonic_feature(n, point):
    x, y, v = point
    z = complex(x, y)
    f = family(n)
    if n == 0:
        return 1.0
    if f == 'A':
        return (z**n).real
    if f == 'B':
        return (z**n).imag
    if f == 'C':
        return v * (z**(n-1)).real
    return v * (z**(n-1)).imag


def make_gram(points, max_degree=120):
    values = np.array([[harmonic_feature(n, p) for p in points]
                       for n in range(max_degree + 1)], dtype=float)
    weights = 2.0**(-np.arange(max_degree + 1))
    return values.T @ (weights[:, None] * values)


def sphere_from_ab(a, b):
    den = 1.0 + a*a + b*b
    return (2*a/den, 2*b/den, (1-a*a-b*b)/den)


def tests():
    checks = 0
    x,y,v=sp.symbols('x y v',real=True)
    z=x+sp.I*y
    # Exact ambient harmonicity for representative polynomials.
    for n in range(0, 17):
        f=family(n)
        if n==0: P=sp.Integer(1)
        elif f=='A': P=sp.re(sp.expand(z**n)).expand(complex=True)
        elif f=='B': P=sp.im(sp.expand(z**n)).expand(complex=True)
        elif f=='C': P=(v*sp.re(sp.expand(z**(n-1)))).expand(complex=True)
        else: P=(v*sp.im(sp.expand(z**(n-1)))).expand(complex=True)
        assert sp.simplify(sp.diff(P,x,2)+sp.diff(P,y,2)+sp.diff(P,v,2)) == 0
        assert sp.simplify(x*sp.diff(P,x)+y*sp.diff(P,y)+v*sp.diff(P,v)-n*P)==0
        checks+=2
    # Long blocks of arbitrarily large sizes are an exact feature of rule.
    for j in range(1, 45):
        s = 2 + j*(j-1)//2
        fam = ('A','B','C','D')[(j-1)%4]
        assert all(family(n)==fam for n in range(s,s+j))
        checks += j
    # Configurations with north/south fibres, equatorial roots of unity,
    # conjugate longitudes, and generic sites.
    near_fibres = [sphere_from_ab(.28,.19), sphere_from_ab(1.08,.73),
                   sphere_from_ab(.45,-.28),sphere_from_ab(-.9,.2)]
    equator = [(cos(2*pi*j/7),sin(2*pi*j/7),0) for j in range(7)]
    poles = [(0,0,1),(0,0,-1)]
    conjugates = [(x0,y0,v0) for x0,y0,v0 in near_fibres] + [
        (x0,-y0,v0) for x0,y0,v0 in near_fibres]
    sameprojection=[]
    for k in range(4):
        r=.22+.13*k
        th=.7+.6*k
        a=r*cos(th); b=r*sin(th)
        v0=sqrt(1-a*a-b*b)
        sameprojection.extend([(a,b,v0),(a,b,-v0)])
    rng=np.random.default_rng(2023)
    samples=[]
    for m in (2,3,5,7):
        aa=rng.uniform(-1.2,1.2,size=(m,2))
        samples.append([sphere_from_ab(float(a),float(b)) for a,b in aa])
    configurations=[poles, equator, conjugates, sameprojection,
                    equator+poles, poles+near_fibres]+samples
    min_vals=[]
    for points in configurations:
        G=make_gram(points, max_degree=170)
        G=(G+G.T)/2
        eig=np.linalg.eigvalsh(G)
        assert eig[0] > max(1e-14,1e-12*eig[-1]), (len(points),eig)
        min_vals.append(float(eig[0]))
        checks+=1
    print('PASS',checks,'checks; configurations',len(configurations),
          'minimum observed Gram eigenvalue',format(min(min_vals),'.8g'))
    print('Every tested feature is an exactly harmonic homogeneous polynomial.')
    print('These finite diagnostics do not certify infinite strict positivity.')

if __name__=='__main__':
    tests()
