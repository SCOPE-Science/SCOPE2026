"""Numerical cross-check of the half-flux three-mode norm formula.

Requires only Python's standard library. This finite test is corroborative;
the proof in RESULT.md is analytic and covers all admissible parameters.
"""
from itertools import product
from math import acos, atan2, cos, pi, sin, sqrt


def closed_norm(a, b, c):
    s = a*a + b*b + c*c
    m = max(a*a, b*b, c*c)
    if 2*m <= s:
        return sqrt(2*s)
    return sqrt(m) + sqrt(max(0.0, s-m))


def fiber_norm(a, b, c, u, v):
    # Largest eigenvalue of (aI + b exp(iu) Z + c exp(iv) X)^* times itself.
    r = a*a+b*b+c*c
    d = (a*b*cos(u))**2 + (a*c*cos(v))**2 + (b*c*sin(v-u))**2
    return sqrt(max(0.0, r+2*sqrt(max(0.0, d))))


def optimizing_phases(a, b, c):
    # Phase solution of the one-variable concave maximization, for a,b,c>0.
    aa, bb, cc = a*a*b*b, a*a*c*c, b*b*c*c
    if min(aa, bb, cc) <= 0:
        raise ValueError('Positive coefficients are required here')
    h = (a**4-b**4-c**4)/(2*b*b*c*c)
    delta = acos(min(1., max(-1., h)))
    # alpha=2u, beta=2v, with beta-alpha=delta.
    beta = -atan2(aa*sin(-delta), aa*cos(-delta)+bb)
    alpha = beta-delta
    return alpha/2, beta/2


def main():
    checked = 0
    # The continuous optimization is analytically established in the proof;
    # this grid plus stationary-point evaluation tests the implementation.
    sizes = [0.2, 0.5, 1.0, 1.4, 2.0, 3.0, 5.0]
    grid = [2*pi*j/43 for j in range(43)]
    for a, b, c in product(sizes, repeat=3):
        target = closed_norm(a,b,c)
        for u in grid:
            for v in grid:
                got = fiber_norm(a,b,c,u,v)
                assert got <= target + 2e-10, (a,b,c,u,v,target,got)
                checked += 1
        u,v = optimizing_phases(a,b,c)
        attained = fiber_norm(a,b,c,u,v)
        assert abs(attained-target) < 4e-10, (a,b,c,attained,target)
        checked += 1
    for a,b,c in [(1.,0.,2.),(0.,1.,2.),(3.,5.,0.),(0.,0.,7.),(0.,0.,0.)]:
        assert abs(closed_norm(a,b,c)-sum((a,b,c))) < 1e-12
        checked += 1
    assert abs(closed_norm(1.,1.,1.)-sqrt(6.))<1e-12
    checked += 1
    print('QUANTUM_TORUS_HALF_FLUX_OK',checked)

if __name__ == '__main__':
    main()
