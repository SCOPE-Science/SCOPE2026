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

Run `python check_cesaro_products.py` in the directory containing this document. The script uses Python's standard library, checks 4056 finite exact algebraic identities or finite inequalities, and prints `COORDINATE_CESARO_FINITE_IDENTITIES_OK 4056` on success.

The factorial-sum identity and the commutator coefficients are verified at finite indices with exact rational arithmetic. The Schur bounds are checked on finite samples, with floating-point tolerance solely for those samples. The full compactness theorem and sharp Hilbert–Schmidt cutoffs are proved analytically in `RESULT.md`. These finite checks are not exhaustive and cannot certify the infinite assertions or publication priority.

Source descriptions are linked in `RESULT.md`. Independent audit has not been performed.
