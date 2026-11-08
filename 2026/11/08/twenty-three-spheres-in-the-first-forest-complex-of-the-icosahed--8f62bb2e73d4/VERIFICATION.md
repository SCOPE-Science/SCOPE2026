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

# Verification and limits

`python3 verify_icosahedron_forest.py` reproduces the exact finite certificate using only the Python 3 standard library. It reconstructs the graph, enumerates every vertex subset, and cross-checks the face predicate with an independent edge-based implementation. It then verifies two complete acyclic matchings, calculates the signed integral critical-boundary matrices, and exhibits two separate unimodular rank-two minors.

The calculation visits exactly 323 nonempty faces and 972 directed Hasse incidences in each acyclicity check. The matchings leave one critical zero-cell, two critical two-cells, and 22 critical three-cells. The unit minors certify integral surjectivity of the attaching map, proving \(\bigvee^{20}S^3\) by CW cancellation. Independent full-simplicial boundary computations yield ranks \((11,55,85)\) over each of \(\mathbb F_2\) and \(\mathbb F_3\); these field checks corroborate, but are not used to replace, the integral proof.

`verification_output.txt` contains all critical-cell masks, both complete integer matrices and the unit-minor column indices. No infinite extrapolation or external independent audit is claimed.
