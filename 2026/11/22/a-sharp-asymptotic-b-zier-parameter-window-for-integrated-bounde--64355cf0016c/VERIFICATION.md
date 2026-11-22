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

# Verification details

The standalone `check.py` was executed with Python 3, NumPy, and SciPy from its own current package path. It completed successfully with these output classes:

- `STEP_RESPONSE_DIRECT_QUADRATURE_PASS: 126`: 126 direct step-response integrations compared with the analytical split integral for selected degrees and parameters.
- `DEGREE_ONE_ENDPOINT_FORMULA_PASS: 5`: the \(n=1\) sharp constants match \(\max\{1,\alpha\}/(1+\alpha)\).
- `GAUSSIAN_PARAMETER_CROSSING_PASS 1.405429234985 0.757497464523`: root and Gaussian integral comparisons, including the exact order-one/order-two constant and parameter classifications at sampled values.
- `FINITE_DEGREE_ASYMPTOTIC_PROFILE`: computed degrees \(16,32,64,128\) for parameters \(1\), the numerical optimum, and \(2\); the observed values converge toward the analytically proved limit. They converge slowly at parameter \(2\), and no finite numerical threshold is asserted.
- `BERNSTEIN_BEZIER_VARIATION_CHECKS_PASS`: all assertions succeeded.

The universal results instead depend on the signed-measure reduction, strict cell convexity, uniform binomial concentration, the central limit theorem, and the separated-support logarithmic ratio argument in RESULT.md. Numerical tests alone cannot establish global extremizers, infinite-degree limits, uniqueness of the minimizer, or historical originality. No independent mathematical audit has been performed.
