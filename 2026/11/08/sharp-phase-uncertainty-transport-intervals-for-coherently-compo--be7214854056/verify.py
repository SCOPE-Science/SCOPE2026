"""Reproduce algebraic and finite-dimensional checks for phase-ambiguous coin composition.

Only Python's standard library is required. These tests are diagnostics; the exact
reachability theorem is proved analytically in RESULT.md.
"""
import cmath
import math
import random

PI = math.pi


def coin(theta, azimuth_a=0.0, azimuth_b=0.0):
    a = math.cos(theta / 2) * cmath.exp(1j * azimuth_a)
    b = math.sin(theta / 2) * cmath.exp(1j * azimuth_b)
    return ((a, b), (-b.conjugate(), a.conjugate()))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def gauge(phi):
    return ((cmath.exp(1j * phi), 0j), (0j, cmath.exp(-1j * phi)))


def transport(c):
    a, b = c[0]
    f = 1 / (1 + abs(b))
    return ((b * a.conjugate()).real * f, -(b * a.conjugate()).imag * f, abs(a) ** 2 * f)


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def distance(z, lo, hi):
    return max(lo - z, 0.0, z - hi)


def reachable(angles):
    lo = hi = angles[0]
    for d in angles[1:]:
        old_lo, old_hi = lo, hi
        lo = distance(d, old_lo, old_hi)
        hi = PI - distance(PI - d, old_lo, old_hi)
    return lo, hi


def composed_angle(matrices, phases):
    product = matrices[0]
    for j in range(1, len(matrices)):
        product = matmul(matrices[j], matmul(gauge(phases[j - 1]), product))
    t = min(1.0, abs(product[0][1]))
    return 2 * math.asin(t)


def drift(theta):
    t = math.sin(theta / 2)
    return math.sqrt(max(0.0, (1 - t) / (1 + t)))


def run():
    rng = random.Random(873209)
    count = 0
    for n in (2, 3, 4, 5, 7):
        for _ in range(25):
            ds = [rng.uniform(0.01, PI - 0.01) for i in range(n)]
            coins = [coin(d, rng.uniform(-PI, PI), rng.uniform(-PI, PI)) for d in ds]
            lo, hi = reachable(ds)
            assert -1e-11 <= lo <= hi <= PI + 1e-11
            for c, delta in zip(coins, ds):
                a, b = c[0]
                x, y, z = transport(c)
                assert abs(z - (1 - abs(b))) < 2e-13
                assert abs(norm((x, y, z)) - drift(delta)) < 2e-13
                rotated = matmul(gauge(rng.uniform(-PI, PI)), c)
                assert max(abs(r - s) for r, s in zip(transport(c), transport(rotated))) < 2e-13
                count += 3
            for _ in range(120):
                angle = composed_angle(coins, [rng.uniform(0, 2 * PI) for i in range(n - 1)])
                assert lo - 5e-12 <= angle <= hi + 5e-12, (n, ds, lo, angle, hi)
                count += 1
    cases = [
        ([0.3 * PI, 0.2 * PI, 0.1 * PI], (0.0, 0.6 * PI)),
        ([0.9 * PI] * 3, (0.7 * PI, PI)),
        ([0.5 * PI] * 3, (0.0, PI)),
        ([0.13 * PI, 0.5 * PI, 0.7 * PI], (0.07 * PI, 0.93 * PI)),
        ([PI, PI, PI], (PI, PI)),
        ([0.0, PI], (PI, PI)),
    ]
    for ds, expected in cases:
        measured = reachable(ds)
        assert all(abs(a - b) < 1e-11 for a, b in zip(measured, expected)), (ds, measured, expected)
        count += 2
    # Search the two phase torus for numerical witnesses near both sharp endpoints.
    for ds in ([0.3 * PI, 0.2 * PI, 0.1 * PI], [0.9 * PI] * 3, [0.5 * PI] * 3):
        coins = [coin(d, 0.17, 0.49) for d in ds]
        lo, hi = reachable(ds)
        angles = [composed_angle(coins, [2 * PI * j / 100, 2 * PI * k / 100])
                  for j in range(101) for k in range(101)]
        assert min(angles) - lo < 0.05
        assert hi - max(angles) < 0.05
        count += 2
    print('PASS: %d transport, reachability, and endpoint diagnostics' % count)


if __name__ == '__main__':
    run()
