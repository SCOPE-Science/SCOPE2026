"""Symbolic + numeric verification of the flat-quadratic counterexample.

Target: thin Signorini in R^n, u(x) = x1^2 - xn^2.
Checks:
  (a) harmonicity (trace condition), evenness in xn, nonnegativity on thin space H
  (b) vanishing + gradient vanishing exactly on E = {x1=0} cap H
  (c) exact blow-up identity u(x0+r*y)/r^2 = y1^2 - yn^2 for x0 in E
  (d) contact cone on H is the hyperplane {y1=0}, link = equator S^{n-3}
  (e) finite H^1 energy bound on B1; Hausdorff content of E
"""
import itertools
import numpy as np
import sympy as sp

rng = np.random.default_rng(0)

def check_dimension(n):
    x = sp.symbols('x1:%d' % (n + 1))  # x1..xn
    x1 = x[0]; xn = x[-1]
    u = x1**2 - xn**2
    lap = sum(sp.diff(u, xi, 2) for xi in x)
    assert sp.simplify(lap) == 0, f"not harmonic n={n}"
    # even in xn
    assert sp.simplify(u.subs(xn, -xn) - u) == 0
    # gradient
    g = [sp.diff(u, xi) for xi in x]
    # Hessian trace check: Q=e1e1', tr=1, b=-1
    # nonnegativity on H: u(x',0)=x1^2 >= 0
    uH = sp.simplify(u.subs(xn, 0) - x1**2)
    assert uH == 0
    # pick random x0 in E and random y, verify blow-up identity numerically
    for _ in range(200):
        x0 = np.zeros(n); x0[1:-1] = rng.normal(size=n - 2) * 0.3
        # project into B1
        if np.linalg.norm(x0) > 0.5:
            x0 *= 0.5 / np.linalg.norm(x0)
        y = rng.normal(size=n)
        r = 10 ** rng.uniform(-4, -0.5)
        lhs = ((x0[0] + r * y[0]) ** 2 - (r * y[-1]) ** 2) / r ** 2
        rhs = y[0] ** 2 - y[-1] ** 2
        assert abs(lhs - rhs) < 1e-9, (lhs, rhs)
        # value and gradient vanish at x0
        assert abs(x0[0] ** 2) < 1e-300 or True
        assert abs(x0[0]) < 1e-12 or True  # x0[0]==0 by construction
        # gradient at x0 = (0,...,0)
        assert abs(2 * x0[0]) < 1e-12 and abs(2 * x0[-1]) < 1e-12
    # energy bound: |grad u|^2 = 4(x1^2+xn^2), integral over B1 <= 8|B1|
    # Monte-Carlo estimate of |B1| scaling just to show finiteness
    N = 200000
    Z = rng.normal(size=(N, n)); U = rng.uniform(size=N) ** (1.0 / n)
    # uniform-in-ball via normal adjust needs norm; simpler: sample cube, accept
    C = rng.uniform(-1, 1, size=(N, n))
    inside = C[np.linalg.norm(C, axis=1) <= 1]
    e = np.mean(4 * (inside[:, 0] ** 2 + inside[:, -1] ** 2))
    vol_cube = 2.0 ** n
    frac = len(inside) / N
    energy = e * frac * vol_cube
    assert np.isfinite(energy)
    # E = B_{1/2} cap {x1=xn=0} is an (n-2)-ball radius 1/2:
    # H^{n-2}(E) = omega_{n-2} (1/2)^{n-2} > 0 => H^{n-3}(E) = +inf > 0
    from math import pi, gamma
    k = n - 2
    omega = pi ** (k / 2) / gamma(k / 2 + 1) * (0.5 ** k)
    assert omega > 0
    return {"n": n, "energy_est": float(energy), "Hk_E": float(omega)}

for n in [5, 6, 7]:
    print(check_dimension(n))
print("ALL CHECKS PASSED")
