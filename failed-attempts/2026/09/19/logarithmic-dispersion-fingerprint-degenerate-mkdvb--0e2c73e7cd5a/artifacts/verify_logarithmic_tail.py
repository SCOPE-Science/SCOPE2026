import sympy as sp

w, nu = sp.symbols("w nu", positive=True)
a3, a4 = sp.symbols("a3 a4")
g = 3*w**2 + a3*w**3 + a4*w**4
p = 3*w**2 + w**3
residual = sp.expand(nu*g*sp.diff(g, w) - (g-p))
a3_value = sp.solve(sp.Eq(residual.coeff(w, 3), 0), a3)[0]
a4_value = sp.solve(sp.Eq(residual.subs(a3, a3_value).coeff(w, 4), 0), a4)[0]
print("center_manifold_a3 =", sp.simplify(a3_value))
print("center_manifold_a4 =", sp.simplify(a4_value))
print("center_manifold_residual =", sp.series(residual.subs({a3:a3_value, a4:a4_value}), w, 0, 5))

mu, kappa, s, x = sp.symbols("mu kappa s x", positive=True)
A, B, C = sp.symbols("A B C")
v = A/x + (B*sp.log(x)+C)/x**2
profile_residual = sp.expand(kappa*sp.diff(v, x, 2) - mu*sp.diff(v, x) - (3*s*v**2-v**3))
t = sp.symbols("t", positive=True)
series = sp.series(profile_residual.subs(x, 1/t), t, 0, 4).removeO().expand()
coef2 = series.coeff(t, 2)
coef3_constant = series.coeff(t, 3).subs(sp.log(t), 0)
A_value = mu/(3*s)
B_value = sp.solve(sp.Eq(sp.simplify(coef3_constant.subs(A, A_value)), 0), B)[0]
print("profile_A =", sp.simplify(A_value))
print("profile_B =", sp.simplify(B_value))
print("dispersion_fingerprint =", sp.simplify(B_value-B_value.subs(kappa, 0)))

Af, Cf, vv = sp.symbols("Af Cf vv", nonzero=True)
qa, qd = sp.symbols("qa qd")
q = qa*vv**2 + qd*vv**3
general_residual = sp.expand(mu*q + kappa*q*sp.diff(q, vv) - (Af*vv**2+Cf*vv**3))
qa_value = sp.solve(sp.Eq(general_residual.coeff(vv, 2), 0), qa)[0]
qd_value = sp.solve(sp.Eq(general_residual.subs(qa, qa_value).coeff(vv, 3), 0), qd)[0]
log_coefficient = sp.simplify(-(qd_value/qa_value)/(qa_value**2))
print("general_q_a =", qa_value)
print("general_q_d =", qd_value)
print("general_profile_log_coefficient =", log_coefficient)
print("general_dispersion_shift =", sp.simplify(log_coefficient-log_coefficient.subs(kappa, 0)))

expected_B = mu**2/(27*s**3) + 2*kappa/(3*s)
assert sp.simplify(a3_value-(1+18*nu)) == 0
assert sp.simplify(a4_value-15*nu*(1+18*nu)) == 0
assert sp.simplify(B_value-expected_B) == 0
assert sp.simplify((B_value-B_value.subs(kappa, 0))-2*kappa/(3*s)) == 0
assert sp.simplify(log_coefficient-(-Cf*mu**2/Af**3+2*kappa/Af)) == 0
print("all_symbolic_checks_passed=True")
