"""Numerical diagnostics for the fixed-side-count tangent-polygon upper-tail expansion.

Run: python verify.py (requires numpy and scipy).
The asymptotic theorem is proved analytically in RESULT.md; this program checks
exact finite-dimensional identities and evaluates high-threshold approximations.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc


def coefficients(n):
    assert n >= 4
    p = 1.0 - n / 2 ** (n - 1)
    c = n * (n - 1) / (math.pi * 2 ** (n - 2) * p)
    r = (n - 1) * (n - 2) * quad(
        lambda u: (1 - u) ** (n - 3) * math.tan(math.pi * u / 2),
        0.0, 1.0, epsabs=2e-12, epsrel=2e-12
    )[0]
    return c, c * (r + (n - 2) / math.pi), r


def polygon_area_from_lines(gaps):
    """Compute the shoelace area from intersections of consecutive tangents."""
    theta = np.r_[0, np.cumsum(gaps[:-1])]
    vertices = []
    for i in range(len(gaps)):
        midpoint = theta[i] + gaps[i] / 2
        vertices.append([math.cos(midpoint) / math.cos(gaps[i] / 2),
                         math.sin(midpoint) / math.cos(gaps[i] / 2)])
    verts = np.asarray(vertices)
    return abs(np.sum(verts[:, 0] * np.roll(verts[:, 1], -1) -
                          verts[:, 1] * np.roll(verts[:, 0], -1))) / 2


def conditional_extreme_quadrature(n, t, sobol_power=18):
    """Quasi-Monte Carlo for the nonoverlapping, finite-residual extreme-gap sector.

    The remainder sector with R0>t^(2/3) is analytically o(t^-2).
    Returned value is a *truncated-sector* approximation, not a confidence bound.
    """
    U = qmc.Sobol(d=n - 1, scramble=True, seed=347).random_base2(sobol_power)
    U = -np.log(np.clip(U, 1e-16, 1.0))
    U /= U.sum(axis=1, keepdims=True)
    R0 = np.tan(math.pi * U / 2).sum(axis=1)
    valid = R0 <= t ** (2 / 3)
    U = U[valid]
    low = np.zeros(len(U))
    high = np.full(len(U), 2 * n / t)
    for _ in range(38):
        mid = (low + high) / 2
        area = 1 / np.tan(mid / 2) + np.tan((math.pi + mid[:, None]) * U / 2).sum(axis=1)
        positive = area > t
        low = np.where(positive, mid, low)
        high = np.where(positive, high, mid)
    delta = (low + high) / 2
    p = 1 - n / 2 ** (n - 1)
    # For a single uniformly spaced gap, Pr(pi-d<G<pi) is this exact beta integral.
    mass = ((math.pi + delta) / (2 * math.pi)) ** (n - 1) - 2 ** (1 - n)
    prob = n / p * np.sum(mass) / (2 ** sobol_power)
    # Rigorous upper bound by a union bound and the exact beta-coordinate tail.
    # Unlike an empirical omitted-sample count, it remains valid when no Sobol
    # point falls in the exceptional sector.
    cutoff = t ** (2 / 3)
    beta_tail_bound = (n - 1) * (1 - (2 / math.pi) * math.atan(cutoff / (n - 1))) ** (n - 2)
    rare_gap_mass = ((math.pi + 2 * n / t) / (2 * math.pi)) ** (n - 1) - 2 ** (1 - n)
    omitted_bound = n / p * beta_tail_bound * rare_gap_mass
    return prob, omitted_bound


def main():
    for n in (4, 5, 6):
        c, d, r = coefficients(n)
        assert c > 0 and d > 0 and r > 0
        print(f'n={n}: C={c:.12f}, D={d:.12f}, residual_mean={r:.12f}')
    c4, d4, r4 = coefficients(4)
    assert abs(c4 - 6 / math.pi) < 1e-13
    assert abs(r4 - 12 * math.log(2) / math.pi) < 1e-12
    assert abs(d4 - (72 * math.log(2) + 12) / math.pi ** 2) < 1e-12

    rng = np.random.default_rng(347)
    for n in (4, 5, 6):
        checked = 0
        while checked < 200:
            y = rng.dirichlet(np.ones(n))
            if max(y) >= 0.5:
                continue
            gaps = 2 * math.pi * y
            geometric = polygon_area_from_lines(gaps)
            tangential = np.tan(gaps / 2).sum()
            assert abs(geometric - tangential) < 2e-9 * max(1, tangential)
            checked += 1
    print('Checked 600 independent tangent-line/shoelace area identities')

    # Large-threshold normalized deviations support the analytic second coefficient.
    for n in (4, 5):
        c, d, _ = coefficients(n)
        for t in (10000.0, 100000.0):
            p, upper_omission = conditional_extreme_quadrature(n, t)
            observed = t * t * (p - c / t)
            print(f'n={n}, t={t:g}, scaled second term={observed:.8f}, '
                  f'target={d:.8f}, omitted scaled upper bound={upper_omission*t*t:.6f}')
            # Numerical diagnostics, not infinite-precision or asymptotic proof.
            assert abs(observed - d) < 0.3
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
