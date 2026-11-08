"""Finite checks of the ideal-hyperbolic-polygon long-distance theorem.

Requires numpy. Simulations are corroboration, not a proof of an asymptotic statement.
"""
import math
import numpy as np


def cusp_widths(finite_vertices):
    a = np.asarray(finite_vertices, dtype=float)
    assert len(a) >= 2 and np.all(np.diff(a) > 0)
    w = np.empty(len(a), dtype=float)
    w[0] = 1.0 / (a[1] - a[0])
    w[-1] = 1.0 / (a[-1] - a[-2])
    if len(a) > 2:
        w[1:-1] = 1.0 / (a[1:-1] - a[:-2]) + 1.0 / (a[2:] - a[1:-1])
    return w, float(a[-1] - a[0])


def tail_coefficient(finite_vertices):
    a = np.asarray(finite_vertices, dtype=float)
    w, w_inf = cusp_widths(a)
    pair_sum = w_inf * w.sum()
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            pair_sum += w[i] * w[j] * (a[j] - a[i]) ** 2
    area = (len(a) - 1) * math.pi
    return float(2.0 * pair_sum / area ** 2)


def exact_uniform_ideal_polygon_points(generator, finite_vertices, number):
    """Exact area sampler: disjoint ideal-triangle decomposition at infinity."""
    a = np.asarray(finite_vertices, dtype=float)
    region = generator.integers(len(a) - 1, size=number)
    theta = (math.pi / 2.0) * generator.random(number)
    x = a[region] + (a[region + 1] - a[region]) * np.sin(theta) ** 2
    lower_y = np.sqrt((x - a[region]) * (a[region + 1] - x))
    y = lower_y / np.maximum(generator.random(number), 1.0e-14)
    return x, y


def numerical_survivals(finite_vertices, sample_size, thresholds, seed):
    generator = np.random.default_rng(seed)
    thresholds = np.asarray(thresholds, dtype=float)
    counts = np.zeros(len(thresholds), dtype=np.int64)
    block_size = 250_000
    for start in range(0, sample_size, block_size):
        count = min(block_size, sample_size - start)
        x1, y1 = exact_uniform_ideal_polygon_points(generator, finite_vertices, count)
        x2, y2 = exact_uniform_ideal_polygon_points(generator, finite_vertices, count)
        distances = np.arccosh(
            1.0 + ((x1 - x2) ** 2 + (y1 - y2) ** 2) / (2.0 * y1 * y2)
        )
        counts += np.count_nonzero(distances[:, None] > thresholds[None, :], axis=0)
    c = tail_coefficient(finite_vertices)
    for threshold, count in zip(thresholds, counts):
        p = count / sample_size
        print('vertices', list(finite_vertices), 'threshold', threshold,
              'sample_count', int(count), 'survival', format(p, '.9g'),
              'exp(t)*survival - C*t', format(math.exp(threshold)*p-c*threshold, '.6g'))
    return counts


def cusp_interval(finite_vertices, cusp_index):
    a = list(map(float, finite_vertices))
    if cusp_index == len(a):  # infinity
        return a[0], a[-1]
    k = cusp_index
    left_neighbor = a[k - 1] if k > 0 else None
    right_neighbor = a[k + 1] if k < len(a) - 1 else None
    def transformed_neighbor(z):
        return 0.0 if z is None else -1.0 / (z - a[k])
    endpoints = (transformed_neighbor(left_neighbor), transformed_neighbor(right_neighbor))
    return min(endpoints), max(endpoints)


def cusp_point(finite_vertices, cusp_index, depth, base_height):
    a = list(map(float, finite_vertices))
    lo, hi = cusp_interval(a, cusp_index)
    w = complex((lo + hi) / 2.0, base_height * math.exp(depth))
    if cusp_index == len(a):
        return w
    return a[cusp_index] - 1.0 / w


def validate_local_distance_asymptotics(finite_vertices):
    a = list(map(float, finite_vertices))
    for i in range(len(a)+1):
        for j in range(i + 1, len(a)+1):
            u, v = 5.0, 6.0
            h1, h2 = 50.0, 70.0
            z = cusp_point(a, i, u, h1)
            w = cusp_point(a, j, v, h2)
            d = math.acosh(1.0 + abs(z-w)**2 / (2.0*z.imag*w.imag))
            delta = (a[i] - a[j]) ** 2 if i < len(a) and j < len(a) else 1.0
            kappa = math.log(delta * h1 * h2)
            assert abs(d-(u+v+kappa)) < 1e-4, (i, j, d, kappa)


def main():
    assert abs(tail_coefficient([0,1])-6.0 / math.pi**2) < 1e-12
    for t in (1.25, 1.5, 2.0, 3.0, 5.0, 10.0):
        expected = 2.0 * t*t / (math.pi**2 * (t-1.0))
        assert abs(tail_coefficient([0,1,t]) - expected) < 1e-12
        assert expected >= 8.0 / math.pi**2 - 1e-12
    for vertices in ([0,1], [0,1,2], [0,1,3], [0,1,2,3]):
        validate_local_distance_asymptotics(vertices)
    for vertices, seed in (([0,1],23), ([0,1,2],29), ([0,1,3],31)):
        counts = numerical_survivals(vertices, sample_size=1_500_000,
                                      thresholds=[6.0,8.0,10.0],seed=seed)
        assert np.all(np.diff(counts) <= 0)
        # Broad numerical sanity: the finite-threshold scaled tail is consistent
        # with a nonzero limiting linear term and a bounded second term.
        c = tail_coefficient(vertices)
        for t, num in zip((6.0,8.0,10.0), counts):
            remainder = math.exp(t) * num / 1_500_000 - c * t
            assert -3.0 < remainder < 5.0
    print('IDEAL_HYPERBOLIC_POLYGON_CUSP_PAIR_TAIL_CHECKS_OK')


if __name__ == '__main__':
    main()
