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

# Verification details

The analytic proof establishes the exact Zak-fiber identity, frequency monotonicity, endpoint upper maximization, one-positive-root lower minimization, and positivity for every positive rate pair. The independent executable `CHECK.py` reconstructs the original Zak transform by truncating translated sums and checks the exact formulas on a finite grid for eight parameter pairs; execution printed `ASYMMETRIC_HALF_DENSITY_GABOR_CHECKS_PASSED 2644`. These finite tests support but cannot prove the infinite-dimensional statement.

The window is unnormalized, the Zak convention uses translations \(x+k\), and the Gabor lattice is exactly \((1,1/2)\). The theorem does not cover other lattice densities or optimal dual windows. No independent audit has been performed.
