"""Numerical cross-checks for the local small-area law of random boundary triangles.

Requires numpy and scipy. These finite calculations are not a proof of the limit.
"""
import math
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid
from scipy.optimize import brentq
from scipy.special import beta

PI = math.pi
BETA = beta(1.0 / 3.0, 1.0 / 3.0)
K = 3.0 * (4.0 ** (2.0 / 3.0)) * BETA
C_CIRCLE = K / (4.0 * PI ** 2)


def circle_cdf(t):
    """One-dimensional quadrature from the exact circular-gap area identity."""
    def peak(x):
        return math.sin(x) * (1.0 + math.cos(x))

    low = brentq(lambda x: peak(x) - t, 0.0, PI / 3.0, xtol=1e-14)
    high = brentq(lambda x: peak(x) - t, PI / 3.0, PI, xtol=1e-14)

    def cross_length(x):
        z = min(1.0, max(-1.0, math.cos(x) - t / math.sin(x)))
        return max(0.0, math.acos(z) - x)

    value = 0.5 * (2 * PI * low - low * low)
    value += quad(cross_length, low, high, epsabs=1e-12, limit=400)[0]
    value += 0.5 * (PI - high) ** 2
    return 2.0 * value / PI ** 2


def ellipse_constants(a, b):
    def speed(theta):
        return math.hypot(a * math.sin(theta), b * math.cos(theta))
    perimeter = quad(speed, 0, 2 * PI, epsabs=1e-12)[0]
    curvature_integral = quad(lambda x: speed(x) ** 3, 0, 2 * PI, epsabs=1e-12)[0] / (a * b) ** (2 / 3)
    affine_length = 2 * PI * (a * b) ** (1 / 3)
    return perimeter, K * curvature_integral / perimeter ** 3, K / affine_length ** 2


def sample_triangle_areas(n, a, b, rng, mode):
    if mode == "affine":
        theta = rng.uniform(0.0, 2 * PI, size=(n, 3))
    else:
        grid = np.linspace(0, 2 * PI, 16385)
        speed = np.hypot(a * np.sin(grid), b * np.cos(grid))
        cdf = np.concatenate([[0.0], cumulative_trapezoid(speed, grid)])
        cdf /= cdf[-1]
        theta = np.interp(rng.uniform(size=(n, 3)), cdf, grid)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    return 0.5 * np.abs((x[:, 1] - x[:, 0]) * (y[:, 2] - y[:, 0]) - (x[:, 2] - x[:, 0]) * (y[:, 1] - y[:, 0]))


def main():
    assert abs(C_CIRCLE - 1.0148546652584383) < 1e-13
    ratios = []
    for t in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
        ratios.append(circle_cdf(t) / (C_CIRCLE * t ** (2 / 3)))
    assert abs(ratios[-1] - 1.0) < 3e-5
    assert all(abs(ratios[k+1]-1)<abs(ratios[k]-1) for k in range(4))

    L1, u1, o1 = ellipse_constants(1, 1)
    assert abs(L1 - 2 * PI) < 1e-12
    assert abs(u1 - C_CIRCLE) < 1e-12 and abs(o1 - C_CIRCLE) < 1e-12
    L2, u2, o2 = ellipse_constants(2, 1)
    assert abs(u2 - 0.736686266391737) < 2e-12
    assert abs(o2 - 0.639318377671560) < 2e-12
    assert u2 > o2
    # independent direct simulation of area, not circular gaps or curvature integration
    rng = np.random.default_rng(41827)
    t = 0.0007
    experiments = []
    for a,b,mode,c in ((1.0,1.0,"affine",C_CIRCLE),(2.0,1.0,"uniform",u2),(2.0,1.0,"affine",o2)):
        n=1500000
        hits=0
        for _ in range(3):
            areas = sample_triangle_areas(n//3,a,b,rng,mode)
            hits += int(np.count_nonzero(areas<t))
        empirical=hits/n
        ratio=empirical/(c*t**(2/3))
        experiments.append((mode,a,b,empirical,ratio))
        assert abs(ratio-1.0) < 0.085
    print("VERIFY_OK")
    print("circle_coeff=%.14f" % C_CIRCLE)
    print("circle_quadrature_limit_ratios", " ".join("%.9f"%z for z in ratios))
    print("ellipse_perimeter=%.11f uniform_coeff=%.11f affine_coeff=%.11f"%(L2,u2,o2))
    for mode,a,b,p,r in experiments:
        print("ellipse_axes=%.1f,%.1f sample=%s probability=%.9f ratio_to_tail=%.6f"%(a,b,mode,p,r))

if __name__ == '__main__':
    main()
