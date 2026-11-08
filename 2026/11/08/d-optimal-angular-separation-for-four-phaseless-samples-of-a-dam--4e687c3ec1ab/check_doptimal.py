"""Reproducible numerical checks for four-sample damped two-mode intensity lifting.

The analytic proof is in RESULT.md; finite numerical tests are only diagnostics.
Run: python3 check_doptimal.py
"""
import math
import cmath
import random


def det_real(a):
    a = [list(map(float, row)) for row in a]
    n = len(a)
    sign = 1.0
    for j in range(n):
        p = max(range(j, n), key=lambda i: abs(a[i][j]))
        if abs(a[p][j]) < 1.e-15:
            return 0.0
        if p != j:
            a[j], a[p] = a[p], a[j]
            sign *= -1.0
        piv = a[j][j]
        sign *= piv
        for i in range(j + 1, n):
            fac = a[i][j] / piv
            for k in range(j + 1, n):
                a[i][k] -= fac * a[j][k]
            a[i][j] = 0.0
    return sign


def matrix(r, theta):
    z = cmath.rect(r, theta)
    return [[1., r**(2*k), (z**k).real, (z**k).imag] for k in range(4)]


def closed_det(r, theta):
    return r**3 * (r*r-1) * (1+r*r-2*r*math.cos(theta))**2 * math.sin(theta)


def cos_opt(r):
    s = r + 1./r
    # Stable for large s by rationalization.
    return -8. / (s + math.sqrt(s*s+96.))


def obj(r, x):
    return (1+r*r-2*r*x)**2 * math.sqrt(max(0.,1-x*x))


def main():
    rng = random.Random(20261102)
    tests = 0
    for j in range(400):
        r = math.exp(rng.uniform(-1.5, 1.5))
        th = rng.uniform(-3.0, 3.0)
        a = det_real(matrix(r, th))
        b = closed_det(r, th)
        assert abs(a-b) <= 3.e-9 * max(1.,abs(b)), (r,th,a,b)
        tests += 1
    for r in [.05, .1, .25, .5, .85, .99, 1.01, 1.25, 2., 4., 10., 20.]:
        x = cos_opt(r)
        assert -1 < x < 0
        assert abs(6*r*x*x-(1+r*r)*x-4*r)<1.e-11*max(1.,r*r)
        assert abs(x-cos_opt(1./r))<1.e-13
        assert abs(x - ((r+1./r-math.sqrt((r+1./r)**2+96))/12))<1.e-13
        tests += 4
        best = obj(r, x)
        for j in range(1001):
            y = -1 + j/500.
            assert obj(r,y) <= best*(1+1.e-13) +1.e-12
            tests += 1
    for r in [.3,.8,1.,1.2,3.]:
        for theta in [0.,math.pi]:
            assert abs(closed_det(r,theta))<1.e-12*max(1.,r**10)
            tests += 1
    for theta in [.4,1.7,2.5]:
        assert abs(closed_det(1.,theta))<1.e-14
        tests += 1
    print('DAMPED_TWO_MODE_DOPT_CHECKS_PASS',tests)


if __name__ == '__main__':
    main()
