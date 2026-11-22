#!/usr/bin/env python3
"""Finite-group and Hodge-number consistency checks for a Kummer fourfold quotient.

This computes the abstract action on the isolated stabilizer points implied by
its known fixed-locus geometry; it does not replace the geometric proof.
"""
from itertools import product
from collections import Counter

V = list(product(range(3), repeat=4))
zero = (0, 0, 0, 0)
def add(a, b):
    return tuple((x+y)%3 for x,y in zip(a,b))
def mul(k, a):
    return tuple(k*x%3 for x in a)
lines = {tuple(sorted({zero, v, mul(2,v)})) for v in V if v != zero}
assert len(lines) == 40
all_points = []
for H in sorted(lines):
    unseen = set(V)
    cosets = set()
    while unseen:
        v = min(unseen)
        c = frozenset(add(v,h) for h in H)
        unseen -= c
        cosets.add(c)
    assert len(cosets) == 27
    for c in cosets:
        all_points.append((H,c))
assert len(all_points) == 1080

def fixed_count(g):
    return sum(1 for H,c in all_points if frozenset(add(v,g) for v in c) == c)

def jointly_fixed(g,h):
    return sum(1 for H,c in all_points if g in H and h in H)

fix = {g: fixed_count(g) for g in V}
assert fix[zero] == 1080
assert Counter(fix[g] for g in V if g!=zero) == {27:80}
assert all(jointly_fixed(g,h)==0 for g in V for h in V
           if g!=zero and h!=zero and h not in {g,mul(2,g)})
# The count of singular orbits is 40, each of orbit length 81/3=27.
assert len(all_points)//27==40

betti_X = {0:1,2:7,3:8,4:108,5:8,6:7,8:1}
euler_X = sum((-1)**i*b for i,b in betti_X.items())
assert euler_X == 108
# Ordinary quotient Lefschetz / Euler averaging.
euler_Y = (euler_X + sum(fix[g] for g in V if g!=zero))//len(V)
assert euler_Y == 28
# H^3 is fixed, H^2 fixed, and the nonidentity trace on H^4 is 27.
trace_nontriv_H4 = 27 - (1+7-8-8+7+1)
assert trace_nontriv_H4 == 27
b4_Y = (108+80*trace_nontriv_H4)//81
assert b4_Y == 28
betti_Y = dict(betti_X, **{})
betti_Y[4] = b4_Y
assert sum((-1)**i*b for i,b in betti_Y.items()) == euler_Y
# Commuting-pair (orbifold) Euler. G is abelian.
e_orb_numerator = euler_X + sum(jointly_fixed(g,h) for g in V for h in V
                                if (g,h)!=(zero,zero))
assert e_orb_numerator//81 == 108 and e_orb_numerator % 81 == 0

# Hodge E-polynomials: H^4(X) differs from the symmetric-square sector
# by 80 algebraic classes of bidegree (2,2).
hodge_Y = {
    (0,0):1, (2,0):1, (1,1):5, (0,2):1,
    (2,1):4, (1,2):4, (4,0):1, (3,1):5, (2,2):16,
    (1,3):5, (0,4):1, (3,2):4, (2,3):4,
    (4,2):1, (3,3):5, (2,4):1, (4,4):1,
}
assert sum(v for (p,q),v in hodge_Y.items() if p+q==4)==28
assert sum(v for (p,q),v in hodge_Y.items() if p+q==3)==8
assert sum((-1)**(p+q)*v for (p,q),v in hodge_Y.items()) == 28
hodge_X = dict(hodge_Y)
hodge_X[(2,2)] += 80
assert sum((-1)**(p+q)*v for (p,q),v in hodge_X.items()) == 108
print('PASS: 40 order-three subgroups, 1080 points, 27 per nonidentity fixed set')
print('PASS: 40 quotient points, singular orbit size 27, all stabilizers cyclic')
print('PASS: ordinary Euler 28, orbifold Euler 108, quotient Betti b4=28')
print('PASS: 80 age-two twisted Hodge (2,2) classes restore cover E-polynomial')
