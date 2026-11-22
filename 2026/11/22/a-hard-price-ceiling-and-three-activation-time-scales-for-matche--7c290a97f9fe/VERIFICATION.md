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

# Reproducibility checks

Run `python3 verify.py` with Python 3, NumPy and SymPy available. The standalone script returns `VERIFY_OK 5289 ...` on a passing run. It tests the claimed spectral decomposition by exact rational eigenvector identities, compares the spectra and heat traces to independently constructed weighted Laplacians, verifies both activation thresholds and the high-price permanent-deletion regime over multiple sizes and costs, checks stationary points and budgets, and samples unrestricted asymmetric allocations and large-network limits.

The proof for all positive real prices, budgets and observation horizons, and all integer graph sizes at least three, is the analytic proof in `RESULT.md`. No finite sample set certifies an infinite quantifier or excludes an unknown prior theorem. The displayed root conditions can be reproduced using bisection of the strictly monotone equations in that proof. The threshold conclusions do not rely on a floating-point solver returning an optimal solution.

An independent mathematical audit has not been performed.
