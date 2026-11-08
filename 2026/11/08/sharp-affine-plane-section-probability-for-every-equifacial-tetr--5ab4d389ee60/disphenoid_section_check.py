"""Independent numerical checks for affine-plane sections of equifacial tetrahedra.

Requires numpy; run: python disphenoid_section_check.py
All random seeds are fixed. Numerical checks complement, not replace, the proof.
"""
import math
import numpy as np


def section_formula(a, b, c):
    xyz = np.array([a, b, c], dtype=float)
    q = xyz**(-2)
    q /= q.sum()
    lengths = 2.0 * np.array([math.hypot(b, c), math.hypot(a, c), math.hypot(a, b)])
    exterior = 2.0 * np.arccos(np.sqrt(q))
    return 2.0 * math.pi * lengths.sum() / (lengths @ exterior) - 3.0


def sampled_section_probability(a, b, c, n, seed):
    rng = np.random.default_rng(seed)
    vertices = np.array([[a, b, c], [a, -b, -c], [-a, b, -c], [-a, -b, c]])
    directions = rng.standard_normal((n, 3))
    directions /= np.linalg.norm(directions, axis=1)[:, None]
    projections = directions @ vertices.T
    lo = projections.min(axis=1)
    width = projections.max(axis=1) - lo
    offset = lo + rng.random(n) * width
    count = np.zeros(n, dtype=np.uint8)
    for i in range(4):
        for j in range(i + 1, 4):
            count += ((projections[:, i] - offset) * (projections[:, j] - offset) < 0)
    assert np.all((count == 3) | (count == 4))
    # Importance weighting by the intersection interval width converts
    # uniform directions to translation-rotation invariant hitting planes.
    return float(width[count == 4].sum() / width.sum())


def main():
    beta0 = math.acos(-1.0 / 3.0)
    lower = 2.0 * math.pi / beta0 - 3.0
    assert abs(section_formula(1, 1, 1) - lower) < 2e-14
    assert beta0 > math.pi * (2 - math.sqrt(2))
    shapes = [(1, 1, 1), (1, 2, 3), (1, 1, .3), (.1, .1, 1), (.01, 1, 1)]
    for k, shape in enumerate(shapes):
        predicted = section_formula(*shape)
        observed = sampled_section_probability(*shape, n=280_000, seed=1901 + k)
        assert abs(predicted - observed) < .012, (shape, predicted, observed)
        assert lower - 1e-12 <= predicted < 1
        print('shape', shape, 'predicted', f'{predicted:.9f}', 'sampled', f'{observed:.9f}')
    rng = np.random.default_rng(2026)
    samples = np.exp(rng.uniform(-9, 9, size=(100000, 3)))
    grid_min = min(section_formula(*row) for row in samples)
    assert grid_min >= lower - 1e-11
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        assert abs(section_formula(eps, eps, 1) - 1) < 30 * math.sqrt(eps)
    for b, c in [(1, 1), (1, 2), (1, 10)]:
        limit = 2 * math.hypot(b, c) / (b + c) - 1
        assert abs(section_formula(1e-7, b, c) - limit) < 2e-5
    print('AFFINE_DISPHENOID_SECTION_OK', 'random_shapes=100000', 'plane_samples=1400000', 'lower=', f'{lower:.12f}')


if __name__ == '__main__':
    main()
