"""Independent finite checks for a reciprocal-quadratic Hausdorff witness theorem.

Uses exact rational alternating differences and floating phase signs. This
checks finite instances only; the written analytic proof handles all orders.
"""
from fractions import Fraction
from math import atan, pi, exp, log


def parameters(u, v):
    u, v = Fraction(u), Fraction(v)
    b = 1 / (u*u + v*v)
    a = 2*u*b
    return a, b


def difference(a, b, n, k):
    values = [1 / (1 + a*j + b*j*j) for j in range(n, n+k+1)]
    for _ in range(k):
        values = [values[j]-values[j+1] for j in range(len(values)-1)]
    return values[0]


def theta(u, v, n, k):
    return sum(atan(float(v)/(float(u)+n+j)) for j in range(k+1))


def first_index(u, v, upper=300_000):
    s = 0.0
    for k in range(upper):
        s += atan(float(v)/(float(u)+k))
        if s > pi:
            return k, s
    raise ValueError('Search bound exceeded')


checks = 0
for u, v in [(Fraction(1), Fraction(1)), (Fraction(1), Fraction(2)),
             (Fraction(1), Fraction(3)), (Fraction(2), Fraction(1)),
             (Fraction(1, 2), Fraction(1)), (Fraction(1), Fraction(2, 1)),
             (Fraction(3, 2), Fraction(2, 3))]:
    a,b = parameters(u,v)
    assert 1+a*0+b*0 == 1
    for n in range(5):
        for k in range(16):
            d = difference(a,b,n,k)
            ph = theta(u,v,n,k)
            # Exclude numerical phase zeros, none occur in these tests.
            assert abs(ph/pi-round(ph/pi)) > 1e-8
            assert (d > 0) == (__import__('math').sin(ph) > 0), (u,v,n,k)
            checks += 1

for u,v,expect in [(1,1,16),(1,Fraction(3,4),43),
                   (1,Fraction(1,2),328),(2,1,36),
                   (Fraction(1,2),1,8),(1,2,4)]:
    K, phase = first_index(u,v)
    assert K == expect, (u,v,K,expect)
    assert phase > pi
    assert phase-atan(float(v)/(float(u)+K)) <= pi
    a,b = parameters(Fraction(u), Fraction(v))
    assert difference(a,b,0,K) < 0
    checks += 4

# Near-critical growth in the predicted logarithmic scale. For u=1,
# psi(1) is minus Euler's constant; this is a coarse asymptotic sanity check.
euler = 0.5772156649015328606
for v in [0.5, 0.4, 0.3, 0.25]:
    K, _ = first_index(1, v)
    discrepancy = log(K) - pi/v + euler
    assert abs(discrepancy) < 2*v*v, (v,K,discrepancy)
    checks += 1

print('RECIPROCAL_QUADRATIC_WITNESS_FINITE_OK', checks)
