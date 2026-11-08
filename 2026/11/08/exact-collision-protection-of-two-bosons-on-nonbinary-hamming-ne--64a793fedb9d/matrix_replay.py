"""Independent spectral diagonalization of finite Hamming collision problems.

Usage: python matrix_replay.py
Requires numpy. This is finite numerical corroboration, not an infinite proof.
"""
from fractions import Fraction
from itertools import combinations_with_replacement, product
import numpy as np


def verify_case(d, q, expected_dimension, expected_probabilities):
    vertices = list(product(range(q), repeat=d))
    n = len(vertices)
    adjacency = np.empty((n, n), dtype=float)
    for i, x in enumerate(vertices):
        for j, y in enumerate(vertices):
            adjacency[i, j] = int(sum(a != b for a, b in zip(x, y)) == 1)

    pairs = list(combinations_with_replacement(range(n), 2))
    index = {pair: k for k, pair in enumerate(pairs)}
    symmetrization = np.zeros((n * n, len(pairs)))
    for k, (i, j) in enumerate(pairs):
        symmetrization[n * i + j, k] = 1 if i == j else 2 ** -0.5
        if i != j:
            symmetrization[n * j + i, k] = 2 ** -0.5
    h_ordered = np.kron(adjacency, np.eye(n)) + np.kron(np.eye(n), adjacency)
    h = symmetrization.T @ h_ordered @ symmetrization
    values, vectors = np.linalg.eigh(h)
    diagonal_indices = [index[(i, i)] for i in range(n)]
    bright = np.zeros_like(h)
    bright_rank = 0
    for energy_index in range(2 * d + 1):
        energy = 2 * d * (q - 1) - q * energy_index
        sector = vectors[:, np.abs(values - energy) < 1e-7]
        if sector.shape[1] == 0:
            continue
        evaluation = sector[diagonal_indices, :].T
        left, singular_values, _ = np.linalg.svd(evaluation, full_matrices=False)
        rank = int(np.count_nonzero(singular_values > 1e-7))
        bright_rank += rank
        if rank:
            frame = sector @ left[:, :rank]
            bright += frame @ frame.T
    assert len(pairs) - bright_rank == expected_dimension
    assert np.linalg.norm(bright @ bright - bright, ord='fro') < 1e-7
    assert np.linalg.norm(bright - bright.T, ord='fro') < 1e-7
    assert all(abs(bright[k, k] - 1) < 1e-7 for k in diagonal_indices)
    for separation, expected in enumerate(expected_probabilities, 1):
        j = next(k for k, x in enumerate(vertices)
                 if sum(a != b for a, b in zip(x, vertices[0])) == separation)
        actual = bright[index[(0, j)], index[(0, j)]]
        assert abs(actual - float(expected)) < 1e-7, (d, q, separation, actual)
    print(f'H({d},{q}): direct symmetric-matrix rank={bright_rank}; '
          f'dark={expected_dimension}; capture matches {expected_probabilities}')


def main():
    cases = [
        (1, 3, 0, [Fraction(1)]),
        (1, 4, 2, [Fraction(2, 3)]),
        (2, 3, 14, [Fraction(13, 18), Fraction(1, 2)]),
        (2, 4, 82, [Fraction(11, 24), Fraction(2, 9)]),
        (2, 5, 242, [Fraction(33, 100), Fraction(1, 8)]),
        (3, 3, 246, [Fraction(119, 243), Fraction(127, 486), Fraction(23, 108)]),
    ]
    for args in cases:
        verify_case(*args)
    print('Independent finite spectral checks passed.')


if __name__ == '__main__':
    main()
