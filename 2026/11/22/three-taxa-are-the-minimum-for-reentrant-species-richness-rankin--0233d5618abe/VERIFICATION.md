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

# Verification notes

Run `python3 checker.py` using Python 3 standard library. The checker performs a coefficient-by-coefficient multiplication confirming the exact eleven-degree difference polynomial, rational sign bracketing of both interior zeros, strict signs at three explicitly rational values of \(e^{-v}\), numerical diagnostics of the plastic-constant expression, and 128,304 finite supplementary evaluations for positive integer two-taxon capture-rate quadruples. The proof of the general one-switch law is the sign/convexity argument in `RESULT.md`; the finite scan is not an exhaustive all-real-parameter certificate. The exact three-taxon root count follows from strict monotonicity of two factored polynomials, not from root-finding alone.

The public Dryad record dates the relevant source material to 2024-08-27. The 2024-12-16 journal date is separately disclosed. The Kirtane field study does not calibrate the hypothetical positive rate vectors and cannot validate their real-world applicability. The mathematical statement is self-contained within the attached sources and checker; no external model fitting, independent audit, or field confirmation has been performed.
