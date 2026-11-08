"""Finite, reproducible checks for the dicyclic four-tap singular-spectrum theorem.

Requires Python 3 and NumPy; finite checks are not substitutes for the proof.
"""
import itertools
import collections
import math
import random
import numpy as np


def multiply(p, g, h):
    e, r = g
    f, s = h
    return e ^ f, ((-1) ** f * r + s + (p if e and f else 0)) % (2 * p)


def convolution_matrix(p, rot, other):
    group = list(itertools.product(range(2), range(2 * p)))
    indices = {g: i for i, g in enumerate(group)}
    taps = [(0, t) for t in rot] + [(1, t) for t in other]
    mat = np.zeros((4 * p, 4 * p), dtype=np.int64)
    for i, g in enumerate(group):
        for h in taps:
            mat[i, indices[multiply(p, g, h)]] += 1
    return mat


def formula_singular_values(p, rot, other):
    r = min(abs(rot[0] - rot[1]), 2 * p - abs(rot[0] - rot[1]))
    s = min(abs(other[0] - other[1]), 2 * p - abs(other[0] - other[1]))
    out = [4., 0., 2. * math.sqrt((r % 2 == 0) + (s % 2 == 0))] 
    out.append(out[-1])
    for k in range(1, p):
        ar = abs(math.cos(math.pi * k * r / (2 * p)))
        bs = abs(math.cos(math.pi * k * s / (2 * p)))
        if k % 2:
            out.extend([2 * math.hypot(ar, bs)] * 4)
        else:
            out.extend([2 * (ar + bs)] * 2)
            out.extend([2 * abs(ar - bs)] * 2)
    return np.sort(np.asarray(out))


def predicted_nullity(p, rot, other):
    r = min(abs(rot[0] - rot[1]), 2 * p - abs(rot[0] - rot[1]))
    s = min(abs(other[0] - other[1]), 2 * p - abs(other[0] - other[1]))
    resonance = (r - s) % p == 0 or (r + s) % p == 0
    return 1 + 2 * (r % 2 == 1 and s % 2 == 1) + (p - 1) * resonance + 2 * (p - 1) * (r == s == p)


def rank_mod_prime(mat, prime=1000003):
    arr = mat.copy() % prime
    rows, cols = arr.shape
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if arr[i, col]), None)
        if pivot is None:
            continue
        if pivot != rank:
            arr[[rank, pivot]] = arr[[pivot, rank]]
        arr[rank, col:] = arr[rank, col:] * pow(int(arr[rank, col]), -1, prime) % prime
        for i in range(rank + 1, rows):
            if arr[i, col]:
                arr[i, col:] = (arr[i, col:] - arr[i, col] * arr[rank, col:]) % prime
        rank += 1
        if rank == rows:
            break
    return rank


def run():
    cases = 0
    singular_comparisons = 0
    for p in (3, 5, 7):
        pairs = list(itertools.combinations(range(2 * p), 2))
        if p <= 5:
            inputs = itertools.product(pairs, pairs)
        else:
            gen = random.Random(2026)
            inputs = ((gen.choice(pairs), gen.choice(pairs)) for _ in range(200))
        counts = collections.Counter()
        for i, (rot, other) in enumerate(inputs):
            mat = convolution_matrix(p, rot, other)
            predicted = predicted_nullity(p, rot, other)
            assert 4 * p - rank_mod_prime(mat) == predicted, (p, rot, other)
            if i < 150 or p == 3:
                actual = np.sort(np.linalg.svd(mat, compute_uv=False))
                expected = formula_singular_values(p, rot, other)
                assert len(actual) == len(expected) == 4 * p
                assert np.max(np.abs(actual - expected)) < 2e-8, (p, rot, other)
                singular_comparisons += 1
            counts[predicted] += 1
            cases += 1
        if p <= 5:
            expected_counts = [
                (1, p * p * (p - 1) * (3 * p - 7)),
                (3, p * p * (p - 1) ** 2),
                (p, 6 * p * p * (p - 1)),
                (p + 2, 2 * p * p * (p - 1)),
                (3 * p, p * p),
            ]
            merged = collections.Counter()
            for nullity, number in expected_counts:
                merged[nullity] += number
            assert counts == merged, (p, counts, merged)
        print('P', p, 'CASES', sum(counts.values()), 'NULLITY_COUNTS', dict(sorted(counts.items())))
    assert cases == 2450 and singular_comparisons == 525
    print('DICYCLIC_FOUR_TAP_CHECKS_PASS', 'rank_cases', cases, 'singular_cases', singular_comparisons)


if __name__ == '__main__':
    run()
