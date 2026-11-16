#!/usr/bin/env python3
"""Finite high-precision consistency checks for a three-digit Fourier-mask theorem.

The all-base theorem is proved analytically in RESULT.md. This script checks
examples only and is not a substitute for the infinite-parameter proof.
"""
from math import gcd
import mpmath as mp

mp.mp.dps = 85
bases = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19]
checks = 0
for b in bases:
    for n in range(1, 4):
        N = b ** n
        if N > 8000:
            continue
        if b % 3 == 0:
            k = b // 3
            v = abs(1+2*mp.cos(2*mp.pi*k/b))/3
            assert v < mp.mpf('1e-75')
            checks += 1
            continue
        expected = mp.mpf(1)
        for j in range(1, n+1):
            m = b**j
            eps = 1 if m % 3 == 2 else -1
            expected *= mp.sin(mp.pi/m)/(3*mp.sin(mp.pi/3+eps*mp.pi/(3*m)))
        wins = []
        tol = mp.mpf('1e-60')
        for k in range(1, N):
            value = mp.mpf(1)
            for j in range(1, n+1):
                value *= abs(1+2*mp.cos(2*mp.pi*k/(b**j)))/3
            assert value >= expected - tol
            if abs(value-expected) < tol:
                wins.append(k)
            checks += 1
        inv = pow(3, -1, N)
        optimal = {inv, (-inv) % N}
        if b == 4 and n == 1:
            optimal.add(2)
        assert set(wins) == optimal, (b, n, wins, optimal)
print(f'PASS: {checks} mask comparisons; congruence winners and zero cases verified.')
