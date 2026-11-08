#!/usr/bin/env python3
"""Exact finite tests for a signed antipodal-bond Ising network.

Run: python3 folded_cube_verifier.py
All loops use integer arithmetic. Exhaustive spin tests are limited to d <= 4;
the accompanying mathematical proof handles arbitrary d >= 2.
"""
from itertools import product


def predicted(d, weights, k):
    minimum = min(weights)
    multiplicity = weights.count(minimum)
    t = ((-1) ** d) * k
    energy = (1 << (d - 1)) * (-sum(weights) + min(t, 2 * minimum - t))
    if t < minimum:
        choices = [(1 << d) - 1]
    elif t > minimum:
        choices = [((1 << d) - 1) ^ (1 << i) for i, w in enumerate(weights) if w == minimum]
    else:
        choices = [(1 << d) - 1] + [((1 << d) - 1) ^ (1 << i) for i, w in enumerate(weights) if w == minimum]
    spin_patterns = set()
    for mode in choices:
        mask = sum((1 << x) for x in range(1 << d) if ((x & mode).bit_count() & 1))
        spin_patterns.add(mask)
        spin_patterns.add(mask ^ ((1 << (1 << d)) - 1))
    return energy, spin_patterns


def brute(d, weights, k):
    nv = 1 << d
    es = []
    for v in range(nv):
        for i in range(d):
            w = v ^ (1 << i)
            if v < w:
                es.append((v, w, weights[i]))
        w = v ^ (nv - 1)
        if v < w:
            es.append((v, w, k))
    assert len(es) == (d + 1) * nv // 2
    best = None
    optima = set()
    for mask in range(1 << nv):
        # +1 for same spins, -1 for different spins.
        e = sum(weight if (((mask >> u) ^ (mask >> v)) & 1) == 0 else -weight for u, v, weight in es)
        if best is None or e < best:
            best, optima = e, {mask}
        elif e == best:
            optima.add(mask)
    return best, optima


def spectral_min(d, weights, k):
    values = []
    for s in range(1 << d):
        eigenvalue = sum((-w if (s >> i) & 1 else w) for i, w in enumerate(weights)) + (k if not (s.bit_count() & 1) else -k)
        values.append(eigenvalue)
    return (1 << (d - 1)) * min(values)


def test():
    cases = []
    for d, weights, ks in [
        (2, (1, 1), (-4, 0, 1, 3)),
        (2, (1, 3), (-3, 1, 2, 4)),
        (3, (1, 1, 2), (-3, -1, 0, 2)),
        (3, (1, 2, 3), (-3, -1, 0, 4)),
        (4, (1, 1, 1, 1), (-2, 0, 1, 3)),
        (4, (1, 1, 2, 2), (-2, 1, 2)),
        (4, (1, 2, 2, 3), (0, 1, 3)),
    ]:
        for k in ks:
            cases.append((d, weights, k))
    for d, weights, k in cases:
        expected, expected_set = predicted(d, weights, k)
        observed, observed_set = brute(d, weights, k)
        assert (expected, expected_set) == (observed, observed_set), (d, weights, k, expected, observed, len(expected_set), len(observed_set))
        assert spectral_min(d, weights, k) == expected
    for d in range(2, 13):
        for scale in (1, 2, 5):
            weights = tuple(scale + ((7*i + d) % 4) for i in range(d))
            for k in range(-8, 9):
                expected, _ = predicted(d, weights, k)
                assert expected == spectral_min(d, weights, k), (d, weights, k)
    print('VERIFY_OK', 'exhaustive_cases='+str(len(cases)), 'spectral_cases='+str(11*3*17), 'max_exhaustive_dimension=4')


if __name__ == '__main__':
    test()
