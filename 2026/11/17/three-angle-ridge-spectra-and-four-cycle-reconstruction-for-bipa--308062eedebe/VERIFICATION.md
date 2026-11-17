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

# Verification

The accompanying pure-standard-library `checker.py` enumerates stable-set vertices, verifies nonredundancy of the prescribed facets, and determines which facet pairs meet in codimension two using exact rational affine-rank elimination. It separately computes leaves, degree wedges, and all four-cycles. The direct run reports:

`BIPARTITE_RIDGE_SPECTRUM_EXACT_PASS graphs=81`

A separate exact symbolic-rank implementation corroborated all 34 isolate-free bipartite graphs in a small unlabeled graph atlas (up to six vertices), and a distinct numerical strict-feasibility linear-programming implementation tested the same 34 graphs. Both passed. This finite set is **not** an exhaustive test of all finite bipartite graphs and is not a replacement for the proof, which separately establishes the universal classification via strict feasible points for each facet-pair type and the exact outward-normal dot products.

The case of a single edge on two vertices is included. Disconnected graphs are permitted. A cycle count is by unoriented four-cycles, not by directed walks. Historical priority and independent mathematical review remain unperformed.
