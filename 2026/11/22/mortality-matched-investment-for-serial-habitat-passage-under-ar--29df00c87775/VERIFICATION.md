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

## Verification scope

The exact density and hyperbolic-sine representation are algebraically reconstructed in `RESULT.md`. The proof of strict rate bias follows from positivity of the coefficients in the \(\operatorname{sinhc}\) power series; the finite tests are supportive only. The symmetric-loss conclusion uses an established stochastic comparison of sums of independent exponential waiting times with fixed total rate. Differentiation of the small-horizon expansion is justified uniformly on a compact rate interval; large-horizon convergence holds for the first two rate derivatives because both mortality rates are positive.

The reproducibility program `check.py` requires Python 3, NumPy and SciPy and evaluates two independently derived integrals, unequal-loss swapped allocations with a deliberately nonmonotone reward window, symmetric-loss deadline balance, and the limiting optima. The tests are numerical and do not establish all-real-parameter correctness or originality. No claim of external review, experimental calibration, or independent certification is made.
