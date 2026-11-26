"""Finite, reproducible checks for the rational-map basin theorem.
These are sanity checks; the infinite-time conclusions are proved analytically.
"""
from fractions import Fraction as F
from math import log, isfinite


def step(q, y, u):
    return y + u, u * (1 - q/(1+y*y))

# Exact algebraic identities for the normalized rational map.
exact = 0
for q in [F(1, 4), F(1,2), F(3,4), F(1)]:
    for y in [F(1,3),F(1),F(2),F(7,2)]:
        for u in [F(1,4),F(1),F(5,2)]:
            Y,U=step(q,y,u)
            assert Y-y == u
            assert u-U == q*u/(1+y*y)
            assert 0 < U < u
            assert Y>y
            if q==1:
                v=y*u
                assert Y*U-1 == (v-1)*(1+v/(1+y*y))
            exact += 1

# The endpoint q=1 has an exact invariant critical graph u=1/y.
y,u=F(1),F(1)
for n in range(8):
    assert y*u==1
    Y,U=step(F(1),y,u)
    assert Y*Y-y*y==2+1/(y*y)
    y,u=Y,U

# Finite rational capture/escape certificates with strictly safe rational bounds.
# For capture: u<q/(1+(y+1)^2) makes the strip y<y+1 forward invariant.
q,y,u=F(1),F(1),F(1,2)
for n in range(12):
    if u < q/(1+(y+1)**2):
        capture_n=n
        break
    y,u=step(q,y,u)
else: raise AssertionError('capture certificate missing')

# For escape: u*(1-q/(1+y^2))>q/y implies positive limit speed,
# since atan(1/y)<1/y and left-rectangle Riemann error is bounded by u/(1+y^2).
q,y,u=F(1),F(1),F(3)
assert u*(1-q/(1+y*y)) > q/y

# Weak-damping test: for q=1 and any y>0, the exact critical initial value is 1/y.
for y in [F(1,3),F(1,2),F(1),F(2),F(5)]:
    u=1/y
    for _ in range(4):
        assert y*u==1
        y,u=step(F(1),y,u)

# Non-certifying asymptotic consistency for the q=1 critical trajectory.
y=1.0
for n in range(1,200001):
    y += 1/y
    assert isfinite(y)
    if n==100000: first_residual=y*y-2*n
second_residual=y*y-400000
assert abs((second_residual-first_residual)-0.5*log(2))<0.001
print('PASS: 48 exact local parameter identities, invariant graph, two rational certificates, five exact critical trajectories, and logarithmic scaling diagnostic')
print('captured initial (q,y,u)=(1,1,1/2) certified after',capture_n,'steps')
print('critical squared-height logarithmic increment=',second_residual-first_residual,'expected=',0.5*log(2))
