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

# Reproducible checks

The complete proof is in `RESULT.md`; this file records supplemental reproducible computation only. In a Python environment with the dependency listed in `requirements.txt`, run `python check.py`. The script uses `mpmath` with 65-digit precision and evaluates the Jacobi theta function, independently inverts the explicit covariance matrices for multiple heat times and noncritical angles, and checks the product-factor polynomial identity. The resulting log is included in `NUMERICAL_CHECKS.txt` and reports 85 passing assertions.

Finite calculations are not an exhaustive enumeration of real parameters, and no claim of independent mathematical audit or formal proof certification is made. The infinite theorem is established by the derivations in `RESULT.md`.
