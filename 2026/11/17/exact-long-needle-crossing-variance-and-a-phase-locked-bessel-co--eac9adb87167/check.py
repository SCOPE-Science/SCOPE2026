"""Independent numerical checks for a long-needle rectangular-grid crossing law."""
from math import acos, asin, cos, floor, pi, sin, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import j0


def angular_coefficient(a, b):
    return (0.5 - 4 / pi**2) * (a**-2 + b**-2) + (2 / pi - 8 / pi**2) / (a * b)


def bessel_variance(length, a, b, count=30000):
    k = np.arange(1, count + 1, dtype=float)
    correction = np.sum((j0(2 * pi * k * length / a) +
                         j0(2 * pi * k * length / b)) / k**2)
    return (angular_coefficient(a, b) * length**2 + 1 / 3
            - correction / pi**2)


def conditional_shift_variance(x):
    fraction = x - floor(x)
    return fraction * (1 - fraction)


def independent_quadrature(length, a, b):
    # Exact breakpoints for the changes of the integer part of each projection.
    cut = [0.0, pi / 2]
    cut += [acos(k * a / length) for k in range(1, int(length / a) + 1)
            if k * a < length]
    cut += [asin(k * b / length) for k in range(1, int(length / b) + 1)
            if k * b < length]
    cut = sorted(set(cut))
    contribution = 0.0
    for low, high in zip(cut[:-1], cut[1:]):
        contribution += quad(
            lambda theta: (
                conditional_shift_variance(length * cos(theta) / a) +
                conditional_shift_variance(length * sin(theta) / b)),
            low, high, epsabs=2e-12, epsrel=2e-12)[0]
    return angular_coefficient(a, b) * length**2 + 2 * contribution / pi


def independent_simulation(length, a, b, size, seed):
    rng = np.random.default_rng(seed)
    theta = rng.uniform(0, 2 * pi, size)
    startx = rng.random(size)
    starty = rng.random(size)
    # Count grid-lines crossed using the two actual endpoints.
    endx = startx + length * np.cos(theta) / a
    endy = starty + length * np.sin(theta) / b
    crossings = (np.abs(np.floor(endx) - np.floor(startx)) +
                 np.abs(np.floor(endy) - np.floor(starty)))
    return float(np.mean(crossings)), float(np.var(crossings))


def main():
    cases = [(0.35, 1.0, 1.0), (0.9, 1.0, 2.0),
             (1.0, 1.0, 1.0), (2.2, 1.0, 1.0),
             (4.4, 1.0, 2.0), (12.7, 1.0, 1.7),
             (20.0, 1.0, 1.0)]
    for length, a, b in cases:
        exact = bessel_variance(length, a, b)
        direct = independent_quadrature(length, a, b)
        assert abs(exact - direct) < 1e-7, (length, a, b, exact, direct)
        if length <= min(a, b):
            mean = 2 * length / pi * (1 / a + 1 / b)
            short = mean + 2 * length**2 / (pi * a * b) - mean**2
            assert abs(exact - short) < 1e-7
    for length, a, b, seed in [(0.6, 1, 1, 22), (2.2, 1, 1, 41),
                                (4.4, 1, 2, 72), (9.3, 2, 1, 99)]:
        mean, var = independent_simulation(length, a, b, 500_000, seed)
        expected_mean = 2 * length / pi * (1 / a + 1 / b)
        expected_var = independent_quadrature(length, a, b)
        assert abs(mean - expected_mean) < 0.04, (mean, expected_mean)
        assert abs(var - expected_var) < max(0.02, 0.02 * expected_var), (var, expected_var)
    z = np.arange(1, 100000, dtype=float)
    for m in (10, 50, 100):
        for shift in (0, 0.5):
            length = m + shift
            actual = sqrt(length) * (
                bessel_variance(length, 1, 1) - angular_coefficient(1, 1) * length**2 - 1 / 3)
            predicted = -(2 / pi**3) * np.sum(np.cos(2*pi*z*shift-pi/4) / z**2.5)
            assert abs(actual - predicted) < 0.0002, (length, actual, predicted)
            print(f'length={length:g}, rescaled={actual:+.9f}, limit={predicted:+.9f}')
    print('LONG_BUFFON_GRID_VARIANCE_OK')


if __name__ == '__main__':
    main()
