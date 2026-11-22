"""Supplementary finite checks for normalized generalized Fock kernel amplification.

Run with Python 3.10+ and no external packages: python verify.py.
Finite numerical checks do not establish the asymptotic theorem.
"""
import cmath
import math


def normalized_kernel_modulus(m: float, radius: float, theta: float) -> float:
    """Stable positive-coefficient normalization of the Mittag-Leffler kernel."""
    peak = m * radius ** (2 * m)
    spread = m * radius ** m
    top = max(50, int(peak + 23 * spread + 120))
    logs = [2 * n * math.log(radius) - math.lgamma((n + 1) / m)
            for n in range(top + 1)]
    shift = max(logs)
    weights = [math.exp(v - shift) for v in logs]
    denom = sum(weights)
    value = sum(w * cmath.exp(1j * n * theta)
                for n, w in enumerate(weights)) / denom
    return abs(value)


def log_amplification_pure(m: float, degree: int, coefficient: float,
                            radius: float, theta: float) -> float:
    phase_gain = 2 * abs(coefficient) * radius ** degree * abs(
        math.sin(degree * theta / 2))
    return phase_gain + math.log(normalized_kernel_modulus(m, radius, theta))


def prediction(m: float, degree: int, coefficient: float, radius: float):
    theta = degree * abs(coefficient) / (m * m) * radius ** (degree - 2 * m)
    value = degree * degree * coefficient * coefficient / (2 * m * m) * (
        radius ** (2 * degree - 2 * m))
    return theta, value


def main():
    checks = 0
    for a in (0.2, 0.5, 1.3):
        for r in (3.0, 5.0, 8.0, 13.0):
            # The Gaussian (m=d=1) saddle is exactly solvable.
            theta = 2 * math.asin(a / (2 * r))
            val = log_amplification_pure(1.0, 1, a, r, theta)
            assert abs(val - a * a / 2) < 1e-9, (a, r, val)
            checks += 1
    for m, d, a, radii, relative_tolerance in (
        (0.75, 1, 1.3, (15.0, 35.0, 65.0), 0.025),
        (1.25, 1, 1.3, (15.0, 35.0, 65.0), 0.002),
        (1.5, 1, 0.8, (10.0, 20.0), 0.002),
        (1.25, 2, 0.2, (4.0, 6.0, 8.0), 0.012),
        (1.5, 2, 0.25, (4.0, 6.0, 8.0), 0.008),
        (2.0, 2, 0.25, (4.0, 6.0, 8.0), 0.005),
    ):
        for r in radii:
            theta, target = prediction(m, d, a, r)
            observed = log_amplification_pure(m, d, a, r, theta)
            relative = abs(observed - target) / target
            assert relative < relative_tolerance, (m, d, a, r, observed, target, relative)
            checks += 1
    # Confirm the kernel modulus is at most one at test angles, by triangle inequality.
    for m, r in ((0.75, 8.0), (1.0, 7.0), (1.5, 5.0)):
        for th in (0.0, 0.015, 0.04, 0.11, 0.23):
            v = normalized_kernel_modulus(m, r, th)
            assert -1e-12 <= v <= 1 + 1e-12
            checks += 1
    print(f"FINITE_CHECKS_OK {checks}")


if __name__ == "__main__":
    main()
