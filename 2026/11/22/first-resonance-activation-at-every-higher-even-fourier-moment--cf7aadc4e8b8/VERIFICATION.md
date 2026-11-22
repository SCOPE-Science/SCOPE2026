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

# Verification record

The proof in `RESULT.md` is an analytic argument. It separately identifies exact multinomial coefficient collisions, establishes strict contractivity at the critical scale, proves local maximizing-branch uniqueness, and computes the two asymptotic scales with explicit positive constants.

The standalone `checker.py` was executed with Python 3 and passed 270 exact assertions. The checks compare \(k\)-fold Fourier coefficient convolution against an independent multinomial moment formula for \(k=3,\ldots,8\), lower frequencies \(m=1,2\), resonant and nonresonant outer frequencies, two rational radii, and two rational coefficient triples. They also verify exact first and second normal-form coefficients, positive gain coefficients, and finite counting inequalities. These finite checks do not constitute exhaustive verification for all \(k,m,n\), nor do they establish originality. There is no independent audit, external validation, or formal proof certificate.
