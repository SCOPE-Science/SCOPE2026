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
# Reproducibility and bounds

Run `python3 check.py` using Python 3 standard library. The checker computes the moments from the coupled moment equations for a stationary symmetric two-state telegraph drive, rather than numerically integrating the four-dimensional cumulant formula. It checks the exact standard telegraph special case, sign and monotone magnitude at multiple orders and times, the dominant power coefficients, the critical logarithmic slope, and convergence toward finite fourth-cumulant limits. Passing finite tests verify numerical consistency, not an asymptotic theorem. The proof of all-time negativity and asymptotic regimes is analytic in `RESULT.md`. An independent external scientific assessment has not been performed.
