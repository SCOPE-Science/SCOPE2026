"""Independent reproducibility checks for the area tail of three random planar lines.
Requires Python 3 and NumPy; experiments corroborate, not prove, asymptotics.
"""
import math
import numpy as np


def algebraic_area(angles, heights):
    a = np.sin(angles[..., 1] - angles[..., 2])
    b = np.sin(angles[..., 2] - angles[..., 0])
    c = np.sin(angles[..., 0] - angles[..., 1])
    return (heights[..., 0] * a + heights[..., 1] * b + heights[..., 2] * c) ** 2 / (2 * np.abs(a * b * c))


def geometric_area(angles, heights):
    normals = np.column_stack([np.cos(angles), np.sin(angles)])
    vertices = []
    for i, j in [(0, 1), (1, 2), (2, 0)]:
        vertices.append(np.linalg.solve(normals[[i, j]], heights[[i, j]]))
    x, y, z = vertices
    return abs(np.linalg.det(np.vstack([y - x, z - x]))) / 2


def sample_angles(rng, count, eta=0):
    if eta == 0:
        return rng.uniform(0, np.pi, (count, 3))
    out = np.empty(count * 3)
    pending = np.arange(count * 3)
    while len(pending):
        proposal = rng.uniform(0, np.pi, len(pending))
        accepted = rng.random(len(pending)) * (1 + abs(eta)) <= (1 + eta * np.cos(2 * proposal))
        out[pending[accepted]] = proposal[accepted]
        pending = pending[~accepted]
    return out.reshape(count, 3)


def main():
    rng = np.random.default_rng(903704)
    for _ in range(200):
        a = rng.uniform(0.05, 3.05, 3)
        h = rng.uniform(-1, 1, 3)
        x, y = algebraic_area(a, h), geometric_area(a, h)
        assert abs(x - y) < 1e-9 * max(1, y), (x, y)
    # Near-parallel asymptotic: delta * area --> (height difference)^2 / 2.
    for _ in range(60):
        a = float(rng.uniform(.3, 1.1))
        z = float(rng.uniform(2.1, 2.8))
        h = rng.uniform(-1, 1, 3)
        assert abs(1e-7 * algebraic_area(np.array([a, a + 1e-7, z]), h) - (h[0] - h[1])**2 / 2) < 1e-5
    for eta in (0, 0.8):
        n = 1_500_000
        angles = sample_angles(rng, n, eta)
        heights = rng.uniform(-1, 1, (n, 3))
        area = algebraic_area(angles, heights)
        threshold = 90.0
        measured = threshold * np.count_nonzero(area > threshold) / n
        predicted = (2 / np.pi) * (1 + eta**2 / 2)
        assert abs(measured - predicted) < 0.085 * predicted, (eta, measured, predicted)
        if eta == 0:
            mask = area > threshold
            # Mark W uses the unique closest-angle pair.
            diffs = np.abs(np.stack((angles[:, 0]-angles[:, 1], angles[:, 0]-angles[:, 2], angles[:, 1]-angles[:, 2]), axis=1))
            j = np.argmin(np.abs(np.sin(diffs[mask])), axis=1)
            dsel = diffs[mask][np.arange(np.count_nonzero(mask)), j]
            hsel = np.stack(((heights[:, 0]-heights[:, 1])**2, (heights[:, 0]-heights[:, 2])**2, (heights[:, 1]-heights[:, 2])**2), axis=1)[mask][np.arange(np.count_nonzero(mask)), j]
            w = 2 * threshold * dsel / hsel
            w = w[np.isfinite(w) & (dsel < .2)]
            assert 0.42 < np.mean(w) < .58, np.mean(w)
    # Atomic offsets: equal heights are allowed, but the heavy-tail coefficient
    # still depends only on the variance.
    a = sample_angles(rng, 1_000_000)
    h = rng.choice([-1.0, 1.0], size=(1_000_000, 3))
    measured = 100.0 * np.mean(algebraic_area(a, h) > 100.0)
    assert abs(measured - 6 / np.pi) < 0.08 * 6 / np.pi, measured
    assert algebraic_area(np.array([0.3, 1.2, 2.3]), np.zeros(3)) == 0
    assert 6 * (1 / 3) / np.pi < 6 * (1 / 3) * (1 + .8**2 / 2) / np.pi
    print('THREE_RANDOM_LINE_AREA_CHECKS_OK')

if __name__ == '__main__':
    main()
