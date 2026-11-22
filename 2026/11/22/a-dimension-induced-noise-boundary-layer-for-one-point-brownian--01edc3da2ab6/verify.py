"""Reproducible finite checks for one-point Brownian-sheet quadrature.

Standard library only. These are reproducibility checks, not infinite proofs.
"""
import math
import random


def root_bisect(dim, noise, iterations=100):
    assert dim >= 2 and noise >= 0
    if noise == 0:
        return 2.0 / 3.0
    low, high = 2.0 / 3.0, 1.0
    for _ in range(iterations):
        mid = (low + high) / 2.0
        f = mid ** dim * (3 * mid - 2) - 4 * noise * (1 - mid)
        if f > 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2.0


def log_info(x, noise):
    if any(z <= 0 for z in x):
        return -math.inf
    a = sum(2 * math.log(z * (1 - z / 2)) for z in x)
    v = math.prod(x)
    if v + noise <= 0:
        return -math.inf
    return a - math.log(v + noise)


def covariance_1d(x):
    # Composite Simpson integral of min(x,t), without using its formula.
    n = 4000
    h = 1.0 / n
    total = min(x, 0.0) + min(x, 1.0)
    for k in range(1, n):
        total += (4 if k % 2 else 2) * min(x, k * h)
    return total * h / 3.0


def lambert_positive(z):
    # Positive real principal W by monotone bisection.
    assert z >= 0
    left, right = 0.0, max(1.0, math.log1p(z))
    for _ in range(130):
        w = (left + right) / 2.0
        if w * math.exp(w) > z:
            right = w
        else:
            left = w
    return (left + right) / 2.0


def main():
    checks = 0
    for i in range(1, 50):
        x = i / 50
        assert abs(covariance_1d(x) - (x - x * x / 2)) < 5e-8
        checks += 1
    rng = random.Random(81423)
    for dim in (2, 3, 5, 8):
        for noise in (0, 0.0001, 0.03, 1, 9):
            root = root_bisect(dim, noise)
            score = log_info([root] * dim, noise)
            assert abs(root ** dim * (3 * root - 2) - 4 * noise * (1 - root)) < 1e-11
            for _ in range(1100):
                point = [rng.random() for _ in range(dim)]
                assert log_info(point, noise) <= score + 1e-11
                checks += 1
            if noise > 0:
                v = root ** dim
                derivative = 4 * (1 - root) / (2 - root) - v / (v + noise)
                assert abs(derivative) < 1e-10
                checks += 1
    for noise in (0.05, 1.0, 10.0):
        for dim in (200, 500, 1200):
            root = root_bisect(dim, noise)
            t = dim * (1 - root)
            target = lambert_positive(dim / (4 * noise))
            assert abs(t - target) < 0.18
            assert root > 2 / 3
            checks += 1
    for c in (0.1, 1.0, 10.0):
        y = 2 * lambert_positive(2 * c / 3) / 3
        for dim in (100, 300, 1000):
            noise = c * (2 / 3) ** dim / dim
            root = root_bisect(dim, noise)
            if noise == 0:  # Floating underflow may occur only at extreme dimensions.
                continue
            scaled_delta = dim * (root - 2 / 3)
            assert abs(scaled_delta - y) < 0.045
            checks += 1
            # Verify the logarithmic information-crossover coefficient too.
            log_h = math.log(root) + 2 * math.log1p(-root / 2)
            log_h0 = math.log(8 / 27)
            observed = -dim * (dim * (log_h - log_h0)
                               - math.log1p(noise / root ** dim))
            expected = 27 * y * y / 16 + c * math.exp(-3 * y / 2)
            assert abs(observed - expected) < 0.02
            checks += 1
    print('PASS:', checks, 'finite checks; no assertion of independent proof')


if __name__ == '__main__':
    main()
