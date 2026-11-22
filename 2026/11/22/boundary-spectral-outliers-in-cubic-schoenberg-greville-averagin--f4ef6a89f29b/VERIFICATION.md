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

The analytical proof derives the rational clamped cubic collocation matrix and its two scalar parity equations. The exact root count follows from explicit positive polynomial factorizations of the relevant derivatives; the splitting constant follows by a simple-root expansion. The symbolic identities, exact Cox–de Boor collocation entries, and finite eigenvalue comparisons were replayed from `checker.py` in the same package.

Computational checks: exact rational cubic spline recursion for mesh counts 4 through 12; exact rational determinants at the band edge for mesh counts 4 through 12; symbolic factor identities and logarithmic-elasticity derivative; numerical eigenvalues and parity equations for mesh counts 4 through 41. These finite checks cannot certify the universal quantifier without the proof in RESULT.md. No independent audit has been performed.
