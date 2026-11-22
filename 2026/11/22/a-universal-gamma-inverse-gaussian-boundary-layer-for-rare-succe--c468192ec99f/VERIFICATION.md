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

# Reproducibility

Run `python conditional_check.py` and `python mfpt_check.py` in a Python 3 environment with `numpy` and `scipy` installed. Both are standalone, contain only scientific checks, and have no remote dependencies. The conditional checker solves the return first-passage boundary-value equation at finite dimensionless stiffness and directly integrates the killed-Brownian alarm density for two parameter choices. The mean-time checker independently evaluates the renewal expression and verifies the boundary flux normalization. Each script terminates with an assertion failure on disagreement.

The tests are finite numerical diagnostics and neither prove an asymptotic theorem nor establish literature priority. The analytic proof in `RESULT.md` derives the singular limit from the killed-resolvent flux, the return boundary-value problem, exact splitting-factor bounds, and the conditioned Laplace transform. The proof assumes the stated local regularity and integrability of the search resolvent; the accompanying Brownian example verifies these assumptions explicitly.
