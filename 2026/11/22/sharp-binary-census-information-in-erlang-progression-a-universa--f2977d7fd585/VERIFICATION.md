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

# Reproducible mathematical checks

Run `python check_erlang.py` with Python 3 and `mpmath`. The numerical script requires no network access. It computes truncated Erlang probabilities directly using finite positive sums with high precision; bisects roots; verifies the conditional-moment identity against the Fisher expression, local maxima near the root for the selected stage values, and the Poisson-score orthogonality; and compares large-stage values with the explicit asymptotic constants. The present replay passed 108 diagnostic assertions at 65 decimal digits of working precision.

The analytic proof in `RESULT.md` is necessary for uniqueness for every integer stage number, optimality among all measurable binary partitions, and the limit expansion. Numerics, even at large stage numbers, are not a substitute for the proof. No assessment by an independent scientific auditor has been performed. Locally optimal sampling requires a nominal stage rate.
