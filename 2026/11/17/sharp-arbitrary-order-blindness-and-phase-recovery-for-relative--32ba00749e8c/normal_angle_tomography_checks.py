"""Finite, reproducible checks for a two-harmonic convex normal-sampling theorem.

The symbolic proof, valid at arbitrary coprime frequencies, is in RESULT.md;
these tests check representative frequency pairs, normalization, and geometry.
"""
from collections import defaultdict
from math import gcd, pi
import numpy as np


def zero_sum_phase_orders(p, q, max_m):
    # Each frequency factor contributes (normal Fourier mode, phase exponent).
    steps = [(0, 0), (p, 0), (-p, 0), (q, -1), (-q, 1)]
    d = {(0, 0): 1}
    data = []
    for m in range(1, max_m + 1):
        nxt = defaultdict(int)
        for (freq, exp), count in d.items():
            for k, e in steps:
                nxt[freq + k, exp + e] += count
        d = nxt
        data.append({e: c for (f, e), c in d.items() if f == 0 and e != 0})
    return data


for p, q in [(2, 3), (2, 5), (3, 4), (2, 7), (3, 5)]:
    assert gcd(p, q) == 1
    data = zero_sum_phase_orders(p, q, p + q)
    assert all(not d for d in data[:-1]), (p, q, data)
    first = data[-1]
    assert set(first) == {-p, p}, (p, q, first)
    from math import comb
    assert first[p] == first[-p] == comb(p + q, p), (p, q, first)

# Independent numerical support-function test at several phases.
for p, q in [(2, 3), (2, 5), (3, 4)]:
    a, b = 0.21, 0.14
    theta = 2 * pi * np.arange(65536) / 65536
    for phi in [0.0, 0.173, pi / p, 1.431]:
        h = 1 - a * np.cos(p * theta) / (p * p - 1) - b * np.cos(q * theta + phi) / (q * q - 1)
        rho = 1 + a * np.cos(p * theta) + b * np.cos(q * theta + phi)
        assert min(rho) >= 1-a-b-1.e-12
        A_numeric = pi * np.mean(h * rho)
        A_exact = pi * (1 - a * a / (2 * (p * p - 1)) - b * b / (2 * (q * q - 1)))
        assert abs(A_numeric - A_exact) < 1.e-11
        assert abs(2 * pi * np.mean(rho) - 2 * pi) < 1.e-11
        if p % 2 == 0 and q % 2 == 1:
            h_shift = 1 - a * np.cos(p * (theta+pi)) / (p * p - 1) - b * np.cos(q * (theta+pi) + phi) / (q * q - 1)
            width = 2 - 2 * a * np.cos(p * theta) / (p * p - 1)
            assert np.max(np.abs(h + h_shift - width)) < 1.e-12

# Direct Fourier-moment integration agrees with the purported first phase witness.
p, q, a, b, phi = 2, 5, 0.21, 0.14, 0.349
th = 2*pi*np.arange(65536)/65536
rho = 1 + a*np.cos(p*th) + b*np.cos(q*th+phi)
cp = np.mean(rho*np.exp(1j*p*th))
cmq = np.mean(rho*np.exp(-1j*q*th))
witness = cp**q * cmq**p
expect = (a/2)**q * (b/2)**p * np.exp(1j*p*phi)
assert abs(witness-expect) < 1.e-16, (witness,expect)

print('CONVEX_NORMAL_PHASE_THRESHOLD_CHECKS_OK')
