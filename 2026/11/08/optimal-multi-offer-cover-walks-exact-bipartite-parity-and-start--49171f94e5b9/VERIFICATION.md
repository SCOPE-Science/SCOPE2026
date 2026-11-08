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

The result is proved by geometric-stage decomposition, log-concave convolution and a pathwise count-process argument. Reproduce the finite independent check with `python checker.py` (Python standard library only). The checker verifies 704 exact labeled-walk CDF identities, 160 odd-parity equalities, 2,564 strict even-time comparisons and 513 likelihood-ratio minor inequalities. It also verifies the four-step \(K_{3,2}\) two-offer probability \(10/27\).

The all-size theorem is an analytic statement, not an extrapolation from computation. The mean difference \(23/28\) for \(K_{3,2}\) follows from a separate geometric generating-function calculation in the proof. No independent external validation has been performed. All source-comparison limitations are recorded in REVIEW.md.
