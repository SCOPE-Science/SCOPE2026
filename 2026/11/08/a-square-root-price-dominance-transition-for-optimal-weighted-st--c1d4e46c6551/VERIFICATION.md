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

# Verification of the weighted-star design theorem

The algebraic proof in `RESULT.md` is the infinite-dimensional-parametric (all positive price vectors, all integers \(m\ge2\)) justification. The executable checker is `verify.py`; extract it from the same data record as the report and run `python3 verify.py` with NumPy installed.

The code tests the unit-threshold leaf-coordinate PSD condition with exact rational principal determinants, the exact candidate budget cost and the predicted Laplacian eigenvalue, and work-normalized information eigenvalues of normalized incidence-row sampling. It also compares against randomly generated nonnegative budgets, across 1367 square-rational price vectors of various sizes and 12980 competitors. A successful run prints `VERIFY_OK exact_design_cases=1367 principal_minors=36225 random_comparisons=12980`. Numerical eigensolvers verify test examples only and cannot certify a universal theorem. Neither the numerical tests nor the analytic derivation establishes optimality for a non-stationary, adaptive, or work-varying runtime objective; those are not claims of this package.
