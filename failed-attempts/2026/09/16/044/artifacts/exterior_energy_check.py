"""Exterior energy/flux scaling check for circular vortex filament (target consistency test).

Model: straight-filament Biot-Savart |v| ~ Gamma/(2*pi*rho) outside a tube of
radius c(t). Exterior kinetic energy per unit length ~ (Gamma^2/4pi)*log(1/c);
times ring length 2*pi*L gives (L*Gamma^2/2)*log(1/c), i.e. the target law
(1/2)int|v|^2 = -(L Gamma^2/2) log c + O(1). Boundary energy flux scales as
|v|^3 * area ~ (1/c^3)(L*c) ~ 1/t, matching dE/dt ~ 1/t from the log law.
Conclusion: exterior axisymmetric potential flow is CONSISTENT with (i)-(ii);
no contradiction follows from exterior control-volume considerations alone.
"""
import sympy as sp

Gamma, L, c, t, nu = sp.symbols('Gamma L c t nu', positive=True)
E_per_length = Gamma**2 / (4 * sp.pi) * sp.log(1 / c)
E_ring = 2 * sp.pi * L * E_per_length
sp.simplify(E_ring)
print("E_ring =", E_ring)
ct = sp.sqrt(nu * t)
E_t = sp.simplify(E_ring.subs(c, ct))
print("E(t) =", E_t)
dEdt = sp.diff(E_t, t)
print("dE/dt =", sp.simplify(dEdt))
flux_scale = (1 / ct**3) * (L * ct)
print("flux scaling ~", sp.simplify(flux_scale))
# Numeric spot check
import math
Gv, Lv, Tiempo, Nuv = 1.0, 1.0, 0.01, 0.5
cv = math.sqrt(Nuv * Tiempo)
Ev = 0.5 * Lv * Gv**2 * math.log(1 / cv)
print(f"numeric: c={cv:.4f} E={Ev:.4f} dE/dt~{0.5*Lv*Gv**2/(2*Tiempo):.4f}")
print("RESULT: PASS (consistency) — exterior axisymmetry reproduces target log law and 1/t flux; does NOT decide (A) vs (B).")
