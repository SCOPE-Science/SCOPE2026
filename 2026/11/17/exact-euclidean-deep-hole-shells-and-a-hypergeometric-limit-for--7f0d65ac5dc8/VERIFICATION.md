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

# Reproducibility and proof boundaries

Run `python verify_panhandle_distance.py` with a Python environment containing NumPy and SciPy. The file independently enumerates the rank-subset vertices, tests each rational nearest-point formula and exact supporting-plane certificate against the full list of allowed bases, checks the exact shell multiplicities, and solves 1,116 small constrained quadratic programs with SciPy.

Observed checks: 56 distinct parameter configurations, 6,034 source vertices, 3,174 excluded vertices, 168,870 exact supporting inequalities, 102 positive shell counts, and 1,116 independently optimized numerical projections; maximum coordinate gap was approximately \(1.08\times10^{-14}\). The program uses the provided original mathematical formulas but derives feasibility and supporting inequalities independently from enumerated base vertices. Numerical tolerances are not exact proofs of high-dimensional or limiting assertions.

The infinite-dimensional statement is proved by the supporting-normal argument and the strict convex-combination identity in `RESULT.md`. The Gaussian limit uses the standard finite-population hypergeometric central limit theorem and a differentiable transformation, not a finite simulation. No independently performed mathematical audit or historical priority certification is asserted.
