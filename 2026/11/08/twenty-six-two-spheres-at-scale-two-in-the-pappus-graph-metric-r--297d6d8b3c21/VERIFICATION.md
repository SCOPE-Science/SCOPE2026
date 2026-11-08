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

# Verification and reproducibility

Run the included `verify_pappus_rips.py` with Python 3 and no third-party packages. It creates the Pappus graph from the explicit 18-entry LCF displacements, computes all 18 BFS distance arrays, checks all 153 unordered vertex pairs and the six distance-four triangles, and reconstructs the graph-metric clique complexes. It verifies the scale-two cover and literal intersection, and constructs a 99-pair discrete-Morse matching on every scale-two simplex. The complete directed Hasse diagram is topologically sorted; there are no directed cycles. Exactly one critical zero-cell and 26 critical two-cells remain. This is an independent integral-homotopy certificate for the principal sphere-wedge result.

The script further performs exact mod-two boundary eliminations at integer scales one, two, and three, verifies the full 4095-face scale-three simplicial join, and verifies diameter four. These field-valued computations corroborate but do not replace the integral geometric argument. `verification_output.txt` records the expected deterministic program output, ending with `PAPPUS_RIPS_EXACT_FINITE_CHECK_PASS`. All finite enumerations are exhaustive. No external audit, broader graph-family proof, or certification beyond the stated checks is asserted.

Limit: the computation is for the one specified 18-vertex graph, with unit-edge shortest-path vertex metric and inclusive thresholds. The earlier scale-three result is credited, not treated as newly established priority.
