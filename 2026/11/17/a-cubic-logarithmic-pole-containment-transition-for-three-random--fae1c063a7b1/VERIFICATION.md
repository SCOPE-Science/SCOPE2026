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

The exact analytical argument is in RESULT.md. The independent numerical implementation `check_cap.py` evaluates the five-variable conditional integral by scrambled Sobol quadrature and separately tests Cartesian cross-products of three directly sampled unit-sphere vertices. NumPy and SciPy versions satisfying `requirements.txt` suffice.

Observed quadrature: for \(h=0.10\), \(\Delta\approx0.0013729664\); for \(h=0.05\), \(\Delta\approx0.0002274707\); for \(h=0.02\), \(\Delta\approx0.0000186758\). Simulations with 1,200,000 triples per selected parameter gave \(0.00137333\) and \(0.000235\) for \(h=0.1\) and \(0.05\), within predicted sampling tolerances. The code printed `SPHERICAL_CAP_POLE_CROSSOVER_CHECKS_OK`.

The finite computations test only particular parameter values and must not be substituted for the uniform analytic asymptotic bounds or historical priority review. No independent audit has been performed.
