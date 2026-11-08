"""Standard-library numerical checks for Poisson tangent-polygon area and perimeter.

All calculations are direct from tangent-line intersections. Monte Carlo checks are
consistency checks, not proofs of the asymptotic central limit theorem.
"""
import math
import random

TAU = 2.0 * math.pi


def support(t, eps):
    return 1.0 - eps * math.cos(2.0 * t) / 3.0


def radius(t, eps):
    return 1.0 + eps * math.cos(2.0 * t)


def poisson_angles(rng, intensity):
    x = 0.0
    out = []
    while True:
        x += rng.expovariate(intensity)
        if x >= TAU:
            return out
        out.append(x)


def polygon_and_gap_energies(angles, eps):
    n = len(angles)
    if n < 3:
        return None
    gaps = [((angles[(j + 1) % n] - angles[j]) % TAU) for j in range(n)]
    if max(gaps) >= 0.55:
        return None
    vertices = []
    for j, t in enumerate(angles):
        u = angles[(j + 1) % n]
        c, s = math.cos(t), math.sin(t)
        C, S = math.cos(u), math.sin(u)
        H, J = support(t, eps), support(u, eps)
        det = c * S - s * C
        vertices.append(((H * S - s * J) / det, (c * J - H * C) / det))
    area = 0.5 * sum(vertices[j][0] * vertices[(j + 1) % n][1]
                     - vertices[j][1] * vertices[(j + 1) % n][0]
                     for j in range(n))
    perimeter = sum(math.hypot(vertices[j][0] - vertices[(j + 1) % n][0],
                               vertices[j][1] - vertices[(j + 1) % n][1])
                    for j in range(n))
    a0 = math.pi * (1.0 - eps * eps / 6.0)
    p0 = TAU
    approx_a = sum(radius(t + d / 2.0, eps)**2 * d**3 / 24.0
                   for t, d in zip(angles, gaps))
    approx_p = sum(radius(t + d / 2.0, eps) * d**3 / 12.0
                   for t, d in zip(angles, gaps))
    if eps == 0.0:
        a_disk = sum(math.tan(d / 2.0) for d in gaps)
        assert abs(area - a_disk) < 2e-8
        assert abs(perimeter - 2.0 * area) < 2e-8
    return (area-a0, perimeter-p0, approx_a, approx_p)


def scaled_covariance(samples, scale):
    n = len(samples)
    ma = sum(x[0] for x in samples) / n
    mp = sum(x[1] for x in samples) / n
    v1 = sum((x[0]-ma)**2 for x in samples) / (n-1) * scale**5
    v2 = sum((x[1]-mp)**2 for x in samples) / (n-1) * scale**5
    v12 = sum((x[0]-ma)*(x[1]-mp) for x in samples) / (n-1) * scale**5
    return ma, mp, (v1, v12, v2)


def test(eps, expected_count=420, trials=3500):
    lam = expected_count / TAU
    rng = random.Random(20261101 + int(eps*100))
    rows = []
    for j in range(trials):
        v = polygon_and_gap_energies(poisson_angles(rng, lam), eps)
        if v is not None:
            rows.append(v)
    assert len(rows) >= trials - 2
    ma, mp, covariance = scaled_covariance(rows, lam)
    i2 = TAU * (1.0 + eps**2/2.0)
    i3 = TAU * (1.0 + 3.0*eps**2/2.0)
    i4 = TAU * (1.0 + 3.0*eps**2 + 3.0*eps**4/8.0)
    pred_mean = (i2 / (4.0*lam**2), TAU / (2.0*lam**2))
    pred_cov = (7*i4/8.0, 7*i3/4.0, 7*i2/2.0)
    for obs, expected in zip((ma,mp), pred_mean):
        assert abs(obs/expected - 1.0) < 0.07, (eps, obs, expected)
    for obs, expected in zip(covariance, pred_cov):
        assert abs(obs/expected - 1.0) < 0.17, (eps, obs, expected)
    # Difference between exact geometric defects and local cubic expansions is
    # negligible under the n^(5/2) fluctuation normalization.
    local_diffs = [lam**2.5 * sum((row[k]-row[k+2]) for row in rows)/len(rows)
                   for k in (0,1)]
    assert all(abs(d) < .10 for d in local_diffs)
    print('radius perturbation:', eps, 'samples:', len(rows))
    print('means: observed', (ma, mp), 'leading', pred_mean)
    print('scaled covariance: observed', covariance, 'leading', pred_cov)
    print('scaled local-expansion bias:', local_diffs)
    return pred_cov


if __name__ == '__main__':
    cc = test(0.0)
    assert abs(cc[0]*cc[2] - cc[1]**2) < 1e-10
    vv = test(0.55)
    assert vv[0]*vv[2] - vv[1]**2 > 1.0
    print('POISSON_TANGENT_GEOMETRY_AND_COVARIANCE_CHECKS_PASSED')
