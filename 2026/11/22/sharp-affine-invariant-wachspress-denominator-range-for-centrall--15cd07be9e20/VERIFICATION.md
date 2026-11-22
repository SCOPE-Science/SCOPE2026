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

# Mathematical verification

The proof is analytic for all real admissible shape parameters; it is not inferred from finite computations. The six explicit Wachspress weights and center/vertex formula can be independently reconstructed from the facet slacks and outward normal determinants.

Run `python verify.py` using the bundled file. It performs exact rational two-variable polynomial arithmetic with no packages other than the Python standard library, checks affine precision and the quadratic formula on 210 genuinely hexagonal rational shapes, then verifies each vertex evaluation, the sorted-gap ratio and its nonnegative deficit.

Analytic checks requiring no computation include the canonical strip normalization, strict positivity of the quadratic penalty's two leading principal minors, monotonicity of the positive harmonic-pair function, and the exact deficit factorization. These support the universal statements and their equality cases.

No independent mathematical audit or validation is asserted. Historical priority remains subject to later independent literature review.
