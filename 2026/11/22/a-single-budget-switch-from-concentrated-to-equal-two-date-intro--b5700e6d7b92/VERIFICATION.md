---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and boundaries

Run `python3 verify.py` with Python 3 and no third-party packages. It checks the direct four-state mixture against the reduced expression, evaluates many allocations and contrasting parameter regimes, validates the derivative identity numerically, checks monotonicity of the crossing function and the at-least-one contrast, and calculates the example root in 60-digit decimal arithmetic. The reference run reports 44,948 passing finite assertions.

The infinite theorem is analytically proved in RESULT.md: conditional Poisson thinning with an environment-independent joint release-count law, the restriction to center and endpoint candidates, the exact endpoint-value factorization and strict decrease of the critical function. Finite sampled parameter grids cannot replace the analytic proof or establish historical novelty. The isolated census-success proxy is not a multigeneration invasion or ecological-management model. The metadata above describe the supplied verification package.
