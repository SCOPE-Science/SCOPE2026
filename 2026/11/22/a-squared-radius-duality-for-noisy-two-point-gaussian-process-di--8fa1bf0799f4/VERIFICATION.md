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

`verify_symbolic.py` checks with SymPy five identities: both normalized derivative-sign factorizations, both optimal explained-variance substitutions and the logarithmic derivative of the common scalar function. This script completed with `Symbolic identities: PASS (5)`.

`verify_numeric.py` uses only Python's standard library. It bisects the critical equation at six strictly positive noise levels, compares the covariance-derived Bayes variances with their exact formulas, checks the strict cross-kernel risk ordering and compares against ten nonoptimal radii per noise level. This script completed with `Numerical covariance and optimum checks: PASS (96)`.

The analytic proof establishes conditional covariance, monotonicity, uniqueness, limiting radii and asymptotics over all positive radii and all positive noise levels. Tests are supporting checks, not an exhaustive numerical proof. Neither script proves absence of older equivalent literature; independent audit has not been performed.
