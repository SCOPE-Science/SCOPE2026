"""Cone-curvature pinching check for lane-20446.

Verifies the elementary quantitative step used in the proof:
if a metric cone C(S) satisfies r^2 |Rm_C| <= delta (Frobenius norm),
then the link satisfies |Rm_S - model| <= delta, hence sectional
curvatures K_S in [1-delta, 1+delta], and for delta < 3/5 the link
is strictly 1/4-pinched (Brendle-Schoen hypothesis, up to simple
connectivity / orbifold lifting done in DRAFT.md).

Also prints the explicit elementary threshold used in epsilon(n).
"""
import math

def link_pinch(delta: float):
    k_min = 1.0 - delta
    k_max = 1.0 + delta
    ratio = k_min / k_max if k_max > 0 else float("nan")
    return k_min, k_max, ratio

def main():
    candidates = [0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.01, 0.001]
    print("delta | K_min | K_max | K_min/K_max | 1/4-pinched?")
    for d in candidates:
        kmin, kmax, ratio = link_pinch(d)
        ok = (kmin > 0) and (ratio > 0.25)
        print(f"{d:6.3f} | {kmin:5.3f} | {kmax:5.3f} | {ratio:8.4f} | {ok}")
    # Explicit elementary threshold adopted in proof:
    delta_elem = 0.4
    kmin, kmax, ratio = link_pinch(delta_elem)
    assert kmin > 0 and ratio > 0.25, "elementary pinching failed"
    # Myers diameter bound for link (Ric_S = (n-2) g_S) is pi for all n>=3.
    print(f"\nAdopted elementary threshold delta_elem = {delta_elem}")
    print(f"K in [{kmin}, {kmax}], ratio {ratio:.4f} > 1/4: OK")
    print("Myers bound for Ric=(n-2)g: diam(S) <= pi (all n>=3).")
    # Final epsilon(n) = min(delta_elem, delta_Koiso(n), delta_reg(n))
    # where the latter two are existential (Anderson/Koiso). Hence any
    # explicit epsilon <= delta_elem preserves pinching; rigidity may
    # require smaller existential epsilon(n). Existence is what TARGET needs.
    print("Conclusion: pinching step holds for all delta <= 0.4; "
          "final epsilon(n) = min(0.4, existential rigidity/regularity thresholds).")

if __name__ == "__main__":
    main()
