"""Bounded recovery test for the target mechanism (split non-PCF map).

Map: Phi([X:Y:Z]) = [X^2+Z^2 : Y^2+Z^2 : Z^2], i.e. affine (x^2+1, y^2+1).
Ramification divisor: three coordinate lines (Jacobian det = 8XYZ).
The line {X=0} has infinite distinct forward images X = c_n Z with
c_{n+1} = c_n^2 + 1, so the map is non-PCF by the WORKLOG section-1 lemma.

Test of the 1-d factor mechanism: discriminants of f^n(x) - 0 for
f(x) = x^2 + 1, n = 1..4. The target mechanism predicts genuinely new
ramified primes appearing as the critical orbit grows.

Run: python3 output/artifacts/split_map_discriminants.py
Requires: sympy
"""
import sympy as sp

x = sp.Symbol('x')
fn = x**2 + 1  # f^1
for i in range(1, 5):
    if i > 1:
        fn = sp.expand(fn.subs(x, x)**2 + 1) if False else None
        # rebuild iteratively: f^{i}(x) = (f^{i-1}(x))^2 + 1 evaluated at x
        fn = sp.expand(prev**2 + 1)
    d = sp.discriminant(fn, x)
    print("level", i, "deg", sp.Poly(fn, x).degree(), "disc =", d)
    print("  prime factors:", sp.factorint(int(d)))
    prev = fn

# Recorded output (sympy 1.12):
# level 1 deg 2  disc = -4                        -> {2}
# level 2 deg 4  disc = 512                       -> {2}
# level 3 deg 8  disc = 335544320                 -> {2, 5}
# level 4 deg 16 disc = 191846138366579336806400  -> {2, 5, 13}
# New ramified primes (5 at level 3, 13 at level 4) divide critical-orbit
# values c_3 = 5, c_4 = 26 = 2*13 with c_{n+1} = c_n^2+1 — confirming the
# predicted mechanism in the split case, but NOT the general P^2 argument.
