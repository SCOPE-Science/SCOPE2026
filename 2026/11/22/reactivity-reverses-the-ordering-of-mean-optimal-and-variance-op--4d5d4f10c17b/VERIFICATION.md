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

# Reproducibility and evidence boundaries

The one-dimensional half-interval and time normalization and the two moment functions are given explicitly in `RESULT.md`. Run `python3 check.py` with Python 3.11 or later (only standard library). The checker evaluates the primary mean and variance formulas in 65-digit decimal arithmetic, reconstructs total variance from independent first-passage plus geometric-number-of-returns components, finds independent stationary points of each objective and tests asymptotic scales and positivity bounds.

Observed checker output: `PASS 122 deterministic assertions`. Sample optimized speeds in the numerical run: at reactivity 0.000001, mean optimum 0.01102156774351 and variance optimum 0.01103064383686; at reactivity 10, mean optimum 4.56964451684 and variance optimum 4.24722283516.

These computations corroborate algebra and finite numerical examples but cannot prove global uniqueness or asymptotic quantifiers. Those properties follow from the analytic bounds, expansion, and derivative arguments presented in `RESULT.md`. Only sufficiently weak and sufficiently strong reactivity variance-minimizer uniqueness is proved. Independent audit: not performed.
