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

`python verify.py` uses only the Python 3 standard library. It checks the scalar recurrence's covariance balance and fourth cumulant by exact rational arithmetic on many choices of step and stage law; tests the exactly calibrated Pythagorean deterministic-stage family, a strict non-Gaussian random-stage family, and the two-eigenvalue covariance contradiction; and supplements the analytic uniqueness of the mixing minimum with 9,999 grid comparisons. Its actual output is in `checks.txt`.

The principal proof is analytic and covers every positive step size, every real SPD precision matrix in finite dimension, and every Borel stage-time distribution on the unit interval. Exact finite tests cannot by themselves prove a continuous-parameter theorem; the uniform statements rely on the equations and monotonicity established in `RESULT.md`. The code and output have been replayed from these standalone package files. No independent mathematical or literature-priority audit has been performed.
