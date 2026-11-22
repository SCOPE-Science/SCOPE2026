"""Numerical checks for additive Fourier sampling of product-one finite-field tori.
Run: python check.py  (requires numpy).  This checks finite examples only.
"""
from itertools import product
from math import comb, factorial
import cmath
import numpy as np


def fadd(q, a, b):
    return a ^ b if q == 4 else (a + b) % q


def fmul(q, a, b):
    if q != 4:
        return a * b % q
    z = 0
    for k in range(2):
        if (b >> k) & 1:
            z ^= a << k
    for k in (2,):
        if (z >> k) & 1:
            z ^= 0b111  # t^2+t+1 = 0 in GF(4)
    return z


def finv(q, a):
    return next(b for b in range(1, q) if fmul(q, a, b) == 1)


def psi(q, a):
    if q == 4:
        # trace_{F4/F2}(a) = 0 for a=0,1 and 1 for a=t,t+1
        return 1.0 if a in (0, 1) else -1.0
    return cmath.exp(2j * cmath.pi * a / q)


def expected(d, q):
    Q = q - 1
    band = [[] for _ in range(d + 1)]
    shells = [[] for _ in range(d + 1)]
    for label in product(range(Q), repeat=d - 1):
        e = (0,) + label
        counts = [e.count(r) for r in range(Q)]
        cum = 0
        for k in range(d + 1):
            numerator = 0
            for m in counts:
                b = k - (d - m)
                if 0 <= b <= m:
                    numerator += (q ** (d - m)) * comb(m, b) * (Q ** (m - b))
            assert numerator % Q == 0
            lam = numerator // Q
            shells[k].append(lam)
            cum += lam
            band[k].append(cum)
    return [sorted(a) for a in shells], [sorted(a) for a in band]


def numerical(d, q, k, j=1, band=True):
    rows = []
    for tup in product(range(1, q), repeat=d - 1):
        pro = 1
        for x in tup:
            pro = fmul(q, pro, x)
        rows.append(tup + (fmul(q, j, finv(q, pro)),))
    cols = [a for a in product(range(q), repeat=d)
            if (sum(t != 0 for t in a) <= k if band
                else sum(t != 0 for t in a) == k)]
    M = np.empty((len(rows), len(cols)), dtype=complex)
    for i, x in enumerate(rows):
        for l, a in enumerate(cols):
            v = 0
            for aa, xx in zip(a, x):
                v = fadd(q, v, fmul(q, aa, xx))
            M[i, l] = psi(q, v)
    return sorted(np.linalg.eigvalsh(M @ M.conj().T))


def run():
    cases = 0
    max_diff = 0.0
    tested_nontrivial_cosets = 0
    for q, max_d in [(2, 6), (3, 5), (4, 4), (5, 4), (7, 3)]:
        for d in range(2, max_d + 1):
            shells, bands = expected(d, q)
            Q = q - 1
            threshold = d - (d + Q - 1) // Q
            for k in range(d + 1):
                assert (min(bands[k]) > 0) == (k >= threshold)
                assert sum(v>0 for v in shells[k]) == sum(v>0 for v in bands[k])
                for band in (False, True):
                    actual = numerical(d, q, k, 1, band)
                    target = bands[k] if band else shells[k]
                    diff = max(abs(a - b) for a, b in zip(actual, target))
                    max_diff = max(max_diff, diff)
                    assert diff < 5e-9 * max(1, max(target)), (q, d, k, band, diff)
                    cases += 1
            # Sharp full-rank near-complete spectral bounds.
            k = d - 1
            a, s = divmod(d, Q)
            t_min = ((s * q ** (d - a - 1)) if s else 0) + (Q - s) * q ** (d - a)
            assert t_min % Q == 0
            lmin = (q ** d - 1) // Q
            lmax = q ** d - t_min // Q
            assert min(bands[k]) == lmin and max(bands[k]) == lmax
            if q > 2:
                assert bands[k].count(lmin) == 1
                denominator = Q
                for m in [a + 1] * s + [a] * (Q - s):
                    denominator *= factorial(m)
                multiplicity = comb(Q, s) * factorial(d) // denominator
                assert bands[k].count(lmax) == multiplicity
            if q in (3, 4, 5) and d <= 3:
                j = q - 1
                target = bands[1]
                actual = numerical(d, q, 1, j, True)
                assert max(abs(a - b) for a, b in zip(actual, target)) < 5e-9 * max(target)
                tested_nontrivial_cosets += 1
    print(f'PASS spectral_cases={cases} nontrivial_coset_cases={tested_nontrivial_cosets} maximum_absolute_error={max_diff:.5g}')

if __name__ == '__main__':
    run()
