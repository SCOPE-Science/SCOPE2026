"""Verify curvature formulas and the a*=1/2 sign bound (TARGET artifact).

Checks (sympy + elementary rigorous bound):
 1. For g = diag(e^{-2f},e^{-2f},e^{2f},e^{2f}) with x1-dependent f:
    R = 2 e^{2f} (-f'' - 3 f'^2).
 2. With V = -k d11 k, k = e^f: R/6 - V = (2/3) f'' e^{2f}.
 3. Rigorous bound: a2(1/2) <= -pi^2/72 < 0 (in (4pi)^{-2} dx normalization).
"""
import sympy as sp
import math

x = sp.symbols('x')
f = sp.Function('f')(x)
fp = sp.diff(f, x)
fpp = sp.diff(fp, x)

# Nonzero Christoffel symbols for g_low = diag(e^{-2f},e^{-2f},e^{2f},e^{2f}}),
# coords 0..3, f = f(x0). Index 0 = x1-direction.
G = {}
G[(0, 0, 0)] = -fp
G[(0, 1, 1)] = fp
G[(0, 2, 2)] = -fp * sp.exp(4 * f)
G[(0, 3, 3)] = -fp * sp.exp(4 * f)
G[(1, 0, 1)] = -fp
G[(1, 1, 0)] = -fp
G[(2, 0, 2)] = fp
G[(2, 2, 0)] = fp
G[(3, 0, 3)] = fp
G[(3, 3, 0)] = fp

def Gam(k, i, j):
    return G.get((k, i, j), sp.Integer(0))

def dGam(k, i, j):
    return sp.diff(Gam(k, i, j), x)

Ric = {}
for i in range(4):
    for j in range(4):
        s = dGam(0, i, j)  # sum_k d_k G^k_ij = d_0 G^0_ij
        t = dGam(0, i, 0) if j == 0 else sum(
            dGam(0, i, k) if False else sp.Integer(0) for k in range(4))
        # -sum_k d_j G^k_ik: nonzero only if j == 0 (x-dependence along x0)
        t = sum(dGam(k, i, k) for k in range(4)) if j == 0 else sp.Integer(0)
        s = s - t
        u = sum(Gam(k, k, m) * Gam(m, i, j) for k in range(4) for m in range(4))
        v = sum(Gam(k, j, m) * Gam(m, i, k) for k in range(4) for m in range(4))
        Ric[(i, j)] = sp.simplify(s + u - v)

gup = [sp.exp(2 * f), sp.exp(2 * f), sp.exp(-2 * f), sp.exp(-2 * f)]
Rscal = sum(gup[i] * Ric[(i, i)] for i in range(4))
Rscal = sp.simplify(Rscal)
target_R = 2 * sp.exp(2 * f) * (-fpp - 3 * fp ** 2)
assert sp.simplify(Rscal - target_R) == 0, f"R mismatch: {Rscal}"
print("R formula verified:", Rscal)

# Potential identity
k = sp.exp(f)
V = -k * sp.diff(k, x, 2)
Q = sp.simplify(Rscal / 6 - V)
target_Q = sp.simplify(sp.Rational(2, 3) * fpp * sp.exp(2 * f))
assert sp.simplify(Q - target_Q) == 0, f"Q mismatch: {Q}"
print("Q identity verified:", Q)

# Specific f = a cos(x1): Q series and q2 integral
a, x0 = sp.symbols('a x0')
fa = a * sp.cos(x0)
ka = sp.exp(fa)
Ra = 2 * sp.exp(2 * fa) * (a * sp.cos(x0) - 3 * a ** 2 * sp.sin(x0) ** 2)
Va = -ka * sp.diff(ka, x0, 2)
Qa = sp.simplify(Ra / 6 - Va)
q2 = sp.expand(Qa.series(a, 0, 3).coeff(a, 2))
assert sp.simplify(q2 + sp.Rational(4, 3) * sp.cos(x0) ** 2) == 0
I2 = (2 * sp.pi) ** 3 * sp.integrate(q2, (x0, 0, 2 * sp.pi))
print("q2 =", q2, " I2 =", I2)
assert I2 == -32 * sp.pi ** 4 / 3
print("small-a coefficient a2/a^2 ->", I2 / (4 * sp.pi) ** 2, "= -2pi^2/3")

# Rigorous bound at a* = 1/2.
# I = int_0^{2pi} (1/4) sin^2(x) e^{cos x} dx >= int_{pi/6}^{pi/3} (1/4) sin^2 dx
#     = pi/48  (there e^{cos x} >= 1 since cos x >= 0 on [0,pi/2]).
lo = math.pi / 48
Jbound = -(4.0 / 3.0) * (2 * math.pi) ** 3 * lo  # upper bound on J (negative)
a2bound = Jbound / (4 * math.pi) ** 2
print("I >= pi/48 =", lo)
print("J(1/2) <= -2pi^4/9 =", -2 * math.pi ** 4 / 9)
print("a2(1/2) <= -pi^2/72 =", -math.pi ** 2 / 72)
assert abs(a2bound - (-math.pi ** 2 / 72)) < 1e-12
assert a2bound < -0.13

# High-precision numeric confirmation (mpmath if available, else math)
try:
    import mpmath as mp
    mp.mp.dps = 30
    g = lambda t: mp.e ** (mp.cos(t)) * (mp.sin(t) ** 2) / 4
    I = mp.quad(g, [0, 2 * mp.pi])
    J = -(mp.mpf(4) / 3) * (2 * mp.pi) ** 3 * I
    a2 = J / (4 * mp.pi) ** 2
    print("numeric I =", I, " numeric a2(1/2) =", a2)
    assert a2 < -0.13
except ImportError:
    print("(mpmath unavailable; elementary bound above is the rigorous part)")

print("ALL CHECKS PASSED")
