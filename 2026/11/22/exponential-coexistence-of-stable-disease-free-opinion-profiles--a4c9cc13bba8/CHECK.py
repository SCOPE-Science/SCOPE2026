"""Exact star-sign census for a coupled epidemic/opinion model.

Run: python3 CHECK.py
All equalities and inequalities use exact rational arithmetic.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def equilibrium(m, w, signs):
    assert m >= 1 and w > 0 and len(signs) == m + 1
    s0 = signs[0]
    P = sum(s == 1 for s in signs[1:])
    z0 = -((1+w)*s0 + w*(2*P-m))/(2*(1+(m+1)*w))
    z = [z0] + [(w*z0-Q(s, 2))/(1+w) for s in signs[1:]]
    o = [s*zj for s, zj in zip(signs, z)]
    assert all(abs(v) <= Q(1, 2) for v in o)
    # Compute the source model's zero-infection opinion field directly.
    center = -o[0] - Q(1, 2) - sum(
        w*(o[0]-signs[0]*signs[j]*o[j]) for j in range(1,m+1))
    assert center == 0
    for j in range(1,m+1):
        leaf = -o[j] - Q(1, 2) - w*(o[j]-signs[j]*signs[0]*o[0])
        assert leaf == 0
    return z, o


def census(m, w):
    states = []
    for signs in product((-1, 1), repeat=m+1):
        z, o = equilibrium(m, w, signs)
        if all(v > 0 for v in z):
            assert all((v > 0) == (s > 0) for v, s in zip(o, signs))
            states.append((signs, o))
    assert len({tuple(o) for _, o in states}) == len(states)
    return states


def expected_count(m):
    if m % 2 == 0:
        return 2**m
    return 2**m - comb(m, (m-1)//2)


def check_inequality(m, w, signs, z):
    P=sum(s==1 for s in signs[1:]); s0=signs[0]
    if s0 == -1 and P == 0:
        expected=True
    elif s0 == -1:
        expected=w*w*(m+1-2*P)-m*w-1 > 0
    elif P == 0:
        expected=w*(m-1)>1
    else:
        expected=w*w*(m-2*P-1)-(m+2)*w-1>0
    assert expected == all(v>0 for v in z)

for m in range(1, 11):
    w=Q(m+3)
    states=census(m,w)
    assert len(states)==expected_count(m),(m,len(states),expected_count(m))
    for signs in product((-1,1),repeat=m+1):
        z,_=equilibrium(m,w,signs)
        check_inequality(m,w,signs,z)
    print(f'm={m}, w={w}, stable healthy states={len(states)}')

m=3;w=Q(2)
states=census(m,w)
assert len(states)==5
for signs,o in states:
    print('three-leaf example',signs,tuple(o))
# Exact global eradication comparison: (sqrt(m)+1)/(4m) < 1.
# Since sqrt(m) <= m for m>=1, the ratio is <=(m+1)/(4m)<=1/2.
for m in range(1,11):
    assert (m+1) < 4*m
print('PASS: rational equilibria, exact census, sign criteria and epidemic bound')
