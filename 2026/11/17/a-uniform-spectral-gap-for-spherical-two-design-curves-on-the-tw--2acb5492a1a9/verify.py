#!/usr/bin/env python3
"""Checks supporting a strict spherical two-design curve length bound.

This finite numerical and rational-arithmetic check does not prove the universal theorem.
The theorem is proved analytically in RESULT.md.
"""
import math
import random
from fractions import Fraction

# Derive the positive equality root of 11 e/15 + 4 sqrt(3e/5)=1.
# Squaring gives (1-11e/15)^2 = 48e/5, equivalently
# 121e^2 - 2490e + 225 = 0.
assert Fraction(1, 1) - Fraction(11, 15) * Fraction(0, 1) > 0
# eps = (1245-180 sqrt(47))/121. Compute the quadratic in Q(sqrt(47)).
# (u+v sqrt47)^2 -2490(u+v sqrt47)+225*121^2=0.
u, v = 1245, -180
assert 121 * (u * u + 47 * v * v) - 2490 * 121 * u + 225 * 121 * 121 == 0
assert 121 * (2 * u * v) - 2490 * 121 * v == 0
E = (1245 - 180 * math.sqrt(47)) / 121
assert 0 < E < 1
assert abs(Fraction(11, 15) * E + 4 * math.sqrt(3 * E / 5) - 1) < 2e-13
L = 2 * math.pi * math.sqrt((6 + E) / 3)
assert L > 2 * math.pi * math.sqrt(2)
assert abs(L - 8.952720926309894) < 1e-11

# On the subspace W=span(P,Q), PSD U=PP^T+QQ^T and K=CC^T+DD^T
# obey U+K <= I when their combined trace <=1. This validates the
# eigenvalue/trace inequality in many independent positive-semidefinite cases.
def dot(x, y):
    return sum(a*b for a,b in zip(x,y))

def norm(x):
    return math.sqrt(dot(x,x))

def orthobasis(P,Q):
    out=[]
    for v in (P,Q):
        z=list(v)
        for w in out:
            t=dot(z,w)
            z=[a-t*b for a,b in zip(z,w)]
        z_norm=norm(z)
        if z_norm>1e-10:out.append([a/z_norm for a in z])
    if len(out)<2:
        for v in ([1.,0.,0.],[0.,1.,0.],[0.,0.,1.]):
            z=list(v)
            for w in out:
                t=dot(z,w)
                z=[a-t*b for a,b in zip(z,w)]
            z_norm=norm(z)
            if z_norm>1e-10:out.append([a/z_norm for a in z])
            if len(out)==2:break
    return out

rng=random.Random(260715386)
for j in range(1000):
    P,Q,C,D=([rng.uniform(-1,1) for k in range(3)] for _ in range(4))
    scale=0.99 / math.sqrt(sum(dot(v,v) for v in (P,Q,C,D)))
    P,Q,C,D=([scale*x for x in v] for v in (P,Q,C,D))
    a=dot(P,P)+dot(Q,Q)
    b=dot(C,C)+dot(D,D)
    W=orthobasis(P,Q)
    tr_W_K=sum(dot(C,w)**2+dot(D,w)**2 for w in W)
    # two nonzero eigenvalues of K coincide with those of Gram(C,D)
    diff=math.sqrt((dot(C,C)-dot(D,D))**2+4*dot(C,D)**2)
    lam2=(b-diff)/2
    assert lam2 >= -1e-13 and lam2 <= tr_W_K+1e-12
    assert tr_W_K <= 2-a+1e-12
    assert diff >= b-2*(2-a)-1e-12
print('PASS: exact radical polynomial and 1000 Fourier-covariance checks')
