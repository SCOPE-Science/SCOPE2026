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

# Reproducibility and scope

Run `python CHECK.py` in an environment with SymPy and mpmath. The checker independently validates three symbolic stationary identities, the degenerate first derivative, the third center coefficient against the second equilibrium derivative in five positive kinetic parameter cases, five local square-root equilibria, and inverse-square finite-time convergence for two numerical trajectories. Its deterministic success marker is:

`VERIFY_OK cubic_degeneracy=5 stationary_identity=3 critical_relaxation=2`

The infinite-time and all-parameter statements follow from the mathematical proof in `RESULT.md`, not from the finite numerical cases. An independent scientific audit has not been performed. Source priority is provisional, particularly for general center-manifold normal forms.
