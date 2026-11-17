---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The hub-and-leaf coalition formula gives vα(h∪K)=αsum_{i∈K}w_i+(1−α)min_{j∉K}w_j. Singleton leaf and complementary-leaf core inequalities give each 0≤x_i≤(2α−1)w_i; for α≥1/2 their product box and efficiency imply every remaining coalition constraint using sum omitted weights≥min omitted. The external unanimity-game telescoping expansion yields leaf Shapley component b_i; internal edge unanimity gives αw_i/2. Writing r_i=b_i/w_i and using summation-by-parts proves r1≥...≥rm≥−1/(m+1); thus first leaf uniquely sets upper-box entry threshold α*=(1+r1)/(3/2+r1). Equality at equal weights and the m=2 formula follow algebraically. Compare marginal of maximum-weight leaf at {hub} versus N\{i} to violate supermodularity for α<1. Inspected standalone exact-rational trust_star_check.py and independently computed two-leaf weights (1/2,1) cutoff 5/8 with all coalition checks; these finite computations corroborate the all-real-weight symbolic proof.

## originality

PASS

A prior October 25 published general directed trust game already establishes empty/point/positive-dimensional *phase* at α=1/2 for all networks, so that phase is explicitly NOT new. However, it neither gives the exact weighted rectangular core of in-stars nor the full weight-dependent fair Shapley-entry α* threshold and stable yet non-supermodular interval. Ryzák–Kroupa (2026) treats fixed unscaled internal-plus-external game and explicitly proposes the convex interpolation for future work. The retained new joint classification is correct, natural and not dominated in inspected earlier sources.

## value

PASS

The core’s complete facet/vertex geometry and an exact, sharp, weight-sensitive threshold for simultaneous Shapley fairness and coalitional stability form a motivated solution concept comparison on a natural network family. Especially the stable non-supermodular interval is not implied by the earlier universal half-weight core-existence theorem. The already known phase boundary alone is not treated as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
