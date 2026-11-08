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

# Reproducibility and limits

Run `python verify.py` using a standard Python installation. The script independently enumerates signatures of every labeled assignment of at most five elements to two or four Boolean types, and at most three elements to eight types. For three quantifier-rank thresholds it compares exact rational collision probabilities with the coefficient formula. For rank one it separately checks the Stirling-surjection sum. This covers 48 finite parameter triples, with no floating-point arithmetic in the finite identities.

The script also evaluates the exact Stirling expression at four larger Boolean-type counts and prints the scaled critical-density values, followed by a numerical tolerance check. These numerical evaluations do not establish an infinite limiting law. The infinite-dimensional claim is proved analytically by exponential tilting and an aperiodic two-dimensional local central limit theorem, with the integer-floor correction controlled by a stationary saddle rate.

Expected concluding lines:

`FINITE_LOGICAL_COLLISION_ENUMERATION_PASS cases=48`

`CRITICAL_SCALE_NUMERICAL_CHECK_PASS`

`ALL_MONADIC_COLLISION_CHECKS_PASS`

Limits: finite tests do not exhaust arbitrary type counts, quantifier ranks, or sample sizes; the universal proof covers fixed rank and positive limiting occupancy ratio. The review is not an independent mathematical audit.
