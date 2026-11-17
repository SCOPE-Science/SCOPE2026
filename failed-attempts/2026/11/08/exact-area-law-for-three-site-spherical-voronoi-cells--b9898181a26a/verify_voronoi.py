#!/usr/bin/env python3
"""Independent numerical consistency tests for the exact three-site spherical Voronoi area law.
Requires Python 3 and numpy.  These are finite tests, not an infinite proof.
"""
import math
import numpy as np

PI = math.pi


def cdf(a):
    if a <= 0.0:
        return 0.0
    if a >= 2 * PI:
        return 1.0
    return (a * (2.0 + math.cos(a)) - 3.0 * math.sin(a)) / (6.0 * PI)


def pdf(a):
    if not 0.0 < a < 2 * PI:
        return 0.0
    t = a / 2.0
    return 2.0 / (3.0 * PI) * math.sin(t) * (math.sin(t) - t * math.cos(t))


def integrate_simpson(fun, a, b, n=8192):
    assert n % 2 == 0
    h = (b - a) / n
    v = fun(a) + fun(b)
    for i in range(1, n):
        v += (4 if i % 2 else 2) * fun(a + i * h)
    return h * v / 3.0


def test_analytic():
    assert abs(cdf(0)) < 1e-14 and abs(cdf(2*PI)-1) < 1e-14
    assert abs(cdf(PI)-1.0/6) < 1e-14
    for t in np.linspace(0.25, 2*PI-0.25, 19):
        h = 1.0e-5
        assert abs((cdf(t+h)-cdf(t-h))/(2*h)-pdf(t)) < 1e-9
    m0 = integrate_simpson(pdf, 0, 2*PI)
    m1 = integrate_simpson(lambda a: a*pdf(a), 0, 2*PI)
    m2 = integrate_simpson(lambda a: a*a*pdf(a), 0, 2*PI)
    assert abs(m0-1) < 1e-10
    assert abs(m1-4*PI/3) < 1e-10
    assert abs(m2-(20*PI**2/9-10.0/3)) < 1e-10
    return m0, m1, m2


def sample_areas(num=500_000, seed=207147):
    rng = np.random.default_rng(seed)
    # Fix first site at (0,0,1), use exact spherical-area sampling for others.
    h = rng.uniform(-1.0, 1.0, size=(num, 2))
    az = rng.uniform(-PI, PI, size=(num, 2))
    radial = np.sqrt(1.0 - h*h)
    xx = radial * np.cos(az)
    yy = radial * np.sin(az)
    # Bisector hemisphere normals (north pole minus each independent site).
    nn = np.stack((-xx, -yy, 1.0-h), axis=-1)
    nn /= np.linalg.norm(nn, axis=-1)[:, :, None]
    cosine = np.einsum('ij,ij->i', nn[:, 0, :], nn[:, 1, :])
    gamma = np.arccos(np.clip(cosine, -1.0, 1.0))
    return 2.0 * (PI-gamma), nn


def test_monte_carlo():
    values, nn = sample_areas()
    assert len(values) == 500000
    for q in [PI/4, PI/2, PI, 3*PI/2, 7*PI/4]:
        observed = float(np.mean(values <= q))
        expected = cdf(q)
        se = math.sqrt(max(expected*(1.0-expected), 1e-6)/len(values))
        assert abs(observed-expected) < 6*se + .0008, (q, observed, expected)
    assert abs(float(np.mean(values)) - 4.0*PI/3) < .012
    assert abs(float(np.var(values)) - (4*PI*PI/9-10.0/3)) < .022
    # Separate geometric area check: spherical-lune area equals 2(pi-angle).
    rng=np.random.default_rng(401)
    count=125000
    z=rng.normal(size=(count,3))
    z/=np.linalg.norm(z,axis=1)[:,None]
    for idx in [0,321,1234,20999]:
        v,w=nn[idx]
        empirical=np.mean((z@v>=0)&(z@w>=0))
        target=values[idx]/(4*PI)
        assert abs(empirical-target)<.007, (idx,empirical,target)
    return len(values), count

if __name__ == '__main__':
    test_analytic()
    N, Q = test_monte_carlo()
    print('THREE_SITE_SPHERICAL_VORONOI_AREA_LAW_OK',N,Q)
