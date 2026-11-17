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

# Reproduction and checks

Run `python root_vertex_deletion_check.py` with Python 3, `numpy`, and `scipy`. This program constructs the complete signed-root polytope and its one-root deletion in an orthonormal basis, evaluates both hull volumes for dimensions \(n-1=2,\ldots,6\), compares ratios with exact rational expressions, verifies the facet Gram determinant and the nearest-point witness, and tests the exact random-direction loss identity on deterministic sample vectors. The program prints `ROOT_VERTEX_DELETION_EXACT_NUMERIC_PASS` on success.

The full-dimensional volume formula is derived analytically from the crosspolytope Gram determinant and the classical simplex difference-body equality, not established by a finite list of convex hulls. The Gaussian extreme-gap conditional weak limit is proved by reduction to the established two-sided Gaussian extreme-value point-process theorem, not by a simulation. The published-record comparison is provisional; no independent audit has been carried out.
