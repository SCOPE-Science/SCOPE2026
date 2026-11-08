#!/usr/bin/env python3
"""Exact independent simplicial volume and covariance checks for symmetric alcoved zonotopes.

Requires Python 3, numpy and scipy (geometry), and sympy (symbolic identity).
Run: python check_isocanted.py
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
import numpy as np
from scipy.spatial import ConvexHull
import sympy as sp


def det(A):
    """Fraction determinant via symbolic determinant, independent of floating hull."""
    return Q(sp.det(sp.Matrix(A)))


def integrate_simplex(vs):
    d = len(vs)
    vol = abs(det(vs)) / factorial(d)
    sm = [sum(v[j] for v in vs) for j in range(d)]
    mm = [[vol * (sm[i]*sm[j] + sum(v[i]*v[j] for v in vs)) / ((d+1)*(d+2))
           for j in range(d)] for i in range(d)]
    return vol, mm


def check_one(d, t):
    vs = sorted(set(tuple(Q(e) + Q(s)*t for e in v) for s in (-1,1)
                    for v in product((-1,1), repeat=d)))
    hull = ConvexHull(np.array([[float(x) for x in v] for v in vs]), qhull_options='Qt')
    total = Q(0)
    mat = [[Q(0) for _ in range(d)] for _ in range(d)]
    for facet in hull.simplices:
        simplex = [vs[int(i)] for i in facet]
        volume, moment = integrate_simplex(simplex)
        total += volume
        for i in range(d):
            for j in range(d):
                mat[i][j] += moment[i][j]
    expected_volume = 2**d * (1+d*t)
    assert total == expected_volume, (d,t,total,expected_volume)
    longitudinal = (d*t*t+2*t+1)/3
    transverse = (1+(d+2)*t)/(3*(1+d*t))
    expected_diag = (longitudinal+(d-1)*transverse)/d
    expected_off = (longitudinal-transverse)/d
    for i in range(d):
        for j in range(d):
            assert mat[i][j]/total == (expected_diag if i==j else expected_off), (d,t,i,j,mat[i][j]/total,expected_diag,expected_off)
    return len(hull.simplices)


def check_symbolic():
    d,t=sp.symbols('d t',positive=True)
    f=d*t*t+2*t+1
    R= f*(1+(d+2)*t)**(d-1)/(1+d*t)**(d+1)
    target = 2*d*(d-1)*t*(t-1)/((d*t+1)*((d+2)*t+1)*f)
    assert sp.factor((2*d*t+2)/f+(d-1)*(d+2)/(1+(d+2)*t)-(d+1)*d/(1+d*t)-target)==0
    # exact gap laws and conditional moments
    ES=2*(d-1)*(1+(d+1)*t)/((d+1)*(1+d*t))
    ES2=4*d*(d-1)*(1+(d+2)*t)/((d+1)*(d+2)*(1+d*t))
    EL2=4*(t+1)**2-4*(t+1)*ES+ES2
    lampara=d*EL2/12+(d-2)*ES2/(12*d)
    lamtrans=(d+1)*(d+2)*ES2/(12*d*(d-1))
    assert sp.factor(lampara-f/3)==0
    assert sp.factor(lamtrans-(1+(d+2)*t)/(3*(1+d*t)))==0
    return 3


def main():
    num=0; facets=0
    for d, tvals in [(2,['0','1/3','1','5/2']), (3,['0','1/2','1','2']), (4,['0','1/2','1','3/2'])]:
        for ts in tvals:
            facets += check_one(d,Q(ts)); num+=1
    s=check_symbolic()
    print(f'ISOCANTED_COVARIANCE_EXACT_CHECKS_PASSED {num} {facets} {s}')

if __name__=='__main__':
    main()
