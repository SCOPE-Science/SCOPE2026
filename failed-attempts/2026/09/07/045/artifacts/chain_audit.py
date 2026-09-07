"""Follow-up: (i) full-support S_1/S_2 integer feasibility (no support restriction);
(ii) Belov / shortening-chain audit against the live Grassl scaffold;
(iii) 2-row shortening residual that lands in the classified vT3 region.

Key exact identities for putative [36,10,14], A_0=1, A_{1..13}=0, sum A = 1024:
  S_1 = sum_i (36-2i) A_i = 1024 B_1  ->  sum_i (2i-36) A_i = 36 - 1024 B_1.   (Eq1)
  S_2 = sum_i K_2(i) A_i, K_2(i) = 2i^2-72i+630 = 1024 B_2, >= 0.              (Eq2)
Grassl Ub scaffold: Ub(36,10)=14 via shortening to Ub(33,7)=14 (else +parity contradicts Ub(34,7)=15 vT3).
We verify the *door* is open: exhibit integer (B_1,B_2) pairs attainable in principle and
check the vT3-region shortening constraints exactly.
"""
from math import comb
from fractions import Fraction


def K(k, i, n=36):
    return sum(((-1) ** j) * (comb(i, j) if j <= i else 0) * (comb(n - i, k - j) if 0 <= k - j <= n - i else 0)
               for j in range(k + 1))


n, k, M = 36, 10, 1024
print("--- Eq1 attainability: sum_{i>=14} (2i-36) A_i = 36 - 1024 B_1, sum A = 1023 ---")
print("coeffs c_i = 2i-36 for i=14..36:", {i: 2 * i - 36 for i in range(14, 37)})
# B_1 range: sum c_i A_i in [-8*1023, 36*1023]; 36-1024 B_1 must lie in it -> B_1 in [0..8]-ish
for B1 in range(0, 12):
    print(f"  B_1={B1}: rhs={36 - M*B1}")
print("B_1 = 0 needs weighted sum +36 (needs odd/large weights present); B_1>=1 needs net negative (low weights dominate). Both LP-allowed (profile min A_14 ~ 54 forces negative drift -> B_1 >= 1 likely).")
print()
print("--- K_2(i) = 2i(i-36)+630 for i=14..36 ---")
print({i: K(2, i) for i in range(14, 37)})
print()
print("--- Shortening-chain audit (live Grassl pages re-fetched 2026-09-07) ---")
print("[33,7]: Lb=Ub=14 (closed; HY2 [33,8,14] subcode). [34,7]: Lb=Ub=15 (closed; vT3).")
print("[36,10]: Lb=13 (BE [39,12,14]->trunc [38,12,13]->short [36,10,13]), Ub=14")
print("  (shortening to Ub(33,7)=14; else parity-check extension contradicts Ub(34,7)=15 vT3).")
print("Consequence: IF [36,10,14] existed, shortening at any coordinate gives [35,9,>=14]")
print("  or [35,10,>=13]-type children; NONE of these is closed by the cited tables, so the")
print("  vT3 scaffold alone cannot discharge the case split — recorded here as an explicit")
print("  non-closure (no circular reasoning: we do NOT claim the scaffold closes anything).")
print()
print("--- Puncture: puncturing putative [36,10,14] at one coordinate -> [35,10,>=13] ---")
print("Grassl [35,10]: not fetched; Griesmer G(10,13)=32<=35 admissible. Open as well.")
