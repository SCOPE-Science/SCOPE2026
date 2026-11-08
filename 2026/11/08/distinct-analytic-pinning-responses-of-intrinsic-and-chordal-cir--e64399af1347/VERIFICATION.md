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

# Reproducibility and verification

Run `python3 verify.py` with the Python standard library. The script independently implements the two cell-centroid integrals by Simpson quadrature; it does not require numerical libraries or any unbundled scientific file.

Expected successful report:

```text
VERIFY_OK drift_sign_checks=132 analytic_branch_cases=20 strict_coefficient_cases=97
```

The computation tests the sign of the first displacement from regular polygons at five polygon sizes and several positive concentrations, checks convergence of iterated updates at small concentrations to the predicted first-order coefficients, and checks strict coefficient ordering for 97 finite sizes. The analytic proof supplies the exact coefficient formulas, all-\(n\) strict inequality, local implicit-function branch construction, and all-positive-concentration sign theorem. Numerical quadrature and finite iteration cannot certify those universal assertions, and the checker is not an independent scientific audit.
