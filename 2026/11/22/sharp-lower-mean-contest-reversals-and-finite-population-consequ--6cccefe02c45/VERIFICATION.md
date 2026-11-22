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

# Verification and scope

The standalone `verify.py` uses only the Python standard library and exact fractions, with `python3 verify.py` as the invocation. It checks the two atomic laws and their first two moments at rational points, cubic distribution and polynomial certificates, the sharp rational sign-reversal witness, the finite-population fixation recurrence and its monotonicity for community sizes 2 through 12, and detailed balance/likelihood-ratio ordering with positive immigration over several independent rational parameter families. It checks that `2/25 - 6/75 = 0` and `-11/65 + 6/75 < 0`, as exact sufficient margins for the all-real-discrimination theorem.

The universal moment bounds use Cauchy–Schwarz, the hard logistic limit uses dominated convergence, the noisy discrepancy uses the uniform beta-density bound and an exact exponential integral, and all-population fixation/stationarity follow from the birth–death equations and detailed balance. These are analytic arguments, not extrapolations from enumerated tests. The beta-opponent benchmark, fixed independent trait draws, finite community update assumptions and lack of empirical validation are material restrictions. Independent external checks have not been performed.
