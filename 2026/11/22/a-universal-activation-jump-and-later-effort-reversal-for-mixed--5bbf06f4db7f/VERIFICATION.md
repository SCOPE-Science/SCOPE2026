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

Run `python3 verify.py` using the standard Python library. It recomputes the implicit root by bisection; checks the stationary equation, global candidate comparisons on finite grids, branch monotonicity, the exact tie formula, and the second equal-effort threshold across a deterministic sample of budgets and values. The output observed from the supplied file was `PASS numerical diagnostic assertions: 75621`.

These are finite diagnostics. The continuum/global proof instead uses unimodality of the derivative factor, a strictly monotone value-difference function on the upper stationary branch, and strict monotonicity of the branch equation. The assumptions are an idealized fixed-mean Poisson allocation and additive fruit value; no field-calibrated empirical claim is made. External independent validation has not been performed.
