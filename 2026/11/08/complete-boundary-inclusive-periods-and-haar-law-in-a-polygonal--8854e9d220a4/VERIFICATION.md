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

The proof is self-contained in `RESULT.md`. A reproducible standard-library checker is included as `checker.py` and can be executed with `python3 checker.py`.

The checker establishes exact rational affine branch identities over each full open face by verifying branch inequalities at all three vertices; it also checks whole-edge affine mappings using exact endpoint inequalities. It composes the face branches symbolically for the three/seven return identities, derives the edge permutation and orientation products, checks the four vertices and the unique interior fixed point, and performs supplementary finite-grid tests. No floating-point approximations or external software dependencies are required.

Finite grid checks are regression tests, not proofs of exhaustive orbit classification. Exhaustiveness comes from the finite geometric partition and whole-stratum affine identities in the written proof. Publication priority and independent verification are not certified.
