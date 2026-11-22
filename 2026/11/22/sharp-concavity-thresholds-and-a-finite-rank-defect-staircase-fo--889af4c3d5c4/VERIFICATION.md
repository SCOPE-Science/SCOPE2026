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

# Verification and reproducibility

The proof of the general theorem is fully analytic in `RESULT.md` and uses telescoping weighted-shift moments, the finite-difference integral formula, positivity of power integrals, strict Cauchy--Schwarz, and a power-law tail estimate. Repeating finitely many examples cannot establish all-index positivity or infinite-dimensional Schatten membership.

The standalone file `verify_fractional_defects.py` uses Python's standard-library `decimal` module at 85 digits. Run `python3 verify_fractional_defects.py`; the expected output is `FRACTIONAL_DEFECT_DIAGNOSTIC_OK 888`. It checks positive denominators, negative numerators, monotone threshold separation, defect sign patterns and large-index leading constants for four integer orders.

The explicit source date and classification were checked against arXiv:2611.20171v1. Primary-literature statement and example comparisons appear in `REVIEW.md` and the structured record. The publication date and priority are not independently certified; independent review has not been performed.
