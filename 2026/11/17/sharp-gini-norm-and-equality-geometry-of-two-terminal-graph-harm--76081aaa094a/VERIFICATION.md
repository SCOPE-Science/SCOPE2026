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
The exact-rational checker `check_harmonic_gini.py` solves the interior Laplacian Dirichlet equations without floating-point arithmetic and evaluates all nonconstant binary cuts. It verifies all 771 connected unweighted simple graphs with two through five vertices, 390 additional randomly generated connected weighted graphs, sorted-gap saturation conditions, balanced split-star upper-envelope witnesses through 29 vertices and endpoint-interpolated unit paths through 49 vertices. Each check is finite corroboration only. The unrestricted theorem follows from the analytical triangle-inequality, Dirichlet uniqueness, and sorted-gap proofs in `RESULT.md`.

No independent audit has been performed.
