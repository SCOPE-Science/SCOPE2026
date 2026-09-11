"""FALLBACK BLOCK (analytic gap ledger, stdlib only).

Fallback needs: sigma(t) <= C t^{-0.9} for ALL t>=1, explicit C.
Best available uniform input chain (granted in strongest form):
  (i)   1D circular mean via energy/coarea: E_th |mu1hat(t cos th)|^2 <= C1 t^{-s1},
        s1 = log6/log20 (Frostman exponent of the factor).
  (ii)  Tensorization by Cauchy-Schwarz + |muhat|<=1:
        sigma(t) = E[A B] <= sqrt(E[A^2] E[B^2]) <= E[A]^{1/2}... concretely
        sigma(t) <= min(E_th|mu1hat(tcos)|^2, E_th|mu1hat(tsin)|^2)
        via |other factor|^2 <= 1  =>  sigma(t) <= C1 t^{-s1}.
  (iii) Fractal-uncertainty (Dyatlov-Zahl, AD-regular) adds only tiny beta << 0.05.
Needed exponent 0.9 vs available s1 ~ 0.598: gap ~0.302, two orders above any
documented explicit FUP epsilon for a small-base alphabet. Cap/bulk refinement
cannot help: caps already beat 0.9 (mass ~1/t), but the bulk needs pointwise 1D
decay, which Route A refuted exactly (mu1hat(20^m) = c0, |c0| >= 0.206).
"""
import math

s1 = math.log(6) / math.log(20)
NEED = 0.9
gap = NEED - s1
FUP_GENEROUS = 0.05  # far above any explicit Dyatlov-Zahl epsilon on record

print("FALLBACK GAP LEDGER")
print(f"available tensorized exponent s1 = {s1:.6f}")
print(f"needed exponent                    = {NEED}")
print(f"gap                                = {gap:.6f}")
print(f"gap after generous FUP beta={FUP_GENEROUS}: {gap - FUP_GENEROUS:.6f}  (still blocked)")
print("bulk-refinement route: needs pointwise 1D decay, REFUTED by Route A resonance.")
print("OUTCOME: FALLBACK BLOCKED at exponent level; no constant C can be certified")
print("because the required decay rate itself is unavailable by ~0.30.")
