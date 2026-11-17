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

# Reproducibility and mathematical checks

The exact hyperbolic area expression was tested against an independently written Gauss--Bonnet angle algorithm on geodesic polygons with \(3,4,5,8,10,30,100\) vertices and multiple Poincaré radii. The attached standalone `checks/hyperbolic_circle_checker.py` repeats selected independent finite-polygon checks and uses the beta marginal of a Dirichlet gap to evaluate the finite-sample mean.

It evaluates the critical mean and variance by numerical quadrature and samples the normalized independent-exponential gap representation. The checks use \(\lambda=0.8,5,20\), \(n=600,2400\), and 2,500 independent polygons per configuration. Finite-sample means and standardized variances are compared with separately integrated predictions. It exits successfully with `HYPERBOLIC_CYCLIC_CRITICAL_AREA_CHECK_OK` when all assertions hold.

The proof of the limiting law and Gaussian fluctuations uses analytic expansions and the classical independent central limit theorem. Simulations and quadrature do not establish the theorem for all \(n\), all \(\lambda\), or unexamined geometries. Historical priority and mathematical verification by independent reviewers have not been established.
