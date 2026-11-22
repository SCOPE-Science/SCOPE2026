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

The proof is analytic: the exact cycloid chord identity establishes the unique global diametral pair; Taylor expansion and arclength Jacobians reduce the near-diameter event to a two-variable simplex, whose beta integral gives the sharp coefficient and normalized Dirichlet limit. The Euler-gamma normalization and absolute cuspidal-curvature conversion are checked algebraically.

The standalone `check.py` can be run with Python 3.13 and SciPy 1.17. In one replay it passed coefficient equivalence, three finite-threshold nested numerical quadratures, a conditional cubic-deficit moment and 20,100 grid pair checks. Ratios of numerical tail probabilities to the claimed leading coefficient were approximately 1.0262350114, 1.0112603268, and 1.0050207385 at deficits 0.01, 0.001 and 0.0001, respectively; these converge toward 1 consistently with the analytic expansion. The conditional mean scaled left deficit was approximately 0.286831903 at 0.0001, against the Dirichlet prediction 2/7.

Finite quadrature and grids do not verify the global infinite theorem; the stepwise proof must be assessed separately. The result excludes alternative sampling laws, arbitrary singularities, multiplicity of diametral pairs and quantitative error rates. Complete texts of some plausible archival works and some indexed scientific records were not available. Historical priority remains provisional; independent audit is not performed.
