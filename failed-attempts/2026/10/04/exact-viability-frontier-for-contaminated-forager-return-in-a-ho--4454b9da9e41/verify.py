from __future__ import annotations
import math
import sympy as sp

B, E, y, p = sp.symbols("B E y p", positive=True)
R = B*E*(1 + p*(y - 1 - E)) / ((y - E)*(1 - p*E))

expected_dp = B*E*(y - 1) / ((y - E)*(1 - p*E)**2)
expected_dy = B*E*(p - 1) / ((1 - p*E)*(y - E)**2)

assert sp.simplify(sp.diff(R, p) - expected_dp) == 0
assert sp.simplify(sp.diff(R, y) - expected_dy) == 0
assert sp.simplify(R.subs(p, 1) - B*E/(1-E)) == 0

pc = (y - E - B*E) / (E*(B*(y - 1 - E) + (y - E)))
assert sp.simplify(R.subs(p, pc) - 1) == 0

limit_pc = sp.simplify(sp.limit(pc, y, sp.oo))
assert sp.simplify(limit_pc - 1/(E*(1+B))) == 0

beta = 2900.0
chi = 11000.0
mu = 0.1
alpha = 0.03
Bv = beta/(2.0*chi)
Ev = math.exp(-mu)
yv = math.exp(alpha)

alpha_star = math.log(Ev*(1.0+Bv))
pc_val = (yv - Ev - Bv*Ev) / (Ev*(Bv*(yv - 1.0 - Ev) + (yv - Ev)))

pv = 0.8
yc = Ev*(Bv*(1.0 - pv*(1.0+Ev)) + (1.0-pv*Ev)) / (1.0-pv*Ev-Bv*Ev*pv)
alpha_c = math.log(yc)

assert abs(alpha_star - 0.023825350112346055) < 1e-14
assert abs(pc_val - 0.6768201794833469) < 1e-14
assert abs(alpha_c - 0.03618032813143622) < 1e-14
assert abs(pc_val - 0.6768) < 3e-5
assert abs(alpha_c - 0.0362) < 3e-5

R0 = Bv*Ev/(1.0-Ev)
assert R0 > 1.0
assert Ev*(1.0+Bv) > 1.0

print("VERIFY_OK")
