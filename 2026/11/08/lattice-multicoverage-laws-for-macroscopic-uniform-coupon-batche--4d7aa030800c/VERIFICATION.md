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

`verify.py` runs exact capped-occupancy and tagged-coupon finite-state calculations with rational arithmetic. Executed successfully: 2,268 assertions across 4–7 coupons, all possible nontrivial uniform batch sizes, multiplicity 1–3, and time horizons 0–5. Checks included distribution normalization, three factorial moments, one-type binomial mean, negative pair covariance, and completion-probability bounds. The analytic proof of the infinite limit and moment corrections does not follow from these finite cases. All asymptotic estimates are proved by finite-degree polynomial coefficients, negative covariance, and uniform tail bounds. Independent external audit has not been performed.
