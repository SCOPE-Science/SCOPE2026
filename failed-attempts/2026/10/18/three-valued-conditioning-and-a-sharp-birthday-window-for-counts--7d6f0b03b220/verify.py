#!/usr/bin/env python3
"""Independent finite-instance checks of the exact CountSketch compression law."""
import itertools
import math
import random
from fractions import Fraction
from collections import Counter
import numpy as np


def exact_probs(m, s):
    falling = lambda k: math.prod(range(s - k + 1, s + 1)) if s >= k else 0
    a = Fraction(falling(m), s**m)
    b = Fraction(math.comb(m, 2) * falling(m - 1), 2 * s**m)
    return (a, b, 1 - a - b)


def classify(hashes, signs):
    m = len(hashes)
    buckets = {}
    for i, h in enumerate(hashes):
        buckets.setdefault(h, []).append(i)
    if len(buckets) == m:
        return 0
    if len(buckets) < m - 1:
        return 2
    pairs = [v for v in buckets.values() if len(v) == 2]
    assert len(pairs) == 1
    i, j = pairs[0]
    return 1 if signs[i] != signs[j] else 2


def gram_eigs(hashes, signs, u):
    m = len(hashes)
    s = max(hashes) + 1
    S = np.zeros((s, m))
    for j, (h, z) in enumerate(zip(hashes, signs)):
        S[h, j] = z
    return np.linalg.eigvalsh((S @ u).T @ (S @ u))


def test_enumeration(m, s):
    u, _ = np.linalg.qr(np.eye(m)[:, :-1] - np.eye(m)[:, -1:])
    counts = Counter()
    all_signs = list(itertools.product((-1, 1), repeat=m))
    for hs in itertools.product(range(s), repeat=m):
        for zs in all_signs:
            category = classify(hs, zs)
            counts[category] += 1
            eigs = gram_eigs(hs, zs, u)
            if category == 0:
                assert np.allclose(eigs, np.ones(m - 1), atol=1e-9), (m, s, hs, zs, eigs)
            elif category == 1:
                expected = np.array([2 / m] + [1] * (m - 3) + [2])
                assert np.allclose(eigs, expected, atol=1e-9), (m, s, hs, zs, eigs)
            else:
                assert abs(eigs[0]) <= 1e-9, (m, s, hs, zs, eigs)
    total = s**m * 2**m
    probs = tuple(Fraction(counts[i], total) for i in range(3))
    assert probs == exact_probs(m, s), (m, s, probs, exact_probs(m, s))
    return total, probs


def test_preconditioned_condition(m, s, trials=300):
    rng = random.Random(m * 1000 + s)
    u, _ = np.linalg.qr(np.eye(m)[:, :-1] - np.eye(m)[:, -1:])
    full = 0
    for _ in range(trials):
        hs = [rng.randrange(s) for __ in range(m)]
        zs = [rng.choice((-1, 1)) for __ in range(m)]
        cat = classify(hs, zs)
        smat = np.zeros((s, m))
        for j, (h, z) in enumerate(zip(hs, zs)):
            smat[h, j] = z
        b = smat @ u
        if cat == 2:
            assert np.linalg.matrix_rank(b, tol=1e-9) < m - 1
        else:
            q, r = np.linalg.qr(b, mode='reduced')
            M = s + m
            a = np.concatenate([u, np.zeros((M - m, m - 1))], axis=0)
            t = a @ np.linalg.inv(r)
            observed = np.linalg.cond(t)
            expected = 1 if cat == 0 else math.sqrt(m)
            assert math.isclose(observed, expected, abs_tol=1e-8), (m, s, hs, zs, observed)
            full += 1
    return full


if __name__ == '__main__':
    exhaustive = []
    for m, s in [(4, 3), (4, 4), (4, 5), (5, 4)]:
        exhaustive.append((m, s, *test_enumeration(m, s)))
    full = sum(test_preconditioned_condition(m, s) for m in (4, 5, 6, 8) for s in (m - 1, m, m * m))
    print('EXHAUSTIVE_COUNTS', exhaustive)
    print('RIGHT_PRECONDITIONED_CONDITION_TESTS_FULL_RANK', full)
    print('VERIFICATION_OK')
