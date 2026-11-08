#!/usr/bin/env python3
"""Supplementary finite checks for the rank-truncation Landweber covariance theorem."""
import math
from fractions import Fraction
import numpy as np


def f(k, z):
    if z <= 0:
        return 0.0
    if z >= 1:
        return 1.0
    return (-math.expm1(k * math.log1p(-z)))**2 / z


def zstar(k):
    if k == 1:
        return 1.0
    lo, hi = 0.0, 1.0  # h(u)=2k u^(k-1)-sum_{j=0}^{k-1}u^j
    for _ in range(100):
        mid = (lo+hi)/2
        h = 2*k*mid**(k-1)-sum(mid**j for j in range(k))
        if h > 0:
            hi = mid
        else:
            lo = mid
    return 1-(lo+hi)/2


def M(k):
    return f(k, zstar(k))


def check():
    assertions = 0
    assert Fraction(2, 3) * (2-Fraction(2, 3))**2 == Fraction(32, 27)
    assertions += 1
    for k in (1, 2, 3, 4, 6, 10, 30, 100, 400):
        z = zstar(k)
        m = M(k)
        assert 0 < z <= 1 and m >= 1-1e-12
        assertions += 1
        if k > 1:
            assert f(k, min(1, z + min(z/20, .001))) <= m + 1e-10
            assert f(k, max(0, z - min(z/20, .001))) <= m + 1e-10
            assertions += 2
        for n in (2, 3, 4, 9, 17):
            for trial in range(90):
                rng = np.random.default_rng(1789+ k*1000+n*200+trial)
                levels = np.sort(rng.uniform(0, 1, size=n))[::-1]
                levels[0] = 1
                weights = np.array([f(k, float(x)) for x in levels])
                for r in range(1, n):
                    top_err = float(np.max(weights[r:]))
                    best_err = float(np.sort(weights)[::-1][r])
                    assert top_err <= m*best_err + 8e-12, (k,n,r,levels,top_err,best_err,m)
                    assertions += 1
        if k >= 2:
            for r in (1, 2, 5, 20):
                spectrum = np.array([1.0]*r+[z])
                w = np.array([f(k,x) for x in spectrum])
                err_top = w[-1]
                err_star = float(np.sort(w)[0])
                assert abs(err_top/err_star-m) < 1e-9
                assertions += 1

    rng = np.random.default_rng(8448)
    for k in (1, 2, 3, 4, 8, 20):
        for _ in range(20):
            vals = rng.uniform(.0005, 1.0, 3)
            A = np.diag(np.sqrt(vals))
            B = A.T @ A
            G = np.eye(3)-B
            H = np.zeros((3, 3))
            P = np.eye(3)
            for _ in range(k):
                H += P @ A.T
                P = P @ G
            C = H @ H.T  # white-noise covariance, omega=1, sigma=1
            C_spectral = np.diag([f(k, float(x)) for x in vals])
            assert np.allclose(C,C_spectral,rtol=3e-10,atol=3e-12)
            assertions += 1

    t = 1.2564312086261697
    c = (1-math.exp(-t))**2/t
    assert abs(math.exp(t) - 1 - 2*t)<1e-12
    assert abs(c-0.40726437758907374)<1e-12
    assertions += 2
    for k in (100, 300, 1000):
        assert abs(k*zstar(k)-t) < 3.0/k
        assert abs(M(k)/k-c) < 2.0/k
        assertions += 2
    print('PASS:', assertions, 'supplementary deterministic assertions')
    print('K=2: z*=',zstar(2),'M=',M(2),'exact M=32/27')
    print('K=1000: Kz*=',1000*zstar(1000),'M/K=',M(1000)/1000)
    print('asymptotic: t*=',t, 'c*=',c)


if __name__ == '__main__':
    check()
