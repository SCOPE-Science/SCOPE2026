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

# Verification and limitations

Execute `python verify.py` using Python 3, NumPy and SymPy. Numba is optional. The self-contained checker tests the second/fourth stationary moment recursions independently of the final compact covariance formula, exact rational specializations for Erlang stages one through eight, rational root brackets, deterministic-clock simplification, small/large confinement limits and exact Gaussian transition simulations of full on/off cycles. Its simulation uses pre-seeded dwell and Brownian innovations and compares covariance estimates to their own batch sampling uncertainty.

The proof in `RESULT.md`, not the numerical samples, establishes all global all-parameter claims. Numeric tests do not certify root uniqueness, infinite-lag signs, novelty or publication priority. For shapes four and above, only the existence of a sign reversal follows from the proved endpoints. The model uses stationary **event-indexed** complete cycles rather than a fixed-time stationary autocovariance. An independent mathematical audit has not been performed.
