#!/usr/bin/env python3
"""Reproducible coefficient and geometric checks for a homothetic-frustum identity.

Finite regressions support an analytic proof; they do not certify all dimensions.
"""
from fractions import Fraction
from math import comb, isclose
import numpy as np
from scipy.spatial import ConvexHull

def coefficient_from_sections(d,k,r,M):
    """Integrate the horizontal-section Minkowski polynomial termwise."""
    a=1-r
    if a:
        positive=Fraction(comb(d-1,k),1)*M[k]*(1-r**(d-k))/(a*(d-k))
        negative=Fraction(comb(d-1,k-1),1)*M[k-1]*(1-r**k)/(a*k)
        return (positive+negative)/comb(d,k)
    positive=Fraction(comb(d-1,k),1)*M[k]
    negative=Fraction(comb(d-1,k-1),1)*M[k-1]
    return (positive+negative)/comb(d,k)

def formula(d,k,r,M):
    if r==1:
        return (Fraction(d-k)*M[k]+Fraction(k)*M[k-1])/d
    return ((1-r**(d-k))*M[k]+(1-r**k)*M[k-1])/(d*(1-r))

checks=0
for d in range(2,13):
    # Formal comparison requires no actual realizability of the independent
    # coefficients, since the identity is a linear polynomial identity in M_j.
    M=[Fraction((j+1)*(d-j)+1, j+2) for j in range(d)]
    for r in (Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(4,5),Fraction(1)):
        for k in range(1,d):
            assert coefficient_from_sections(d,k,r,M)==formula(d,k,r,M)
            checks+=1
    # Strictly decreasing elementary coefficient functions for rational ratios.
    ratios=[Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(4,5),Fraction(1)]
    for p in range(1,d):
        vals=[(1-r**p)/(1-r**d) if r<1 else Fraction(p,d) for r in ratios]
        assert all(vals[i]>vals[i+1] for i in range(4))
        checks+=1

def vertices(base,r):
    B=np.asarray(base,dtype=float)
    return np.vstack([np.column_stack([B,np.zeros(len(B))]),
                      np.column_stack([r*B,np.ones(len(B))])])

def predicted_3d(base_type,r,t):
    if base_type=='triangle':
        area=3.0
        M=[area,2*area,area]
    else:
        area=4.0
        M=[area,area,area]
    d=3
    answer=0.0
    for k in range(d+1):
        if k in (0,d):
            Vk=area*sum(r**j for j in range(d))/d
        else:
            Vk=(((1-r**(d-k))*M[k]+(1-r**k)*M[k-1])/(d*(1-r))
                if r!=1 else ((d-k)*M[k]+k*M[k-1])/d)
        answer+=comb(d,k)*t**k*Vk
    return answer

for kind,B in (('triangle',[(0,0),(3,0),(0,2)]),
               ('square',[(-1,-1),(-1,1),(1,-1),(1,1)])):
    for r in (0.0,0.2,0.6,1.0):
        pts=vertices(B,r)
        for t in (0.15,0.7,2.3):
            Mink=np.asarray([p-t*q for p in pts for q in pts])
            measured=ConvexHull(Mink).volume
            expected=predicted_3d(kind,r,t)
            assert isclose(measured,expected,rel_tol=1e-10,abs_tol=1e-10),(kind,r,t,measured,expected)
            checks+=1
print('FRUSTUM_VERIFY_OK',checks)
