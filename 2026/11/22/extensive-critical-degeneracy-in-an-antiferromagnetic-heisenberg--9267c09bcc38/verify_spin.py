"""Independent finite-size checks for the spin-half triangular-bouquet Hamiltonian.

Run: python verify_spin.py
Requires Python 3 and NumPy. The all-size theorem uses angular-momentum algebra,
not these finite matrix comparisons.
"""
from collections import Counter
from math import comb
import numpy as np


def weight(k, s):
    # Dimension of weight-s subspace of k spin-1 representations.
    total = 0
    for low in range(k + 1):
        high = low + s
        if high <= k - low:
            total += comb(k, low) * comb(k - low, high)
    return total


def predicted_eigenvalues(m, J, K):
    out = []
    for k in range(m + 1):
        for spin in range(k + 1):
            multiplicity = weight(k, spin) - weight(k, spin + 1)
            if multiplicity == 0:
                continue
            copies = comb(m, k) * multiplicity
            pair_energy = K * (k - 3 * m / 4)
            out.extend([pair_energy + J * spin / 2] * (copies * (2 * spin + 2)))
            if spin > 0:
                out.extend([pair_energy - J * (spin + 1) / 2] * (copies * 2 * spin))
    assert len(out) == 2 ** (2 * m + 1)
    return np.sort(np.asarray(out))


def direct_matrix(m, J, K):
    sites = 2 * m + 1
    dimension = 1 << sites
    matrix = np.zeros((dimension, dimension), dtype=np.float64)
    edges = []
    for i in range(m):
        a, b = 2 * i + 1, 2 * i + 2
        edges.extend([(0, a, J), (0, b, J), (a, b, K)])
    for state in range(dimension):
        for a, b, coupling in edges:
            bit_a, bit_b = (state >> a) & 1, (state >> b) & 1
            matrix[state, state] += coupling * (0.25 if bit_a == bit_b else -0.25)
            if bit_a != bit_b:
                swapped = state ^ (1 << a) ^ (1 << b)
                matrix[state, swapped] += coupling / 2
    return matrix


def expected_ground(m, J, K):
    base = -3 * m * K / 4
    return base + min(0, K - J, m * K - J * (m + 1) / 2)


def expected_degeneracy(m, J, K):
    x = K / J
    if abs(x - 0.5) < 1e-12:
        return m * 2 ** m
    if abs(x - 1.0) < 1e-12:
        return 2 * (m + 1)
    return 2 if x > 1 else 2 * m


def expected_gap(J, K):
    x = K / J
    if abs(x - 0.5) < 1e-12 or abs(x - 1) < 1e-12:
        return J / 2
    if x < 0.5:
        return J / 2 - K
    if x < 1:
        return min(K - J / 2, J - K)
    return K - J


max_error = 0.0
cases = 0
for m in (2, 3, 4):
    for K in (0.2, 0.5, 0.75, 1.0, 1.2):
        J = 1.0
        direct = np.linalg.eigvalsh(direct_matrix(m, J, K))
        predicted = predicted_eigenvalues(m, J, K)
        difference = float(np.max(np.abs(direct - predicted)))
        max_error = max(max_error, difference)
        assert difference < 2e-11, (m, K, difference)
        ground = direct[0]
        ground_count = int(np.count_nonzero(np.abs(direct - ground) < 2e-9))
        assert abs(ground - expected_ground(m, J, K)) < 2e-11
        assert ground_count == expected_degeneracy(m, J, K)
        gap = direct[ground_count] - ground
        assert abs(gap - expected_gap(J, K)) < 2e-11, (m, K, gap)
        cases += 1

for m in range(2, 11):
    assert len(predicted_eigenvalues(m, 1.0, 0.7)) == 2 ** (2 * m + 1)
print(f"PASS: {cases} independent dense-matrix full-spectrum cases; largest eigenvalue discrepancy {max_error:.3g}")
print("PASS: Hilbert-space dimension identities for m=2,...,10")
