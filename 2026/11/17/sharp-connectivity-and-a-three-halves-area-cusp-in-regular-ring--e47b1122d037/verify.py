"""Independent numerical checks for regular-ring weighted Voronoi formulas.
Only standard Python is needed. Numerical tests complement, not replace, proof.
"""
import math


def radii(n, lam, radius):
    beta = math.pi / n
    c = lam * lam * radius / (lam * lam - 1)
    r = lam * radius / (lam * lam - 1)
    return beta, c, r


def inner_radius(n, lam, radius, angle):
    beta, c, r = radii(n, lam, radius)
    delta = ((angle + beta) % (2 * beta)) - beta
    return c * math.cos(delta) - math.sqrt(max(0.0, r * r - c * c * math.sin(delta) ** 2))


def area_formula(n, lam, radius):
    beta, c, r = radii(n, lam, radius)
    z = lam * math.sin(beta)
    assert 1 < lam < 1 / math.sin(beta)
    return n * (c * c * math.sin(beta) * math.cos(beta)
                + r * r * (beta - math.asin(z) - z * math.sqrt(1 - z * z)))


def area_simpson(n, lam, radius, intervals=8192):
    beta = math.pi / n
    h = beta / intervals
    value = inner_radius(n, lam, radius, 0) ** 2
    value += inner_radius(n, lam, radius, beta) ** 2
    for k in range(1, intervals):
        value += (4 if k % 2 else 2) * inner_radius(n, lam, radius, k * h) ** 2
    return n * h * value / 3


def assert_close(x, y, rel=4e-8):
    assert abs(x - y) < rel * (1 + abs(y)), (x, y)


checks = 0
for n in (3, 4, 5, 7, 11, 20):
    critical = 1 / math.sin(math.pi / n)
    for frac in (.08, .25, .53, .8, .93):
        lam = 1 + frac * (critical - 1)
        a = area_formula(n, lam, 1.3)
        assert_close(a, area_simpson(n, lam, 1.3))
        checks += 1
    # Assert the closed disk separation criterion at both sides.
    for frac in (.65, 1, 1.2):
        lam = 1 + frac * (critical - 1)
        beta, c, r = radii(n, lam, 1.3)
        connected_disks = r >= c * math.sin(beta)
        assert connected_disks == (lam <= critical + 1e-12)
        checks += 1

# Compare radial inequality directly with all n quadratic weighted distances.
for n in (3, 4, 7, 11):
    critical = 1 / math.sin(math.pi / n)
    lam = 1 + .54 * (critical - 1)
    for j in range(65):
        angle = 2 * math.pi * (j + .23) / 65
        edge = inner_radius(n, lam, 1, angle)
        for t in (.55 * edge, 1.45 * edge):
            x, y = t * math.cos(angle), t * math.sin(angle)
            inside = all(t <= lam * math.hypot(x - math.cos(2 * math.pi * k / n),
                                           y - math.sin(2 * math.pi * k / n))
                         for k in range(n))
            assert inside == (t < edge)
            checks += 1

# Test positive central-area limit and the cusp amplitude in a stable range.
for n in (3, 4, 6, 9):
    beta = math.pi / n
    s, h = math.sin(beta), math.cos(beta)
    critical = 1 / s
    rstar = critical / (critical * critical - 1)
    coefficient = 2 * n / 3 * rstar ** 2 * (2 * s) ** 1.5
    for eps in (0.00001, 0.000002):
        lam = critical - eps
        _, c, r = radii(n, lam, 1)
        # Calculate the nonanalytic remainder without subtracting large areas.
        z = lam * s
        remainder = n * r * r * (math.acos(z) - z * math.sqrt(1-z*z))
        assert_close(remainder / eps ** 1.5, coefficient, rel=.003)
        checks += 1

print('PASS: ', checks, 'comparisons; area, radial eligibility, connectivity, cusp')
