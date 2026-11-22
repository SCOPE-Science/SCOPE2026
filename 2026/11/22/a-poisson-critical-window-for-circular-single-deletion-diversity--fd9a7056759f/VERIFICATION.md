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

Run `python3 verify.py` with Python 3 standard library. The verifier generates each indexed nonconstant binary word of lengths three through twelve, computes its necklace-valued deletion degree from literal deletion, tests the upper bound by circular runs, and verifies exact run-count coefficients and first moments for each fixed weight. It separately checks the factor-uniqueness implication at every allowed short length and the translation-forest property for lengths four through forty.

Observed result: `VERIFY_OK binary_sources 8164 forest_cases 9690`.

The checker is not an infinite certificate. The all-length assertions use the proofs in RESULT.md, including the Bernoulli conditioning bound and factorial-moment argument. The matching finite checks do not independently validate novelty or the limiting result. No independent mathematical audit has been performed.
