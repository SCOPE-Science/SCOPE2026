"""Standalone consistency checks for an explicit critical cubic-flow theorem.

Only Python 3 standard-library modules are used.  Finite quadrature does not prove
infinite-time claims; the corresponding analytic proof is in RESULT.md.
"""
import math
from fractions import Fraction


def H(lam, h, theta):
    return 1 / lam - h * (lam * math.cos(2 * theta) + math.sin(2 * theta)) / (1 + lam * lam)


def true_area(lam, R):
    c = math.sqrt(lam / 2)
    if R <= c:
        return math.pi * R * R
    return 2 * R * R * math.asin(c / R) + 2 * c * R * math.sqrt(1 - (c / R) ** 2)


def quadrature_area(lam, h, R, N=240000):
    vals = 0.0
    for j in range(N):
        angle = (j + 0.5) * (2 * math.pi / N)
        ht = H(lam, h, angle)
        vals += min(R * R, 1 / max(ht, 1e-14))
    return math.pi * vals / N


def check():
    # Exact rational coefficient verification for the linear inverse-square ODE.
    for lam in (Fraction(1, 2), Fraction(3, 2), Fraction(3, 1)):
        for h in (Fraction(2, 1), Fraction(-3, 2)):
            A = 1 / lam
            B = -h * lam / (1 + lam * lam)
            C = -h / (1 + lam * lam)
            assert -2 * lam * A + 2 == 0
            assert 2 * C == -2 * lam * B - 2 * h
            assert -2 * B == -2 * lam * C
    for lam in (0.5, 1.3, 3.0):
        hcrit = math.hypot(1, lam) / lam
        for h in (hcrit, -hcrit):
            c = math.sqrt(lam / 2)
            # Angle of a double zero of the critical periodic inverse-radius function.
            theta_star = 0.5 * math.atan2(1, lam) + (0 if h > 0 else math.pi / 2)
            for angle in (0.0, 0.2, 0.7, 1.1, 2.4):
                ht = H(lam, h, angle)
                rhs = 2 / lam * math.sin(angle - theta_star) ** 2
                assert abs(ht - rhs) < 2e-13, (lam, h, angle, ht, rhs)
                # Verify H' = -2 lambda H + 2(1-h cos 2 theta).
                hd = 2 * h * (lam * math.sin(2 * angle) - math.cos(2 * angle)) / (lam * lam + 1)
                assert abs(hd + 2 * lam * ht - 2 * (1 - h * math.cos(2 * angle))) < 2e-13
            for R in (c * 0.7, c * 1.1, c * 3, c * 12):
                exact = true_area(lam, R)
                actual = quadrature_area(lam, h, R)
                assert abs(exact - actual) < 2e-4, (lam, h, R, exact, actual)
            # A complete orbit has positive Delta and exact phase-sampled radii.
            theta0 = theta_star + 0.23
            r0 = 0.5 * c / abs(math.sin(theta0 - theta_star))
            delta = r0 ** -2 - H(lam, h, theta0)
            assert delta > 0
            for k in ((1, 2) if lam < 2 else (1,)):
                t = theta_star - theta0 + math.pi * k
                assert t > 0
                u = H(lam, h, theta0 + t) + delta * math.exp(-2 * lam * t)
                expected = math.exp(lam * t) / math.sqrt(delta)
                assert abs((1 / math.sqrt(u)) / expected - 1) < 3e-5
    print('CRITICAL_RIGID_COMPLETENESS_VERIFY_OK')


if __name__ == '__main__':
    check()
