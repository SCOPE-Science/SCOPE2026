"""Independent deterministic quadrature and geometric sampling checks for a cone's short Euclidean surface-pair distances.

Install NumPy (see requirements.txt), then run: python checks/verify_cone_short_chords.py.
The proof is analytic; these finite computations are not its substitute.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

N = 250
hx, hw = leggauss(N)
xn, xw = leggauss(N)


def cdf_exact_quadrature(r, q, length=1.0):
    """Numerically integrates the exact conditional-angle formula, including full-angle cap."""
    if not (0.0 < q <= 1.0 and 0.0 < r < length / 4):
        raise ValueError("expected 0<q<=1 and 0<r<L/4")
    h = (hx + 1.0) * r / 2.0
    weights_h = hw * r / 2.0
    x0 = 0.5 * np.sqrt(h * h + (r * r - h * h) / (q * q))
    xhi = length - h / 2.0
    xlo = h / 2.0
    all_angles = (x0 ** 3 - xlo ** 3) / 3.0 - h * h * (x0 - xlo) / 4.0
    v = (xn + 1.0) / 2.0
    wv = xw / 2.0
    x = x0[:, None] + (xhi - x0)[:, None] * v[None, :] ** 2
    uv = np.maximum(0.0, x * x - h[:, None] ** 2 / 4.0)
    z = np.sqrt(np.maximum(0.0, r * r - h[:, None] ** 2)) / (2.0 * q * np.sqrt(uv))
    angle_fraction = (2.0 / math.pi) * np.arcsin(np.clip(z, 0.0, 1.0))
    partial = np.sum(wv[None, :] * (xhi - x0)[:, None] * 2.0 * v[None, :] * uv * angle_fraction, axis=1)
    return (8.0 / length ** 4) * float(np.dot(weights_h, all_angles + partial))


def coeff(q, L=1.0):
    a2 = 1.0 / (q * L * L)
    a3 = -4.0 / (3.0 * math.pi * q * L ** 3)
    a4log = (1.0 - q * q) / (16.0 * q ** 3 * L ** 4)
    return a2, a3, a4log


def check():
    radii = [0.12, 0.065, 0.035]
    for q in [0.5, 0.7, 0.9]:
        a2, a3, a4 = coeff(q)
        values = [cdf_exact_quadrature(r, q) for r in radii]
        adjusted = [(p - a2 * r ** 2 - a3 * r ** 3) / r ** 4 for p, r in zip(values, radii)]
        slopes = [(adjusted[i + 1] - adjusted[i]) / math.log(radii[i] / radii[i + 1]) for i in range(2)]
        assert all(abs(s - a4) < 0.008 for s in slopes), (q, slopes, a4)
        # Cross-check logarithmic coefficient via extrinsic normal curvature: k1=0, k2=cot(alpha)/s.
        geom = (1 - q*q) / (16*q**3)
        assert math.isclose(geom, a4, rel_tol=1e-14)
        # Invert area and logarithmic coefficient into opening angle and slant length.
        A = math.pi * q
        B = A * A * a4
        beta = 16 * B / (math.pi * math.pi)
        qi = 2 / (math.sqrt(beta * beta + 4) + beta)
        Li = math.sqrt(A / (math.pi * qi))
        assert abs(qi - q) < 2e-15 and abs(Li - 1) < 2e-15
    # Independent 3D pair sampling, without the conditional arclength integration.
    rng = np.random.default_rng(20261115)
    n = 200000
    q, r = 0.65, 0.25
    s = np.sqrt(rng.random(n)); t = np.sqrt(rng.random(n))
    a = rng.uniform(0, 2 * math.pi, n)
    b = rng.uniform(0, 2 * math.pi, n)
    dist2 = (s-t)**2 + 2*q*q*s*t*(1-np.cos(a-b))
    empirical = np.mean(dist2 <= r*r)
    predicted = cdf_exact_quadrature(r - 1e-12, q)
    assert abs(empirical - predicted) < 0.006, (empirical, predicted)
    print("CONE_EXTRINSIC_SMALL_CHORD_LOG_CHECKS_OK numerical=9 inversion=3 sampling=200000")


if __name__ == '__main__':
    check()
