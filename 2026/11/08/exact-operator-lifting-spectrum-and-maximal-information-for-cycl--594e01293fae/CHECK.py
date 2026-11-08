"""Reproduce the finite matrix-lifting singular spectrum for quadratic phase masks.

Run: python CHECK.py (requires numpy). All dimensions used in tests are finite;
unbounded assertions require the elementary character-orthogonality proof in RESULT.md.
"""
import collections
import itertools
import math
import numpy as np


def predicted(n, slopes):
    blocks = []
    for lag in range(n):
        modulus = n // math.gcd(n, 2 * lag)
        multiplicities = collections.Counter(s % modulus for s in slopes)
        blocks.extend(multiplicities.values())
    return sorted((math.sqrt(x) for x in blocks), reverse=True)


def direct(n, slopes, add_coordinates=False):
    j = np.arange(n)
    rows = []
    for s in slopes:
        for k in range(n):
            v = np.exp(2j * np.pi * (s * j * j + k * j) / n) / np.sqrt(n)
            P = np.outer(v, np.conj(v))
            rows.append(P.flatten().conj())
    if add_coordinates:
        for k in range(n):
            P = np.zeros((n, n), dtype=complex)
            P[k, k] = 1
            rows.append(P.flatten())
    sig = np.linalg.svd(np.array(rows), compute_uv=False)
    return sorted((float(x) for x in sig if x > 1e-8), reverse=True)


def optimum(n, r):
    return sum(min(r, n // math.gcd(n, 2 * lag)) for lag in range(n))


def objective(n, slopes):
    return len(predicted(n, slopes))

checks = 0
# Independent SVD comparisons for arbitrary slope families, odd and even dimensions.
for n in range(2, 17):
    masks = [tuple(range(r)) for r in range(1, min(4, n) + 1)]
    masks.extend([tuple(range(n)), (0, n - 1)])
    if n > 2:
        masks.append((0, 2))
    for slopes in masks:
        p = predicted(n, slopes)
        a = direct(n, slopes)
        assert len(p) == len(a), (n, slopes)
        assert max(abs(x - y) for x, y in zip(p, a)) < 2e-10, (n, slopes)
        checks += 1

# Every mask subset, not just consecutive ones, for small dimensions.
for n in range(2, 11):
    for r in range(1, n + 1):
        best = optimum(n, r)
        for slopes in itertools.combinations(range(n), r):
            z = objective(n, slopes)
            assert z <= best
            assert z == best if slopes == tuple(range(r)) else True
            checks += 1

# Coordinate basis restores precisely n-1 diagonal directions.
for n in range(2, 14):
    p = len(predicted(n, tuple(range(n)))) + n - 1
    d = len(direct(n, tuple(range(n)), add_coordinates=True))
    assert p == d
    assert (p == n * n) == (n >= 3 and all(n % t for t in range(2, math.isqrt(n) + 1)) and n % 2 != 0)
    checks += 1

# Verify the real Hermitian normalization independently of complexification.
for n in range(2, 10):
    E = []
    for j in range(n):
        H = np.zeros((n, n), dtype=complex)
        H[j, j] = 1
        E.append(H)
    for a in range(n):
        for b in range(a+1, n):
            H = np.zeros((n, n), dtype=complex)
            K = np.zeros((n, n), dtype=complex)
            H[a, b] = H[b, a] = 1 / np.sqrt(2)
            K[a, b] = 1j / np.sqrt(2)
            K[b, a] = -1j / np.sqrt(2)
            E.extend([H, K])
    for r in sorted(set([1, min(3,n), n])):
        j = np.arange(n)
        R = []
        for a in range(r):
            for k in range(n):
                v = np.exp(2j*np.pi*(a*j*j+k*j)/n)/np.sqrt(n)
                P = np.outer(v,np.conj(v))
                R.append([np.trace(P@H).real for H in E])
        actual = np.linalg.svd(np.array(R), compute_uv=False)
        actual = sorted([x for x in actual if x>1e-8], reverse=True)
        theory = predicted(n, tuple(range(r)))
        assert len(actual)==len(theory)
        assert max(abs(x-y) for x,y in zip(actual,theory))<2e-10
        checks += 1

# Exhaustive parity-saturation optimizer counts for every small even order.
for n in range(2, 13, 2):
    h = n // 2
    for r in range(h, n + 1):
        winners = sum(objective(n, slopes) == optimum(n,r)
                      for slopes in itertools.combinations(range(n),r))
        assert winners == math.comb(h, r-h) * 2**(n-r), (n,r,winners)
        checks += 1

# Check both exact balancing and minimum fourth-overlap frame potential.
for n in range(2, 31):
    for r in range(1, n + 1):
        S = list(range(r))
        for lag in range(n):
            m = n // math.gcd(n, 2 * lag)
            c = collections.Counter(s % m for s in S)
            q,t = divmod(r,m)
            assert sorted([c.get(k,0) for k in range(m)]) == [q]*(m-t)+[q+1]*t
            checks += 1

print("QUADRATIC_CHIRP_PROJECTOR_SPECTRUM_CHECKS_PASSED", checks)
