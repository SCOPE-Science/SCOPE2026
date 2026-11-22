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

The proof uses the published facet decomposition and volume generating function, then independently derives the full area-weighted limit and log-moment bound. Run `python verify_surface_rank.py` with NumPy and SciPy to cross-check the stated exact formulas against convex-hull triangulations in dimensions 2 through 4 for four parameters. Numerical convergence checks supplement the analytic coefficient proof and are not treated as an infinite-dimensional certificate. The 12 direct area and volume comparisons passed; no independent audit was performed.
