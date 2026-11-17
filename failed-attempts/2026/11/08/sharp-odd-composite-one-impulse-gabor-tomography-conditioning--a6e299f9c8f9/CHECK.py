"""Reproduce finite checks for odd-composite one-impulse Gabor conditioning.

Requires NumPy. These checks do not replace the analytic all-order proof.
"""
import math
import cmath
import numpy as np


def normalized_margin(n, z):
    denominator = n + abs(z) ** 2 + 2 * z.real
    assert denominator > 0
    cross = [abs(z + z.conjugate() * cmath.exp(2j * math.pi * ((a * b) % n) / n))
             for a in range(1, n) for b in range(1, n)]
    values = [abs(n + 2 * z.real), abs(abs(z) ** 2 + 2 * z.real)] + cross
    return min(values) / denominator


def full_lifting_singular_values(n, z):
    h = np.ones(n, dtype=complex)
    h[0] += z
    h /= np.linalg.norm(h)
    idx = np.arange(n)
    rows = []
    for a in range(n):
        for b in range(n):
            v = np.roll(h, a) * np.exp(2j * math.pi * b * idx / n)
            p = np.outer(v, v.conjugate())
            rows.append(p.T.reshape(-1))
    return np.linalg.svd(np.array(rows), compute_uv=False)


def run():
    tests = 0
    for n in (9, 15, 21, 25, 27, 33, 35, 45):
        delta = math.pi / (2 * n)
        predicted = math.sin(delta) / (math.sqrt(n) - 1)
        observed = normalized_margin(n, -math.sqrt(n))
        assert abs(observed - predicted) < 1e-11
        tests += 1
        # Independent finite-parameter, not exhaustive, corroboration.
        rng = np.random.default_rng(1000 + n)
        for _ in range(120):
            z = math.sqrt(n) * (rng.uniform(-3, 3) + 1j * rng.uniform(-3, 3))
            assert normalized_margin(n, z) <= predicted + 1e-12
            tests += 1
    n = 9
    sv = full_lifting_singular_values(n, -math.sqrt(n))
    predicted = math.sin(math.pi / (2 * n)) / (math.sqrt(n) - 1)
    assert abs(sv[0] - math.sqrt(n)) < 1e-11
    assert abs(sv[-1] / sv[0] - predicted) < 1e-11
    tests += 2
    # Composite products include zero, unlike prime nonzero-label products.
    for n in (9, 15, 21, 25, 27, 33, 35, 45):
        products = {(a * b) % n for a in range(1, n) for b in range(1, n)}
        assert products == set(range(n))
        tests += 1
    print("ODD_COMPOSITE_ONE_IMPULSE_CHECKS_PASSED", tests)


if __name__ == "__main__":
    run()
