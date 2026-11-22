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

Run `python verify.py` using Python 3. The included checker uses only `fractions.Fraction` and `itertools.product`. It executes exact-rational transitions for Beverton–Holt recruitment and a second admissible recruitment function, checks the multiplicative exclusion identity, the uniformly bounded juvenile-predator coordinate, and checks the strict positive-equilibrium parameter wedge and explicit rational witness.

The correctness of the global infinite-time exclusion theorem depends on the algebraic identity and monotone infinite-product argument given in RESULT.md, **not** on finite numerical trajectories. The finite checker does not independently verify historical originality, model adequacy, stability of equilibrium, or finite-population ecological outcomes. Independent audit has not been performed.
