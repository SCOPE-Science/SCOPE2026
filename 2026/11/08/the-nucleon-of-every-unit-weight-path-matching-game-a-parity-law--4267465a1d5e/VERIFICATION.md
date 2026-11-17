---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The nonnegative efficient core is exactly the edge-inequality polytope x_i+x_(i+1)>=1: matching lower bound proves sufficiency. Odd n=2m+1 has a unique core (0,1,...,0) because deleting any odd vertex leaves a perfect matching of worth m, forcing its payoff zero. For even n=2m≥4 disjoint base pairs force core first ratio 1 and x_(2j−1)=a_j, x_(2j)=1−a_j with 0≤a_1≤...≤a_m≤1. Defining m+1 nonnegative gaps g_0=a1, g_j=a_(j+1)−a_j, g_m=1−a_m summing 1, m+1 proper coalitions have worth m−1 and ratios 1+g_j/(m−1). Maximizing the second lexicographic level forces all gaps 1/(m+1), giving alpha2=1+1/(m²−1), unique even path allocation. All other nonfixed coalitions at this allocation have positive integer numerator surplus at least 1/(m+1) and worth ≤m−1. The exceptional n=2 has nonunique splits and is correctly excluded. Independently tested all proper positive-worth coalitions for P3 through P16 via induced matching DP and exact fractions; this is corroboration, not infinite proof.

## originality

PASS

Closed parity-sensitive allocation vectors and the exact universal second lexicographic level were not identified in the checked general matching-game computation literature. Existing algorithmic dominance is acknowledged, full specialist paper access limitation retained as risk; no automatic fail.

## value

PASS

An explicit infinite path-family nucleon theorem with a parity dichotomy, exact rational payoffs and next-level bottleneck gap is independently useful for cooperative allocation and tests the geometry of the nucleon beyond algorithmic availability. Its content is not the routine textbook core test alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
