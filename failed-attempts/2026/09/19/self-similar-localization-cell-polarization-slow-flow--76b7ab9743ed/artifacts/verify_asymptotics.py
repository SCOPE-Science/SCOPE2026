"""Symbolic checks for the cell-polarization localization asymptotics."""

import sympy as sp

m, C, t = sp.symbols("m C t", positive=True)
q = 1 + sp.Rational(2, 1) / m
rho = sp.Rational(2, 1) / (m + 2)
A = C ** (-m / (m + 2))
sigma = A * t ** (-m / (m + 2))
Phi = A * t ** rho
phi = sp.diff(Phi, t)

checks = {
    "inverse_exponent": sp.simplify(1 / q - m / (m + 2)),
    "clock_normalization": sp.simplify(t * C * sigma ** q - 1),
    "Phi_over_t_sigma": sp.simplify(Phi / (t * sigma) - 1),
    "phi_over_sigma": sp.simplify(phi / sigma - sp.Rational(2, 1) / (m + 2)),
    "sigma_log_derivative": sp.simplify(t * sp.diff(sigma, t) / sigma + m / (m + 2)),
}

r = sp.symbols("r", nonnegative=True)
radial_ratio = sp.simplify(2 * sp.integrate((1 - r**m) * r, (r, 0, 1)))
checks["homogeneous_C_over_B"] = sp.simplify(radial_ratio - m / (m + 2))

support = sp.simplify((m + 2) / m * C * sigma ** (sp.Rational(2, 1) / m))
checks["morse_sigma"] = sp.simplify(sigma.subs(m, 2) - 1 / sp.sqrt(C * t))
checks["morse_Phi"] = sp.simplify(Phi.subs(m, 2) - sp.sqrt(t / C))
checks["morse_phi"] = sp.simplify(phi.subs(m, 2) - 1 / (2 * sp.sqrt(C * t)))
checks["morse_support_area"] = sp.simplify(support.subs(m, 2) - 2 * sp.sqrt(C / t))

failed = {name: value for name, value in checks.items() if value != 0}
print("sympy_version=" + sp.__version__)
for name, value in checks.items():
    print(f"{name}={value}")
print("all_symbolic_checks_passed=" + str(not failed))
if failed:
    raise SystemExit(1)
