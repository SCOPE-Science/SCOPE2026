#!/usr/bin/env python3
"""Independent finite sanity checks for the one-erasure cyclic-chirp identities.

This script is numerical corroboration, not a proof for arbitrary prime length.
It requires only the Python standard library.
"""
from cmath import exp
from math import cos, pi, sqrt


def primes_up_to(n):
    for p in range(3, n + 1, 2):
        if all(p % d for d in range(3, int(sqrt(p)) + 1, 2)):
            yield p


def predicted(p, u, residues):
    attainable = {u * r % p for r in residues}
    nearest = min(min(r, p - r) for r in attainable)
    peak = 2 * cos(pi * nearest / p)
    energy = 2 * (p - 2)
    if p % 4 == 1:
        energy += 2 * sqrt(p) * (1 if u in residues else -1)
    return peak, energy


def direct_correlations(p, u, erased):
    c = [exp(-1j * pi * u * n * (n + 1) / p) for n in range(p)]
    c[erased] = 0j
    return [sum(c[n] * c[(n + k) % p].conjugate() for n in range(p))
            for k in range(1, p)]


def test():
    cases = 0
    for p in primes_up_to(101):
        residues = {n * n % p for n in range(1, p)}
        least_nonresidue = next((r for r in range(1, (p + 1) // 2)
                                 if r not in residues), None)
        predicted_winners = (set(range(1, p)) - residues) if p % 4 == 1 else set(range(1, p))
        measured_peaks = {}
        for u in range(1, p):
            peak, energy = predicted(p, u, residues)
            measured_peaks[u] = peak
            for erased in (0, p // 2):
                observed = direct_correlations(p, u, erased)
                formula = [-2 * exp(1j * pi * u * k * (2 * erased + 1) / p)
                           * cos(pi * u * k * k / p) for k in range(1, p)]
                assert max(abs(a - b) for a, b in zip(observed, formula)) < 1e-8, (p, u, erased)
                assert abs(max(abs(v) for v in observed) - peak) < 1e-8, (p, u)
                assert abs(sum(abs(v) ** 2 for v in observed) - energy) < 1e-7, (p, u)
                cases += 1
        best = min(measured_peaks.values())
        winning_roots = {u for u in measured_peaks if abs(measured_peaks[u] - best) < 1e-10}
        assert winning_roots == predicted_winners, p
        expected = 2 * cos(pi * (least_nonresidue if p % 4 == 1 else 1) / p)
        assert abs(best - expected) < 1e-12, p
    print('ZC_ONE_ERASURE_CHECK_PASS cyclic_cases=%d prime_range=3..101' % cases)


if __name__ == '__main__':
    test()
