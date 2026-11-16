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
Run `python CHECK.py` in a Python 3 environment with `mpmath` installed. The script uses finite complex contour quadrature (on a mathematically justified ray), low-order triangular determinants, and an independent incomplete-Gamma evaluation. A successful local run returned 37 assertions.

The numerical checks cover representative values, not all integer orders or all parameters. In particular, they cannot replace the analytic contour deformation, saddle-point uniform tail estimates, every-Schatten summability, infinite Fredholm determinant continuity, or conditional oscillatory trace argument. No independent mathematical audit has been performed.
