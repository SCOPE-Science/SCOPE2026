#!/usr/bin/env python3
"""Independent floating-point diagnostics for a quantile-spacing theorem.

The inequalities for all parameters are established analytically in RESULT.md;
this code checks explicit quantiles, derivatives and finite parameter grids.
Only Python's standard library is needed.
"""
import math


def quantile(r, u):
    assert r > 0 and 0 < u < 1
    z = math.log(u) / r
    w = -math.expm1(z)
    return math.log(-math.log(w))


def slope(r, u):
    a = -math.log(u)
    z = a / r
    t = math.exp(-z)
    return z * t / (a * u * (-math.expm1(-z)) * (-math.log1p(-t)))


def cdf(r, x):
    return (-math.expm1(-math.exp(x))) ** r


def test():
    checks = 0
    rlist = [0.75, 1.0, 1.25, 2.0, 2.5, 4.0, 8.0, 20.0, 100.0]
    us = [1e-6, 1e-4, 1e-3, 0.005, 0.01, 0.025, 0.05, 0.1,
          0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.975,
          0.99, 0.995, 0.999, 0.9999, 1 - 1e-6]
    for r in rlist:
        for u in us:
            q = quantile(r, u)
            assert abs(cdf(r, q) - u) < 5e-11
            checks += 1
            derivative = slope(r, u)
            assert derivative > 0
            checks += 1
            h = min(u, 1-u) * 1e-4
            fd = (quantile(r, u+h) - quantile(r, u-h)) / (2*h)
            assert abs(fd/derivative - 1) < 1e-5, (r, u, fd, derivative)
            checks += 1
    for i, r in enumerate(rlist):
        for s in rlist[i+1:]:
            for u in us:
                assert slope(s, u) < slope(r, u), (r, s, u)
                checks += 1
            for i1, u in enumerate(us):
                for v in us[i1+1:]:
                    assert quantile(s, v)-quantile(s, u) < quantile(r, v)-quantile(r, u), (r,s,u,v)
                    checks += 1
    # The analytic comparison covers every real 0<r<s and 0<u<v<1,
    # whereas the machine checks below are finite stress tests only.
    print('PASS: {} finite diagnostic comparisons'.format(checks))


if __name__ == '__main__':
    test()
