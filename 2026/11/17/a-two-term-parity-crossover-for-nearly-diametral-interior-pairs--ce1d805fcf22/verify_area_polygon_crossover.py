"""Independent quadrature and finite-polygon checks for a near-diameter area-pair law.

Run: python verify_area_polygon_crossover.py
Dependencies: numpy, scipy. Numerical agreement is not a proof of asymptotics.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.stats import qmc


def h(x):
    v = np.mod(x, 1.0)
    return v * (1.0 - v) / 2.0


def k(x):
    a = np.mod(x, 1.0) - 0.5
    return -5.0 * a**4 / 24.0 + a**2 / 16.0 - 1.0 / 384.0


def profiles(t, sigma, nu=150, nw=1400):
    uu, uw = leggauss(nu)
    ww, wweights = leggauss(nw)
    u = (uu + 1.0) / 2.0
    uw = uw / 2.0
    w = ww * 2.0 * math.sqrt(t)
    wweights = wweights * 2.0 * math.sqrt(t)
    hs = h(u[:, None]) + h(u[:, None] + sigma + w[None, :])
    ks = k(u[:, None]) + k(u[:, None] + sigma + w[None, :])
    W = w[None, :]
    B = np.maximum(t - hs - W**2 / 4.0, 0.0)
    Q = t * W**2 / 8.0 - 5.0 * W**4 / 192.0 - ks
    first = B**2
    second = B**2 / 3.0 + 2.0 * B * Q - hs * B**2 - 2.0 * B**3 / 3.0
    return (float(np.einsum('i,ij,j->', uw, first, wweights)),
            float(np.einsum('i,ij,j->', uw, second, wweights)))


def finite_polygon_integral(n, t, m=19):
    """Sobol integrate the exact 4D polar event (not a Taylor distance)."""
    delta = 2.0 * math.pi / n
    area = n * math.sin(delta) / 2.0
    sigma = 0.0 if n % 2 == 0 else 0.5
    points = qmc.Sobol(d=4, scramble=False).random_base2(m)
    u = points[:, 0]
    W = 2.0 * math.sqrt(t) + 2.0 * delta**2 * t**1.5
    w = (2.0 * points[:, 1] - 1.0) * W
    z1, z2 = t * points[:, 2], t * points[:, 3]
    r1, r2 = 1.0 - delta**2 * z1, 1.0 - delta**2 * z2

    def boundary(v):
        return np.cos(delta / 2.0) / np.cos(delta * (np.mod(v, 1.0) - 0.5))

    inside = ((r1 > 0) & (r2 > 0) & (r1 <= boundary(u))
              & (r2 <= boundary(u + sigma + w)))
    distance_squared = ((r1 - r2)**2
                        + 4.0 * r1 * r2 * np.cos(delta * w / 2.0)**2)
    valid = inside & (distance_squared > (2.0 - delta**2 * t)**2)
    scaled = (2.0 * math.pi**2 / area**2) * (2.0 * W * t**2) * np.mean(valid * r1 * r2)
    return float(scaled)


def run():
    assert abs(k(0.0)) < 1e-14
    assert abs(k(0.5) + 1.0/384.0) < 1e-14
    for t in (0.004, 0.008):
        f, _ = profiles(t, 0.0)
        assert abs(f / (4.0 * t**4 / 3.0) - 1.0) < 0.03
    for t in (0.069, 0.073):
        f, _ = profiles(t, 0.5)
        assert abs(f / ((128.0 / 27.0) * (t - 0.0625)**4) - 1.0) < 0.04
    assert profiles(0.0625, 0.5)[0] < 1e-13
    for sigma in (0.0, 0.5):
        f, _ = profiles(100.0, sigma)
        assert abs(f / ((32.0 / 15.0) * 100.0**2.5) - 1.0) < 0.01

    comparisons = 0
    for n, t in ((31, 3.0), (32, 3.0), (63, 3.0), (64, 3.0),
                 (31, 8.0), (32, 8.0), (63, 8.0), (64, 8.0)):
        sigma = 0.0 if n % 2 == 0 else 0.5
        delta = 2.0 * math.pi / n
        f, j = profiles(t, sigma)
        exact = finite_polygon_integral(n, t)
        first_err = abs(exact - f)
        second_err = abs(exact - f - delta**2 * j)
        assert abs(exact / f - (1.0 + delta**2 * j / f)) < 0.008, (n, t, exact, f, j)
        assert second_err < first_err, (n, t, first_err, second_err)
        comparisons += 1
        print(f'n={n:3d} t={t:g} integral={exact:.9f} '
              f'leading={f:.9f} two_term={f+delta**2*j:.9f}')
    print(f'AREA_POLYGON_PARITY_TWO_TERM_OK comparisons={comparisons}')


if __name__ == '__main__':
    run()
