"""Standalone finite consistency tests for a triangular split-product Gram theorem.

Run: python verify_splitmask.py (requires NumPy).
Finite tests supplement, and do not replace, the symbolic argument.
"""
from fractions import Fraction
from itertools import product
from math import ceil, floor, pi, sin
import numpy as np

checks = 0
for d in range(1, 41):
    H = np.fromfunction(lambda i, j: (i + j <= d-1).astype(float), (d, d))
    expected = np.array([(-1)**(k-1)/(2*sin((2*k-1)*pi/(4*d+2))) for k in range(1, d+1)])
    actual = np.linalg.eigvalsh(H)
    assert np.allclose(sorted(expected), actual, atol=2e-12, rtol=1e-12)
    checks += 1
    assert sum(actual > 1e-10) == ceil(d/2)
    assert sum(actual < -1e-10) == floor(d/2)
    checks += 2
    assert np.allclose(H @ H, np.fromfunction(lambda i,j: d-np.maximum(i,j), (d,d)))
    checks += 1
    for k in range(1, d+1):
        theta = (2*k-1)*pi/(2*d+1)
        u = np.array([sin((d-i)*theta) for i in range(d)])
        assert np.linalg.norm(H@u-expected[k-1]*u) < 1e-9
        checks += 1
    if d >= 2:
        eta = 1/(2*sin(3*pi/(4*d+2)))
        assert abs(actual[0]+eta) < 2e-11
        checks += 1
        for q in [0.02, 0.1, 0.5]:
            B=(np.eye(d)+np.ones((d,d))) @ np.diag(np.power(q, np.arange(d)))
            T=B@H@B.T
            G=np.outer(B@np.ones(d), B@np.ones(d))
            assert d > 10 or np.linalg.eigvalsh(T)[0] < -1e-16
            assert np.linalg.norm(T-G,2) <= (d*(d-1)/2)*(d+3)*(q**d)+1e-9
            checks += 2

# Exact rational obstruction in two dimensions: det(T_2) = -9 q^2.
for numerator in range(1, 20):
    q=Fraction(numerator, 20)
    v1=(Fraction(2), Fraction(1))
    v2=(q, 2*q)
    t00=v1[0]*v1[0]+2*v1[0]*v2[0]
    t01=v1[0]*v1[1]+v1[0]*v2[1]+v2[0]*v1[1]
    t11=v1[1]*v1[1]+2*v1[1]*v2[1]
    assert t00*t11-t01*t01 == -9*q*q
    checks += 1

# For a symmetric binary mask containing the triangular retained positions,
# PSD necessitates every missing coefficient: a 2x2 principal-minor proof.
for d in range(2, 7):
    mandatory = {(i,j) for i in range(d) for j in range(d) if i+j <= d-1}
    optional = [(i,j) for i in range(d) for j in range(i,d) if (i,j) not in mandatory]
    for bits in product([0,1], repeat=len(optional)):
        M=[[int((i,j) in mandatory) for j in range(d)] for i in range(d)]
        for ((i,j), bit) in zip(optional,bits):
            M[i][j]=M[j][i]=bit
        if M != [[1]*d for _ in range(d)]:
            # Any such matrix must either have a zero diagonal or a row
            # differing from its first row, which violates PSD with M[0,j]=1.
            witness=any(M[j][j]==0 or any(M[j][k]!=1 for k in range(d)) for j in range(d))
            assert witness
        checks += 1

print(f'VERIFY_OK {checks}')
