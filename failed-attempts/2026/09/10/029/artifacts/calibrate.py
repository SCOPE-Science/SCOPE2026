"""Exact ensemble calibration for standardized symmetric Pareto(alpha=4.5).

Stdlib only. Verifies: normalization xm=sqrt(5)/3, E X^2=1, E X^4=25/9,
tail constant, Lee-Yin s^4-tail vanishing, truncation exponent tau=37/81,
variance-shift constant, M5 constant. All identities asserted.
"""
from fractions import Fraction
import math
import sys

ALPHA = Fraction(9, 2)  # 4.5
A = 4.5
# E[Y^2] = alpha/(alpha-2) xm^2 = (9/5) xm^2 = 1  ->  xm^2 = 5/9
XM2 = Fraction(5, 9)
XM = math.sqrt(5.0) / 3.0
assert abs(XM * XM - float(XM2)) < 1e-15, "xm^2 != 5/9"

def abs_moment(p):
    # E|X|^p = alpha xm^p / (alpha - p), p < alpha
    return A * (XM ** p) / (A - p)

m2 = abs_moment(2)
m4 = abs_moment(4)
print(f"xm = sqrt(5)/3 = {XM:.12f}")
print(f"E X^2 = {m2:.12f} (expect 1)")
print(f"E X^4 = {m4:.12f} (expect 25/9 = {25.0/9.0:.12f})")
assert abs(m2 - 1.0) < 1e-12
assert abs(m4 - 25.0 / 9.0) < 1e-12

C_TAIL = XM ** 4.5  # P(|X|>=s) = (xm/s)^4.5
print(f"tail const xm^4.5 = {C_TAIL:.12f} (expect ~0.2664)")
assert 0.26 < C_TAIL < 0.28

# Lee-Yin threshold quantity s^4 P(|X|>=s) = xm^4.5 s^{-1/2} -> 0
for s in (1.0, 10.0, 100.0):
    q = s ** 4 * (C_TAIL * s ** -4.5)
    print(f"s={s:>6}: s^4 P(|X|>=s) = {q:.6f}")
    assert abs(q - C_TAIL * s ** -0.5) < 1e-12

# Truncation exponent: N^2 T^-4.5 = N^{-1/18}  <=>  2 - 4.5 tau = -1/18
TAU = Fraction(37, 81)
assert ALPHA * TAU - 2 == Fraction(1, 18), "tau identity"
print(f"tau = 37/81 = {float(TAU):.8f}")

# Max-entry scale: (N^2)^{1/4.5} N^{-1/2} = N^{4/9-1/2} = N^{-1/18}
assert Fraction(2, 1) / ALPHA - Fraction(1, 2) == Fraction(-1, 18)
print("max-entry scale exponent 2/4.5 - 1/2 = -1/18 OK")

# Variance-shift constant: 1 - sig^2 = 1.8 xm^4.5 T^-2.5 ; exponent 2.5*37/81=185/162
assert Fraction(5, 2) * TAU == Fraction(185, 162)
C_VAR = 1.8 * C_TAIL
print(f"var-shift: 1-sig^2 = {C_VAR:.8f} N^(-185/162)")

# M5 constant: E|X|^5 1_{<=T} <= 9 xm^4.5 T^{1/2}
C_M5 = 9.0 * C_TAIL
print(f"M5 const 9 xm^4.5 = {C_M5:.8f} (expect ~2.3976)")
assert 2.39 < C_M5 < 2.41

# Coincidence constant check at a few N: P(fail) = N^2 (xm/N^tau)^4.5 = C_TAIL N^{-1/18}
for N in (100, 1000, 10000):
    T = N ** float(TAU)
    assert T >= XM  # tail formula valid
    pf = N * N * (C_TAIL * T ** -4.5)
    tgt = C_TAIL * N ** (-1.0 / 18.0)
    assert abs(pf / tgt - 1.0) < 1e-9
    print(f"N={N:>6}: P(H!=H~) <= {pf:.3e} = {C_TAIL:.4f} N^(-1/18)")

print("CALIBRATE_OK")
sys.exit(0)
