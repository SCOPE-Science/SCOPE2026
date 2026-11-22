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

The derivation uses the exact published rank bands and a monotone quantile perturbation supported only between their quantile levels. The analytic derivative inequality proves positivity of the alternative density. The two sample QCMs agree on the count event defined in the proof. Binomial union bounds and matching lower-event counts give the stated exponential rate for the canonical coupling disagreement. No numerical or simulation claim is used to prove an infinite-sample theorem.

`python3 checker.py` was executed with Python 3 standard library and returned **24,271 assertions passed**. It verifies the derivative margin, rank-band identity and strict failure event, exact finite-n binomial bounds, Chernoff inequalities, and the distinguishable alternative's CDF discrepancy. The test cases and deterministic random seed are documented in the script. Executions are reproducible without network access.

The available published materials were checked at the level of functional form and mathematical implication. Database-search incompleteness and potential older general theorems are acknowledged. Independent mathematical audit has not been performed.
