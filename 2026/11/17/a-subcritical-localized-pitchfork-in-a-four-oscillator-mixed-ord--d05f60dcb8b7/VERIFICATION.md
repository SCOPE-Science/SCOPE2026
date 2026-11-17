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

# Verification evidence and boundaries

The standalone `checker.py` was run against the exact four-oscillator model with the repeated-index triple interaction. It symbolically checks the full characteristic polynomial, verifies the cubic center coefficient, checks the invariant reflection slice against the full field, compares explicit 64-term sums against order-parameter factorization, tests numerical Jacobians, and solves six local saddle branches. The execution reported PASS.

Critical proof steps not delegated to computation are the smooth center-manifold construction, the sign of the reduced cubic coefficient, the implicit-function equation for the off-axis equilibria, and the index calculation from the local eigenvalues. These are reconstructed algebraically in `RESULT.md`. Finite experiments do not establish any global claim, basin measure, or completeness of equilibria outside the local reflection neighborhood. No external independent audit has been conducted.
