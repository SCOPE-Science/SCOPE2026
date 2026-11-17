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

PASS: Inspected frozen RESULT.md and verify_euler_fairness.py. In Eulerian support every degree is even, so first-group EF1 for a vertex with x_v incident selected goods is exactly 2x_v>=d_v. Component double-counting gives minimum ceil(|E(H)|/2), and alternating edge colors along an Euler circuit achieve this bound even with odd circuit length; moving extra edges to first group preserves EF1. This proves min |X|=(m+r)/2, minimum imbalance r, and after h neutral goods the optimal parity-constrained gap max((m+h) mod 2, r-h). With 2-regular support the discarded edge set is a matching; count optimal assignments by two perfect matchings of even cycles and length-many maximum matchings of odd cycles. Exponential formula for labeled undirected cycles yields EGFs E(z), O(z), D(z); parity-extracted singularity transfer gives C*n^(-1/4) even and C/4*n^(-1/4)*log n odd. Independently enumerated two disjoint triangles: 9 minimum EF1 allocations with first-group size 4, not balanced without h>=1; source verifier code inspected but its logged 741 and 4058 counts not represented as independent execution.

## originality

PASS

PASS, best-of-knowledge: general group EF1 hardness and balanced existence are prior; the deterministic Eulerian odd-component obstruction, exact neutral-goods budget, and parity-separated random labeled-cycle probability address narrower yet structurally distinct observables. No inspected related literature or Resultary entry implies these exact expressions. Full Deligkas paper inaccessible (including any appendices), and possible exact graph-incidence allocation model elsewhere remains a historical risk.

## value

PASS

PASS: For a natural 2-sparse binary approval incidence model with fixed groups, a sharp constructive fairness/cardinality obstruction improves on bare feasibility/complexity, and exact distribution in random 2-regular cases quantifies rarity. The odd/even n logarithmic asymptotic is an independently meaningful structural probabilistic boundary, not a known lookup-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
