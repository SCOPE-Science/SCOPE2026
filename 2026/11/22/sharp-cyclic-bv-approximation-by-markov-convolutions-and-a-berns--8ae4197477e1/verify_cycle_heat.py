#!/usr/bin/env python3
"""Independent numerical and exact-integer checks for finite-cycle heat/BV theorem.

Requires numpy and scipy. This finite test supports but does not replace the proof.
"""
import numpy as np
from scipy.linalg import expm


def dist(n):
    j = np.arange(n)
    return np.minimum(j, n - j)


def kernel_matrix(n, t):
    L = 2.0 * np.eye(n)
    for j in range(n):
        L[j, (j-1) % n] -= 1
        L[j, (j+1) % n] -= 1
    return expm(-t * L)


def Fourier_formula(n, t):
    ks = np.arange(1, n)
    lam = 2 - 2 * np.cos(2 * np.pi * ks / n)
    if n % 2 == 0:
        a = 1 - (-1.0) ** ks
    else:
        a = 1 - (-1.0) ** ks * np.cos(np.pi * ks / n)
    lim = (n * n // 4) / n
    return lim - (2.0/n) * np.sum((a/lam) * np.exp(-t*lam))


def tv(x):
    return sum(abs(x[i] - x[(i+1) % len(x)]) for i in range(len(x)))


exact_cuts = 0
numeric_cuts = 0
spectral_checks = 0
random_checks = 0
rng = np.random.default_rng(20261018)
for n in range(3, 13):
    d = dist(n)
    for bits in range(1, (1 << n)-1):
        x = np.array([(bits >> j) & 1 for j in range(n)], dtype=float)
        b = int(tv(x))
        runs = b // 2
        size = int(sum(x))
        for j in range(1, n):
            sep = sum(int(x[i] == 1 and x[(i + j) % n] == 0) for i in range(n))
            assert sep <= runs * min(j, n-j), (n, bits, j)
            exact_cuts += 1
            if all(sum(int(x[i] == 1 and x[(i + j) % n] == 0)
                       for i in range(n)) == runs * min(j, n-j)
                   for j in range(1, n)):
                assert b == 2 and size in (n//2, (n+1)//2), (n, bits)
    for t in (0.05, 0.37, 1.4, 4.0):
        H = kernel_matrix(n, t)
        k = float(np.dot(H[0], d))
        assert abs(k - Fourier_formula(n,t)) < 4e-10, (n,t,k)
        spectral_checks += 1
        for bits in range(1, (1 << n)-1):
            x = np.array([(bits >> j) & 1 for j in range(n)], dtype=float)
            b = tv(x)
            v = sum(abs(x-H@x))/b
            assert v <= k + 4e-10, (n,t,bits,v,k)
            if b == 2 and int(sum(x)) in (n//2, (n+1)//2):
                assert abs(v-k) <= 4e-10, (n,t,bits)
            numeric_cuts += 1
        for _ in range(100):
            x = rng.uniform(-3, 3, size=n)
            assert sum(abs(x-H@x)) <= k*tv(x) + 4e-10
            random_checks += 1
    # positive spectral coefficients imply increasing concavity analytically.
    ks = np.arange(1, n)
    coeff = (1-(-1.0)**ks) if n % 2 == 0 else (1-(-1.0)**ks*np.cos(np.pi*ks/n))
    assert all(coeff >= -1e-10) and any(coeff > 0)
general_kernel_checks = 0
for n in range(3, 10):
    for seed in (1, 3, 8):
        w = [1 + ((7*d + 3*n + seed*d*d) % 17) for d in range(n)]
        Z = sum(w)
        Cnum = sum(w[d]*min(d, n-d) for d in range(n))
        for bits in range(1, (1 << n)-1):
            x = [(bits >> i) & 1 for i in range(n)]
            b = tv(x)
            output = sum(abs(Z*x[i] - sum(w[d]*x[(i+d) % n] for d in range(n))) for i in range(n))
            assert output <= b*Cnum
            if output == b*Cnum:
                assert b == 2 and sum(x) in (n//2, (n+1)//2)
            if b == 2 and sum(x) in (n//2, (n+1)//2):
                assert output == b*Cnum
            general_kernel_checks += 1
print('EXACT_GENERAL_CIRCULANT_KERNEL_AND_RIGIDITY_PASS', general_kernel_checks)
print('EXACT_INTEGER_CUT_BOUNDS_AND_EQUALITY_PASS', exact_cuts)
print('MATRIX_EXPONENTIAL_ALL_CUT_PASS', numeric_cuts)
print('FOURIER_FORMULA_PASS', spectral_checks)
print('RANDOM_REAL_SIGNAL_PASS', random_checks)
print('CYCLE_HEAT_BV_CHECKS_PASS')
