"""Exact algebraic checks for the three-species Wilhelm oscillator.

Requires Python 3 and SymPy. The invariant-measure theorem is analytical;
these checks only verify its pointwise identities and equilibrium.
"""
import sympy as s

x, y, z = s.symbols("x y z", positive=True)
k1, k2, k3, k4 = s.symbols("k1 k2 k3 k4", positive=True)
a = s.sqrt(2 * k4 / k2)
f = s.Matrix([k3 * y * z - 2 * k2 * x**2,
              k1 * y - k3 * y * z,
              k2 * x**2 - 2 * k4 * z**2])
zstar = k1 / k3
xstar = a * zstar
ystar = 4 * k1 * k4 / k3**2
assert all(s.simplify(v.subs({x: xstar, y: ystar, z: zstar})) == 0 for v in f)
# Positive-coordinate logarithmic drift produces conditional catalysis law.
assert s.simplify(f[1] / y - (k1 - k3 * z)) == 0
# Sum-of-species drift produces the exact variance defect.
assert s.simplify(sum((f[0], f[1], 2 * f[2])) - (k1 * y - 4 * k4 * z**2)) == 0
# Logarithmic z drift produces the nonnegative x-mean deficit.
weighted = (x - a * z)**2 / (2 * a * z)
assert s.simplify(weighted + x - a * z - f[2] / (2 * a * k2 * z)) == 0
# Coordinatewise conditional flux balances.
assert s.simplify(f[0] - (k3 * y * z - 2 * k2 * x**2)) == 0
assert s.simplify(f[2] - (k2 * x**2 - 2 * k4 * z**2)) == 0
print("WILHELM_FLUX_IDENTITIES_OK")
