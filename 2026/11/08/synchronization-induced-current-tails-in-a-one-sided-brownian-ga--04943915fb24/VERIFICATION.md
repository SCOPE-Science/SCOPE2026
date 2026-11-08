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

# Reproducibility and scope of checks

Run `python check_current.py` with Python 3 and SciPy installed. The test program checks numerical integrals against the Brownian thinning identity, exact Rayleigh mixed-Poisson generating function and factorial moments, variance and higher factorial cumulant, finite-time mean equality, an endpoint-integral representation of the fixed-time count tail, and the fixed-parameter stationary large-current asymptotic. It prints an explicit PASS message only if its assertions succeed.

The proof does not rely on Monte Carlo extrapolation. Finite precision calculations cannot establish the integer-uniform \(q\to\infty\) assertions; those follow from the Gamma representation, Gaussian concentration and Stirling analysis in RESULT.md. The tests do not address quenched currents, finite-return dynamics, or convergence uniform in joint limit parameters.
