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

The standalone `verify.py` script uses only the Python standard library and exact integers. It checks independent forest enumeration, exact Walsh transforms, independent Bareiss determinants, a complete small-parameter spectrum and finite instances of both infinite-family classifications. Run `python verify.py` from the extracted package directory.

The matrix-forest identity is proved in the result by adjoining a new vertex and using a cofactor of the augmented Laplacian; the Schur complement and arithmetic inequalities supply all infinite assertions. Finite checks are not used as a substitute for those steps. No external or independent audit is asserted.
