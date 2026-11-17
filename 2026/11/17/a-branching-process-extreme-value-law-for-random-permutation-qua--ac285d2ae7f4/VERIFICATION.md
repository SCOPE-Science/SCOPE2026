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

# Reproducibility and boundaries

Run `python verify_cycle_maximum.py` using Python 3 with the standard library only. Successful execution prints `PERMUTATION_QSO_MAXIMUM_BRANCHING_CHECK_OK`. The executable checks both the exact single-orbit equilibrium projection at two mixing coefficients and full permutation enumeration through size six, then compares the limiting branching law against analytic cycle-index approximations and seeded Monte Carlo of the actual normalized extreme. The expected Monte Carlo estimates at size 350 are approximately 0.564 at threshold 1.5 and 0.795 at threshold 2, compared to limiting predictions 0.582812 and 0.796812. Small finite-size deviations are not mathematical contradictions.

The generating-function argument, the analytic Chernoff estimate, and the branching-progeny Lagrange inversion are proved in RESULT.md and are not delegated to numerical computation. The executable is a finite test, not an infinite certificate or independent mathematical audit. The random generator seed is fixed for reproducibility. Complete full-text inspection of a plausible related 2024 article remained unavailable, and that priority risk is recorded.
