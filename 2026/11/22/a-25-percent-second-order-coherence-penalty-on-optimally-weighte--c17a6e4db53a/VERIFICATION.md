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

# Direct reproducibility

Run `python verify_double_star.py`. Its exact rational portion constructs weighted Laplacians for 15 double-star test instances with 2 to 6 leaves per hub, forms the pseudoinverse using the rank-one centering formula, and checks both reciprocal spectral-moment traces (30 exact assertions). Its numerical portion checks 27 optimum/derivative comparisons and 3 large-order asymptotic root tests, totaling 60 assertions. These finite checks are subordinate to the exact analytic proof in RESULT.md.

There is no independent mathematical review or external certification. The originality analysis acknowledges published first-order all-tree optimality and published unweighted double-star biharmonic formulas. No unsupported external verification channel is asserted.
