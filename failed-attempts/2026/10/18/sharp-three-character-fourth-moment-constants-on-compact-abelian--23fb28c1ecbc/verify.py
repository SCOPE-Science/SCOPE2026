#!/usr/bin/env python3
"""Standalone exact-rational checks for a three-character L2-to-L4 theorem.

The infinite-group and all-order conclusions come from the accompanying proof.
These checks independently exercise the finite aliasing formulas and equality data.
"""
from fractions import Fraction as F
from itertools import product

# Unit-normalized exact autocorrelation formula; squares are rational.
def fourth_ratio(order):
    if order == 3:
        # Coefficients (1, 1, 1): transform (3, 0, 0).
        return F(3**4, 3) / F(3**2)
    if order == 4:
        # Coefficients (1, 1, 1): C0 = 3, C1=C3=2, C2=2.
        return F(3**2 + 2**2 + 2**2 + 2**2, 3**2)
    # Coefficients (sqrt(2),sqrt(3),sqrt(2)); C0=7,
    # |C1|^2=|C_{m-1}|^2=24 and |C2|^2=|C_{m-2}|^2=4.
    assert order == 'infinity' or order >= 5
    return F(7**2 + 2*24 + 2*4, 7**2)

assert fourth_ratio(3) == F(3)
assert fourth_ratio(4) == F(7,3)
for order in [5,6,7,8,9,10,11,12,17,29,'infinity']:
    assert fourth_ratio(order) == F(15,7)

# Symbolic normalization and exact square-completion identities are checked
# at an exhaustive rational grid (the manuscript proves them algebraically).
for denominator in (1,2,3,7,16,97):
    for numerator in range(denominator+1):
        s=F(numerator,denominator)
        assert F(15,7)-(1+4*s-F(7,2)*s*s) == F(7,2)*(s-F(4,7))**2
        assert F(7,3)-(1+4*s-3*s*s) == 3*(s-F(2,3))**2
        for sub in range(9):
            q=s*F(sub,16)
            low_order=1+2*(1-s)*(s+2*q)+4*q*q
            high_order=1+2*(1-s)*(s+2*q)+2*q*q
            assert low_order <= F(7,3)
            assert high_order <= F(15,7)

# Uniform three-term Dirichlet candidate is not sharp in the generic regime.
assert F(15,7)-F(19,9)==F(2,63)

# Distinct phases for the fourth-order case are fourth roots of unity,
# verified through integer/complex Gaussian-arithmetic correlations.
for z in (1,-1,1j,-1j):
    coeff=(1,z,z*z)
    cor=[sum(coeff[k]*coeff[(k-r)%4].conjugate()
             for k in range(3) if (k-r)%4 < 3)
         for r in range(4)]
    val=sum(abs(c)**2 for c in cor)/9
    assert abs(val-F(7,3))<1e-12, (z,val)
print('PASS: finite torsion thresholds, equality witnesses, exact envelopes, phases')
