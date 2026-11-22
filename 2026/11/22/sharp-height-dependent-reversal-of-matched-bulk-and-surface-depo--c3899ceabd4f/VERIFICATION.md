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

The exact steady profile was verified by differentiation away from the source, both Robin boundary conditions, the central derivative jump, positivity and uniqueness of the Robin operator, and the integrated stationary mass balance. The global-removal comparator uses the explicit surface-to-volume rate, not an imported empirical calibration. The strict inequalities at the walls, centre, and spatial mean are derived for all positive parameters in RESULT.md. The dose statement uses semigroup convergence and is restricted to fixed receiver heights and sufficiently long finite exposures.

Execute `python checker.py` under Python 3 to check the exact elementary case and a reproducible finite sampling of 504 parameter choices. The numerical output is not an infinite proof. No independent audit or external scientific validation has been performed.
