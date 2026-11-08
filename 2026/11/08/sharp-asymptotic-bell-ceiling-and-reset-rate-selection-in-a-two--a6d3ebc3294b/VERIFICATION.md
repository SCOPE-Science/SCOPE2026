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

The self-contained mathematical proof is in `RESULT.md`, and reproducible computational checks are in `check.py`. Install the dependency from `requirements.txt`, then run `python check.py`. The deterministic checker passed 262 assertions on the actual packaged code. It independently derives the stationary density matrix through (i) a spectral Poisson integral and (ii) a sixteen-variable stationary Liouvillian linear solve. It checks trace, Hermiticity, positivity, the uniform trace-norm and CHSH error bounds, the limiting Bell profile and the fixed-interaction zero-reset boundary.

The checks do **not** certify the infinite strong-interaction limit, uniqueness of maximizers, or novelty. Those depend on the analytic three-state spectral reduction, the uniform error estimate, and the stated comparison with prior publications. The arXiv first-public date used for the motivating research source is 2023-07-14. Independent scientific audit has not been performed.
