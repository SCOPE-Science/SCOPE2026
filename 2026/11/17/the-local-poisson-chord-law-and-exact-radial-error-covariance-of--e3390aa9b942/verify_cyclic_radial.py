#!/usr/bin/env python3
"""Reproducible checks for a Poisson-chord limit of random cyclic polygons.

Requires Python 3 standard library only. Numerical tests support, but do not
replace, the analytic convergence and renewal identities in RESULT.md.
"""
import bisect
import math
import random

PI = math.pi
LAM = 1 / (2 * PI)


def theoretical_cov(s):
    u = LAM * abs(s)
    return math.exp(-u) * (u * u / 2 + 3 * u + 3) / (4 * LAM ** 4)


def direct_integral_cov(s):
    """Numerical quadrature of two independently derived conditional cases."""
    u = LAM * abs(s)
    n = 12000
    dx = u / n
    terms = [math.exp(-u) * (u + 2) ** 2]
    integral = 0.0
    for k in range(n + 1):
        z = k * dx
        f = z * math.exp(-z) * (1 - math.exp(-(u - z)))
        integral += (1 if k in (0, n) else (4 if k % 2 else 2)) * f
    return ((terms[0] + integral * dx / 3) - 1) / (4 * LAM ** 4)


def sim_poisson(t, samples=160000, seed=202606):
    rng = random.Random(seed + int(t * 100))
    sums = [0., 0., 0., 0., 0.]
    for _ in range(samples):
        a = rng.expovariate(LAM)
        b = rng.expovariate(LAM)
        d0 = a * b / 2
        if b > t:
            dt = (a + t) * (b - t) / 2
        else:
            left = b
            while True:
                gap = rng.expovariate(LAM)
                if left + gap > t:
                    dt = (t - left) * (left + gap - t) / 2
                    break
                left += gap
        sums[0] += d0
        sums[1] += dt
        sums[2] += d0 * dt
        sums[3] += d0 ** 2
        sums[4] += dt ** 2
    mean0, meant, prod, sq0, sqt = [s / samples for s in sums]
    return prod - mean0 * meant, (mean0, meant), (sq0, sqt)


def cyclic_deficit(angles, theta):
    """Actual Euclidean radial chord intersections, not small-gap approximation."""
    n = len(angles)
    j = bisect.bisect_right(angles, theta)
    left = angles[j - 1] if j else angles[-1] - 2 * PI
    right = angles[j] if j < n else angles[0] + 2 * PI
    a = theta - left
    b = right - theta
    if a + b >= PI:
        return 1.0
    r = math.sin(a + b) / (math.sin(a) + math.sin(b))
    return 1 - r


def finite_cover_probability(n, x):
    r = 1 - x / (n * n)
    k = 8192
    d = 2 * PI / k
    avg = sum((0.5 + math.asin(r * math.sin((j + 0.5) * d)) / PI) ** (n - 1)
              for j in range(k)) / k
    return 1 - n * avg


def limit_cover_probability(x):
    bound = 30 * PI
    k = 20000
    ds = 2 * bound / k
    val = sum(math.exp(-math.sqrt(2 * x + (-bound + (j + 0.5) * ds) ** 2) / PI)
              for j in range(k)) * ds / (2 * PI)
    return 1 - val


def main():
    assert abs(theoretical_cov(0) - 12 * PI ** 4) < 1e-10
    for u in (0.25, 1., 2., 4.):
        t = u / LAM
        a = theoretical_cov(t)
        b = direct_integral_cov(t)
        assert abs(a - b) < 3e-7 * max(1, a), (u, a, b)
        c, means, _ = sim_poisson(t)
        assert abs(c - a) < 0.11 * a, (u, c, a)
        for mean in means:
            assert abs(mean - 1 / (2 * LAM ** 2)) < 0.035 * (1 / (2 * LAM ** 2))
    for x in (0.25, 1., 4., 10.):
        for n in (120, 360):
            p = finite_cover_probability(n, x)
            lim = limit_cover_probability(x)
            assert abs(p - lim) < 0.015, (n, x, p, lim)
    rng = random.Random(3522026)
    for n in (400, 1000):
        a = b = ab = 0.
        samples = 18000
        t = 2 * PI / n
        for _ in range(samples):
            angles = sorted(rng.uniform(0, 2 * PI) for __ in range(n))
            v = n * n * cyclic_deficit(angles, 0)
            w = n * n * cyclic_deficit(angles, t)
            a += v
            b += w
            ab += v * w
        empirical = ab / samples - (a / samples) * (b / samples)
        expected = theoretical_cov(2 * PI)
        assert abs(empirical - expected) < 0.16 * expected, (n, empirical, expected)
    print('PASS: conditional-renewal quadrature (4 cases), Poisson moments and covariance,')
    print('finite-sample containment quadrature (8 cases), and Euclidean chord geometry')
    print('with independent random cyclic polygons (2 sample sizes).')
    print('Mean 2pi^2 =', 2 * PI * PI, ' Var 12pi^4 =', 12 * PI ** 4)
    print('C(2pi) =', theoretical_cov(2 * PI))
    print('Bessel-type limit containment at x=1 =', limit_cover_probability(1.))

if __name__ == '__main__':
    main()
