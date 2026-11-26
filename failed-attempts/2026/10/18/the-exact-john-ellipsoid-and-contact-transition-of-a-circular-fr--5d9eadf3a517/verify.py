"""Standalone exact-arithmetic and numerical diagnostics for the frustum John ellipsoid."""
from fractions import Fraction as F
from math import sqrt, gamma, pi
from random import Random


def parameters(d, t):
    assert isinstance(d, int) and d >= 2 and 0 <= t <= 1
    k = 1 - t
    if k == 0 or (d + 1) * k <= 2:
        return sqrt(float(t)), F(1, 2)
    return sqrt(F(d - 1, d + 1)), 1 / ((d + 1) * k)


def kappa(d):
    return pi ** (d / 2) / gamma(d / 2 + 1)


def normalized_ratio_sq(d, t):
    """Exact squared ratio with the constant (kappa_d/kappa_(d-1))^2 removed."""
    k = 1 - t
    if k == 0 or (d + 1) * k <= 2:
        a2, b = t, F(1, 2)
    else:
        a2, b = F(d - 1, d + 1), 1 / ((d + 1) * k)
    return d * d * a2 ** (d - 1) * b * b / sum(t ** j for j in range(d)) ** 2


rng = Random(20261011)
exact_compares = 0
boundary_checks = 0
support_samples = 0
monotone_checks = 0
for d in range(2, 19):
    k_transition = F(2, d + 1)
    a2 = F(d - 1, d + 1)
    # Exact junction consistency and contact identities.
    assert F(1, 1) - k_transition == a2
    assert F(1, (d + 1)) / k_transition == F(1, 2)
    boundary_checks += 2
    for j in range(21):
        k = F(j, 20)
        t = 1 - k
        a, b_star = parameters(d, t)
        opt_sq = b_star ** 2 * (1 - 2 * k * b_star) ** (d - 1)
        assert 1 - 2 * k * b_star > 0
        # Complete rational finite grid of symmetric competitor ellipsoids.
        for b_n in range(1, 41):
            b = F(b_n, 80)
            if 1 - 2 * k * b <= 0:
                continue
            trial_sq = b ** 2 * (1 - 2 * k * b) ** (d - 1)
            assert trial_sq <= opt_sq
            exact_compares += 1
        expected_a2 = 1 - 2 * k * b_star
        assert abs(a * a - float(expected_a2)) < 3e-14
        # Independent inclusion check at uniformly random ellipsoid boundary points.
        for _ in range(16):
            zeta = rng.uniform(-1, 1)
            z = float(b_star) * (1 + zeta)
            radius = a * sqrt(max(0, 1 - zeta * zeta))
            assert -1e-12 <= z <= 1 + 1e-12
            assert radius + float(k) * z <= 1 + 1e-12
            support_samples += 1
    last = normalized_ratio_sq(d, F(0))
    for j in range(1, 201):
        now = normalized_ratio_sq(d, F(j, 200))
        assert now > last
        last = now
        monotone_checks += 1
print('VERIFY_OK', 'exact_rational_competitors='+str(exact_compares),
      'junction_identities='+str(boundary_checks),
      'boundary_samples='+str(support_samples),
      'monotone_ratio_steps='+str(monotone_checks))
