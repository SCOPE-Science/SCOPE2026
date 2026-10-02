#!/usr/bin/env python3
"""Numerical checks for the spherical Morse-Bott example in RESULT.md."""
import math

# Unit sphere, normalized signal deficit h=z^2/2.
# The maximum set is the equator.  In geodesic normal coordinates the
# normal Hessian is 1 and the equator has length 2*pi.
C = 8.0 * math.pi * math.sqrt(2.0) / 3.0
K = C ** (-2.0 / 3.0)
U0 = 1.0 / (4.0 * math.pi)  # constant initial density, unit total mass


def G(s: float) -> float:
    """Exact cap integral int_{S^2} (s-h)_+ dS for 0<=s<=1/2."""
    if not (0.0 <= s <= 0.5):
        raise ValueError("s outside the exact-formula range")
    return C * s ** 1.5


def mass_residual(omega: float, t: float) -> float:
    B = t / (1.0 - omega)
    theta = omega + U0 / B
    return B * G(theta) - 1.0


def solve_omega(t: float) -> float:
    lo, hi = 0.0, 0.25
    flo, fhi = mass_residual(lo, t), mass_residual(hi, t)
    if not (flo < 0.0 < fhi):
        raise RuntimeError("root is not bracketed")
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if mass_residual(mid, t) > 0.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def A_of_t(t: float) -> float:
    omega = solve_omega(t)
    return t * omega / (1.0 - omega)


print(f"C_curve={C:.15f}")
print(f"K=C^(-2/3)={K:.15f}")
print(f"predicted_phi_prefactor=K/3={K/3.0:.15f}")
print(f"exact_G_ratio={G(1e-4)/(1e-4**1.5):.15f}")

last_clock = None
for t in (1e2, 1e3, 1e4, 1e5, 1e6):
    omega = solve_omega(t)
    clock = omega * t ** (2.0 / 3.0)
    tG = t * G(omega)
    last_clock = clock
    print(f"clock t={t:.0e} omega*t^(2/3)={clock:.12f} tG={tG:.12f}")

last_phi = None
for t in (1e3, 1e4, 1e5, 1e6):
    eps = 1e-4
    phi = (A_of_t(t * (1.0 + eps)) - A_of_t(t * (1.0 - eps))) / (2.0 * eps * t)
    scaled = phi * t ** (2.0 / 3.0)
    last_phi = scaled
    print(f"phi t={t:.0e} phi*t^(2/3)={scaled:.12f}")

assert abs(G(1e-4)/(1e-4**1.5) - C) < 1e-12
assert abs(last_clock / K - 1.0) < 5e-3
assert abs(last_phi / (K/3.0) - 1.0) < 5e-4
print("all_checks_passed=True")
