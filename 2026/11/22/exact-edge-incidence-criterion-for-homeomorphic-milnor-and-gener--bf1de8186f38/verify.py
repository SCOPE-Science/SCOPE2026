#!/usr/bin/env python3
"""Exact checks and finite illustrations for an interval gap homeomorphism.

The infinite-topology argument is in RESULT.md, not inferred from this script.
Only Python standard-library modules are required.
"""
from fractions import Fraction as Q
from decimal import Decimal, getcontext


def h(u, mode):
    if mode == 'two':
        return u + Q(1, 2) * u * (1-u) * (u-Q(1, 2))
    if mode == 'left':
        return u - Q(1, 2) * u * (1-u)
    if mode == 'right':
        return u + Q(1, 2) * u * (1-u)
    raise ValueError(mode)

for mode in ('two', 'left', 'right'):
    assert h(Q(0), mode) == 0 and h(Q(1), mode) == 1
    grid = [Q(i, 60) for i in range(61)]
    assert all(h(a,mode) < h(b,mode) for a,b in zip(grid,grid[1:]))
    assert all(Q(0) <= h(a,mode) <= Q(1) for a in grid)

assert h(Q(1,2),'two') == Q(1,2)
for u in (Q(1,8),Q(1,4),Q(3,8)):
    assert h(u,'two') < u
for u in (Q(5,8),Q(3,4),Q(7,8)):
    assert h(u,'two') > u
for u in (Q(1,4),Q(1,2),Q(3,4)):
    assert h(u,'right') > u > h(u,'left')
# The derivative of 'two' is 3/4 + (3/2)*u - (3/2)*u*u,
# with minimum 3/4 at endpoints and maximum 9/8 at u=1/2.
assert min(Q(3,4),Q(9,8)) == Q(3,4)
assert Q(3,4)+Q(3,2)*Q(1,2)-Q(3,2)*Q(1,4) == Q(9,8)
# 'left' and 'right' have derivative intervals [1/2,3/2].

# Reproducible finite calculation for K={1/4,3/4}.
getcontext().prec=60
K1=Decimal(1)/4
K2=Decimal(3)/4

def apply(x):
    if x in (Decimal(0),K1,K2,Decimal(1)):
        return x
    if x<K1:
        a,b,mode=Decimal(0),K1,'right'
    elif x<K2:
        a,b,mode=K1,K2,'two'
    else:
        a,b,mode=K2,Decimal(1),'left'
    u=(x-a)/(b-a)
    if mode=='two':
        v=u+Decimal('0.5')*u*(1-u)*(u-Decimal('0.5'))
    elif mode=='right':
        v=u+Decimal('0.5')*u*(1-u)
    else:
        v=u-Decimal('0.5')*u*(1-u)
    return a+(b-a)*v

for start, target in [('0.0625', K1),('0.40',K1),('0.60',K2),('0.90',K2)]:
    z=Decimal(start)
    for _ in range(200):
        z=apply(z)
    assert abs(z-target)<Decimal('1e-9'), (start,z,target)

# Edge-cover examples: lists of vertex sets representing essential edge closures.
# A graph has a realizable finite vertex subset precisely when it hits all closures.
def hits_all(A,edges):
    return all(bool(set(A)&set(e)) for e in edges)
assert hits_all({'center'},[{'center','a'},{'center','b'},{'center','c'}])
assert not hits_all({'a'},[{'center','a'},{'center','b'},{'center','c'}])
assert hits_all({'v'},[{'v','w'},{'v','w'},{'v','w'}])
assert not hits_all({'w'},[{'w','p'},{'p','q'}])
print('PASS: exact polynomial identities, monotonicity signs, finite trajectories, and sample edge obstructions')
print('LIMIT: finite checks do not prove the general compact-graph classification')
