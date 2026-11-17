#!/usr/bin/env python3
"""Finite diagnostics for Aluthge binomial convolution and spectral homogenization."""
import cmath
import math

t = 0.37
beta = 0.8
f_period = [0.6, -0.3, 0.2]
m = sum(f_period) / len(f_period)
checks = 0

def weights(n):
    return [math.comb(n, k) * (t ** k) * ((1 - t) ** (n - k)) for k in range(n + 1)]

def measure(n, j, f):
    b = weights(n)
    return sum(b[k] * (-beta * math.log(j + k + 1) + f(j + k)) for k in range(n + 1))

for n in (10, 25, 50, 100):
    b = weights(n)
    assert abs(sum(b)-1) < 1e-10
    for j in range(31):
        f = lambda i: f_period[i % 3]
        logw = measure(n, j, f)
        alpha = sum(b[k] * f(j + k) for k in range(n + 1))
        D = j + 1 + n*t
        approx = m - beta*math.log(D) + beta*n*t*(1-t)/(2*D*D)
        assert abs(logw - approx - (alpha-m)) < 0.013
        # Exact period-three Fourier mixing makes the residual exponentially small.
        rho = max(abs(1-t+t*cmath.exp(2j*math.pi*ell/3)) for ell in (1,2))
        assert abs(alpha-m) <= 3*rho**n + 1e-10
        checks += 2

# Arbitrary irrational frequencies are damped by the same binomial characteristic function.
frequency = math.sqrt(2) - 1
for n in (5, 12, 40, 90):
    b = weights(n)
    z = sum(b[k] * cmath.exp(2j*math.pi*frequency*k) for k in range(n+1))
    expected = (1-t+t*cmath.exp(2j*math.pi*frequency))**n
    assert abs(z-expected) < 1e-9
    checks += 1
print('ALMOST_PERIODIC_ALUTHGE_DIAGNOSTICS_OK', checks)
