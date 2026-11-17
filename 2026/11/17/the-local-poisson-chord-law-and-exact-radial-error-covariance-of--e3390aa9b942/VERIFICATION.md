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

Run `python verify_cyclic_radial.py` with Python 3; only the standard library is required. Its independent routes are: (i) direct Euclidean line-segment intersection for randomly sampled circle polygons, without the small-angle approximation; (ii) stationary exponential renewal trajectories for two query points; (iii) numerical quadrature of the two conditional expectation integrals; (iv) finite-sample semicircle-coverage quadrature compared with the limiting integral.

Observed output: `PASS: conditional-renewal quadrature (4 cases), Poisson moments and covariance, finite-sample containment quadrature (8 cases), and Euclidean chord geometry with independent random cyclic polygons (2 sample sizes).` The corresponding theoretical zero-lag variance is \(12\pi^4\), and the predicted lag-\(2\pi\) covariance is approximately \(931.704851339781\). The boundary-window inclusion limit at \(x=1\) is approximately \(0.1488873611052518\).

The analytical proof requires no random simulation for its universal statements. The checker does not certify independence from every earlier publication, global-process convergence, or a uniform asymptotic in query location.
