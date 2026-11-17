#!/usr/bin/env python3
"""Finite reproducibility checks for an exact Ky Fan-two projection theorem."""
from fractions import Fraction as F
from math import sqrt, cos, sin, pi
import random
import numpy as np

# Exact algebraic ranks and critical equations.
r2 = F(3, 8)
s2 = 1 - r2
assert s2 == F(5, 8)
assert 1 - F(8, 9)*r2 == F(2, 3)
assert F(16, 9)*r2 == F(2, 3)
assert F(9, 4)*4*(1-F(1, 8)**2)+(1+F(1,8))**2 == F(81,8)
assert 0.5+sqrt(6)/4 > 3/(2*sqrt(2))  # Strict bound gap.
print('EXACT_RANK_ONE_CRITICAL_IDENTITIES_PASSED')
print('EXACT_FULL_RANK_QUADRATIC_ENVELOPE_PASSED')

z = np.zeros((3,3))
z[0,0], z[0,1] = sqrt(3/8), sqrt(5/8)
def ky2(a):
    return float(np.linalg.svd(a,compute_uv=False)[:2].sum())
def center(a):
    return a - np.trace(a)*np.eye(3)/3
sharp = 0.5+sqrt(6)/4
assert abs(ky2(z)-1)<1e-12
assert abs(ky2(center(z))-sharp)<1e-12
print('EXPLICIT_RANK_ONE_MATRIX_ATTAINMENT_PASSED')

random.seed(20261109)
n=0
for complex_case in (False,True):
    for j in range(1,4):
        for t in range(500):
            q=np.array([[random.gauss(0,1)+ (1j*random.gauss(0,1) if complex_case else 0) for _ in range(3)] for _ in range(3)])
            v=np.array([[random.gauss(0,1)+ (1j*random.gauss(0,1) if complex_case else 0) for _ in range(3)] for _ in range(3)])
            U,_=np.linalg.qr(q); V,_=np.linalg.qr(v)
            a=U[:,:j]@V[:,:j].conj().T/min(j,2)
            ratio=ky2(center(a))/ky2(a)
            assert ratio < sharp+1e-10, (complex_case,j,t,ratio)
            n+=1
print('INDEPENDENT_PARTIAL_ISOMETRY_SAMPLES_PASSED',n)

m=0
for t in range(120):
    for s in range(120):
        points=np.exp(1j*np.array([0,2*pi*t/120,2*pi*s/120]))
        norm=sum(sorted(abs(points-points.mean()))[-2:])/2
        assert norm <= 3/(2*sqrt(2))+1e-12
        m+=1
print('FULL_RANK_UNITARY_EIGENANGLE_GRID_PASSED',m)
print('ALL_KY_FAN_TWO_DIMENSION_THREE_CHECKS_PASSED')
