#!/usr/bin/env python3
"""Exact finite-instance ambiguity and lifting multiplicity checks for Gold graph windows.

No computer experiment is used to prove the universal theorem; this script
checks independently all Gabor ambiguity coefficients in small binary fields.
Requires Python 3 standard library. Optional NumPy checks a projector Gram matrix.
"""
from collections import Counter
from math import gcd, isqrt


def mul(a, b, m, polynomial):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= polynomial
    return out


def power(a, exponent, m, polynomial):
    out = 1
    while exponent:
        if exponent & 1:
            out = mul(out, a, m, polynomial)
        a = mul(a, a, m, polynomial)
        exponent >>= 1
    return out


def fwht(xs):
    z = xs[:]
    h = 1
    n = len(z)
    while h < n:
        for k in range(0, n, 2 * h):
            for j in range(h):
                x = z[k + j]
                y = z[k + j + h]
                z[k + j] = x + y
                z[k + j + h] = x - y
        h *= 2
    return z


def expected_counts(m, r):
    q = 1 << m
    K = 1 << gcd(m, r)
    u = m // gcd(m, r)
    out = Counter()
    out[K] += (q-1) * q**3 // K**2
    out[q] += 1
    if u & 1:
        out[isqrt(q*K)] += (q-1)*q // K
    else:
        div = (q-1) // (K+1)
        out[K*isqrt(q)] += div*q // K**2
        out[isqrt(q)] += (q-1-div)*q
    return out


def check(m, r, polynomial):
    q = 1 << m
    n = q*q
    f = [power(x, (1 << r)+1, m, polynomial) for x in range(q)]
    support = {x | (f[x] << m) for x in range(q)}
    observed = Counter()
    zero_shift = Counter()
    for a in range(q):
        for c in range(q):
            shift = a | (c << m)
            overlap = [int(z in support and ((z ^ shift) in support)) for z in range(n)]
            coefficients = fwht(overlap)
            local = Counter(abs(v) for v in coefficients)
            local.pop(0, None)
            observed.update(local)
            if a == 0 and c == 0:
                zero_shift.update(local)
    expected = expected_counts(m, r)
    assert observed == expected, (m, r, observed, expected)
    assert sum(observed.values()) <= n*n
    return q, dict(sorted(observed.items())), sum(observed.values()), zero_shift


def optional_projector_check():
    try:
        import numpy as np
    except ImportError:
        print('direct_projector_check=SKIPPED (optional NumPy unavailable)')
        return
    m, r, polynomial = 2, 1, 0b111
    q = 1 << m
    N = q*q
    f = [power(x, 3, m, polynomial) for x in range(q)]
    g = np.array([int((z >> m) == f[z & (q-1)]) for z in range(N)], dtype=float)
    # Labels of additive characters are binary-dot-product labels; all are represented.
    vectors = []
    for sh in range(N):
        tg = g[np.array([z ^ sh for z in range(N)], dtype=int)]
        for freq in range(N):
            sig = np.array([(-1)**((z & freq).bit_count() & 1) for z in range(N)])
            vectors.append(tg * sig)
    V = np.stack(vectors)
    gram = (V @ V.T)**2
    eig = np.linalg.eigvalsh(gram)
    expect = expected_counts(m, r)
    spectrum = []
    for amplitude, number in expect.items():
        spectrum.extend([N*amplitude*amplitude] * number)
    spectrum.extend([0]*(N*N-len(spectrum)))
    assert np.max(np.abs(np.sort(eig)-np.sort(spectrum))) < 1e-7
    print('direct_projector_Gram_eigenvalues_q4=PASS')


if __name__ == '__main__':
    for m, poly, rs in [(2, 0b111, [1]), (3, 0b1011, [1,2]),
                        (4, 0b10011, [1,2,3]), (5, 0b100101, [1,2])]:
        for r in rs:
            q, histogram, rank, z = check(m, r, poly)
            print('q=%d r=%d rank=%d ambiguity=%s zero_shift=%s' %
                  (q, r, rank, histogram, dict(z)))
    optional_projector_check()
    print('GOLD_GABOR_ALL_EXACT_TESTS_PASS')
