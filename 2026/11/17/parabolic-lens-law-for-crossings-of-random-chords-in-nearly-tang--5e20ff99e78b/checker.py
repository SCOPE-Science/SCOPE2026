"""Numerical diagnostics for chord crossings of nearly tangent equal circles.

Requires numpy and scipy; these finite checks are not a proof of any limit.
"""
import numpy as np
from scipy.special import roots_legendre


def angular_integral(delta, nodes=1200):
    v, wt = roots_legendre(nodes)
    phi = np.pi * (v + 1) / 2
    wt = wt * np.pi / 2
    radius = 1 - delta / 2
    h = 1 / np.sqrt(1 - radius**2 * np.cos(phi)**2)
    matrix = np.abs(np.sin(phi[:, None] - phi[None, :]))
    return np.einsum('i,ij,j->', wt * h, matrix, wt * h)


def crossed(a, b):
    return a[..., 0] * b[..., 1] - a[..., 1] * b[..., 0]


def sample(delta, n=3500000, seed=731):
    rng = np.random.default_rng(seed)
    count = 0
    xscaled, yscaled = [], []
    done = 0
    while done < n:
        k = min(100000, n - done)
        theta = rng.uniform(0, 2 * np.pi, (k, 4))
        points = np.stack((np.cos(theta), np.sin(theta)), axis=2)
        points[:, :2, 0] -= (2 - delta) / 2
        points[:, 2:, 0] += (2 - delta) / 2
        a, b, c, d = np.moveaxis(points, 1, 0)
        v, w = b - a, d - c
        determinant = crossed(v, w)
        transverse = c - a
        t = crossed(transverse, w) / determinant
        u = crossed(transverse, v) / determinant
        hit = (t > 0) & (t < 1) & (u > 0) & (u < 1)
        z = a[hit] + t[hit, None] * v[hit]
        xscaled.extend((z[:, 0] / delta).tolist())
        yscaled.extend((z[:, 1] / np.sqrt(delta)).tolist())
        count += np.count_nonzero(hit)
        done += k
    return count / n, np.array(xscaled), np.array(yscaled)


def main():
    target = 2 * np.pi
    values = [(e, angular_integral(e) / np.log(1 / e))
              for e in (0.002, 0.0005)]
    assert abs(values[-1][1] - target) < 0.04, values
    assert abs(values[-1][1] - target) < abs(values[0][1] - target)
    print('ANGULAR_LOGARITHM_CHECK_OK:', values, 'limit', target)

    delta = 0.02
    phat, x, y = sample(delta)
    leading = (8 / (3 * np.pi**3)) * delta**1.5 * np.log(1 / delta)
    assert 1.05 < phat / leading < 1.35, (phat, leading)
    assert len(y) > 3000, len(y)
    assert np.all(y * y + 2 * np.abs(x) < 1.02)
    assert abs(np.mean(y*y) - 0.2) < 0.035, np.mean(y*y)
    cdf = lambda t: 0.5 + 0.75 * t - 0.25 * t**3
    test_y = (-0.75, -0.5, 0.0, 0.5, 0.75)
    assert max(abs(np.mean(y <= t) - cdf(t)) for t in test_y) < 0.045
    print('CARTESIAN_INTERSECTION_AND_SCALED_LOCATION_OK:',
          {'gap':delta,'crossings':len(y),'probability':phat,'leading':leading,
           'ratio':phat/leading, 'empirical_scaled_y2':np.mean(y*y)})
    print('NEAR_TANGENT_CHORD_CHECKS_OK')


if __name__ == '__main__':
    main()
