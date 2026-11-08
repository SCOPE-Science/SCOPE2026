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

The analytical proof establishes the cut-halfspace description, Laplacian eigenvalue bound, strict separation of nonsingleton cut planes, the key quadratic inequality, and the middle-cut threshold for every integer parameter in scope. No finite test substitutes for these arguments.

Actual reproducibility check: execute `python verify_bipartite_centers.py`. It tests pairs (4,4), (4,5), (4,11), (4,12), (4,15), (5,5), (5,6), (5,20), (6,6), (6,7), (6,29), (6,30), (7,7), (7,8), and (7,50). Each test checks the least cut-plane distance across all cut cardinalities, and for 120 seeded randomly generated candidates compares the asserted center classification against the full cut-inequality family. It checks cube-section vertex counts separately for part orders 4 through 11. Expected successful output: `BIPARTITE_GRAPHICAL_ZONOTOPE_CENTER_CHECKS_PASSED`.

Limits: these are finite checks of sampled centers and of count-reduced cut families, not exhaustive sampling of the continuum. All-parameter correctness depends on the proof. Historical priority has not received an independent review.
