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

The analytic proof explicitly establishes sufficiency across the full closed upper boundary by an all-index nonnegative power-series recurrence, and necessity on the complementary positive-parameter region using generator curvature or a negative second exponential coefficient and Laplace-measure positivity. The fractions and boundary values in `RESULT.md` were reconstructed independently from derivatives and binomial expansions.

Execute `python3 verify_coefficients.py` alongside this document. The script is self-contained in the Python standard library and uses exact `fractions.Fraction` arithmetic, cross-comparing nine explicit parameter cases through polynomial degree 26. It also checks first 81 recurrence terms of admissible cases, verifies a negative second coefficient for inadmissible scale cases, and tests the exact boundary weights. The observed output was `PASS`.

**Scope of checking:** The finite script is not a certificate for infinitely many coefficients or every dimension; the written induction, normalization and Laplace-transform argument carry those proofs. Historical priority remains provisional. No external or independent mathematical audit has taken place.
