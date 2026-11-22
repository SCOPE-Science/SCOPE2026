"""Exact-rational finite checks for the two-step DR/RD residual formulas.

The all-parameter asymptotic statements are proved in RESULT.md, not
certified by a finite test. Requires Python >= 3.9, standard library only.
"""
from fractions import Fraction as F
from math import isfinite, sqrt

count = 0

def verify(K, t):
    global count
    K, t = F(K), F(t)
    assert K > 1 and t > 0
    # Squared lengths of the two components of the unit initial residual.
    u, v = t / (1+t), 1 / (1+t)
    a0 = (1+t) / (1+K*t)
    r1u = (1-K*a0)**2 * u
    r1v = (1-a0)**2 * v
    # Source-defined delayed-residual step and residual-difference step.
    adr = a0
    ard = (K*K*t+1) / (K*K*K*t+1)
    dr = (1-K*adr)**2*r1u + (1-adr)**2*r1v
    rd = (1-K*ard)**2*r1u + (1-ard)**2*r1v
    fdr = (K-1)**4 * (t+t**4) / ((1+t)*(1+K*t)**4)
    frd = (K-1)**4 * (t+K**4*t**4) / ((1+t)*(1+K*t)**2*(1+K**3*t)**2)
    assert dr == fdr
    assert rd == frd
    assert ard <= adr
    # Exact transformations used in the uniform asymptotic proof.
    y = K*t
    z = K**3*t
    transform_dr = ((1-1/K)**4 * y * (1-y/K+(y/K)**2)/(1+y)**4)
    transform_rd = ((1-1/K)**4 * (z+z**4/K**5) /
                    ((1+z/K**3)*(1+z/K**2)**2*(1+z)**2))
    assert dr/K**3 == transform_dr
    assert rd/K == transform_rd
    # The uniform RD bound in the proof holds for every positive parameter.
    assert transform_rd <= (1-1/K)**4*(F(1,4)+1/K)
    count += 7

for K in (2, 3, 4, 5, 10, 30, 100, 1000):
    ts = [F(i, 31) for i in range(1, 40)]
    ts += [F(i, j*K) for i in (1, 2, 3, 5, 10)
           for j in (1, 2, 3, 10)]
    ts += [F(i, j*K**3) for i in (1, 2, 3, 5, 10)
           for j in (1, 2, 3, 10)]
    for t in ts:
        verify(K, t)

# The near-maximizing choices converge to the stated sharp constants.
for K in (1000, 3000, 10000):
    gdr = float((F(K-1)**4 * (F(1,3*K)+F(1,3*K)**4) /
        ((1+F(1,3*K))*(1+K*F(1,3*K))**4)) / K**3)
    grd = float((F(K-1)**4 * (F(1,K**3)+K**4*F(1,K**3)**4) /
        ((1+F(1,K**3))*(1+K*F(1,K**3))**2*(1+K**3*F(1,K**3))**2)) / K)
    assert abs(gdr - 27/256) < 0.001
    assert abs(grd - 1/4) < 0.003
    count += 2

print('VERIFY_OK', count)
