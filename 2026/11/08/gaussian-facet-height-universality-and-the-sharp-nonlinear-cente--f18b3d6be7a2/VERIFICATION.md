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

# Computational checks

Run `python verify.py` with Python 3, NumPy and SciPy installed. The program uses deterministic numerical quadrature and seeded random sphere-point simulations. It directly constructs candidate affine supporting planes from singular-value decompositions, conditions on the facet event, and compares the observed mean heights with integration of the exact conditional density. It separately checks curvature, saddle Gaussian variances/CDFs, sphere/Gaussian total-variation integrals, and the coefficient in the nonlinear centering transition.

Representative results: for \(d=600,m=1800\), the integrated centered variance is \(0.46175\), compared with the predicted \(0.46130\). For \(d=500,m=1000\), the computed total-variation distance between spherical and Gaussian conditional offset densities is approximately \(0.01630\). For the critical-centering calculation at \(d=3000000\), the finite shift is \(-0.49869\), approaching \(-\mu^3=-0.50795\). The completed script prints `ALL_HEIGHT_UNIVERSALITY_CHECKS_PASSED`.

The proof is analytical. Numerical quadrature and finite random experiments neither establish infinite-dimensional limits nor independently certify the mathematical result. Independent audit has not been performed.
