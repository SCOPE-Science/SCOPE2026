"""Finite consistency checks for parity-sublattice value/derivative sampling.

Run with Python 3 and NumPy: python verify_bounds.py
The infinite-dimensional assertions rely on the mathematical proof, not on
these finite random or corner-fiber tests.
"""
import itertools
import math
import random
import numpy as np

PI = math.pi


def sharp_bounds(v, gain, offset):
    """The conjectured closed-form squared frame endpoints (proved separately)."""
    l1 = sum(abs(x) for x in v)
    signed_gap = min(
        abs(sum(x * e for x, e in zip(v, eps)))
        for eps in itertools.product((-1, 1), repeat=len(v))
    )
    q = offset.real ** 2 + (abs(offset.imag) + gain * PI * l1 / 2) ** 2

    def pair(z):
        trace_unscaled = 2 + 2 * q + gain * gain * PI * PI * z * z / 2
        disc = max(0, trace_unscaled ** 2 - 4 * gain ** 2 * PI ** 2 * z ** 2)
        return ((trace_unscaled - math.sqrt(disc)) / 4,
                (trace_unscaled + math.sqrt(disc)) / 4)

    return pair(signed_gap)[0], pair(l1)[1]


def local_eigenvalues(v, gain, offset, eps, center):
    m = sum(a * x for a, x in zip(v, center))
    half_delta = PI * sum(a * x for a, x in zip(v, eps)) / 2
    mat = np.array([[1, 1],
                    [offset + 1j * gain * (m - half_delta),
                     offset + 1j * gain * (m + half_delta)]],
                   dtype=complex) / math.sqrt(2)
    return np.linalg.eigvalsh(mat.conj().T @ mat)


def test():
    rng = random.Random(511)
    count = 0
    corner_count = 0
    for dim in (2, 3, 4, 5):
        for _ in range(48):
            v = np.array([rng.gauss(0, 1) for _ in range(dim)])
            v /= np.linalg.norm(v)
            gain = math.exp(rng.uniform(-2, 1.3))
            offset = complex(rng.uniform(-2, 2), rng.uniform(-2, 2))
            lower, upper = sharp_bounds(v, gain, offset)
            for _ in range(35):
                eps = [rng.choice((-1, 1)) for _ in range(dim)]
                center = [rng.uniform(-PI / 2, PI / 2) for _ in range(dim)]
                vals = local_eigenvalues(v, gain, offset, eps, center)
                assert vals[0] >= lower - 1e-9
                assert vals[1] <= upper + 1e-9
                count += 1
            # Every fiber endpoint is a limiting point of a positive-measure
            # frequency cell. Enumerate corners to test both sharp extrema.
            min_corner, max_corner = math.inf, 0.0
            for eps in itertools.product((-1, 1), repeat=dim):
                for xsign in (-1, 1):
                    center = [xsign * PI / 2 * (1 if a >= 0 else -1) for a in v]
                    vals = local_eigenvalues(v, gain, offset, eps, center)
                    min_corner = min(min_corner, vals[0])
                    max_corner = max(max_corner, vals[1])
                    corner_count += 1
            assert abs(min_corner - lower) < 1e-8
            assert abs(max_corner - upper) < 1e-8
    print('CHECK_OK random_fibers=', count, 'endpoint_fibers=', corner_count)
    gain = math.sqrt(2) / PI
    for dim in (2, 4, 7):
        v = [1.] + [0.] * (dim - 1)
        a, b = sharp_bounds(v, gain, 0j)
        assert abs(a - (1 - 1 / math.sqrt(2))) < 1e-12
        assert abs(b - (1 + 1 / math.sqrt(2))) < 1e-12
        assert abs(math.sqrt(b / a) - (1 + math.sqrt(2))) < 1e-12
    assert sharp_bounds([1 / math.sqrt(2)] * 2, gain, 0j)[0] == 0
    print('CHECK_OK minimax', a, b, math.sqrt(b / a))
    # Independent finite cyclic-torus sampling with a unitary DFT
    # checks the factor 1/sqrt(2) in the parity-lattice fiber matrix.
    n = 8
    modes = [(j, k) for j in range(n) for k in range(n)]
    sites = [(j, k) for j in range(n) for k in range(n) if (j + k) % 2 == 0]
    value = np.zeros((len(sites), len(modes)), dtype=complex)
    derivative = np.zeros_like(value)
    for i, (x, y) in enumerate(sites):
        for j, (k, l) in enumerate(modes):
            frequency = 2 * PI * (k if k < n // 2 else k - n) / n
            value[i, j] = np.exp(2j * PI * (x * k + y * l) / n) / n
            derivative[i, j] = 1j * gain * frequency * value[i, j]
    sq = np.linalg.svd(np.vstack((value, derivative)), compute_uv=False) ** 2
    assert abs(min(sq) - a) < 1e-10
    assert abs(max(sq) - b) < 1e-10
    print('CHECK_OK cyclic_torus=8x8')


if __name__ == '__main__':
    test()
