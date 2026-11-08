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
# Reproducibility and verification

The defining endpoint polynomials, derivative identities and proofs appear in `RESULT.md`. Run `python3 verify.py` using an ordinary Python 3 interpreter. The program depends only on the standard library and checks mechanical-word and derivative identities with exact arithmetic for reduced fractions with denominators \(2\le q\le45\); it also checks a rational endpoint sample and computes no extrapolated theorem. Each finite assertion is supporting evidence, not a replacement for the analytical proof of all cases.

Scientific limits: the published direct rational plateau formula is assumed; the inverse-slope monotonicity is established by the full symbolic prefix-sum proof. The opening expansion is local at fixed \(p,q\), and independent validation is not claimed. The source comparison has a residual publication-priority uncertainty for alternate terminology in historical mode-locking literature.
