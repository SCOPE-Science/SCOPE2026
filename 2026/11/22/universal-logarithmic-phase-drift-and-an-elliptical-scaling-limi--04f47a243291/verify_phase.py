"""Finite independent diagnostics for the exact neutral cubic business-cycle map.

This is a reproducibility aid, not a proof of infinite-time assertions.
Requires only the Python standard library.
"""
import cmath
import math


def check(alpha, count=300_000):
    s = math.sqrt(1 - alpha * alpha)
    c = math.sqrt((1 - alpha) / (1 + alpha))
    theta = math.acos(alpha)
    tau = c / 2
    expected = (1 + alpha) / (3 * alpha)
    omega = complex(alpha, s)
    a = 3 * alpha / (2 * (1 + alpha))
    C = -a * (1 + 1j * c)
    d = (1 + 1j * c) / 2
    assert abs(C - (-6 * alpha * d * d * d.conjugate())) < 1e-12
    assert abs(C / omega - complex(-a, a * c)) < 1e-12

    # Compare the exact real map with the full polynomial complex map.
    x, y = 0.15, -0.03
    z = complex((1 - alpha) * x + y, s * x)
    for _ in range(100):
        xn = x + y
        yn = -2 * (1 - alpha) * x + (2 * alpha - 1) * y - 2 * alpha * y ** 3
        zz = complex((1 - alpha) * xn + yn, s * xn)
        direct = omega * z - 2 * alpha * (z.real - c * z.imag) ** 3
        assert abs(zz - direct) < 5e-14
        x, y, z = xn, yn, zz

    # Start a separate orbit and lift its physical angular increments.
    x, y = 0.15, -0.03
    z = complex((1 - alpha) * x + y, s * x)
    unwrapped = cmath.phase(z)
    measurements = {}
    for n in range(1, count + 1):
        xn = x + y
        yn = -2 * (1 - alpha) * x + (2 * alpha - 1) * y - 2 * alpha * y ** 3
        zz = complex((1 - alpha) * xn + yn, s * xn)
        unwrapped += cmath.phase(zz / z)
        x, y, z = xn, yn, zz
        if n in (100_000, count):
            scaled_q = n * abs(z) ** 2
            corrected_phi = unwrapped - n * theta - tau * math.log(n)
            measurements[n] = (scaled_q, corrected_phi)
    q_early, ph_early = measurements[100_000]
    q_late, ph_late = measurements[count]
    assert abs(q_late - expected) < 0.003, (alpha, q_late, expected)
    assert abs(q_late - expected) < abs(q_early - expected)
    assert abs(ph_late - ph_early) < 0.003, (alpha, ph_early, ph_late)
    print("PASS alpha=%.12f nQ=%.9f expected=%.9f phase100k=%.9f phase300k=%.9f" %
          (alpha, q_late, expected, ph_early, ph_late))


if __name__ == "__main__":
    check(0.75)                       # Irrational theta/(2*pi)
    check(math.cos(math.pi / 5))     # Rational theta/(2*pi) = 1/10
    check(0.99)                       # Small but strictly positive angular drift
    print("PASS: exact identities and finite diagnostics")
