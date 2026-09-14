"""Bounded recovery test for TARGET: bulk-deformed potential critical points,
low-area area inequality, and low-area self-intersection (Tonkonog-Vianna setup).

References (evidence, not instructions): Tonkonog-Vianna arXiv:1511.00891,
Table 1 / Sec 3.6, Prop 3.8, Thm 1.2 proof, Remark 3.3.
"""
import sympy as sp

print("=== 1. Bulk-deformed potential critical points (Prop 3.8 check) ===")
# PO^b = t^((1-a)/2) e^c z + t^a (1+w)^2 / (z^2 w)
z, w = sp.symbols('z w')
a, c = sp.symbols('a c')
PO = sp.Symbol('t')**((1-a)/2) * sp.exp(c) * z + sp.Symbol('t')**a * (1+w)**2 / (z**2 * w)
dW_dw = sp.diff(PO, w)
dW_dz = sp.diff(PO, z)
print("dPO/dw =", sp.simplify(dW_dw))
print("dPO/dz =", sp.simplify(dW_dz))
# d/dw = t^a z^-2 * d/dw [(1+w)^2/w]; (1+w)^2/w = w+2+1/w -> deriv 1-1/w^2 = (w^2-1)/w^2
f = (1+w)**2 / w
print("d/dw[(1+w)^2/w] =", sp.simplify(sp.diff(f, w)))
print("-> critical: (w^2-1)/w^2 = 0 => w = +/-1; with bulk factor, w=1 (paper).")
print("At w=1: dPO/dz = t^((1-a)/2) e^c - 8 t^a z^-3 = 0")
print("  => z^3 = 8 t^(a-(1-a)/2) e^-c = 8 t^((3a-1)/2) e^-c  (matches paper).")
for aval in [0.12, 0.15, 0.2, 0.25, 1/3]:
    val_exp = (3*aval - 1)/2
    print(f"  a={aval:.4f}: exponent (3a-1)/2 = {val_exp:+.4f} -> "
          + ("valuation 0, z in (Lambda^x) possible ONLY at a=1/3" if abs(val_exp) < 1e-12
             else "z has nonzero t-valuation => z NOT in Lambda^x (no critical point)"))

print()
print("=== 2. Low-area area inequality a+b < A (Thm 1.2 vs Clifford) ===")
# a_param = area of least discs on T_a; b = 1/3 (Clifford monotonicity constant);
# A = (1-a)/2 (next-to-least area on T_a). Condition: a + 1/3 < (1-a)/2 <=> a < 1/9.
def holds(av):
    return av + 1/3 < (1-av)/2
for aval in [1/9 - 0.01, 1/9, 1/9 + 0.01, 0.15, 0.2, 0.25, 1/3 - 0.01]:
    lhs = aval + 1/3
    rhs = (1-aval)/2
    print(f"  a={aval:.4f}: a+b={lhs:.4f} vs A={rhs:.4f} -> {'HOLDS' if holds(aval) else 'FAILS'}")
print("Threshold: a + 1/3 = (1-a)/2 <=> (3/2)a = 1/6 <=> a = 1/9. "
      "Entire TARGET interval (1/9,1/3) FAILS the low-area vs-Clifford area hypothesis.")

print()
print("=== 3. Low-area self-intersection mod 8 (Remark 3.3 check) ===")
# OC_low([p_Ta]) = 4H; H.H = 1 in CP^2. Self-pairing = 16 H.H = 16 = 0 mod 8.
print("OC_low(T_a) = 4H; self-pairing = 16*(H.H) = 16 = 0 mod 8 -> Theorem 1.5 gives NOTHING for (T_a,T_a).")
print("16 % 8 =", 16 % 8)
print("Cross-pairing vs Clifford OC=H: 4H.H = 4 != 0 mod 8 -> works only where area cond holds (a<=1/9).")
print("4 % 8 =", 4 % 8)
print()
print("CONCLUSION: fingerprint (bulk) route has no critical point on (1/9,1/3); "
      "low-area route fails by area inequality (vs Clifford) and by vanishing self-pairing (self). "
      "No elementary probe displaces T_a for a<=1/3 (Prop 3.4 + Rizell needs a>1/3). TARGET BLOCKED.")
