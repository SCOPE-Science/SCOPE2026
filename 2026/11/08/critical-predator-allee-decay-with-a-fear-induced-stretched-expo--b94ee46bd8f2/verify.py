"""Exact algebraic checks and optional finite-time diagnostics for a critical Leslie-Gower model."""
from fractions import Fraction
import math

import sympy as sp

x, y, r, e, b, p, a, k, s, n, c = sp.symbols(
    "x y r e b p a k s n c", positive=True
)
f = x * (r / (1 + k * y) - e - b * x - p * y / (x + a * y))
g = s * y**2 * (1 / (y + c) - 1 / (n * x + c))
h = c / (s * y) + c**2 / (2 * s * y**2)
assert sp.cancel(sp.diff(h, y) * g - (1 - n * x * (y + c) / (y * (n * x + c)))) == 0

mu = e + p / a - r
z = x / y
remainder = -b * x + p * z / (a * (a + z)) - r * k**3 * y**3 / (1 + k * y)
assert sp.cancel(f / x - (-mu - r * k * y + r * k**2 * y**2 + remainder)) == 0

# The two asymptotic coefficients follow from h(y)=t+constant+o(1).
E = sp.symbols("E", positive=True)
y_approx = c / sp.sqrt(2 * s) * E + c / (2 * s) * E**2
assert sp.simplify(sp.limit(E**2 * h.subs(y, y_approx), E, 0)) == 1
assert sp.simplify(sp.limit(E * (h.subs(y, y_approx) - E**(-2)), E, 0)) == 0
sigma = r * k * c * (k * c - 1) / (2 * s)
assert sp.simplify(sigma - (-r * k * c / (2 * s) + r * k**2 * c**2 / (2 * s))) == 0

# The explicit all-rational parameter wedge uses q=1/10, delta=1/4.
q, delta = Fraction(1, 10), Fraction(1, 4)
mu_ex = Fraction(1, 2)
assert q < 1
assert Fraction(1, 2) - Fraction(1, 1) / (1 + q) < -Fraction(3, 4) * mu_ex
assert delta**2 < mu_ex / 4
assert sp.simplify(mu.subs({r: 1, e: sp.Rational(1, 2), p: 1, a: 1}) - sp.Rational(1, 2)) == 0
assert sp.simplify(sigma.subs({r: 1, k: 2, c: 1, s: 1}) - 1) == 0

# Non-certifying numerical illustration; logx avoids underflow in the state variable.
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, state):
    logx, yy = state
    xx = math.exp(logx) if logx > -700 else 0.0
    return [1 / (1 + 2 * yy) - 0.5 - xx - yy / (xx + yy),
            yy * yy * (1 / (yy + 1) - 1 / (xx + 1))]

sol = solve_ivp(rhs, (0, 8000), (math.log(0.002), 0.2),
                t_eval=[400, 1600, 8000], rtol=1e-10, atol=1e-12)
assert sol.success
for t, logx, yy in zip(sol.t, *sol.y):
    assert yy > 0
    diag = logx + 0.5 * t + 2 * math.sqrt(2 * t) - math.log(t)
    assert math.isfinite(diag)
    print("t", t, "rescaled_predator", round(math.sqrt(2 * t) * yy, 8),
          "normalized_prey_log", round(diag, 8))
print("VERIFY_OK")
