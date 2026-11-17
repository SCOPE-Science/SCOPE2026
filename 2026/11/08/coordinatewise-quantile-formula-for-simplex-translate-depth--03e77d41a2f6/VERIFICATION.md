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

For an excluded translate of S, some barycentric lower threshold b_j is strictly above λ_j(y). Since the measure is supported on S, captured mass is at most P[λ_j>λ_j(y)]. Conversely b_j=λ_j(y)+ε and b_i=−b_j/d for the other facets realizes the corresponding one-coordinate cap, with atom-sensitive strict inequality; taking ε↓0 yields equality by continuity from below. Right-continuity of each CDF makes F_i(t)≥α exactly equivalent to t≥q_i(α). The sum-one barycentric constraint proves sum q_i≤1 iff feasible, and sorted sample coordinates give k*. Uniform-simplex Beta(1,d) marginals give unique barycentric center with depth 1-(d/(d+1))^d; opposite-facet-center atoms give sharp centerpoint 1/(d+1). Inspected source exact-rational verify.py independently enumerates feasible finite sample subsets; additional independent seven-query finite sample test reproduced the cap formula, not a proof for arbitrary measures.

## originality

PASS

Molchanov–Nagy introduced general translate depth, erosion regions, general empirical representations and translative Helly bounds; all acknowledged. Full online manuscript was read in substantive Sections 2,6,7 and did not give the same any-measure, same-simplex-support barycentric marginal closed formula with atom handling and exact sorting algorithm. Other related Resultary records are uniform-only or assume dilation beyond an explicit threshold. Priority remains best-knowledge.

## value

PASS

An exact atom-robust dimensional reduction of convex depth to d+1 scalar CDFs, including all depth regions and O(nd log n) exact sample median computation from barycentric input, is an independently useful mathematical classification and algorithm; its value is not the already known universal centerpoint bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
