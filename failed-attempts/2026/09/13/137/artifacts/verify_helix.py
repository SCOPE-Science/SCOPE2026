"""Verify the helix counterexample: unit speed, curvature 1/2, torsion 1/2."""
import sympy as sp

t = sp.symbols('t', real=True)
c = sp.sqrt(2)
g = sp.Matrix([sp.cos(t / c), sp.sin(t / c), t / c])
gp = g.diff(t)
gpp = gp.diff(t)
gppp = gpp.diff(t)

speed2 = sp.simplify(gp.dot(gp))
kappa = sp.simplify(gpp.norm())  # = |g''| for unit-speed curves
cross = gp.cross(gpp)
tau = sp.simplify(cross.dot(gppp) / cross.dot(cross))

print('speed^2 =', speed2)
print('kappa   =', kappa)
print('tau     =', tau)
assert speed2 == 1
assert kappa == sp.Rational(1, 2)
assert tau == sp.Rational(1, 2)

# Injectivity on [0,1] via strictly increasing z-coordinate: z(t) = t/sqrt(2).
assert float(g[2].subs(t, 0)) == 0.0
assert abs(float(g[2].subs(t, 1)) - 1 / float(c)) < 1e-12
print('OK: unit speed, kappa=1/2, tau=1/2, injective on [0,1].')
