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

# Verification of the finite-grid stochastic-rounding result

The included `verify.py` executes with standard Python 3 and requires no external data or packages. It performs 422 assertions. Exact rational checks cover unique finite-grid threshold values, budget feasibility, KKT active-set structure, the Markov first-step moment recurrence, unbiased coupon-collector inclusion-exclusion, and comparisons with explicit competitors. Finite numerical comparisons check the predicted asymptotic coefficients at growing grid sizes. The actual terminal output is embedded as `check_output.txt`.

The proof of strict convex global optimality for every integer \(M\ge2\), the fixed-budget asymptotic expansion, and the Gaussian fluctuation law are mathematical arguments in `RESULT.md`; the finite checker is not represented as an exhaustive or infinite certificate. The result is unverified by a scientifically independent reviewer.
