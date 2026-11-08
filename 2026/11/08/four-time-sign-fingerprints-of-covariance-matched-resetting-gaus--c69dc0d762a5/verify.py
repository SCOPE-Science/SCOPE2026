"""Independent finite diagnostics for stationary four-time bath cumulants.

Run with NumPy and SciPy installed. Analytical proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.linalg import expm


def propagate_polynomial(D, r, t):
    # Columns encode the generator acting on the monomial basis 1,y,...,y^4.
    A = np.zeros((5, 5))
    for n in range(1, 5):
        A[n, n] = -r
        if n >= 2:
            A[n - 2, n] = D * n * (n - 1)
    return expm(t * A)


def multiply_y(c):
    out = np.zeros(5)
    out[1:] = c[:4]
    return out


def four_brownian_semigroup(D, r, u, v, w):
    coeff = np.array([0., 1., 0., 0., 0.])
    for gap in (w, v, u):
        coeff = multiply_y(propagate_polynomial(D, r, gap) @ coeff)
    return np.dot(coeff, np.array([1., 0., 2 * D / r, 0., 24 * (D / r) ** 2]))


def four_brownian_formula(D, r, u, v, w):
    return 4 * (D / r) ** 2 * np.exp(-r * (u + w)) * (1 + np.exp(-r * v) * (5 + 3 * r * u))


def fourth_cumulant_B(D, r, u, v, w):
    return 4 * (D / r) ** 2 * np.exp(-r * (u + v + w)) * (5 + 3 * r * u - 2 * np.exp(-r * v))


def telegraph_four_semigroup(D, r, u, v, w):
    a = np.sqrt(2 * D / r)
    A = np.array([[-r / 2, r / 2], [r / 2, -r / 2]])
    # States ordered +a,-a. Repeated multiplication by observation coordinate.
    m = np.diag([a, -a])
    p = np.array([.5, .5])
    ones = np.ones(2)
    return p @ m @ expm(u * A) @ m @ expm(v * A) @ m @ expm(w * A) @ m @ ones


def kappa_telegraph(D, r, u, v, w):
    return -8 * (D / r) ** 2 * np.exp(-r * (u + 2 * v + w))


def covariance(D, r, gap):
    return (2 * D / r) * np.exp(-r * abs(gap))


def pairings(D, r, u, v, w):
    return (covariance(D, r, u) * covariance(D, r, w)
            + 2 * covariance(D, r, u + v) * covariance(D, r, v + w))


def sign_kernel_at_times(D, r, times, typ):
    t = sorted(times)
    gaps = [t[i + 1] - t[i] for i in range(3)]
    if typ == 'reset':
        return fourth_cumulant_B(D, r, *gaps)
    if typ == 'telegraph':
        return kappa_telegraph(D, r, *gaps)
    return 0.


def main():
    count = 0
    for D in (0.3, 1.2, 3.):
        for r in (0.4, 1., 2.3):
            for u in (0., 0.1, 0.4, 1.3):
                for v in (0., 0.3, 1., 3.):
                    for w in (0., 0.15, 1.):
                        a = four_brownian_semigroup(D, r, u, v, w)
                        b = four_brownian_formula(D, r, u, v, w)
                        assert math.isclose(a, b, rel_tol=2e-12, abs_tol=1e-11)
                        assert math.isclose(a - pairings(D, r, u, v, w),
                                            fourth_cumulant_B(D, r, u, v, w),
                                            rel_tol=2e-10, abs_tol=1e-11)
                        c = telegraph_four_semigroup(D, r, u, v, w)
                        assert math.isclose(c - pairings(D, r, u, v, w),
                                            kappa_telegraph(D, r, u, v, w),
                                            rel_tol=2e-10, abs_tol=1e-11)
                        assert fourth_cumulant_B(D, r, u, v, w) > 0
                        assert kappa_telegraph(D, r, u, v, w) < 0
                        count += 1
    # Discrete approximations to unequal positive harmonic response kernels.
    D, r = 1.2, 1.3
    grid = np.arange(0., 3.01, 0.25)
    weights = [np.exp(-mu * grid) * 0.25 for mu in (0.7, 1.4, 0.9, 2.1)]
    times = [0.1, 0.6, 0.9, 1.5]
    reset_total = tele_total = 0.
    for i, s1 in enumerate(grid):
        for j, s2 in enumerate(grid):
            for k, s3 in enumerate(grid):
                for l, s4 in enumerate(grid):
                    times_shifted = [times[0] - s1, times[1] - s2,
                                     times[2] - s3, times[3] - s4]
                    factor = weights[0][i] * weights[1][j] * weights[2][k] * weights[3][l]
                    reset_total += factor * sign_kernel_at_times(D, r, times_shifted, 'reset')
                    tele_total += factor * sign_kernel_at_times(D, r, times_shifted, 'telegraph')
    assert reset_total > 0 and tele_total < 0
    assert sign_kernel_at_times(D, r, times, 'gaussian') == 0.
    print(f'PASS {count} independent generator/matrix cases; positive-filter quadrature signs verified')


if __name__ == '__main__':
    main()
