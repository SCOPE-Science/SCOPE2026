"""Finite diagnostics for logarithmic returns of polynomially scaled shifts.

Run with Python 3; no external packages. The analytic proof is separate.
"""
import math

assertions = 0

def check(condition):
    global assertions
    assert condition
    assertions += 1

alpha, epsilon, p = 0.75, 0.2, 2
ratio = ((1 - epsilon) / epsilon) ** (1 / alpha)
q_p = (1 + epsilon ** (-p)) ** (1 / (alpha * p))
check(ratio > 1)
check(10 > q_p > ratio)
for j in range(1, 9):
    n = 10 ** j
    err = sum((n / (10 ** k)) ** (alpha * p) for k in range(j + 1, 17)) ** (1 / p)
    check(err < epsilon)
    check(err <= (10 ** (alpha * p) - 1) ** (-1 / p))
q, a = 7, 0.82
check(q > ratio)
check(1 - epsilon < a < 1 + epsilon)
check(a * q ** (-alpha) < epsilon)
for j in range(1, 9):
    n = q ** j
    tail = max([a * (n / (q ** k)) ** alpha for k in range(j + 1, 17)] + [0])
    check(max(1 - a, tail) < epsilon)
    check(tail <= a * q ** (-alpha) * (1 + 1e-12))
for small in (0.1, 0.01, 0.001):
    lo = alpha * p / math.log(1 + small ** (-p))
    hi = alpha / math.log((1 - small) / small)
    check(0 < lo <= hi)
    check(lo * math.log(1 / small) < alpha + 1e-12)
    check(hi * math.log(1 / small) > alpha - 1e-12)
print(f"POLYNOMIAL_SHIFT_DIAGNOSTICS_OK {assertions}")
