"""Recovery test: quantify why direct AFE + primitive orthogonality cannot reach
delta=1/40 with A<=10 for the depth moment target.

Computes, for q=p^kappa:
 - AFE length N ~ q^1.5
 - residue class n=1 mod p^{kappa-1} count in [1,N] (off-diagonal load)
 - trivial Cauchy majorant ~ p^0.5 * q^0.25 (grows; target needs q^-0.025 decay)
 - dual length M ~ q^3/N ~ q^1.5 (no shortening)
 - individual-bound gap: Sun-Zhao q^{3/4-3/40} per chi vs covering O(q^eps) average
All stdlib only.
"""
import math

def report(p, kappa):
    q = p ** kappa
    N = q ** 1.5
    mod = p ** (kappa - 1)
    count = int((N - 1) // mod)  # n<=N, n=1 mod p^{kappa-1}, excluding n=1
    cauchy = math.sqrt(p) * (q ** 0.25)
    target = q ** (-1 / 40)
    gap_factor = cauchy / target  # how far trivial majorant is from target
    M = q ** 3 / N
    sun = q ** (0.75 - 3 / 40)  # per-chi individual bound exponent
    return {
        "p": p, "kappa": kappa, "q": q, "N": N,
        "offdiag_count": count, "cauchy_majorant": cauchy,
        "target_tol": target, "gap_factor": gap_factor,
        "dual_len": M, "sun_individual": sun,
    }

print(f"{'p':>3} {'kap':>4} {'q':>16} {'N~q^1.5':>16} {'offdiag#':>12} "
      f"{'Cauchy~p^.5q^.25':>18} {'tgt q^-1/40':>12} {'gap':>12} {'dual M':>12} {'Sun/chi':>12}")
for p in (2, 3, 5):
    for kappa in (10, 12, 14):
        r = report(p, kappa)
        print(f"{r['p']:3d} {r['kappa']:4d} {r['q']:16.3g} {r['N']:16.3g} "
              f"{r['offdiag_count']:12d} {r['cauchy_majorant']:18.3g} "
              f"{r['target_tol']:12.3g} {r['gap_factor']:12.3g} "
              f"{r['dual_len']:12.3g} {r['sun_individual']:12.3g}")

print()
print("Conclusion: Cauchy majorant grows as q^+1/4 while target decays as q^-1/40;")
print("gap factor = p^1/2 q^{1/4+1/40} >> p^10 allowance in the wrong direction")
print("(p^A multiplies, not cancels). Dual length stays ~q^1.5: no shortening.")
print("Sun-Zhao per-chi q^{0.675} vs covering average O(q^eps): averaging absolutes")
print("cannot bridge q^0.675 gap. Missing piece is a uniform depth-Voronoi")
print("p-adic stationary-phase lemma, not available in-pass.")
