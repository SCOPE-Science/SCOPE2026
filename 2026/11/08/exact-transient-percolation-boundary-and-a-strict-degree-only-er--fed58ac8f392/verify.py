"""Independent numerical and symbolic checks of a transient age-kernel threshold.

Run: python verify.py
Dependencies: Python 3, numpy, scipy, sympy.
This script supplements, but does not replace, the analytic operator proof.
"""

import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import j0, j1, y0, y1, jn_zeros
from numpy.polynomial.legendre import leggauss


def moments(u):
    e = math.exp(-u)
    m1 = (1 - e**2) / 2
    m2 = (1 - 3 * e**2 + 2 * e**3) / 3
    return m1, m2


def degree_only_threshold(u):
    m1, m2 = moments(u)
    return m1 / m2


def operator_norm(u, n=180):
    points, weights = leggauss(n)
    xs = (points + 1) * (u / 2)
    ws = weights * (u / 2) * np.exp(-xs)
    xs = np.append(xs, u)
    ws = np.append(ws, np.exp(-u))
    # Symmetric Nyström matrix includes the endpoint atom of mass exp(-u).
    matrix = np.sqrt(np.outer(ws, ws)) * np.minimum.outer(xs, xs)
    return np.linalg.eigvalsh(matrix)[-1]


def robin_residual(ell, u):
    def ode(x, y):
        return [y[1], -math.exp(-x) * y[0] / ell]
    solution = solve_ivp(
        ode, (0, u), [0.0, 1.0],
        rtol=2e-12, atol=2e-13,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    y, dy = solution.y[:, -1]
    return ell * dy - math.exp(-u) * y


def principal_eigenvalue(u):
    near = operator_norm(u, n=120)
    return brentq(
        lambda ell: robin_residual(ell, u),
        near * 0.9, near * 1.1,
        xtol=3e-14,
    )


def bessel_residual(ell, u):
    q = 2 / math.sqrt(ell)
    v = q * math.exp(-u / 2)
    return (y0(q) * (2 * j1(v) - v * j0(v))
            - j0(q) * (2 * y1(v) - v * y0(v)))


def main():
    checks = 0
    x, u = sp.symbols('x u', positive=True, real=True)
    # For a bounded age X=min(E,u), E~Exp(1), expectations include an endpoint atom.
    g = 1-sp.exp(-x)
    for power, formula in [
        (1, (1-sp.exp(-2*u))/2),
        (2, (1-3*sp.exp(-2*u)+2*sp.exp(-3*u))/3),
    ]:
        moment = sp.integrate(sp.exp(-x)*g**power, (x, 0, u)) \
                 + sp.exp(-u)*(1-sp.exp(-u))**power
        assert sp.simplify(sp.expand(moment-formula)) == 0
        checks += 1

    values = [0.1, 0.5, 1.0, 2.0, 4.0, 6.0]
    critical_values = []
    for horizon in values:
        ell = principal_eigenvalue(horizon)
        quad120 = operator_norm(horizon, 120)
        quad240 = operator_norm(horizon, 240)
        assert 0 < ell < horizon
        checks += 1
        assert abs(quad240-ell) < 2e-5
        checks += 1
        assert abs(quad240-ell) < abs(quad120-ell)
        checks += 1
        assert abs(robin_residual(ell, horizon)) < 4e-11
        checks += 1
        assert abs(bessel_residual(ell, horizon)) < 6e-9
        checks += 1
        true_critical = 1/ell
        closure_critical = degree_only_threshold(horizon)
        assert true_critical < closure_critical
        checks += 1
        critical_values.append(true_critical)
        print(f"u={horizon:g}: exact={true_critical:.12f}; "
              f"degree-only={closure_critical:.12f}")

    assert all(a > b for a, b in zip(critical_values, critical_values[1:]))
    checks += 1
    jroot = jn_zeros(0, 1)[0]
    stationary = jroot*jroot/4
    assert 1.44 < stationary < 1.45
    checks += 1
    assert critical_values[-1] > stationary
    checks += 1
    assert abs(critical_values[-1]-stationary) < 3e-5
    checks += 1

    print(f"Stationary exact={stationary:.12f}; degree-only=1.500000000000")
    print(f"{checks} verification assertions passed")


if __name__ == '__main__':
    main()
