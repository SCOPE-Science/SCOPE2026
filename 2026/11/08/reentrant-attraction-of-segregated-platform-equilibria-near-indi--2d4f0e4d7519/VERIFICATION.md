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

# Reproducibility and checks

Run `python3 verify.py` with Python 3; no third-party dependencies are required. The checker reconstructs the two original logistic platform probabilities, the activity-weighted platform opinions, the absolute-value diversity rewards, and the full two-dimensional counterfactual differential equation. It evaluates the candidate segregated states directly and verifies small equilibrium residuals; it differentiates the original equations numerically in both original state coordinates and compares the Jacobian trace/determinant with the two derived analytic eigenvalues. It also brackets the unique minimum of \(B\), the two crossings at \(\beta=8\), and the stable–saddle–stable sample sequence.

The general results, including the uniqueness of the minimum and the strict negativity of the longitudinal eigenvalue, are proved by symbolic differentiation and monotonicity in RESULT.md. The finite checks confirm calculations but are not substitutes for those arguments. Parameters at the transverse-zero points are deliberately excluded from local exponential stability assertions. The supplementary document cited by the primary article was not retrieved, and prior-work coverage cannot be formally ruled out.
