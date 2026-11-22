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

The self-contained checker `verify_polygon.py` reconstructs the entire Gram matrix from squared vertex radii and adjacent inner products for deterministic random convex and radial nonconvex-capable cycles, as well as checking dihedral color-preserving permutations. Executed in Python 3 with NumPy in the same directory: `python verify_polygon.py`; output `RADIAL_CYCLE_GRAM_COMPLETION_PASS cases= 792 dihedral_checks= 22932`.

The analytic proof, not any finite experiment, establishes the result for all vertex counts. The most important assumptions are strict positivity of all oriented edge determinants with the origin and winding number one. The result does not imply uniqueness of arbitrary unconstrained embeddings.
