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

# Reproducibility and limits

Execute `python3 checker.py` with Python 3 and no third-party packages. The checker bisects the exact two-equation critical-point system, verifies the positive local slopes and Hessian, compares the predicted global diameters against a finite mesh over the curve parameter, and numerically integrates local arclength-weighted extreme-chord neighborhoods on both sides of the critical span.

The package was tested with the embedded `checker.py` and its diagnostics passed. Finite mesh comparisons and quadrature do not establish global uniqueness or asymptotic error terms. Those assertions rely on the analytical monotonicity, stationarity, and local-volume arguments in `RESULT.md`. Decimal constants are evaluations, not certified enclosures. No independent audit has been performed.
