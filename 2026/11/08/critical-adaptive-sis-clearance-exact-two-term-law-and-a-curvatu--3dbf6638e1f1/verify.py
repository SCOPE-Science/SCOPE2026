#!/usr/bin/env python3
"""Exact response-jet identities and diagnostic ODE checks for a critical adaptive SIS model."""

import math

import sympy as sp
from scipy.integrate import solve_ivp


def exact_checks():
    y, tau = sp.symbols("y tau", real=True)
    l0, l1, a1, a2 = sp.symbols("l0 l1 a1 a2", real=True)
    h1 = a1 / l0
    k = 1 - tau * h1
    h2 = (a2 + (k - l1) * h1) / l0
    w = h1 * y + h2 * y**2
    # At the exact threshold, the two-dimensional field in (y,w) begins:
    fy = -y**2 + tau * y * (1 - y) * w
    fw = a1 * y + a2 * y**2 - (l0 + l1 * y) * w
    defect = sp.expand(sp.diff(w, y) * fy - fw)
    for order in (0, 1, 2):
        assert sp.simplify(defect.coeff(y, order)) == 0
    assert sp.simplify(sp.expand(fy).coeff(y, 2) + k) == 0
    assert sp.simplify(sp.expand(fy).coeff(y, 3) - tau * (h2 - h1)) == 0
    q = sp.symbols("q", nonnegative=True)
    b = 1 + y + q * y * y
    z0 = sp.Rational(1, 2)
    L = b + 1
    A = (1 - z0) - z0 * b
    ll0 = L.subs(y, 0)
    ll1 = sp.diff(L, y).subs(y, 0)
    aa1 = sp.diff(A, y).subs(y, 0)
    aa2 = sp.diff(A, y, 2).subs(y, 0) / 2
    hh1 = aa1 / ll0
    kk = 1 - 2 * hh1
    hh2 = sp.simplify((aa2 + (kk - ll1) * hh1) / ll0)
    bb = sp.simplify(2 * (hh1 - hh2) / kk)
    assert (ll0, ll1, aa1, hh1, kk) == (
        2, 1, -sp.Rational(1, 2), -sp.Rational(1, 4), sp.Rational(3, 2)
    )
    assert sp.simplify(hh2 + q / 4 + sp.Rational(1, 16)) == 0
    assert sp.simplify(bb - q / 3 + sp.Rational(1, 4)) == 0
    assert sp.solve(bb, q) == [sp.Rational(3, 4)]
    assert bb.subs(q, 0) == -sp.Rational(1, 4)
    assert bb.subs(q, 1) == sp.Rational(1, 12)


def numerical_diagnostics():
    for curvature in (0.0, 1.0):
        coefficient = curvature / 3.0 - 0.25

        def ode(t, state):
            prevalence, contacts = state
            return (
                -prevalence + 2.0 * prevalence * (1 - prevalence) * contacts,
                -(1 + prevalence + curvature * prevalence * prevalence) * contacts
                + 1 - contacts,
            )

        sol = solve_ivp(
            ode,
            (0.0, 10000.0),
            (0.35, 0.9),
            method="BDF",
            rtol=1e-11,
            atol=1e-14,
            t_eval=(1000.0, 10000.0),
        )
        assert sol.success, sol.message
        remainder = []
        for t, prevalence in zip(sol.t, sol.y[0]):
            assert 0 < prevalence < 1
            assert abs(prevalence * t - (2 / 3)) < 0.003
            remainder.append(1 / prevalence - 1.5 * t - coefficient * math.log(t))
        # The residual converges to a trajectory-dependent constant.
        assert abs(remainder[-1] - remainder[0]) < 0.02, remainder
        print("curvature", curvature, "expected_log_coefficient", coefficient,
              "remainder_diagnostics", remainder)


if __name__ == "__main__":
    exact_checks()
    numerical_diagnostics()
    print("VERIFY_OK")
