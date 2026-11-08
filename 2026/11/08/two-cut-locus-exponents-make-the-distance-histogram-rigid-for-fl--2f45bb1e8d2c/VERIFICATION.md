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

The complete analytic derivation appears in `RESULT.md`. Numerical cross-checks only: `python3 verify_klein.py` uses independent pair sampling in the fundamental domain and checks nearest lifts, local circular-lens integration, and cutoff coefficients.

Recorded output:

`VERIFICATION_OK distance_pair_sampling=6 local_coefficients=18 small_epsilon_ratios= [(2.0, 3.0, 1.00174842), (3.0, 2.0, 1.00249922), (2.0, 2.0, 1.00204285)]`

The six simulated CDF comparisons are checked against tolerance `0.004`; small-offset asymptotic ratios are checked to lie between `0.985` and `1.018`. All three asymptotic regimes are checked, with the explicit quadratic glide correction subtracted for equal parameters. Numerical evidence cannot establish the exact distribution formula for every positive pair; that claim is supported by the written proof. The source comparisons provide a best-knowledge originality assessment and not an independent external certification.
