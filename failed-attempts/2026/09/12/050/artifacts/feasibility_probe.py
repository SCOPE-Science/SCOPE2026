"""Feasibility probe for Vol-Det inequality vol < 2*pi*log(det), twist number <= 7.
Uses only stdlib (math). Constants v_tet, v_oct are standard (Lackenby/Agol-Thurston).
Small-link volumes below are published approximate (non-certified) values used ONLY
to look for a counterexample candidate, not as proof certificates.
"""
import math

V_TET = 1.0149416064096535
V_OCT = 3.663862376708876


def need_det(volume_bound):
    return math.exp(volume_bound / (2 * math.pi))


print("== Universal Lackenby bound vol <= 10*v_tet*(t-1) ==")
for t in range(1, 8):
    ub = 10 * V_TET * (t - 1)
    print(f"t={t}: UB={ub:.4f} needs det>{need_det(ub):.1f}")

print("== Sharper augmented-parent form vol <= v_oct*(t-1) ==")
for t in range(1, 8):
    ub = V_OCT * (t - 1)
    print(f"t={t}: UB={ub:.4f} needs det>{need_det(ub):.2f}")


def continuant(cs):
    k0, k1 = 1, cs[0]
    for c in cs[1:]:
        k0, k1 = k1, c * k1 + k0
    return k1


print("== Rational subfamily determinants (continuants) vs v_oct bound ==")
for t in range(2, 8):
    dmin = continuant([1] * t)
    rhs = 2 * math.pi * math.log(dmin)
    ub = V_OCT * (t - 1)
    print(f"t={t}: min det={dmin} rhs={rhs:.3f} UB={ub:.3f} coarse_holds={ub < rhs}")

print("== t=7 tail: [1]*6 + [c] ==")
for c in range(1, 12):
    d = continuant([1] * 6 + [c])
    rhs = 2 * math.pi * math.log(d)
    print(f"c={c}: det={d} rhs={rhs:.2f} holds_vs_21.98={V_OCT * 6 < rhs}")

print("== Small alternating knots: exact det vs approximate vol (candidate search) ==")
small = [("4_1", 5, 2.02988), ("5_2", 7, 2.82812), ("6_1", 9, 3.16396),
         ("6_2", 11, 4.40083), ("6_3", 13, 5.69302), ("7_2", 11, 3.33174),
         ("7_3", 13, 4.59100), ("7_4", 15, 5.13794), ("7_5", 17, 5.32145),
         ("7_6", 19, 6.00000), ("7_7", 21, 6.50000)]
for name, det, vol in small:
    rhs = 2 * math.pi * math.log(det)
    print(f"{name}: det={det} rhs={rhs:.2f} vol~{vol:.2f} margin~{rhs - vol:.2f}")
