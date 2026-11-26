---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Disjoint clocks and the deterministic hub give independent petals, and their all-positive states are absorbing, so the bouquet time is their maximum. At a fixed observation time all vertices are positive exactly when every backward lineage has reached the hub, allowing mergers. With k active lineages, each has k rate-1/r destinations that reduce the count (hub plus k−1 occupied sites); all relocations preserve this hazard, giving independent Exp(k²/r) holding times. Partial fractions give the alternating factorial coefficients, including c_r=2r/(r+1). As a separate algebraic check, the forward negative-count chain has rates x(r−x)/r up and x(r−x+1)/r down. In the basis f_j(x)=binom(x,j)/binom(r,j) on states 0,…,r, Lf_j=[j(j−1)f_{j−1}−j²f_j]/r for j≥1. The killed generator thus has poles −j²/r; the endpoint-to-endpoint tridiagonal resolvent gives the product of the down rates divided by ∏(s+j²/r), agreeing with the petal Laplace transform. After scaling time by r, the residue bound |a_{r,j}|≤2 gives a uniform remainder ≤2e^(−4y)/(1−e^(−5y)). At y=log(mc_r)+x it is O_x(m^−4); m times the survival converges uniformly to e^(−x), and the maximum gives the Gumbel CDF. The centered positive tails are bounded by a constant times e^(−x), and the Exp(1) summand gives negative tails ≤exp(−e^x/2) when the threshold is nonnegative, zero otherwise. These bounds justify uniform mean convergence. The star and friendship specializations check directly; the double-log contrast is with nontrivial flooding petals of size at least two, not flooding on a star. The frozen verifier was inspected, not executed; finite rational checks cannot certify the uniform limit.

## originality

PASS

Classical voter duality, single-clique zealot mean calculations, fixed-hub star extremes and clique-bouquet flooding are acknowledged overlaps. The evidence supports the distinct all-petal-size voter law and the unrestricted uniform-in-size Gumbel and mean approximations. The exact distributional overlap with the older single-clique zealot paper remains access-limited; no absolute priority is claimed.

## value

PASS

The explicit spectrum and residue allow calibrated predictions for clique bouquets even when petal sizes change without bound, and the mean has the same centering with an explicit constant. The comparison to repeated-pole flooding identifies why the same geometry does not produce the same correction, a distinction not supplied by a fixed-size Gumbel theorem or a single-clique mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
