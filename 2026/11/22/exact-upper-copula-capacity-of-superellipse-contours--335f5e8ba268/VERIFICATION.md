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

# Verification

The analytic proof in `RESULT.md` applies to every real \(p>0\), every pair of positive semiaxes at most \(1/2\), and every admissible center. Its key steps are the folded-marginal density inequalities, an explicitly attained upper bound by four sign choices and a product residual, and a unique unit-slope crossing. All endpoints have zero marginal atoms. All prescribed marginal densities are verified pointwise almost everywhere rather than inferred from numerical simulations.

The numerical file `checks/verify.py` requires Python and `mpmath`; execute `python checks/verify.py`. It evaluates the closed formulas and numerical integrals for positive semiaxis pairs and exponents on both sides of \(1\), checks strictness of the projection bound, and reproduces circle and diamond specializations. The replayed run reported 139 passed finite assertions/comparisons. These tests support reproducibility only and are not an exhaustive validation of universal real-parameter statements.

Mathematical limitations: higher-dimensional contours, general mixed exponents and full-copula optimizer uniqueness are outside scope. An equivalent result not located in earlier sources remains a historical-priority risk. Independent mathematical review has not been performed.
