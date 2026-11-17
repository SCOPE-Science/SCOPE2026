---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof concerns every pair of integers \(2\le p<q\). Exhaustive finite enumeration checked seven small rectangular complete bipartite graphs, including all convex-polytope vertices, their pairwise squared Euclidean distances, and the predicted counts of unordered extremal pairs.

The included `check_exact.py` checks exact integers (not floating-point approximations). Larger-parameter constructions were also tested; these do not replace the analytic combinatorial proof.

Critical arguments to verify independently are the two objects-per-right-column inequality, strict exclusion of alternative shore choices when \(p<q\), constructive attainment in each regime, and the inclusion-exclusion count avoiding duplicated edges.

No independent audit has been performed. Historical priority remains provisional.
