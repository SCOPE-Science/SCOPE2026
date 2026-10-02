#!/usr/bin/env python3
"""
Numerical sanity checks for the generalized Kanter bound.

This script is supplementary: the proof in RESULT.md is analytic.
It verifies the stated Bessel/gamma inequality and the auxiliary
boundary-integral identity on representative parameter grids.
"""
import mpmath as mp

mp.mp.dps = 60

def phi(nu, r):
    # Phi_nu(2r)
    if r == 0:
        return 1 / (mp.power(2, nu) * mp.gamma(nu + 1))
    x = 2 * r
    return mp.e**(-x) * x**(-nu) * (mp.besseli(nu, x) + mp.besseli(nu + 1, x))

def rhs(nu, r):
    return mp.gamma(r + mp.mpf("0.5")) / (
        mp.sqrt(mp.pi) * mp.power(2, nu) * mp.gamma(r + nu + 1)
    )

def B(x, r):
    k = 2 * r
    return (
        (1 + x) * mp.e**(-k * (1 - x))
        + (1 - x) * mp.e**(-k * (1 + x))
        - 2 * x**k
    )

def boundary_integral(r):
    f = lambda x: B(x, r) / (1 - x*x)
    return mp.quad(f, [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), 1])

def boundary_closed_form(r):
    return mp.digamma(r + mp.mpf("0.5")) - mp.log(r) + mp.ei(-4*r)

nus = [
    mp.mpf("-0.49"), mp.mpf("-0.25"), mp.mpf("0"),
    mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("5")
]
rs = [
    mp.mpf("0.001"), mp.mpf("0.01"), mp.mpf("0.1"),
    mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"),
    mp.mpf("10"), mp.mpf("50")
]

min_gap = mp.inf
where = None
for nu in nus:
    for r in rs:
        gap = phi(nu, r) - rhs(nu, r)
        if gap < min_gap:
            min_gap, where = gap, (nu, r)
        if not (gap > 0):
            raise AssertionError(f"nonpositive gap at nu={nu}, r={r}: {gap}")

max_identity_error = mp.mpf("0")
for r in [mp.mpf("0.05"), mp.mpf("0.1"), mp.mpf("0.5"),
          mp.mpf("1"), mp.mpf("2"), mp.mpf("10")]:
    err = abs(boundary_integral(r) - boundary_closed_form(r))
    max_identity_error = max(max_identity_error, err)
    if boundary_closed_form(r) <= 0:
        raise AssertionError(f"boundary expression nonpositive at r={r}")

print("grid minimum strict gap =", mp.nstr(min_gap, 20), "at", where)
print("max boundary identity error =", mp.nstr(max_identity_error, 10))
print("all checks passed")
