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

# Verification and reproducibility

The theorem is proved analytically in `RESULT.md`, using strict convexity of spectral trace functions, exact book-graph eigenvalues, a one-variable optimization, a sharp derivative sign comparison, and an order-dependent monotonicity calculation. The proof covers all \(m\ge2\), all real \(p\ge0\) and all positive edge prices and budgets, with disconnected allocations assigned infinite cost.

Run `python verify_book_moments.py` with Python, NumPy and SciPy to reproduce **13,679 finite assertions**. The code independently builds the complete weighted Laplacian, compares its spectrum with the three-mode formula, checks the explicit allocation against independent scalar minimization, compares against diverse asymmetric allocations, and tests representative thresholds, peak locations and asymptotic regimes. No optimization solver is used in the proof. Numerical comparisons are supporting diagnostics rather than exhaustive verification of real-parameter or unrestricted-global claims.

Scientific limits: the calculation does not generalize to heterogeneous spoke prices, nonlinear budget constraints, or different graph families. Published-work comparison is bounded by the cited material; unindexed prior formulations may exist. No independent audit or external mathematical validation is claimed.
