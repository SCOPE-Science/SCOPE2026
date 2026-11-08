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

## Reproduction

Run `python verify.py` in the extracted package with Python 3 and NumPy. The checker performs exact rational tests of the tridiagonal determinant recurrence, the two-periodic even-subsequence recurrence and the boundary repeated-root identity. It then constructs linear-variable-preconditioner FGMRES equality witnesses using explicit Arnoldi vectors and least-squares projection, and verifies representative strict and supercritical regimes.

## Limits

The finite checker is not a proof for arbitrary dimensions or real parameters; the symbolic geometry, spectral frontier and induction are fully proved in `RESULT.md`. The inner maps are invertible rank-one perturbations of the identity in the sharpness construction, not necessarily produced by any particular inner Krylov solver. Literature searches and same-model mathematical scrutiny do not establish independently certified priority.
