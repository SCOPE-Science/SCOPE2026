"""Independent numerical diagnostics for the maximal-exradius distribution.

Run with Python 3, NumPy and SciPy. Finite tests support but cannot prove
an infinite asymptotic or historical originality.
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi


def exact_cdf(t):
    """One-dimensional integral for the largest unit-circumradius exradius."""
    if t <= 1.5:
        return 0.0
    if t >= 4.0:
        return 1.0

    def length(u):
        m = min(u, 2.0 * PI - 3.0 * u)
        c = math.cos(u / 2)
        z = t / (2 * c) - c
        if z <= math.cos(m / 2):
            return 0.0
        if z >= 1:
            return m
        return m - 2 * math.acos(z)

    first = quad(length, 0.0, PI / 2, epsabs=3e-12, limit=300)[0]
    second = quad(length, PI / 2, 2 * PI / 3, epsabs=3e-12, limit=300)[0]
    return (6.0 / PI**2) * (first + second)


def cartesian_max_exradius(angles):
    """Geometric lengths and area, without the half-angle exradius formula."""
    pts = np.stack([np.cos(angles), np.sin(angles)], axis=-1)
    x0, x1, x2 = pts[:, 0], pts[:, 1], pts[:, 2]
    side = np.stack([np.linalg.norm(x1 - x2, axis=1),
                     np.linalg.norm(x0 - x2, axis=1),
                     np.linalg.norm(x0 - x1, axis=1)], axis=-1)
    s = side.sum(axis=1) / 2
    d1, d2 = x1 - x0, x2 - x0
    area = 0.5 * np.abs(d1[:, 0] * d2[:, 1] - d1[:, 1] * d2[:, 0])
    return np.max(area[:, None] / (s[:, None] - side), axis=1), side, s


def main():
    rng = np.random.default_rng(20261110)
    # Different sample representations: independent polar points for the
    # Cartesian exradii; a uniform angular simplex for exact integration.
    polar = rng.uniform(0.0, 2 * PI, size=(650_000, 3))
    geom, sides, s = cartesian_max_exradius(polar)
    keep = np.min(s[:, None] - sides, axis=1) > 1e-5
    a, b, c = (sides[keep, 0], sides[keep, 1], sides[keep, 2])
    A = np.arccos(np.clip((b*b+c*c-a*a)/(2*b*c), -1, 1))
    B = np.arccos(np.clip((a*a+c*c-b*b)/(2*a*c), -1, 1))
    C = PI - A - B
    half_angle_exradii = 4 * np.stack([
        np.sin(A / 2) * np.cos(B / 2) * np.cos(C / 2),
        np.sin(B / 2) * np.cos(A / 2) * np.cos(C / 2),
        np.sin(C / 2) * np.cos(A / 2) * np.cos(B / 2)], axis=1)
    dif = np.max(np.abs(np.max(half_angle_exradii, axis=1) - geom[keep]))
    print('max Cartesian versus half-angle discrepancy:', dif)
    assert dif < 1e-7

    for t in [1.55, 1.70, 2.00, 2.50, 3.00, 3.80]:
        theor = exact_cdf(t)
        empirical = float(np.mean(geom <= t))
        sigma = math.sqrt(theor * (1 - theor) / len(geom))
        print(f'Cdf t={t:.2f}: exact={theor:.9f}, Monte Carlo={empirical:.9f}, sigma={sigma:.7f}')
        assert abs(empirical - theor) <= 5 * sigma + 0.0004

    low_c = 3 / PI**2
    up_c = 2 / (PI * math.sqrt(3))
    for eps in [0.01, 0.005]:
        approx = exact_cdf(1.5 + eps) / eps**2
        print('lower ratio:', eps, approx, low_c)
        assert abs(approx / low_c - 1) < 0.005
    for eps in [0.01, 0.002]:
        approx = (1 - exact_cdf(4 - eps)) / eps
        print('upper ratio:', eps, approx, up_c)
        assert abs(approx / up_c - 1) < 0.005

    # Marked limit: use the ordered angular simplex in an independent sample.
    ang = rng.dirichlet([1.0, 1.0, 1.0], size=1_200_000) * PI
    e = 4 * np.sin(ang / 2) * np.prod(np.cos(ang / 2), axis=1)[:, None] / np.cos(ang / 2)
    rmax = e.max(axis=1)
    eps = 0.02
    chosen = (rmax > 4 - eps)
    largest = np.argmax(ang, axis=1)
    # Rotate angular labels so the largest angle is first; the following
    # two coordinates generate one 60-degree wedge in transformed space.
    rotated = np.take_along_axis(ang,
         (largest[:, None] + np.arange(3)) % 3, axis=1)
    y, z = rotated[chosen, 1] / math.sqrt(eps), rotated[chosen, 2] / math.sqrt(eps)
    X = y + z / 2
    Y = math.sqrt(3) * z / 2
    sector_angle = np.arctan2(Y, X)
    radial2 = X * X + Y * Y
    print('marked upper-tail count:', chosen.sum(), 'radial squared mean:', radial2.mean(),
          'sector angle mean:', sector_angle.mean(), 'label shares:',
          np.bincount(largest[chosen], minlength=3) / chosen.sum())
    assert abs(float(radial2.mean()) - 0.5) < 0.035
    assert abs(float(sector_angle.mean()) - PI / 6) < 0.035
    assert np.all(np.abs(np.bincount(largest[chosen], minlength=3) / chosen.sum() - 1/3) < .035)

    print('MAXIMAL_EXRADIUS_EXACT_CDF_AND_MARKED_TAILS_OK')


if __name__ == '__main__':
    main()
