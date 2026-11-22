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

The correctness proof establishes exact moment identities for every permitted graph and every integer order strictly below both girths. The included Python checker, executed using `python3 verify.py`, gave `HIGH_GIRTH_WIDTH_MOMENT_EXACT_PASS k=1..4` for the dodecahedral–Desargues witness. It uses exact combinatorial support enumeration, graph girth BFS and integer Bareiss reduced-Laplacian determinants. Dependencies: Python 3, NetworkX.

Observed cardinalities: 20 vertices, 30 edges, cubic degrees, girths 5 and 6. For edge-support cardinalities one through four, every forest-shape census agrees exactly; the fourth support histogram contains seven types with the counts recorded in RESULT.md. Exact spanning-tree counts are 5184000 and 6144000. The volume factor uses the tree-incidence Gram determinant \(n\).

The theorem is not inferred from finite enumeration. No numerical Monte Carlo, external infinite proof certification or independent mathematical audit is claimed. Publication-priority limitations appear in REVIEW.md.
