"""Bounded recovery test for the wedge-map/Clifford route toward the target.

Target threshold: rho(k,g) = 3g-3 - C(k+1,2); claim is B_{X0}(k) empty iff rho<0.
Best bound available without new theory (granted in optimal form):
  semistable rank-2 E0 with det K_{X0} (deg 2g-2) satisfies h0(E0) <= g+1
  (standard semistable Clifford form: h0 <= deg/2 + rank = g+1).
Test: list (g,k) where Clifford permits (k<=g+1) but rho<0 (target says empty).
A persistent gap means this route can never prove sharp emptiness.

Also checks two numerics used in the normalization-reduction attempt:
 (L1) no-numerical-gap lemma: rho_g(k)<0 implies the classical naive
      fixed-determinant expected dim on C (genus g-1, deg 2g-2, chi=2),
      3(g-1)-3-k(k-2), is also <0 (so failure is not a numerical gap);
 (L2) Osserman-type modified lower bound for the automatic m>=k+2 gluing
      route, R = 3g-6-k(k+2)+C(k,2), is <0 whenever rho_g(k)<0, i.e. the only
      available bound there is vacuous where emptiness is needed.

Writes output/artifacts/clifford_gap.txt and prints a short summary.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "clifford_gap.txt")


def rho(g, k):
    return 3 * g - 3 - k * (k + 1) // 2


def main():
    lines = []
    lines.append("Granted Clifford form: h0(E0) <= g+1.")
    lines.append("Target threshold: rho(k,g) = 3g-3-C(k+1,2).")
    lines.append("")
    lines.append("Gap cases 3<=g<=20 with k<=g+1 but rho<0:")
    gap = []
    for g in range(3, 21):
        for k in range(1, g + 2):
            r = rho(g, k)
            if r < 0:
                gap.append((g, k, r))
                lines.append(f"  g={g:2d} k={k:2d} rho={r:4d}  (Clifford allows k<={g+1})")
    lines.append(f"Total gap cases: {len(gap)}")
    lines.append("")
    # L1
    bad1 = [(g, k) for g in range(3, 61) for k in range(1, 40)
            if rho(g, k) < 0 and 3 * (g - 1) - 3 - k * (k - 2) >= 0]
    lines.append(f"L1 no-numerical-gap check (3<=g<=60): violations = {bad1}")
    # L2
    bad2 = [(g, k) for g in range(3, 61) for k in range(1, 40)
            if rho(g, k) < 0 and 3 * g - 6 - k * (k + 2) + k * (k - 1) // 2 >= 0]
    lines.append(f"L2 Osserman-bound-vacuous check (3<=g<=60): violations = {bad2}")
    lines.append("")
    lines.append("Conclusion: Clifford/wedge route leaves "
                 f"{len(gap)} sharp-emptiness cases unprovable; L1/L2 hold with "
                 "no violations, so the block is missing upper-bound theorems, "
                 "not numerics.")
    text = "\n".join(lines) + "\n"
    with open(OUT, "w") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
