#!/usr/bin/env python3
"""Exact tests of the area-weighted stellar intensity projection and its three cancellation radii."""
from fractions import Fraction as F
from math import sqrt

H = [[F(2,i+j+2) for j in range(3)] for i in range(3)]
v = [F(4,2*i+7) for i in range(3)]
c = [F(-8,231), F(40,77), F(40,77)]
assert all(sum(H[i][j]*c[j] for j in range(3)) == v[i] for i in range(3))
# A positive-definite Gram determinant and principal minors certify uniqueness.
assert H[0][0] > 0
assert H[0][0]*H[1][1] - H[0][1]**2 > 0
assert (H[0][0]*(H[1][1]*H[2][2]-H[1][2]**2)
        -H[0][1]*(H[1][0]*H[2][2]-H[1][2]*H[2][0])
        +H[0][2]*(H[1][0]*H[2][1]-H[1][1]*H[2][0])) > 0

def poly(t):
    return 120*t**4 - 231*t**3 + 120*t**2 - 8

brackets = [(F(435,1000),F(437,1000)),
            (F(751,1000),F(753,1000)),
            (F(950,1000),F(952,1000))]
for low,high in brackets:
    assert poly(low)*poly(high)<0 and 0<low<high<1
# There are at least 3 positive roots by sign changes; Descartes permits at most 3
# positive roots, since the coefficient sequence is (+,-,+,-).
assert poly(F(-1,4))*poly(F(0)) < 0  # a fourth negative root
assert poly(F(0)) < 0 and poly(F(1)) > 0
# Exact disk-normalization equality: integral residual = zero.
assert F(4,7) - sum(c[i]*F(2,i+2) for i in range(3)) == 0
# 61 exact rational test points for the residual factorization.
for k in range(61):
    t=F(k,60)
    r=t**3-sum(c[i]*t**(2*i) for i in range(3))
    assert 231*r == -poly(t)
# Physical admissibility example I(mu)=1+mu^(3/2)/10, Q(mu)=1+P(mu)/10.
# Since P(mu) >= -8/231 for mu in [0,1], Q stays positive.
assert F(1)-F(8,2310)>0
# Bisection gives reported decimals, but is supplementary, not proof.
for lo,hi in brackets:
    for i in range(80):
        mid=(lo+hi)/2
        if poly(lo)*poly(mid)<=0: hi=mid
        else:lo=mid
    t=float((lo+hi)/2)
    print(f't={t:.15f}, impact_b={sqrt(1-t**4):.15f}')
print('PASS: exact Gram, orthogonality, three positive intervals, fourth negative interval, 61 identities, admissibility')
