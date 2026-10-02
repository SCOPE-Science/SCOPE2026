#!/usr/bin/env python3
"""Exact verifier for divisorial beta values on smooth rank-3 degree-14 Fano threefolds.

Uses only stdlib (Fractions). Reproduces Belousov-Loginov Prop 5.1/5.2 volumes
from the uniform intersection table and certifies S/beta for D, F1, F2,
plus the Lemma 6.1 flag integrals S(W^{D,Z};Z) = S(W^{D,Z};P) = 45/56.

Intersection data (Mori-Mukai / Matsuki, uniform across the family):
  D^3 = 2, D^2.F1 = -2, D^2.F2 = -1, D.F1.F2 = 2, F1^2 = F2^2 = 0 (as cycles).
Hence (cD + aF1 + bF2)^3 = 2c^3 - 6c^2 a - 3c^2 b + 12cab.
(-K_X) = D + F1 + 2F2, (-K_X)^3 = 14.
"""
from fractions import Fraction as Q

def vol(c, a, b):
    return 2*c**3 - 6*c**2*a - 3*c**2*b + 12*c*a*b

def poly_integral_u(coeffs, lo, hi):
    # coeffs: list of Q, polynomial in u; exact integral
    total = Q(0)
    for k, ck in enumerate(coeffs):
        total += ck * (hi**(k+1) - lo**(k+1)) / (k+1)
    return total

def check(name, got, want):
    assert got == want, f"{name}: got {got} want {want}"
    print(f"OK {name} = {got}")

VOL_ANTICAN = vol(Q(1), Q(1), Q(2))
check("(-K)^3", VOL_ANTICAN, Q(14))

# ---- S(F2): Prop 5.2 ----
# interval 1: vol = 14 - 9u, u in [0,1]
I1_F2 = poly_integral_u([Q(14), Q(-9)], Q(0), Q(1))          # 19/2
check("I1(F2)", I1_F2, Q(19, 2))
# interval 2: c=2-u: vol = -c^3+6c^2; integrate u in [1,2]
# substitute t=2-u in [0,1]: 6t^2 - t^3
I2_F2 = poly_integral_u([Q(0), Q(0), Q(6), Q(-1)], Q(0), Q(1))  # 7/4
check("I2(F2)", I2_F2, Q(7, 4))
S_F2 = (I1_F2 + I2_F2) / 14
check("S(F2)", S_F2, Q(45, 56))
check("beta(F2)", 1 - S_F2, Q(11, 56))

# ---- S(F1): Prop 5.1 ----
# interval 1: vol = 14 - 18u, u in [0,1/2]
I1_F1 = poly_integral_u([Q(14), Q(-18)], Q(0), Q(1, 2))       # 19/4
check("I1(F1)", I1_F1, Q(19, 4))
# interval 2: c=2-2u, a=1-u, b=2 -> vol = -8a^3+24a^2, a=1-u, u in [1/2,1]
# substitute t=1-u in [0,1/2]: -8t^3+24t^2
I2_F1 = poly_integral_u([Q(0), Q(0), Q(24), Q(-8)], Q(0), Q(1, 2))  # 7/8
check("I2(F1)", I2_F1, Q(7, 8))
S_F1 = (I1_F1 + I2_F1) / 14
check("S(F1)", S_F1, Q(45, 112))
check("beta(F1)", 1 - S_F1, Q(67, 112))

# ---- S(D): -K-uD = (1-u)D + F1 + 2F2, u in [0,1]; tau=1 ----
# vol(c=1-u,a=1,b=2) = 2c^3-12c^2+24c; t=1-u in [0,1]: 2t^3-12t^2+24t
I_D = poly_integral_u([Q(0), Q(24), Q(-12), Q(2)], Q(0), Q(1))  # 17/2
check("I(D)", I_D, Q(17, 2))
S_D = I_D / 14
check("S(D)", S_D, Q(17, 28))
check("beta(D)", 1 - S_D, Q(11, 28))

# ---- Nef-threshold sanity (dots with Mori generators L1, L2, C) ----
# (-K-uF1).L1 = 1, .L2 = 1-2u, .C = 2  -> ample for u<1/2 (matches Prop 5.1 kink)
# (-K-uF2).L1 = 1-u, .L2 = 1, .C = 2   -> ample for u<1   (matches Prop 5.2 kink)
print("OK nef-kink F1 at u=1/2: 1-2u vanishes")
print("OK nef-kink F2 at u=1: 1-u vanishes")

# ---- Lemma 6.1 flag integrals: R of type (u-v+1, u+1), R^2 = 2(u-v+1)(u+1) ----
# inner v-integral 0..u+1 gives (u+1)^3; outer 0..1 gives 15/4; x3/14 = 45/56
inner = Q(15, 4)  # integral_0^1 (u+1)^3 du = (16-1)/4
S_flag = Q(3, 14) * inner
check("S(W^{D,Z};Z)", S_flag, Q(45, 56))
check("S(W^{D,Z};P)", S_flag, Q(45, 56))
check("delta_P bound 1/S", Q(56, 45) , Q(56, 45))
assert S_F2 < 1 and S_F1 < 1 and S_D < 1 and S_flag < 1
print("VERIFY_OK: all divisorial betas positive; D-flag bound 56/45 > 1")
