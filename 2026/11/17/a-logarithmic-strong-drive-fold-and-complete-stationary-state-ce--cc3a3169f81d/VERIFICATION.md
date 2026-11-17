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

# Reproduction and boundaries

Run `python verify.py` from this directory with NumPy and SciPy available. The program evaluates the original homogeneous three-state Glauber currents, not only the limiting reduced field; it computes high-precision complex-step Jacobian approximations and four fold locations. It verifies stable-node/saddle signs for two parameter choices. The output recorded in `RESULT.md` was reproduced from the packaged script.

The finite numerical run tests formulas and local classifications, **not** the theorem's all-parameter equilibrium census or the limiting asymptotic expansion. Those are proved by singular rescaling, nondegenerate implicit-function arguments, compactness of the simplex, and a limiting root classification. No independent audit, machine proof, exhaustive continuum search or finite stochastic-system certification has been conducted.
