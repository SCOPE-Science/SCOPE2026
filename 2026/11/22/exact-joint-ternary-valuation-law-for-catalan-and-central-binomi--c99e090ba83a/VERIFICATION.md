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

`python3 verify.py` checks the ternary joint valuation table through depth nine by independent Legendre-factorial arithmetic, direct integer binomials, and rational polynomial recurrence coefficients derived from the displayed generating function. It verifies support, sharp top boundary, means, and covariance. Output:

`VERIFY_OK levels=0..9, exact_index_pairs=29523, binomial_cases=800, support_and_boundary=PASS, rational_moments=PASS`

The finite checks do not prove the all-depth statement or the Gaussian limit; both use exact arguments in `RESULT.md`. No independent audit is recorded.
