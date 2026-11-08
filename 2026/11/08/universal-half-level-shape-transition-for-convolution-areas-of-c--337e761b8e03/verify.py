"""Independent numerical checks for the co-oriented parallelogram theta-convolution theorem.

Run with Python 3 standard library: python3 verify.py
Numerics corroborate the analytic proof; they do not certify universal quantifiers.
"""
import math
import random


def formula(r, s, theta):
    assert r > 0 and s > 0 and 0 < theta < 1
    m1, m2 = min(r, 1.0), min(s, 1.0)
    d1, d2 = abs(r - 1.0), abs(s - 1.0)
    return (d1 * d2 + 2 * (1 - theta) * (m1 * d2 + m2 * d1)
            + 4 * (1 - theta + theta * math.log(theta)) * m1 * m2)


def minimum(rho, theta):
    assert rho >= 1 and 0 < theta < 1
    m = 2 * math.sqrt(rho) if theta <= 0.5 else rho + 1
    return rho + 1 + 4 * theta * math.log(theta) + (1 - 2 * theta) * m


def integrand(z, r, s, theta):
    # Genuine interval intersections for unit interval and interval of length s.
    oy = max(0.0, min(1.0, z) - max(0.0, z - s))
    threshold = theta * min(1.0, r) * min(1.0, s)
    if oy < threshold or oy == 0:
        return 0.0
    xratio = threshold / (oy * min(1.0, r))
    return max(0.0, 1.0 + r - 2 * min(1.0, r) * xratio)


def simpson(f, a, b, segments=1200):
    if b <= a:
        return 0.0
    assert segments % 2 == 0
    step = (b-a) / segments
    v = f(a) + f(b)
    v += 4 * sum(f(a + step * j) for j in range(1, segments, 2))
    v += 2 * sum(f(a + step * j) for j in range(2, segments, 2))
    return v * step / 3


def direct_overlap_quadrature(r, s, theta):
    # Independently integrate the true 1D rectangle-intersection function.
    # Logarithmic variable change resolves the narrow ramp near theta=0.
    m = min(1.0, s)
    plateau = abs(1.0 - s)
    ell = -math.log(theta)
    def ramp_integrand(u):
        y = max(m * theta, m * math.exp((u - 1) * ell))
        return integrand(y, r, s, theta) * ell * y
    return plateau * integrand(m, r, s, theta) + 2 * simpson(ramp_integrand, 0.0, 1.0)


def check():
    rng = random.Random(261027)
    tested = 0
    for i in range(180):
        rho = math.exp(rng.uniform(0, math.log(20)))
        r = math.exp(rng.uniform(-1.2, math.log(rho) + 1.2))
        s = rho/r
        t = (0.0003 if i % 19 == 0 else
             0.9997 if i % 23 == 0 else rng.uniform(0.02, 0.98))
        exact = formula(r, s, t)
        independent = direct_overlap_quadrature(r, s, t)
        assert abs(exact-independent) <= 6e-6 * max(1, exact), (i, r, s, t, exact, independent)
        tested += 1
    for rho in [1.0, 1.03, 1.5, 2.0, 5.0, 50.0]:
        for theta in [0.001, 0.1, 0.49, 0.5, 0.51, 0.85, 0.999]:
            val = minimum(rho, theta)
            assert val >= -1e-12
            candidate = math.sqrt(rho) if theta < 0.5 else 1.0
            assert math.isclose(formula(candidate, rho / candidate, theta), val,
                                rel_tol=1e-10, abs_tol=1e-10)
            for j in range(121):
                r = math.exp((j / 120 * 1.6 - 0.3) * math.log(max(rho, 1.001)))
                assert formula(r, rho / r, theta) + 1e-9 >= val
                tested += 1
    for rho in [1.01, 2.0, 9.0]:
        for theta in [0.11, 0.5, 0.9]:
            for j in range(101):
                r = 1+(rho-1)*j/100
                val = formula(r, rho/r, theta)
                base = minimum(rho, theta)
                if theta < .5:
                    deficit = (1-2*theta) * (r-math.sqrt(rho))**2/r
                elif theta > .5:
                    deficit = (2*theta-1)*(r-1)*(rho-r)/r
                else:
                    deficit = 0.0
                assert math.isclose(val-base, deficit, abs_tol=1e-10, rel_tol=1e-10)
                tested += 1
    print(f"CHECKS_OK {tested}; independent Simpson quadrature + phase, equality and deficit sweeps")


if __name__ == '__main__':
    check()
