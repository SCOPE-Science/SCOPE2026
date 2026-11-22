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

# Reproduction

Use `python checks/check.py` from this package. Python 3.10 or later is sufficient for its 266 exact-rational assertions. When NumPy and SciPy are installed, the same command also performs 16 optional numerical assertions comparing central jump quadrature at degrees 24 and 48 with the Gaussian sharp constants.

The exact checker uses independent polynomial integration with rational coefficients, and finite Markov transition matrices for the two integral averaging operators. It verifies stochasticity, reflection, one-step known Durrmeyer \(L^1\) constants, and multiple-iterate jump residuals at low degrees. Sample exact squared \(L^2\) values at the midpoint after two iterations: at degree 2 the Kantorovich value is \(13/108\) and Durrmeyer is \(43/256\).

The numerical extension checks only finite degrees; the convergence, concentration, and uniform endpoint theorem require the analytic Gaussian limit, endpoint tail bound, derivative-measure representation, and strict-maximizer argument in RESULT.md. The original 1976 Jones article was not available in full; the archive description and independent later restatement were used, and a historical priority risk remains. Independent mathematical audit is not performed.
