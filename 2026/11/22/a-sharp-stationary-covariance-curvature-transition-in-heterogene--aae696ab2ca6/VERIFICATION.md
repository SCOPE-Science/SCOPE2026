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

The stationary covariance derivatives follow from the regenerative bilateral-exponential law and the signed-coordinate telegraph generator. The independent finite checks in `checker.py` use exact rational moment and generator arithmetic for three odd integral Lamperti powers and floating Gamma checks for noninteger exponents, with 1,343 assertions.

Run `python checker.py` with Python 3 and no third-party libraries. It should report `PASS: 1343 exact-rational and floating-point consistency assertions`. Exact rational checks validate selected parameter tuples; they do not establish the all-parameter theorem, which follows from the analytic moment and semigroup proof in `RESULT.md`. No independent audit, physical experiment, or inference-noise calibration is claimed.
