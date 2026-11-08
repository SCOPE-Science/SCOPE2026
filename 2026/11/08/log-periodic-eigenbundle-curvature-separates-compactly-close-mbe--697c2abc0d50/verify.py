#!/usr/bin/env python3
"""Finite floating-point consistency checks for the explicitly defined weighted shifts.
Not a certificate of the infinite-dimensional results.
"""
import math


def gaussian_variance(h, s, radius=70):
    center = math.floor(s)
    weights = [(n, math.exp(-h * (n - s) ** 2)) for n in range(center - radius, center + radius + 1)]
    z = sum(w for _, w in weights)
    mu = sum(n * w for n, w in weights) / z
    return sum((n - mu) ** 2 * w for n, w in weights) / z


def finite_shift_variance(h, s):
    L = h * (s - 0.5)
    assert L > 0
    logs = [(m, -2 * L * m) for m in range(75)]
    logs += [(-n, -h * n * (n - 1) + 2 * L * n) for n in range(1, max(170, math.ceil(s) + 70))]
    biggest = max(v for _, v in logs)
    weights = [(k, math.exp(v - biggest)) for k, v in logs]
    z = sum(w for _, w in weights)
    mu = sum(k * w for k, w in weights) / z
    return sum((k - mu) ** 2 * w for k, w in weights) / z


def main():
    tested = 0
    for h in (math.log(2), 1.0, 2.0, 3.0):
        assert abs(gaussian_variance(h, 0.0) - gaussian_variance(h, 1.0)) < 1e-11
        tested += 1
        assert gaussian_variance(h, 0.5) > gaussian_variance(h, 0.0)
        tested += 1
        avg = sum(gaussian_variance(h, j / 512) for j in range(512)) / 512
        assert abs(avg - 1 / (2 * h)) < 1e-11, (h, avg)
        tested += 1
        for phase in (0.0, 0.13, 0.5, 0.79, 0.99):
            s = 25 + phase
            v = finite_shift_variance(h, s)
            g = gaussian_variance(h, s)
            assert abs(v - g) < 5e-10, (h, phase, v, g)
            tested += 1
        for j in range(-30, 30):
            weight = 1 if j <= 0 else math.exp(-h * j)
            # Weighted-shift eigenfunction coefficient recursion at lambda=e^{-0.37}
            lam = math.exp(-0.37)
            def coef(i):
                if i <= 0:
                    return lam ** (-i)
                return math.exp(-h * i * (i - 1) / 2) * lam ** (-i)
            a, b = weight * coef(j), lam * coef(j + 1)
            assert abs(a - b) <= 5e-11 * max(1, abs(a), abs(b))
            tested += 1
    print('BILATERAL_CURVATURE_FINITE_CONSISTENCY_OK', tested)


if __name__ == '__main__':
    main()
