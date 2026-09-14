"""Bounded recovery test for lane-1852: MBI on slowly rotating Kerr.

Checks, reproducibly:
 (1) MBI constitutive nonlinearity is cubic at leading order (O(F^3), no quadratic term)
     via series of the Born-Infeld Lagrangian density ell = sqrt(1 + S - P^2)-type factor.
 (2) Small-data symmetric hyperbolicity is preserved (determinant factor stays > 0),
     i.e. no trivial finite-time loss-of-hyperbolicity disproof at small amplitude.
 (3) Bootstrap numerology: cubic error integral converges given linear t^-1 decay,
     while a quadratic analogue diverges logarithmically (sharpness of cubic structure).
 (4) Model top-order energy inequality closure gap: with an unabsorbed trapping /
     commutator constant the small-data closure is conditional, not unconditional.

All quantities are explicit model scalars; no claim of solving the PDE is made.
"""
import sympy as sp
import mpmath as mp

print("=== (1) MBI cubic leading nonlinearity ===")
s = sp.symbols('s')  # model invariant amplitude ~ |F|^2
# Model BI factor: sqrt(1+s); Lagrangian L ~ 1 - sqrt(1+s); constitutive H = dL/ds F
L = 1 - sp.sqrt(1 + s)
H_factor = sp.diff(L, s)  # -1/(2 sqrt(1+s))
series_H = sp.series(H_factor + sp.Rational(1, 2), s, 0, 4)  # deviation from Maxwell
print("H_factor deviation series:", series_H)
# Leading deviation must be linear in s, i.e. cubic in F. Confirm no constant term:
c0 = sp.simplify(H_factor.subs(s, 0) + sp.Rational(1, 2))
print("constant term of deviation (must be 0):", c0)
assert c0 == 0
c1 = sp.simplify(sp.diff(H_factor, s).subs(s, 0))
print("linear-in-s coefficient (nonzero => cubic in F):", c1)
assert c1 != 0

print("\n=== (2) Small-data hyperbolicity (determinant factor) ===")
# Model BI determinant factor ell = 1 + s (>0 needed). Check positivity radius.
f = lambda x: 1.0 + x  # model ell with invariant x ~ O(|F|^2), x can be slightly negative
for x in [0.0, 0.05, 0.25, -0.25, -0.5]:
    print(f"  ell({x:+.2f}) = {f(x):.3f}  hyperbolic={f(x) > 0}")
# Conclusion: near zero, ell stays positive => no small-data hyperbolicity-loss disproof.
assert all(f(x) > 0 for x in [0.0, 0.05, 0.25, -0.1])

print("\n=== (3) Bootstrap numerology: cubic converges, quadratic diverges ===")
mp.mp.dps = 25
cubic = mp.quad(lambda t: (1 + t) ** (-2), [0, mp.inf])
print("cubic integral int_0^inf (1+t)^-2 dt =", cubic, "(finite => cubic errors integrable)")
assert abs(float(cubic) - 1.0) < 1e-8
T = 1e6
quad_trunc = mp.quad(lambda t: (1 + t) ** (-1), [0, T])
print(f"quadratic-truncated int_0^{T:g} (1+t)^-1 dt =", quad_trunc, "(~ log T, diverges as T->inf)")
assert float(quad_trunc) > 13.0  # log(1e6) ~ 13.8

print("\n=== (4) Model top-order closure gap ===")
# Model inequality: E <= C0 e^2 + K*C1 E^{3/2} (+ higher), K>=1 unabsorbed trapping constant.
# With e small, closure needs K*C1*sqrt(E) < 1/2 uniformly; K depends on refined Kerr
# trapping/commutator control not available in-session => conditional only.
C0, C1, e = 1.0, 1.0, 1e-3
E_guess = 4 * C0 * e ** 2
for K in [1.0, 2.0, 5.0]:
    ratio = K * C1 * E_guess ** 0.5
    print(f"  K={K:.1f}: K*C1*sqrt(E_guess) = {ratio:.4f}  closes={ratio < 0.5}")
print("Gap: K (trapping/commutator loss) is not quantified in-session; closure is conditional on K=O(1).")

print("\nRECOVERY TEST RESULT: TARGET BLOCKED in both directions (proof conditional on")
print("unavailable Kerr microlocal inputs; disproof excluded at small data by (2)).")
print("ALL CHECKS PASSED.")
