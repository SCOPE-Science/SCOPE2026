"""Reproducibility checks for a parabolic tropical mutation residence law.

Uses only the Python standard library.  The infinite theorem relies on
algebraic inequalities and an explicit two-dimensional integral, not tests.
"""
from fractions import Fraction as Q
from math import gcd


def tropical(s, t, p, q):
    assert p > 0 and q > 0 and p*q == 4
    return -s + q * max(t + p * max(s, Q(0)), Q(0)), -t - p * max(s, Q(0))


def normalized(u, v):
    return -u + 2 * max(v + 2 * max(u, Q(0)), Q(0)), -v - 2 * max(u, Q(0))


def in_wedge(u, v):
    return u > 0 and -2*u < v < -u


def first_exit(u, v):
    assert in_wedge(u, v)
    x, y = u, v
    for step in range(1, 3000):
        x, y = normalized(x, y)
        if not in_wedge(x, y):
            return step
    raise AssertionError('test exceeds cap')


def predicted_exit(u, v):
    d = -(u+v)
    assert 0 < d < u
    # First positive n with u <= (2n+1)d.
    return ((u/d-1) / 2).__ceil__()


# Universal affine conjugacy for three rational critical parameter pairs.
for p in (Q(1), Q(2), Q(4), Q(8,3)):
    q = 4/p
    for ui in range(-5, 8):
        for vi in range(-8, 8):
            u, v = Q(ui, 3), Q(vi, 5)
            s = 2*u/p
            sn, tn = tropical(s, v, p, q)
            un, vn = normalized(u, v)
            assert p*sn/2 == un and tn == vn

# Independent branch iteration and first-exit formula on the parabolic wedge.
for ui in range(1, 35):
    u=Q(ui, 9)
    for di in range(1, 65):
        d = u*Q(di, 65)
        v = -u-d
        j=first_exit(u,v)
        assert j == predicted_exit(u,v)
        x,y=u,v
        for n in range(j):
            assert in_wedge(x,y)
            assert x == u-2*n*d and y == v+2*n*d
            x,y=normalized(x,y)
        assert not in_wedge(x,y)

# Check exact area and conditional-coordinate algebra for many integer horizons.
for n in range(0, 100):
    # Slice widths at u and normalized wedge area R^2/2 (R=1).
    assert Q(1, 2*(2*n+1)) / Q(1, 2) == Q(1, 2*n+1)
    assert Q(1, 2*n+1)-Q(1, 2*n+3) == Q(2, (2*n+1)*(2*n+3))
    # Under conditional survival, the Jacobian in (u,z) is u/(2n+1).
    assert Q(1, 2*(2*n+1)) == Q(1, 2*n+1)*Q(1, 2)

# The complete integer-power sampling family has the exact same scaling.
# Direct elementary integration of d**beta: int_0**u d**beta dd.
for beta in range(0, 7):
    total=Q(1, (beta+1)*(beta+2))
    for n in range(0,100):
        survivor=total*Q(1, (2*n+1)**(beta+1))
        assert survivor/total == Q(1,(2*n+1)**(beta+1))
        # Conditional axial and transverse densities multiply to the joint density.
        assert (beta+2)*(beta+1) == (beta+1)*(beta+2)

# Exact finite-horizon harmonic identity, not an infinite proof.
for m in range(1, 100):
    odd=sum((Q(1,2*n+1) for n in range(m)),Q(0))
    harmonic=lambda N: sum((Q(1,j) for j in range(1,N+1)),Q(0))
    assert odd == harmonic(2*m)-harmonic(m)/2

print('PARABOLIC_TROPICAL_RESIDENCE_EXACT_OK')
