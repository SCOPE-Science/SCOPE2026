#!/usr/bin/env python3
"""Finite regression checks for the sharp all-orientation Parry spectral law."""
from itertools import product
from math import sqrt
import numpy as np

for n in range(3, 13):
    count = 0
    for word in product((-1, 1), repeat=n):
        u = np.zeros(n, dtype=int)
        v = np.zeros(n, dtype=int)
        A = B = 0
        for j in range(1, n):
            if word[j - 1] == -1 and word[j] == 1:
                u[j] = 1
                A += 1
            if word[j - 1] == 1 and word[j] == -1:
                v[j] = 1
                B += 1
        M = np.ones((n, n), dtype=int)
        M[:, 0] -= u
        M[:, -1] -= v
        assert np.min(M @ M) > 0
        eig = sorted(np.linalg.eigvals(M.astype(float)), key=abs, reverse=True)
        assert abs(eig[0].imag) < 1e-7
        assert n - 1 - 1e-7 <= eig[0].real <= n + 1e-7
        assert max(abs(z) for z in eig[1:]) <= 1 + 1e-7
        last_mp = int(word[-2] == -1 and word[-1] == 1)
        last_pm = int(word[-2] == 1 and word[-1] == -1)
        for z in eig:
            if abs(z) > 1e-5:
                q = z**3 - (n - last_pm)*z**2 + (A+B-n*last_pm)*z + (A*last_pm-B*last_mp)
                assert abs(q) < 1e-4
        count += 1
    assert count == 2**n
    sharp_word = (1,)*(n-1)+(-1,)
    d = sqrt((n-1)*(n+3))
    lam = ((n-1)+d)/2
    rate = (n-1)/(lam*lam)
    assert np.isclose(rate, (d-(n-1))/(d+(n-1)))
    if n >= 10:
        assert n*rate < 1.1
    print('n=', n, 'orientations=', count, 'sharp_rate=', format(rate, '.12g'))
print('All finite regression checks passed.')
