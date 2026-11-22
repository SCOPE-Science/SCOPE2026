"""Deterministic diagnostics for the planar random-section record theorem.

No external data, private provenance, or third-party libraries are required.
Finite tests are not a proof of the infinite-horizon statements.
"""
from fractions import Fraction
from itertools import permutations
from math import acos, asin, cos, pi, sin, sqrt


def simpson(f, a, b, m=10000):
    assert m % 2 == 0
    h = (b - a) / m
    v = f(a) + f(b)
    for j in range(1, m):
        v += (4 if j % 2 else 2) * f(a + h*j)
    return v*h/3


def F(t):
    return 2*asin(sqrt(t/2))/pi


def drift(h):
    return (sqrt(h*(2-h))-(1-h)*acos(1-h))/pi


# Exact angle-doubling: for each rational boundary angle phi, every one
# of m equally spaced line orientations gives exactly one point of the
# rotated uniform m-point circle grid.
for m in (7, 17, 43, 101):
    for phi in (Fraction(0), Fraction(1, 7), Fraction(53, 149)):
        observed = sorted((Fraction(2*j+1, 2*m)-phi+Fraction(1, 2)) % 1
                          for j in range(m))
        assert len(set(observed)) == m
        differences = [(observed[(i+1) % m]-observed[i]) % 1
                       for i in range(m)]
        assert all(d == Fraction(1, m) for d in differences)

# Geometric chord endpoint formula for non-tangent angles, checked
# numerically for a dense deterministic grid of angles.
for j in range(1, 51):
    phi = 2*pi*j/61
    x = (cos(phi), sin(phi))
    for k in range(1, 79):
        theta = pi*k/83
        u = (cos(theta), sin(theta))
        dot = x[0]*u[0]+x[1]*u[1]
        q = (x[0]-2*dot*u[0], x[1]-2*dot*u[1])
        target = (-cos(2*theta-phi), -sin(2*theta-phi))
        assert max(abs(q[0]-target[0]), abs(q[1]-target[1])) < 3e-14
        assert abs(q[0]*q[0]+q[1]*q[1]-1) < 4e-14

# Count record events exactly over all rank permutations for N <= 7.
for n in range(1, 8):
    perms = list(permutations(range(n)))
    for j in range(1, n+1):
        flags = [int(a[j-1] == min(a[:j])) for a in perms]
        assert sum(flags)*j == len(perms)
        for k in range(1, j):
            joint = sum(a[j-1] == min(a[:j]) and
                        a[k-1] == min(a[:k]) for a in perms)
            assert joint*j*k == len(perms)
    expected_count = sum(Fraction(1, j) for j in range(1, n+1))
    actual_count = Fraction(sum(sum(a[j-1] == min(a[:j])
                                 for j in range(1, n+1)) for a in perms), len(perms))
    assert actual_count == expected_count

# Tail integral = exact beta/trigonometric integral, and the conditional
# drift = integrated CDF. These are numerical consistency tests only.
for n in (1, 2, 3, 5, 10, 37):
    e_tail = simpson(lambda t: (1-F(t))**n, 0, 2, 200000)
    e_beta = pi*simpson(lambda u: u**n*sin(pi*u), 0, 1)
    assert abs(e_tail-e_beta) < 8e-8, (n, e_tail, e_beta)
for h in (0.001, 0.01, 0.1, 0.5, 1, 1.5, 2):
    e_direct = simpson(F, 0, h)
    assert abs(e_direct-drift(h)) < 1e-6

# Sharp asymptotic rate and drift, indicative but not exhaustive.
for n in (1000, 2000):
    e = pi*simpson(lambda u: u**n*sin(pi*u), 0, 1, 20000)
    assert abs(n*n*e/pi**2 - 1) < 0.01
for h in (1e-3, 1e-4):
    asymptotic = 2*sqrt(2)/(3*pi)*h**1.5
    assert abs(drift(h)/asymptotic-1) < 0.003

print('VERIFY_OK')
