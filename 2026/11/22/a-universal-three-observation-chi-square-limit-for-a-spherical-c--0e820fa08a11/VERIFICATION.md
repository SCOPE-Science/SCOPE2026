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

# Verification record

The reviewed scientific claim is the universal fixed-three-observation, increasing-coordinate limit for the exact sphere-integrated, column-standardized characteristic-function statistic. In the included `check.py`, reproducibility was exercised with `python check.py` (requires NumPy and SciPy). The actual output reported `CHECKS PASSED: 267` and constants:

- \(C_3=0.128595873650625\ldots\)
- \(\beta=-0.201475334564041\ldots\)
- \(\gamma=0.037820472231185\ldots\)
- limiting upper 5% normalized-and-scaled cutoff \(0.0251246839639858\ldots\)

Numerical checks compare spherical quadrature and hypergeometric evaluations, reproduce the Bessel special case, verify zero-row-sum Gram tangent identities and the scale of the analytic Taylor expansion, and check the coordinate covariance for Gaussian, uniform, and Laplace samples. Those samples provide only reproducibility checks. The proof of universal weak convergence uses exact algebra, a uniform hypergeometric expansion, and a bounded i.i.d. vector central limit theorem. The total-variation separation uses an exact Hellinger-affinity inequality. These analytic components are fully stated in `RESULT.md`.

Unproved limits: the same second-order law is not asserted for four or more observations, dependent columns, general covariance whitening, approximate integration, or simultaneously growing sample sizes. The scientific review was same-model only; no independent mathematical audit or external validation has been performed.
