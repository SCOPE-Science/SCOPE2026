#!/usr/bin/env python3
"""Reproducible finite checks for flux-optimized spectral separation on cycles.

Only Python's standard library is required. These finite checks are
corroboration, not a substitute for the all-size trigonometric proof.
"""
import cmath
import math
import random

PI = math.pi
checks = 0


def check(flag, label):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(f"check {checks}: {label}")


def numeric_gap(n, flux):
    v = [2.0 * math.cos((2 * PI * k + flux) / n) for k in range(n)]
    return min(abs(v[j] - v[k]) for j in range(n) for k in range(j))


def exact_gap(n, flux):
    a = PI / n
    theta = flux / n
    if n % 2:
        return 4.0 * math.sin(a) * min(math.sin(theta), math.sin(a - theta))
    return 4.0 * min(math.sin(2 * a) * math.sin(theta),
                     math.sin(a) * math.sin(a - theta))


def optimizer(n):
    a = PI / n
    return PI / 2.0 if n % 2 else n * math.atan(math.tan(a) / 3.0)


def optimal_gap(n):
    a = PI / n
    if n % 2:
        return 4.0 * math.sin(a) * math.sin(a / 2.0)
    return 8.0 * math.sin(a) ** 2 * math.cos(a) / math.sqrt(1.0 + 8.0 * math.cos(a) ** 2)


rng = random.Random(421731)
for n in range(3, 70):
    a = PI / n
    opt = optimizer(n)
    check(0.0 < opt < PI, f"optimizer interior n={n}")
    check(math.isclose(numeric_gap(n, opt), optimal_gap(n), rel_tol=2e-10, abs_tol=2e-12), f"optimizer value n={n}")
    check(math.isclose(exact_gap(n, opt), optimal_gap(n), rel_tol=2e-10, abs_tol=2e-12), f"closed optimum n={n}")
    for phi in [0.0, PI, PI / 2.0, opt, PI / 17.0, 13.0 * PI / 17.0] + [PI * rng.random() for _ in range(17)]:
        ng = numeric_gap(n, phi)
        eg = exact_gap(n, phi)
        check(math.isclose(ng, eg, rel_tol=2e-9, abs_tol=3e-13), f"spectrum gap n={n},phi={phi}")
        check(ng <= optimal_gap(n) + 2e-12, f"global max n={n},phi={phi}")
        if 1e-7 < phi < PI - 1e-7 and abs(phi - opt) > 1e-7:
            check(ng < optimal_gap(n) - 1e-12, f"strict optimum n={n},phi={phi}")
    # Eigenvector residual for the Hermitian nearest-neighbor magnetic ring:
    # (Hv)_j = exp(i theta) v_(j+1) + exp(-i theta) v_(j-1).
    phi = 0.23 * PI
    theta = phi / n
    for k in {0, n // 3, n - 1}:
        lam = 2.0 * math.cos((2.0 * PI * k + phi) / n)
        for j in {0, 1, n - 1}:
            v = lambda t: cmath.exp(2j * PI * k * (t % n) / n)
            hv = cmath.exp(1j * theta) * v(j + 1) + cmath.exp(-1j * theta) * v(j - 1)
            check(abs(hv - lam * v(j)) < 3e-12, f"eigenvector residual n={n},k={k},j={j}")

for n in range(3, 35):
    phi = optimizer(n)
    lam = [2.0 * math.cos((2 * PI * k + phi) / n) for k in range(n)]
    gap = numeric_gap(n, phi)
    for t in [0.5, 1.0, 10.0, 100.0]:
        # Evaluate the integrated Fourier interference exactly, term by term.
        probs = []
        for j in range(n):
            z = 0j
            for k in range(n):
                for l in range(n):
                    d = lam[k] - lam[l]
                    w = d * t / 2.0
                    sinc = math.sin(w) / w if abs(w) > 1e-12 else 1.0
                    z += cmath.exp(2j * PI * (k - l) * j / n - 1j * w) * sinc
            pp = (z / (n * n)).real
            check(-1e-12 <= pp <= 1.0 + 1e-12, f"averaged probability range n={n},j={j}")
            check(abs(pp - 1.0 / n) <= 2.0 * (n - 1) / (n * t * gap) + 1e-10,
                  f"Cesaro bound n={n},j={j},t={t}")
            probs.append(pp)
        check(abs(sum(probs) - 1.0) < 1e-9, f"normalization n={n},t={t}")

for n in [1001, 3001, 10000, 30000]:
    x = optimizer(n)
    check(abs(x - (PI / 2.0 if n % 2 else PI / 3.0)) < 3.2 / (n * n), f"parity flux limit n={n}")
    target = 2.0 * PI * PI if n % 2 else 8.0 * PI * PI / 3.0
    check(abs(n * n * optimal_gap(n) - target) < 300.0 / (n * n), f"parity gap limit n={n}")

print(f"PASS: {checks} numerical checks for n=3..69, aperiodic phases, Hermitian matrix modes, Cesaro estimates, and large-n limits.")
