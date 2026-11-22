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

# Reproduction checks

From a directory containing `verify.py`, run `python verify.py` with Python 3, NumPy and SymPy available. The script checks exact rational and radical formulae, the explicit two-sided invasion thresholds, 4,400 randomly sampled matrix eigenvalue comparisons, and 3,216 sampled moment-envelope checks. A successful execution prints two PASS lines.

These experiments are neither exhaustive nor sufficient for the universal infinite-parameter theorem. The general facts are proved in RESULT.md from matrix similarity, Rayleigh–Ritz, convexity of the top symmetric eigenvalue, isolated-eigenvalue perturbation and the dimension-two compression plus interpolation rigidity argument.

The law of large numbers needed to connect a sparse random network epidemic to the finite-dimensional mean-field description is not asserted here. No finite-network stochastic outbreak probability or independent external verification is certified.
