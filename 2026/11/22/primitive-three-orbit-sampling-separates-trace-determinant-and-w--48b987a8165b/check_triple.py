#!/usr/bin/env python3
"""Independent finite diagnostics for primitive three-site cyclic sampling.
Requires numpy and mpmath. Finite computations do not replace proof.
"""
import math
import numpy as np
import mpmath as mp
checks = 0
for N in (9, 18, 27, 36):
    d = N // 3
    L = 2 * np.eye(N)
    for j in range(N):
        L[j, (j - 1) % N] -= 1
        L[j, (j + 1) % N] -= 1
    for mass in (0.1, 1.0, 2.0):
        Q = L + mass * np.eye(N)
        theta = math.acosh(1 + mass / 2)
        F = lambda g: (g / math.tanh(g * theta) - 1 / math.tanh(theta)) / (2 * math.sinh(theta))
        for t in (d - 1, d + 1):
            observed = [0, t, 2 * t]
            unseen = [i for i in range(N) if i not in observed]
            block = Q[np.ix_(unseen, unseen)]
            covariance = np.linalg.inv(block)
            gaps = [t, t, N - 2 * t]
            tr = sum(F(g) for g in gaps)
            logdet = sum(math.log(math.sinh(theta) / math.sinh(g * theta)) for g in gaps)
            norm = 1 / (mass + 2 - 2 * math.cos(math.pi / max(gaps)))
            assert abs(float(np.trace(covariance)) - tr) < 1e-9
            assert abs(float(np.linalg.slogdet(covariance)[1]) - logdet) < 1e-9
            assert abs(1 / float(np.linalg.eigvalsh(block)[0]) - norm) < 1e-9
            checks += 3
mp.mp.dps = 160
for d in range(3, 61, 3):
    N = 3 * d
    ts = [t for t in range(1, N // 2 + 1) if 2 * t < N and math.gcd(t, N) == 1]
    for raw_theta in ("0.01", "0.1", "0.5", "1.25"):
        theta = mp.mpf(raw_theta)
        F = lambda g: (g * mp.coth(g * theta) - mp.coth(theta)) / (2 * mp.sinh(theta))
        A = lambda t: 2 * F(t) + F(N - 2 * t)
        D = lambda t: -2 * mp.log(mp.sinh(t * theta)) - mp.log(mp.sinh((N - 2 * t) * theta))
        E = lambda t: max(t, N - 2 * t)
        assert min(ts, key=A) == d - 1
        assert min(ts, key=D) == d - 1
        assert min(ts, key=E) == d + 1
        assert A(d - 1) < A(d + 1)
        assert D(d - 1) < D(d + 1)
        checks += 5
print("PRIMITIVE_TRIPLE_ORBIT_DIAGNOSTIC_OK", checks)
