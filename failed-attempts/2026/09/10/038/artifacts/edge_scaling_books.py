"""Exponent bookkeeping for lane-605 target (DBM t=n^{-1/3}, eta0=n^{-3/4+tau}).

Computes, with explicit arithmetic:
 (B1) DBM criticality ratio  sqrt(t)/cell-width  (Gaussian spread vs edge cell).
 (B2) Girko small-eta truncation under Wegner-only input (layer-cake integral).
 (B3) Quantifier-defect check: width(n)=A n^{-1/2} log n -> 0, so no nonzero
      n-independent smooth f sits inside E_n for all large n (vacuous literal).
 (B4) Relaxation-vs-comparison tradeoff: t >> n^{-1/3} needed for contraction,
      but comparison error grows with t; no window at critical t.
Prints a table; exits 0. stdlib+numpy only.
"""
import math

def width(n, A=1.0):
    return A * n ** (-0.5) * math.log(n)

def report(A=1.0, tau=0.05):
    print(f"{'n':>12} {'cellwidth':>12} {'sqrt(t)':>12} {'ratio R':>12} "
          f"{'n*eta0':>12} {'1/(n eta0)':>12} {'trunc n^-5/4':>12}")
    for n in [10**6, 10**9, 10**12, 10**15]:
        t = n ** (-1.0 / 3.0)
        sq = math.sqrt(t)
        w = width(n, A)
        R = sq / w
        eta0 = n ** (-0.75 + tau)
        neta = n * eta0
        inv = 1.0 / neta
        trunc = n ** (-1.25 + tau) * math.log(n)
        print(f"{n:>12} {w:>12.3e} {sq:>12.3e} {R:>12.3e} "
              f"{neta:>12.3e} {inv:>12.3e} {trunc:>12.3e}")
    print()
    # B2: layer-cake constant: E sum log(1+eta0^2/lam^2) <= C n * pi * eta0
    # per-z Girko factor (1/n)*that times cell area |E_n| ~ 4 pi A n^-1/2 log n
    n = 10**9
    eta0 = n ** (-0.75 + tau)
    per_z = math.pi * eta0  # (1/n) * (C n pi eta0), C=1
    area = 4 * math.pi * A * n ** (-0.5) * math.log(n)
    print(f"B2 @n=1e9: per-z small-eta factor ~ {per_z:.3e}, "
          f"cell area ~ {area:.3e}, product ~ {per_z*area:.3e} "
          f"(<< n^-1/24 = {1e9**(-1/24):.3e}) -> truncation closable in isolation")
    print("B2 caveat: uses Wegner E N_I <= C n|I| uniformly to eta->0, which is NOT")
    print("available from bounded-density alone at the cusp; sharp tail (CES Prop 2)")
    print("gives only unspecified n^-c. One-scale eta0 input does not supply it.")
    print()
    # B3 quantifier defect
    print("B3: width(n) for n=10^2..10^15:")
    for n in [10**2, 10**4, 10**6, 10**9, 10**12, 10**15]:
        print(f"   n={n:<16} width={width(n):.3e}")
    print("   width decreases monotonically to 0 for n>e^2; cap_n E_n = unit circle.")
    print("   Hence no nonzero n-independent smooth f has supp f in E_n^k for all")
    print("   large n (compact support inside every E_n => support in circle => f=0).")
    print("   Literal universal reading is vacuous; per-n reading makes C_f n-dependent,")
    print("   breaking the claimed uniformity. Statement needs repair to rescaled profiles,")
    print("   after which the claim is the open microscopic problem (blocked by B1/B4).")
    print()
    # B4 tradeoff
    print("B4: relaxation needs t >> n^-1/3 for edge-scale contraction (supercritical),")
    print("    but 4th-cumulant comparison error of X vs X_t grows with t while the")
    print("    Gaussian spread sqrt(t) >> cell width for every fixed large n (R>>1 above).")
    print("    At critical t=n^-1/3 the coupling displaces edge points by R x cell width,")
    print("    R = n^{1/3}/log n -> inf. No window yields n^-1/24. This is why CES")
    print("    circumvents short-time DBM via long-time OU + Girko (admission record).")

if __name__ == "__main__":
    report()
