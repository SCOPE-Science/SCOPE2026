"""Independent numerical checks for the area of exactly-two coverage of four
center-to-vertex diameter disks of an axis-aligned rectangle.

The proof is analytic; the finite checks below are not a proof.
"""
import math


def exact_fraction(lam):
    if lam < 1:
        lam = 1 / lam
    ans = math.pi / 8 * (lam + 1 / lam) - 0.5
    if lam > math.sqrt(8):
        t = math.sqrt(lam * lam - 8)
        phi = (lam * lam + 1) * math.atan(t / 3) - 3 * t
        ans -= phi / (4 * lam)
    return ans


def integral_fraction(lam, steps=20000):
    assert steps % 2 == 0
    def integrand(x, y):
        val = (math.sqrt(1 + 4 * y * y * x * (1 - x)) - 1) / 2
        return min(1.0, val)
    h = 1 / steps
    ans = 0
    for i in range(steps + 1):
        x = i * h
        w = (1 if i in (0, steps) else (4 if i % 2 else 2))
        ans += w * (integrand(x, lam) + integrand(x, 1 / lam))
    return ans * h / 3


def direct_grid_fraction(lam, steps=360):
    a, b = lam, 1.0
    count2 = 0
    counts = {}
    for i in range(steps):
        x = -a + 2 * a * (i + 0.5) / steps
        for j in range(steps):
            y = -b + 2 * b * (j + 0.5) / steps
            r2 = x * x + y * y
            hits = sum(r2 <= sx * a * x + sy * b * y for sx in (-1, 1) for sy in (-1, 1))
            counts[hits] = counts.get(hits, 0) + 1
            assert hits in (1, 2)
            count2 += hits == 2
    return count2 / (steps * steps), counts


def run():
    cases = (1, 1.3, 2, math.sqrt(8), 2.85, 3, 4, 10)
    for lam in cases:
        exact = exact_fraction(lam)
        integral = integral_fraction(lam)
        grid, counts = direct_grid_fraction(lam)
        assert 0 < exact < 1
        assert abs(integral - exact) < 1.0e-8, (lam, integral, exact)
        assert abs(grid - exact) < 0.006, (lam, grid, exact)
        assert counts.get(0, 0) == 0 and counts.get(3, 0) == 0
        print(f'lambda={lam:.8g}, exact={exact:.10f}, independent integral={integral:.10f}, grid={grid:.8f}')
    for j in range(1, 1000):
        lam = 1 + 9 * j / 1000
        assert exact_fraction(lam + 0.009) > exact_fraction(lam)
    assert abs(exact_fraction(1) - (math.pi / 4 - 0.5)) < 1e-12
    for lam in (15.0, 30.0, 80.0):
        asymptotic_coefficient = lam ** 2 * (1 - exact_fraction(lam))
        assert 1.45 < asymptotic_coefficient < 1.55
    print('PASS: 8 independent integrals, 8 direct covering grids, 999 monotonicity samples, and asymptotic checks')


if __name__ == '__main__':
    run()
