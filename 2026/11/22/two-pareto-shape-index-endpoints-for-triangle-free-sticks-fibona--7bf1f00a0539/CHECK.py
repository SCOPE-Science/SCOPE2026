#!/usr/bin/env python3
"""Reproducible exact finite checks and deterministic quadrature for Pareto sticks."""
import math
from fractions import Fraction


def fibonacci(n):
    f = [0, 1, 1]
    for _ in range(3, n + 1):
        f.append(f[-1] + f[-2])
    return f


def coefficients(n):
    f = fibonacci(n)
    b = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        b[i][1] = f[i]
        if i >= 2:
            b[i][2] = f[i - 1]
        for j in range(3, i + 1):
            b[i][j] = f[i - j + 1]
    c = [Fraction(0)] + [sum((Fraction(b[i][j], f[i])
                                   for i in range(j, n + 1)), Fraction(0))
                            for j in range(1, n + 1)]
    prefactor = Fraction(math.factorial(n), math.prod(f[1:]))
    for j in range(1, n + 1):
        prefactor /= c[j]
    return f, b, c, prefactor


def reconstruct(u, n):
    x = [Fraction(0)] * (n + 1)
    x[1] = 1 + u[1]
    x[2] = x[1] + u[2]
    for i in range(3, n + 1):
        x[i] = x[i-1] + x[i-2] + u[i]
    return x


def simpson(func, steps=16000):
    assert steps % 2 == 0
    h = 1.0 / steps
    total = func(0.0) + func(1.0)
    for k in range(1, steps):
        total += (4 if k % 2 else 2) * func(h*k)
    return total * h / 3


def p3(alpha):
    # From Pareto log-spacing independence, t=exp(-2 alpha y):
    # P(A_3) = int_0^1 (1+t^(1/(2 alpha)))^(-alpha) dt.
    return simpson(lambda s: 2.0*s*(1.0 + s**(1.0/alpha))**(-alpha))


def run():
    checks = 0
    for n in range(3, 12):
        f, b, c, C = coefficients(n)
        assert C > 0 and c[1] == n
        checks += 1
        for j in range(1, n + 1):
            assert c[j] > 0 and b[j][j] == 1
            checks += 1
        for seed in range(25):
            u = [Fraction(0)] + [Fraction((17*seed + 3*j) % 29, 29)
                                  for j in range(1, n + 1)]
            x = reconstruct(u, n)
            for i in range(1, n + 1):
                assert x[i] == f[i] + sum(b[i][j]*u[j]
                                         for j in range(1, i + 1))
                assert x[i] >= f[i] + u[i]
                checks += 2
            for i in range(3, n + 1):
                assert x[i]-x[i-1]-x[i-2] == u[i]
                checks += 1
        for j in range(1, n + 1):
            u = [Fraction(0)] * (n + 1)
            x0 = reconstruct(u, n)
            u[j] = Fraction(1,137)
            x1 = reconstruct(u, n)
            assert all((x1[i]-x0[i])*137 == b[i][j]
                       for i in range(1, n+1))
            checks += 1
    assert coefficients(3)[-1] == Fraction(4,3)
    assert coefficients(4)[-1] == Fraction(108,65)
    checks += 2
    log_integral = simpson(lambda t: math.log1p(t)/t if t else 1.0)
    assert abs(log_integral - math.pi**2/12) < 1e-10
    checks += 1
    assert abs(p3(1.0) - 2*(1-math.log(2))) < 1e-9
    checks += 1
    for alpha in (10, 20, 40, 80):
        ratio = p3(alpha)/(4.0/3.0*2**(-alpha))
        assert 0.98 < ratio < 1.005
        print('large alpha',alpha,'ratio',round(ratio,12))
        checks += 1
    for alpha in (0.05, 0.02, 0.01):
        ratio = (1-p3(alpha))/(math.pi**2/6*alpha**2)
        assert 0.88 < ratio < 1.01
        print('small alpha',alpha,'ratio',round(ratio,12))
        checks += 1
    print('PASS', checks, 'finite exact or deterministic quadrature assertions')

if __name__ == '__main__':
    run()
