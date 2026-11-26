#!/usr/bin/env python3
"""Independent exact coefficient checks for an odd-mex overpartition congruence.

The two coefficient engines use (i) an enumeration by the first missing part
and (ii) a published generating series; both work over integers modulo 128.
"""
from math import isqrt

N = 300
MOD = 128


def overpart_mex_coefficients(nmax):
    total = [0] * (nmax + 1)
    max_k = 1
    while (max_k - 1) * max_k // 2 <= nmax:
        max_k += 2
    for k in range(1, max_k, 2):
        if (k - 1) * k // 2 > nmax:
            break
        dp = [0] * (nmax + 1)
        dp[0] = 1
        for m in range(1, nmax + 1):
            if m == k:
                continue
            inv = dp[:]
            for t in range(m, nmax + 1):
                inv[t] = (inv[t] + inv[t - m]) % MOD
            if m < k:  # Force positive multiplicity; two overlining choices.
                dp = [0] * m + [(2 * inv[t - m]) % MOD for t in range(m, nmax + 1)]
            else:  # Any multiplicity: 1 + 2*q^m/(1-q^m).
                dp = [(2 * inv[t] - dp[t]) % MOD for t in range(nmax + 1)]
        for n in range(nmax + 1):
            total[n] = (total[n] + k * dp[n]) % MOD
    return total


def source_series_coefficients(nmax):
    p = [0] * (nmax + 1)
    p[0] = 1
    for m in range(1, nmax + 1):
        for n in range(m, nmax + 1):
            p[n] = (p[n] + p[n - m]) % MOD
    out = [0] * (nmax + 1)
    j = 0
    while j * (2 * j + 1) <= nmax:
        shift = j * (2 * j + 1)
        degree = 2 * j + 1
        q = p[:]
        for m in range(2 * j + 2, nmax + 1):
            for n in range(nmax, m - 1, -1):
                q[n] = (q[n] + q[n - m]) % MOD
        factor = (degree * 4 ** j) % MOD
        for n in range(shift, nmax + 1):
            t = n - shift
            out[n] = (out[n] + factor * (q[t] - (q[t - degree] if t >= degree else 0))) % MOD
        j += 1
    return out


def formula(n):
    if n == 0:
        return 1
    sq = isqrt(n)
    square = sq * sq == n
    t = 2 * (1 if n % 2 == 0 else -1)
    if square:
        t -= 2 * (1 if sq % 2 == 0 else -1)
    twosquare = (n % 2 == 0 and isqrt(n // 2) ** 2 == n // 2)
    return (t + 4 * (int(twosquare) + isqrt(n - 1) + (n - 1) // 2)) % 8


if __name__ == '__main__':
    from_mex = overpart_mex_coefficients(N)
    from_gf = source_series_coefficients(N)
    assert from_mex == from_gf, [(i, from_mex[i], from_gf[i]) for i in range(N + 1) if from_mex[i] != from_gf[i]][:10]
    assert all(from_mex[n] % 8 == formula(n) for n in range(N + 1))
    assert all((from_mex[n] % 8 == 0) == (n > 0 and isqrt(n) ** 2 == n) for n in range(1, N + 1))
    assert from_mex[36] % 16 == 8, from_mex[36]
    assert from_mex[0] == 1
    print('VERIFY_OK n=0..300 first-missing-part=yes generating-function=yes exact-mod128=yes mod8_formula=yes zero_iff_square=yes square_36_mod16=8')
