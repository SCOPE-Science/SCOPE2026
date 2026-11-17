"""Reproduce analytic identity checks and Monte Carlo tests for the Brocard law.

Run: python check_brocard.py
Only Python's standard library is required. Numerical tests corroborate, not prove,
the full analytic change-of-variables calculation in RESULT.md.
"""
import math
import random

PI = math.pi
SQ3 = math.sqrt(3.0)


def integrate_periodic(fn, N=24000):
    assert N % 6 == 0
    step = 2 * PI / N
    return step * sum(fn((j + 0.5) * step) for j in range(N))


def marked_joint(k, phi):
    s3 = (k * k - 3) ** 1.5
    return 9 * SQ3 / (PI * PI * (k ** 3 + 9 * k - s3 * math.cos(3 * phi)))


def k_density(k):
    return 6 / (PI * (1 + k * k))


def conditional_phase_density(k, phi):
    return marked_joint(k, phi) / k_density(k)


def phase_from_cots(x, y, z):
    k = x + y + z
    s = math.sqrt(k * k - 3)
    cs = max(-1.0, min(1.0, (3 * x - k) / (2 * s)))
    sn = (z - y) * SQ3 / (2 * s)  # since z-y = (2 sqrt(3) s / 3) sin(phi)
    # Correct inversion: sin(phi) = sqrt(3)*(z-y)/(2s).
    return math.atan2(sn, cs) % (2 * PI)


def analytic_checks():
    for k in (SQ3 + 0.001, 2.0, 3.1, 7.0, 22.0):
        s = math.sqrt(k * k - 3)
        a = k ** 3 + 9 * k
        b = s ** 3
        discriminant = a * a - b * b
        assert abs(discriminant / (27 * (1 + k * k) ** 2) - 1) < 1e-11
        num_density = integrate_periodic(lambda phi: marked_joint(k, phi))
        assert abs(num_density / k_density(k) - 1) < 3e-11
        norm = integrate_periodic(lambda phi: conditional_phase_density(k, phi))
        assert abs(norm - 1) < 3e-11
        r = b / (a + math.sqrt(discriminant))
        assert 0 <= r < 1
        for phi in (0.0, 0.6, 1.4, 3.1, 5.9):
            poisson = (1 - r * r) / (2 * PI * (1 - 2 * r * math.cos(3 * phi) + r * r))
            assert abs(poisson / conditional_phase_density(k, phi) - 1) < 1e-10
    for a, b, c in ((PI / 3, PI / 3, PI / 3), (PI / 2, PI / 4, PI / 4), (0.2, 1.3, PI - 1.5)):
        x, y, z = [1 / math.tan(t) for t in (a, b, c)]
        assert abs(x * y + y * z + z * x - 1) < 1e-12
        k = x + y + z
        assert k >= SQ3 - 1e-12
        assert abs((k - x * y * z) * math.sin(a) * math.sin(b) * math.sin(c) - 1) < 1e-11
        if k > SQ3 + 1e-8:
            phi = phase_from_cots(x, y, z)
            s = math.sqrt(k * k - 3)
            xx = (k + 2 * s * math.cos(phi)) / 3
            yy = (k + 2 * s * math.cos(phi + 2 * PI / 3)) / 3
            zz = (k + 2 * s * math.cos(phi + 4 * PI / 3)) / 3
            assert max(abs(xx - x), abs(yy - y), abs(zz - z)) < 1e-10


def independent_circle_checks(n=300000):
    rng = random.Random(2026111221)
    counts = [0, 0, 0, 0, 0]
    thresholds = [PI / 36, PI / 18, PI / 12, PI / 9, 5 * PI / 36]
    # Direct circle-point coordinates; no Dirichlet sampling or angle cotangent formula.
    for _ in range(n):
        ts = [rng.random() * 2 * PI for _ in range(3)]
        pts = [(math.cos(t), math.sin(t)) for t in ts]
        (ax, ay), (bx, by), (cx, cy) = pts
        qa = (bx - cx) ** 2 + (by - cy) ** 2
        qb = (ax - cx) ** 2 + (ay - cy) ** 2
        qc = (ax - bx) ** 2 + (ay - by) ** 2
        double_area = abs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))
        omega = math.atan2(2 * double_area, qa + qb + qc)
        for i, threshold in enumerate(thresholds):
            if omega <= threshold:
                counts[i] += 1
    for threshold, count in zip(thresholds, counts):
        actual = count / n
        expected = 6 * threshold / PI
        sigma = math.sqrt(expected * (1 - expected) / n)
        assert abs(actual - expected) < 5.5 * sigma + 0.0002, (threshold, actual, expected, sigma)
        print(f'CDF at {threshold:.9f}: observed {actual:.6f}, exact {expected:.6f}')


if __name__ == '__main__':
    analytic_checks()
    independent_circle_checks()
    print('BROCARD_UNIFORM_PHASE_CHECKS_OK')
