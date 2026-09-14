"""Barrier exponent model for short-window degree-6 moment.

 Compares diagonal size D ~ T*Delta against optimistic off-diagonal (OD)
 estimates for Kuznetsov + Weil (+Voronoi) routes, and the spectral large
 sieve route. Purely an exponent-balance heuristic with explicit formulas,
 to bound what standard technology can reach. No external data.
"""
import math

def report(Texp=1.0):
    # Work in exponents of T (T symbolic large). Use T = 1e12 for arithmetic illustration.
    T = 1e12
    print("=== Short-window degree-6 moment barrier model ===")
    print(f"illustrative T = {T:.0e}")
    N_afe = T**2          # AFE length Q^{1/2}, Q ~ T^4
    for delta_exp in [1/5, 1/3, 1/2]:
        D = T * T**delta_exp
        print(f"\n-- Delta = T^{delta_exp:.3f}: diagonal D ~ T^{1+delta_exp:.3f} = {D:.3e}")
        # Route B: spectral large sieve. Bound ~ (T*Delta + N_eff) * sum|a|^2,
        # sum|a|^2 ~ log T (normalized). N_eff in {T^2 (optimistic: square-root
        # arguments stay <= AFE length), T^4 (pessimistic: squared moduli)}.
        for ne in [2.0, 4.0]:
            sieve = max(T * T**delta_exp, T**ne)
            gap = sieve / D
            print(f"   large sieve N_eff=T^{ne:.0f}: bound/sieve-vs-target ratio ~ T^{ne-(1+delta_exp):.3f} = {gap:.2e}")
        # Route A: Kuznetsov-Weil OD, optimistic template.
        # Trivial OD before cancellation: sum over m,n <= N (N^2 terms /N after
        # 1/sqrt(mn)) times c-sum. After Weil (c^{-1/2}) + optimal stationary
        # phase/Voronoi savings, the BEST documented GL2 short-moment analyses
        # (Jutila/Motohashi-type) still require Delta >> T^{1/3}; i.e. effective
        # OD/D ~ T^{1/3}/Delta (optimistic GL2 template). For squared moduli
        # the c-length and Voronoi conductor are squared, shifting threshold to
        # T^{1/2} or worse: OD/D ~ T^{1/2}/Delta (optimistic squared template).
        for thr, name in [(1/3, "GL2-template (generous lower bound)"),
                          [(1/2, "squared-moduli template (generous)")][0]]:
            ratio = T**thr / T**delta_exp
            print(f"   Kuznetsov OD/D [{name}]: ~ T^{thr-delta_exp:.3f} = {ratio:.2e} "
                  + ("(OD exceeds diagonal)" if ratio > 1 else "(OD controlled)"))
    # Crossover deltas
    print("\nCrossover Delta* where OD ~ D:")
    print(f"  GL2-template: Delta* ~ T^0.333 (vs claimed T^0.200)")
    print(f"  squared-moduli template: Delta* ~ T^0.500 (vs claimed T^0.200)")
    # Individual-subconvexity sanity check (not a disproof)
    print("\nImplied individual bound at Delta=T^{1/5}: |L| << T^{1/2}Delta^{1/2} = T^0.600,")
    print("vs convexity T^1.000: target implies genuine subconvexity T^{0.6} on average;")
    print("no contradiction, confirms target is a breakthrough-level claim.")
    print("\nConclusion: under generous standard-technology savings, OD/D >> 1 at")
    print("Delta=T^{1/5} (gap is a positive power of T); crossover sits at")
    print("Delta* >= T^{1/3} (GL2) and >= T^{1/2} (squared), so T^{1/5} is out of reach")
    print("without a fundamentally new cancellation input.")

if __name__ == "__main__":
    report()
